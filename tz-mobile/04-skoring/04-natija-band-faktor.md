# Skoring natijasi — band va faktorlar

**Rollar:** 👤 Ijarachi (natija barcha rollarga ko'rinadi; xarid faqat ijarachi)    **Holat:** ✅ Bajarilgan

## TZ manbai
S1 — Rentmi hisobotini xarid qilish · §4.1.1.4 (S1, 8–13 qadam). Bal (0–100) hisoblanadi, umumiy xulosa shakllantiriladi va natija profilga saqlanadi.
> «Bal asosida umumiy xulosa shakllantiriladi (**past/o'rtacha/yuqori** ishonchlilik); Natija foydalanuvchi profiliga saqlanadi; Tizim hisobotni ko'rish ekraniga yo'naltiradi.»
> §4.3.1: «Rentmi bali (skoring ko'rsatkichi)ni hisoblash — **0 dan 100 gacha** diapazonda … to'liq avtomatik skoring muhim biznes qarorlariga qo'llanilmaydi.»

## Reliz / R5
- **RELIZ:** `2-6 Skoring / US 6, Scenario 5,7` — natijada «**GREEN / YELLOW / RED band**, raw score, **affordability indicator**, ijobiy va salbiy faktorlar, shaxsiy ma'lumotlar, **depozit va predoplata** hisobi, kredit tarixi/qarzdorliklar, ijara tarixi». «**Hard reject** bo'lsa ham score/band ko'rsatiladi, lekin hard reject score balidan oshib ketmasligi kerak».
- **R5 o'zgarishi:** yo'q (band rangi va faktor breakdown R1 US 6 doirasida).

## Bajarish tartibi
1. `GET /mobile/tenant/rentme-score/{userId}/?rental_request_id=` to'liq hisobotni oladi → `RentmeScore`.
2. `scoring_result_page` speedometer (`CustomPainter`) chizadi; band rangi (GREEN/YELLOW/RED/unknown) `ScoreBand.fromString` orqali inline keladi.
3. 6 faktor breakdown ko'rsatiladi: `income, credit, mib, rentalHistory, affordability, adjustments`.
4. `HardRules` (hard reject / sariqqa cheklash) va `DataQualityFlags` ogohlantirishlari ko'rsatiladi; deposit/pre-deposit tavsiyalari (`depositRecommendation`, `preDepositRecommendation`).
5. To'liq hisobot **Pro-gated** — `SubscriptionCubit.isProUser` bo'lmasa `ProLockedOverlay` orqali yopiladi (`ProUpgradeSheet`).
6. **PDF yuklab olish** (TZ S1, 14-qadam): to'liq hisobot PDF sifatida yuklanadi (`full_report_purchase_card` / `tenant_self_scoring_page` `onDownload`, `DioClient` orqali) — Pro funksiyasi.

## Qabul kriteriyalari (BDD)
- **GIVEN** hisoblash yakunlangan **WHEN** natija sahifasi ochiladi **THEN** band, raw/display score, affordability, 6 faktor, deposit tavsiyasi va tarix ma'lumotlari ko'rsatiladi.
- **GIVEN** foydalanuvchi hard reject qoidasiga tushdi **WHEN** skoring hisoblanadi **THEN** score va band baribir ko'rsatiladi, lekin hard reject cap'idan oshmaydi.
- **GIVEN** foydalanuvchi Pro emas **WHEN** to'liq natijani ochadi **THEN** `ProLockedOverlay` ko'rsatiladi va Pro sahifaga yo'naltiriladi.

## Kod joylashuvi
- **Modul:** `lib/features/scoring` (entity/widget) + `lib/features/core_screens/scoring` (sahifa) + `lib/features/subscription` (Pro-gate)
- **Sahifa / BLoC:** `ScoringResultPage` (`CustomPainter` speedometer) / `SubscriptionCubit` (`isProUser`)
- **Endpoint:** `GET /mobile/tenant/rentme-score/{userId}/?rental_request_id=` (to'liq); legacy `GET /mobile/scoring/{userId}/`
- **Entity:** `RentmeScore` → `RentmeScoreDetail{displayScore, rawScore, band, factors, depositRecommendation, preDepositRecommendation}`, `ScoringFactors` (6), `HardRules`, `DataQualityFlags`, `validUntil`.

## Konflikt / farqlar
- ⚠ **C6 — xulosa turi:** TZ "**past / o'rtacha / yuqori** ishonchlilik" ↔ reliz/kod "**GREEN / YELLOW / RED** band + hard reject". → [`_konfliktlar.md`](../_konfliktlar.md).
- ⚠ **C4 — amal muddati:** entity'da `validUntil` maydoni bor, ammo amal muddati qiymati birorta relizda belgilanmagan (`R1` "muddatsiz" ↔ `R4` "muddati o'tadi"). → [`_konfliktlar.md`](../_konfliktlar.md).
- ⚠ **Band manbai:** band backend'dan **inline** keladi (`ScoreBand.fromString`); alohida `/score-band` endpoint **YO'Q** (CLAUDE.md noaniq). → [`_konfliktlar.md`](../_konfliktlar.md).
