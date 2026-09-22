# To'lov provayderlari (Atmos / Payme / Click / Uzum)

**Rollar:** 👤 Ijarachi    **Holat:** ✅ Bajarilgan

## TZ manbai
S1 — Rentmi hisobotini xarid qilish · Skoring moduli (4–5 qadam). Tizim to'lov tizimi bilan integratsiya orqali to'lov oynasini shakllantiradi, foydalanuvchi to'lovni amalga oshiradi.
> «Tizim to'lov tizimi bilan integratsiya orqali to'lov oynasini shakllantiradi; Foydalanuvchi to'lovni amalga oshiradi.»

## Reliz / R5
- **RELIZ:** to'lov provayderlari alohida user-story sifatida ajratilmagan; skoring xaridi oqimi ichida amalga oshirilgan. To'rt provayder qo'llab-quvvatlanadi: **Atmos** (karta biriktirish + OTP), **Payme**, **Click**, **Uzum**.
- **R5 o'zgarishi:** yo'q (R5 to'lov provayderlarini o'zgartirmaydi).

## Bajarish tartibi
1. Foydalanuvchi skoring xaridida provayderni tanlaydi (`PaymentMethodsCard`); mavjudlik `GET /mobile/payments/status/` orqali tekshiriladi.
2. **Atmos (karta + OTP):** karta ro'yxati `GET /mobile/card/list/`; yangi karta — `POST /mobile/card/bind/init/` `{card_number, expiry}` → `POST /mobile/card/bind/confirm/` `{transaction_id, otp}`. To'lov: `POST /mobile/payment/create/` `{amount}` → `POST /mobile/payment/pre-apply/` `{transaction_id, card_token}` → `POST /mobile/payment/apply/` `{transaction_id, otp}`.
3. **Payme:** `POST /mobile/payme/create-order/` `{amount}` → `payUrl`; holat `GET /mobile/payme/order/{id}/`.
4. **Click:** `POST /mobile/click/order-create/` `{amount}` → `payUrl`; holat `POST /mobile/click/status/` `{order_id}`.
5. **Uzum:** `POST /mobile/orders/create/` `{amount}` → `deepLink`; holat `GET /mobile/orders/{id}/status/`.
6. Payme/Click/Uzum'da `payUrl`/`deepLink` tashqi ilovada ochiladi, so'ng holat pollingi orqali tasdiqlanadi; muvaffaqiyatda Universal Order `paid` bo'ladi ([`universal-order.md`](universal-order.md)).

## Qabul kriteriyalari (BDD)
- **GIVEN** foydalanuvchi Atmos'da yangi karta kiritdi **WHEN** `card/bind/init` chaqiriladi **THEN** SMS OTP yuboriladi va `card/bind/confirm` OTP bilan kartani biriktiradi.
- **GIVEN** Payme/Click orqali order yaratildi **WHEN** `payUrl` ochiladi **THEN** tashqi to'lov oynasi ochiladi va holat pollingi to'lovni tasdiqlaydi.
- **GIVEN** tashqi to'lov tizimi mavjud emas **WHEN** provayder tanlanadi **THEN** `payments/status/` uni nofaol ko'rsatadi va keyinroq urinish taklif qilinadi.

## Kod joylashuvi
- **Modul:** `lib/features/subscription`
- **Sahifa / BLoC:** `PaymentCardPage`, `AddCardPage`, `CardOtpPage`, `PaymentPage` / `PaymentBloc` (Atmos), `PaymeBloc`, `ClickBloc`, `UzumBloc`, `PaymentStatusCubit`
- **Endpoint:** Atmos `card/bind/init`, `card/bind/confirm`, `payment/create`, `payment/pre-apply`, `payment/apply`, `card/{id}/delete`; `payme/create-order`, `payme/order/{id}`; `click/order-create`, `click/status`; `orders/create`, `orders/{id}/status`; `payments/status`
- Pul: Atmos — **tiyin** (`priceTiyin`); Payme/Click/Uzum — **so'm**.

## Konflikt / farqlar
- ⚠ **To'lov simulyatsiyasi:** Pro'ni faollashtiruvchi bosqich hozircha client-only (`TODO_SUBSCRIPTION.md`); real gateway integratsiyasi va `/subscription/activate/` backend tomonda hali yo'q. → [`_konfliktlar.md`](../_konfliktlar.md) B5.
- Provayder endpointlari (order create + status) real ishlaydi; farq faqat Pro-obuna yozuvida.
