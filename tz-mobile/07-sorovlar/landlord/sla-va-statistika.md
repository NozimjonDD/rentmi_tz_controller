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

## Release 5 — R5-UE-02 — SLA 24 soat va countdown
**Kod holati:** ❌ (24h countdown kodda yo'q — K3/C3)

**User Story:** Uy egasi sifatida men har so'rovga javob berish uchun qancha vaqt qolganini ko'rishni xohlayman, shunda ijarachini kuttirib qo'ymayman.

**Tavsif:** Har yangi so'rovda "Javob berishingiz kerak: HH:MM:SS" countdown (deadline = so'rov vaqti + 24 soat); **1 soatdan kam qolganda qizil**. Asosiy sahifada "Diqqat talab qiladi" bloki: javob kutayotgan arizalar soni va eng eskisiga qolgan vaqt. Muddati o'tsa so'rov "ko'rib chiqilmagan"ga o'tadi, ikki tomonga push. Eslatma pushlari 12- va 22-soatlarda. "Ko'rib chiqilmagan" yakuniy rad emas — keyin ham javob berish mumkin.

> ⚠ **R5 ichida ziddiyat:** bu batafsil story «**1 soatdan** kam qolganda qizil» deydi; `Release 5 17.08.2026.pdf` xulosasi esa «**7 soatdan** kam qolganda qizil». → [`_konfliktlar.md`](../../_konfliktlar.md) (C-R5-1).

**Qabul mezonlari:**
- GIVEN yangi so'rov keldi WHEN karta ko'rsatilsa THEN countdown 24:00:00 dan boshlab kamayadi
- GIVEN qolgan vaqt 1 soatdan kam WHEN karta ko'rsatilsa THEN countdown qizil rangda
- GIVEN 24 soat o'tdi va javob berilmadi WHEN scheduler ishga tushsa THEN so'rov "ko'rib chiqilmagan"ga o'tadi va ikkala tomonga push
- GIVEN so'rov "ko'rib chiqilmagan" WHEN uy egasi qabul qilsa THEN "qabul qilindi"ga o'tadi va first_response_time yoziladi
- GIVEN javob kutayotgan so'rovlar bor WHEN uy egasi asosiy sahifani ochsa THEN "Diqqat talab qiladi" blokida soni va eng eskisiga qolgan vaqt ko'rinadi

## Release 5 — R5-UE-03 — Javob vaqti indikatori
**Kod holati:** ❌ (first_response_time / indikator kodda yo'q)

**User Story:** Uy egasi sifatida men tez javob berishim ijarachilarga ko'rinishini xohlayman, shunda e'lonlarim ko'proq ariza oladi.

**Tavsif:** Har so'rov bo'yicha first_response_time yoziladi. Ko'rsatkich — oxirgi 30 kun medianasi, soatlik pog'onaga yaxlitlanadi ("odatda 1 soat ichida javob beradi"...). Kamida 3 ta javob bo'lsagina e'lon sahifasida va ommaviy profilda chiqadi. Uy egasiga onboarding tooltip orqali tushuntiriladi.

**Qabul mezonlari:**
- GIVEN uy egasida kamida 3 ta javob yozuvi bor WHEN e'lon yoki profil ochilsa THEN indikator mediana asosida ko'rinadi
- GIVEN javoblar 3 tadan kam WHEN sahifa ochilsa THEN indikator ko'rsatilmaydi
- GIVEN bitta so'rovga juda kech javob berilgan WHEN mediana hisoblansa THEN bitta chetlanish ko'rsatkichni keskin buzmaydi (mediana, o'rtacha emas)
- GIVEN uy egasi birinchi marta So'rovlar sahifasini ochdi WHEN sahifa yuklansa THEN tez javob foydasi haqida tooltip ko'rsatiladi
