# SLA countdown va statistika

**Rollar:** 🏠 Uy egasi    **Holat:** ❌ SLA yo'q · 🟡 statistika qisman

## TZ manbai
R2 (9-qadam) — «Uy egasi e'lonlar so'rovlari bo'yicha statistik ma'lumotlar va tavsiyalarni ko'radi». R2 kengaytmasi: «So'rov **7 kun** davomida ko'rib chiqilmasa → avtomatik 'ko'rib chiqilmagan' deb belgilanadi va uy egasiga push-bildirishnoma yuboriladi».

## Reliz / R5
- **RELIZ:** `R4 · Uy egasi — So'rovlar boshqaruvi` — so'rovlar statistikasi.
- **R5 o'zgarishi (markaziy):**
  - `R5-UE-02` **SLA 24 soat** — har yangi so'rovda «Javob berishingiz kerak: HH:MM:SS» countdown; 7 soatdan kam qolganda qizil; muddati o'tsa so'rov «ko'rib chiqilmagan» + ikki tomonga push. Asosiy sahifada «Diqqat talab qiladi» bloki. (TZ 7 kun o'rniga 24 soat — ichki qaror.)
  - `R5-UE-03` **javob vaqti indikatori** — «Odatda N soatda javob beradi» (oxirgi 30 kun mediana, ≥3 javob).
  - `R5-UE-04` statistika mini-grafigi (N ta so'rov, trend %), Analitika 7/30 kun.

## Bajarish tartibi (kod)
1. Statistika sahifasi: `LandlordRequestsStatisticsPage` / `LandlordRequestsStatisticsCubit`.
2. Mulklar karuseli va "E'lon bo'yicha" to'liqlik (`ListingCompletion`) — **real ma'lumot** (uy egasi mulklari + har e'lon detali).
3. Dinamika grafigi (`requests_dynamics_chart`) va yig'indi tile'lar (`requests_stat_tiles`) — **mock** (`PropertyRequestStats.mockSeries` / `.mock`; backend stats endpointi yo'q).
4. "AI maslahat" kartasi/sheeti (`stats_ai_advice_card` / `_sheet`).

## Qabul kriteriyalari (BDD)
- **GIVEN** uy egasi statistika sahifasi **WHEN** ochiladi **THEN** mulk karuseli va to'liqlik real ko'rinadi, dinamika grafigi mock qiymatlarni chizadi.
- **GIVEN** yangi so'rov **WHEN** kelib tushadi **THEN** ⚠ R5 countdown **ko'rinmaydi** (amalga oshirilmagan).

## Kod joylashuvi
- **Modul:** `lib/features/landlord_requests`
- **Sahifa / BLoC:** `LandlordRequestsStatisticsPage` / `LandlordRequestsStatisticsCubit`; `requests_dynamics_chart`, `requests_stat_tiles`, `stats_property_selector`, `stats_ai_advice_card`
- **Endpoint:** statistika uchun **alohida backend endpoint yo'q** — mulklar `GET /mobile/homeowner/...` + e'lon detali orqali on-device hisob; qolgani mock.

## Konflikt / farqlar
- ⚠ **24 soatlik SLA countdown amalga oshirilmagan** (R5-UE-02 markaziy funksiyasi): kodda `countdown`, `SLA`, `deadline`, `first_response`, «Javob berishingiz», «ko'rib chiqilmagan», «Diqqat talab qiladi» hech biri yo'q. → [`_konfliktlar.md`](../../_konfliktlar.md).
- ⚠ **SLA muddati konflikti:** TZ R2 = **7 kun**, R5-UE-02 = **24 soat** (ichki qaror). Ikkalasi ham kodda amalga oshirilmagan.
- ⚠ **Javob vaqti indikatori yo'q** (R5-UE-03 «Odatda N soatda javob beradi»).
- ⚠ **Dinamika grafigi + tile'lar mock** — real backend stats endpointi yo'q (karusel/to'liqlik esa real).
