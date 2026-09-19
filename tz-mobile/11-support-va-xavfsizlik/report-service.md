# To'liq hisobot (Rentmi) tarifi xizmati

**Rollar:** 👤 Ijarachi    **Holat:** ✅ Bajarilgan

## TZ manbai
Bevosita T1 (qo'llab-quvvatlash) emas — bu **pullik to'liq hisobot (Rentmi bali) tarifi** xizmati bo'lib, S1 (Rentmi hisobotini xarid qilish) va to'liq skoring hisobotini sotib olish oqimini quvvatlaydi. TZ da S1 skoring moduli doirasida ([`04-skoring/`](../04-skoring/about.md), [`05-billing/`](../05-billing/about.md)).
> Bu yerda hujjatlanishi sababi: parent mapping'da `report_service` "chipta-simon oqim" deb belgilangan — aslida kodda bu **read-only tarif** olish, chipta (ticket) tizimi emas.

## Reliz / R5
- **RELIZ:** S1 — Rentmi hisobotini xarid qilish (skoring bilan bog'liq).
- **R5 o'zgarishi:** narx yaxlitlash (mln so'm / 100$) umumiy terminologiyaga taalluqli; report-service tarifi backend'dan.

## Bajarish tartibi (kod)
1. `GET /mobile/report-service/` → faol tarif (`ReportService`: `id`, `priceSom`, `isActive`, `description`).
2. Narx tiyin'ga aylantiriladi (`priceTiyin = priceSom * 100`) — Atmos to'lovlari uchun.
3. To'lov sahifalarida ishlatiladi: `score_payment_page`, `onboarding_payment_page`, `tenant_self_scoring_page`, `full_report_purchase_card`.

## Qabul kriteriyalari (BDD)
- **GIVEN** foydalanuvchi hisobot sotib olmoqchi **WHEN** to'lov sahifasi ochiladi **THEN** faol tarif narxi ko'rsatiladi.
- **GIVEN** tarif faol emas **WHEN** olinadi **THEN** `isActive=false` bilan qaytadi.

## Kod joylashuvi
- **Modul:** `lib/features/report_service` — `ReportServiceCubit` / `ReportServiceState`; usecase `get_report_service`
- **Endpoint:** `GET /mobile/report-service/` (faqat o'qish; POST/yaratish yo'q)
- **Entity:** `ReportService{id, priceSom, isActive, description}`

## Konflikt / farqlar
- ⚠ **Chipta emas:** `report_service` — pullik hisobot **tarifi** (read-only), qo'llab-quvvatlash murojaati / ticket tizimi EMAS. T1 chipta oqimi kodda umuman yo'q. → [`murojaat-t1.md`](murojaat-t1.md), [`_konfliktlar.md`](../_konfliktlar.md).
- Funksional jihatdan skoring/billing modullariga tegishli — bu yerda faqat parent mapping izohi uchun hujjatlangan.
