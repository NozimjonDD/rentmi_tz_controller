# 04 — Skoring (Rentmi bali)

Ijarachining ishonchlilik darajasini — **Rentmi bali (0–100)** — baholash, skoring xulosasi va hisobotini shakllantirish. TZ use-case'lari: **S1** (Rentmi hisobotini xarid qilish), **S2** (skoring ma'lumotlarini tashqi manbadan olish). Faqat 👤 ijarachi xarid qiladi; natija barcha rollarga (ijarachi/uy egasi/operator) qisman va to'liq ko'rinadi.

## Quyi tugunlar

| Tugun | Mazmun | TZ | Holat |
|---|---|---|---|
| [`01-intro-motivatsiya.md`](01-intro-motivatsiya.md) | Motivatsion sahifa, narx ko'rsatish | S1 (1–3) | ✅ |
| [`02-tolov.md`](02-tolov.md) | Skoring uchun to'lov (karta+OTP / Payme / Click / Uzum) | S1 (4–5) | ✅ |
| [`03-hisoblash-process.md`](03-hisoblash-process.md) | Async check → status polling, background jarayon | S1 (6–8) | ✅ |
| [`04-natija-band-faktor.md`](04-natija-band-faktor.md) | Natija: band, 6 faktor, hard-reject, affordability, deposit tavsiyasi | S1 (8–11) | ✅ |
| [`05-tashqi-manba-s2.md`](05-tashqi-manba-s2.md) | Tashqi manba (kredit byurosi/soliq) — backend ichida | S2 | 🟡 |
| [`06-recommendations-improve.md`](06-recommendations-improve.md) | Tavsiyalar, skoringni yaxshilash, self-scoring | S1 (15) | ✅ |
| [`07-income-upload.md`](07-income-upload.md) | Daromad va oilaviy holat hujjatlarini yuklash (affordability input) | S1 (15) | ✅ |

## Umumiy oqim (kod'dagi haqiqiy holat)

```
MyID (02) → skoring intro (motivatsiya + narx)  [faqat ijarachi]
   → to'lov (karta+OTP / Payme / Click / Uzum) — 05-billing
   → POST /scoring/check/ {rent_amount}  (async boshlanadi)
   → GET /scoring/status/  (Timer.periodic 1s polling, background)
   → GET /tenant/rentme-score/{userId}/  (to'liq hisobot)
   → natija: band (GREEN/YELLOW/RED) + speedometer + 6 faktor  [Pro-gated]
      → tavsiyalar / skoringni yaxshilash / daromad-hujjat yuklash
```

## Model qisqacha — `RentmeScore` (`lib/features/scoring/domain/entities/`)

- `RentmeScoreDetail` : `displayScore`, `rawScore`, `band` (`ScoreBand`), `factors`, `depositRecommendation`, `preDepositRecommendation`.
- `ScoreBand{green, yellow, red, unknown}` — **inline keladi** (`ScoreBand.fromString`); noma'lum/tanilmagan qiymat `unknown`. ⚠ alohida `/score-band` endpoint **YO'Q**.
- `ScoringFactors{income, credit, mib, rentalHistory, affordability, adjustments}` — 6 faktor.
- `HardRules{hardReject, hardCapYellow, reasons}` — qat'iy qoidalar (hard reject / sariqqa cheklash).
- `DataQualityFlags{cbNoData, cbStale, mibNoData, mibStale, noDataCap}` — tashqi manba sifat bayroqlari.
- `validUntil` (`DateTime?`) — amal muddati maydoni mavjud, ⚠ ammo qiymati birorta relizda belgilanmagan (C4).

## Kod modullari

`lib/features/scoring` (model + widget; sahifa yo'q) · oqim sahifalari `lib/features/core_screens/scoring/` · narx `lib/features/report_service` · daromad/oila `lib/features/scoring` (income) + `lib/features/marital_status` · Pro-gate `lib/features/subscription` (`SubscriptionCubit.isProUser`).

## Asosiy endpointlar

| Amal | Endpoint |
|---|---|
| Skoring boshlash (async) | `POST /mobile/scoring/check/` — `{rent_amount}` |
| Holat (polling) | `GET /mobile/scoring/status/` |
| To'liq hisobot | `GET /mobile/tenant/rentme-score/{userId}/?rental_request_id=` |
| Legacy skoring | `GET /mobile/scoring/{userId}/` |
| Narx (tarif) | `GET /mobile/report-service/` (fallback 49000 so'm) |
| Daromad davri | `PATCH /mobile/unconfirmed_income-period/update/` — `{unconfirmed_income_period}` |
| Daromad hujjati | `POST /mobile/attachments/income-status/` (multipart) |

## Konflikt / farqlar

- ⚠ **C4 — amal muddati:** skoring **amal muddati** hech qayerda belgilanmagan (`R1 · US 6` "muddatsiz" ↔ `R4 · IJ-R1` "muddati o'tadi"). → [`_konfliktlar.md`](../_konfliktlar.md).
- ⚠ **C6 — xulosa turi:** TZ "**past / o'rtacha / yuqori** ishonchlilik" ↔ reliz/kod "**GREEN / YELLOW / RED** band + hard reject". → [`_konfliktlar.md`](../_konfliktlar.md).
