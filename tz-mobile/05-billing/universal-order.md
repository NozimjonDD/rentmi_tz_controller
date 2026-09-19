# Universal Order — skoring access gate

**Rollar:** 👤 Ijarachi    **Holat:** ✅ Bajarilgan

## TZ manbai
S1 — Rentmi hisobotini xarid qilish · Skoring moduli. To'lov muvaffaqiyatli yakunlangach hisobot shakllantiriladi va foydalanuvchi profiliga saqlanadi; skoring balini ko'rish imkoniyati ochiladi.
> «Natija foydalanuvchi profiliga saqlanadi; ... foydalanuvchi skoring balini ijarachi asosiy sahifasi va profili orqali ko'rishi mumkin.»

## Reliz / R5
- **RELIZ:** skoring access provayderdan mustaqil, yagona **Universal Order** obyekti orqali boshqariladi — «paid Order mavjudligi = skoring access». Bir vaqtda bitta faol order; yangi order yaratilganda oldingisi backend'da atomik arxivlanadi.
- **R5 o'zgarishi:** yo'q.

## Bajarish tartibi
1. Ilova ochilishida yoki skoring sahifasida faol order tekshiriladi: `GET /mobile/orders/active/` → `Order` yoki 204 (null).
2. Order yo'q bo'lsa — provayder tanlangach `POST /mobile/universal/orders/` `{provider, amount}` yuboriladi; `Order.status = new`, `payUrl` (Payme) yoki `transaction_id` (Atmos) qaytadi.
3. Provayder to'lovni tasdiqlagach backend `Order.status = paid` qiladi va `scoringId` ni order'ga bog'laydi (order ↔ skoring aloqasi).
4. `Order.isPaid == true` — skoring access ochiq deb hisoblanadi (`SubscriptionState.isProUser`).
5. Logout / yangi login'da `SubscriptionCubit.resetSession()` lokal order keshini tozalaydi — oldingi foydalanuvchining "paid" holati keyingisiga o'tmaydi.

## Qabul kriteriyalari (BDD)
- **GIVEN** foydalanuvchida `status=paid` Order mavjud **WHEN** skoring sahifasi ochiladi **THEN** hisobot ko'rinadi (access ochiq).
- **GIVEN** faol order yo'q (204) **WHEN** skoring so'raladi **THEN** xarid oqimi (provayder tanlash) taklif qilinadi.
- **GIVEN** foydalanuvchi tizimdan chiqdi **WHEN** boshqa foydalanuvchi kiradi **THEN** order keshi tozalangan, oldingi access o'tmaydi.

## Kod joylashuvi
- **Modul:** `lib/features/subscription`
- **Sahifa / BLoC:** `ProPurchasePage`, `ProLockedOverlay`, `ProUpgradeSheet` / `SubscriptionCubit` (`loadActiveOrder`, `refreshActiveOrder`, `createOrder`, `resetSession`); entity `Order` (`OrderProvider{atmos, payme}`, `OrderStatus{new_, paid, cancelled, archived, unknown}`, `scoringId`, `isPaid`, `isActive`)
- **Endpoint:** `GET /mobile/orders/active/` · `POST /mobile/universal/orders/` `{provider, amount}` → `Order`

## Konflikt / farqlar
- ⚠ **Pro/obuna model — legacy shim:** `ProStatus`/`SubscriptionPlan{lite, pro}` va `activatePro`/`deactivatePro`/`loadProStatus` saqlangan, lekin gating endi faqat `activeOrder` (paid Order) orqali; `/subscription/status|activate|cancel` endpointlar kodda **yo'q**. → [`_konfliktlar.md`](../_konfliktlar.md) B5.
- ⚠ TZ obuna darajalari (lite/pro) yoki hisobot narxlash siyosatini rasmiy belgilamaydi; kod bir martalik `Order` amount modelidan foydalanadi. → B6.
