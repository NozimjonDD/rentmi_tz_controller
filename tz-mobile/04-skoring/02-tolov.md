# Skoring uchun to'lov

**Rollar:** 👤 Ijarachi    **Holat:** ✅ Bajarilgan

## TZ manbai
S1 — Rentmi hisobotini xarid qilish · §4.1.1.4 (S1, 4–5 qadam). Tizim to'lov integratsiyasi orqali to'lov oynasini shakllantiradi, foydalanuvchi to'lovni amalga oshiradi.
> «Tizim to'lov tizimi bilan integratsiya orqali to'lov oynasini shakllantiradi; Foydalanuvchi to'lovni amalga oshiradi.»
> Vaqt reglamenti: «To'lov oynasini shakllantirish — ≤5 s; to'lov tasdig'i — ≤15 s.»

## Reliz / R5
- **RELIZ:** `2-6 Skoring / US 6, Scenario 3` — «Foydalanuvchi **Payme, Click yoki bank kartasi** orqali to'lovni amalga oshiradi; to'lov muvaffaqiyatli yakunlangach scoring calculation boshlanadi; tranzaksiya tizimga saqlanadi».
- **R5 o'zgarishi:** yo'q.

## Bajarish tartibi
1. Skoring to'lov usullari sahifasi (`score_payment_page`) ochiladi: **bank kartasi** (raqam + amal muddati) yoki **Payme / Click / Uzum** tile'lari.
2. Karta orqali: karta ma'lumoti kiritiladi → SMS OTP sahifasi (`score_payment_otp_page`, Atmos protokoli) → `ConfirmCardBind(transactionId, otp)` → karta bog'lanadi (`cardToken`).
3. Bog'langach `ExecutePayment(amount, cardToken)` avtomatik ishga tushadi (`createPayment` → `preApplyPayment` → `applyPayment`).
4. Payme / Click / Uzum: tegishli provayder bloki orqali universal order yaratiladi (batafsil: [`05-billing`](../05-billing/about.md)).
5. To'lov muvaffaqiyatli → skoring hisoblash jarayoni boshlanadi ([`03-hisoblash-process.md`](03-hisoblash-process.md)).

> To'lov tafsilotlari (Atmos/Payme/Click/Uzum, universal order, `scoringId` bog'lanishi, receipt) markaziy [`05-billing`](../05-billing/about.md) da hujjatlangan; bu yerda faqat skoring konteksti ko'rsatiladi.

## Qabul kriteriyalari (BDD)
- **GIVEN** foydalanuvchi to'lov sahifasida **WHEN** "Skoring sotib olish" bosiladi va karta/provayder orqali to'lov muvaffaqiyatli **THEN** scoring calculation ishga tushadi va tranzaksiya saqlanadi.
- **GIVEN** karta to'lovi tanlangan **WHEN** SMS OTP kiritiladi **THEN** karta bog'lanadi va to'lov avtomatik bajariladi.
- **GIVEN** to'lov muvaffaqiyatsiz **WHEN** xatolik yuz beradi **THEN** xabar ko'rsatiladi va qayta urinish taklif qilinadi (TZ kengaytmasi).

## Kod joylashuvi
- **Modul:** `lib/features/core_screens/scoring` + to'lov bloklari `lib/features/subscription`
- **Sahifa / BLoC:** `ScorePaymentPage`, `ScorePaymentOtpPage` / `PaymentBloc`, `PaymeBloc`, `ClickBloc`, `UzumBloc`
- **Endpoint:** to'lov endpointlari — 05-billing (karta bog'lash `POST /mobile/card/bind/init/`, Atmos `ConfirmCardBind`/`ExecutePayment`); narx `GET /mobile/report-service/`

## Konflikt / farqlar
- ⚠ **Provayderlar:** TZ (billing §) — «Click / Payme / Uzum» ↔ kod qo'shimcha **karta+OTP (Atmos)** oqimini ham qo'llaydi. Batafsil: [`05-billing`](../05-billing/about.md). → [`_konfliktlar.md`](../_konfliktlar.md).
