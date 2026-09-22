# Shartnoma moduli holati (nega o'chirilgan)

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi    **Holat:** 💤 O'chirilgan (dormant)

## TZ manbai
TZ R2 (5-qadam) elektron ijara shartnomasini **3-bosqich** deb belgilaydi — mazkur (1-bosqich) TT doirasiga kirmaydi. So'rov tasdiqlangach ssenariy kontakt ochilishida yakunlanadi.
> «…mazkur TT doirasida ssenariy shu yerda yakunlanadi (keyingi bosqich — elektron ijara shartnomasi — 3-bosqichda).»

## Reliz / R5
- **RELIZ:** shartnoma R1–R5 (1-bosqich) doirasida faol emas.
- **R5 o'zgarishi:** yo'q. R5 so'rovlar sahifasida «Shartnomalar» tab'i va deep-link route'lari mavjud, lekin ular uyqudagi funksiyaga bog'lanmagan (so'rovlar sahifasiga yo'naltiriladi).

## Nega o'chirilgan (kod holati)
1. **`TODO(contract-removal)`** — butun modul bo'ylab marker; router (`app_router.dart`) da `contractsList`, `contractCreation`, `contractAcceptance`, `contractView` case'lari **izohlangan** (comment).
2. Import'lar izohlangan (`contract_*_page.dart`).
3. `NotificationNavigator` da shartnoma route'lari (`contractsList/Detail/Acceptance`) izohlangan; backend `contracts/detail/<pk>/` push'i **so'rovlar sahifasiga** yo'naltiriladi (rolga qarab).
4. Modul kodi (BLoC, sahifalar, datasource) **saqlangan** — 3-bosqichda qayta yoqish uchun tayyor.

## Islomiy moliya (Shariah) ramkasi
- Tenant oqimi: `step1_islamic_finance_page`, `contract_view_islamic_finance_card`, `offerta_page` — shartnoma islomiy moliya tamoyillari asosida tuzilgan.
- To'liq bosqichli oqim: uy egasi (`step1..step4`: shartnoma turi, mulk ma'lumoti, qoidalar, ko'rib chiqish) va ijarachi qabul qilish (`contract_acceptance`).

## Qabul kriteriyalari (BDD)
- **GIVEN** 1-bosqich build **WHEN** shartnoma sahifasi ochilishga urinilsa **THEN** route mavjud emas (izohlangan), so'rovlar sahifasi ochiladi.
- **GIVEN** shartnoma push'i **WHEN** keladi **THEN** rolga qarab tenant/landlord so'rovlar sahifasiga o'tadi.

## Kod joylashuvi
- **Modul:** `lib/features/contract` (to'liq, faol emas)
- **Marker:** `TODO(contract-removal)` — `lib/core/routes/app_router.dart`, `lib/core/services/notification_navigator.dart` va b.
- **Uyqudagi endpointlar:** `POST /mobile/contracts/create/`, `GET /mobile/contracts/detail/{id}/`, `PATCH /mobile/contracts/update/{id}/`, `GET /mobile/homeowner/contract/list/`, `GET /mobile/tenant/contract/list/`

## Konflikt / farqlar
- ⚠ **3-bosqich funksiyasi kodda mavjud, lekin o'chirilgan** — TZ 1-bosqich doirasiga kirmaydi; hujjatda 💤 sifatida belgilanadi. → [`_konfliktlar.md`](../_konfliktlar.md).
- So'rovlar global inbox'idagi `contracts` tab'i shu uyqudagi funksiyaga ishora qiladi — [`07-sorovlar/landlord/korib-chiqish.md`](../07-sorovlar/landlord/korib-chiqish.md).
