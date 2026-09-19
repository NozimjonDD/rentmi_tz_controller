# Tenant skoring detali

**Rollar:** 🏠 Uy egasi    **Holat:** ✅ Bajarilgan

## TZ manbai
R2 (3-qadam) — Uy egasi so'rov tafsilotlarida ijarachining ma'lumotlari, **Rentmi bali va xulosasi**, so'rov xabarini ko'rib chiqadi.
> «…tafsilotlarni ko'rib chiqadi (ijarachi ma'lumotlari, Rentmi bali va xulosa, so'rov xabari va chat orqali xabarlashish imkoniyati)…»

## Reliz / R5
- **RELIZ:** `R4 · Uy egasi — So'rovlar boshqaruvi` — ijarachi skoring xulosasi so'rov detalida.
- **R5 o'zgarishi:** `R5-UE-01` — ijarachi kartasida gauge (ball/100 + label), oila tarkibi chips; e'lon formasida "ijarachi skoring qismidagi eski tekst olib tashlanadi" (`R5-AD` / e'lon tomoni).

## Bajarish tartibi (kod)
1. So'rov detalida ijarachining shaxsiy ma'lumotlari (`landlord_detail_personal_info_section`).
2. Skoring bloki (`landlord_detail_scoring_section`) — Rentmi bali + xulosa.
3. To'lov intizomi (`landlord_detail_payment_discipline_section`) va ijara tarixi (`landlord_detail_rental_history_section`).
4. To'liq skoring sahifasi: `tenant_scoring_detail_page` — batafsil skoring (compact gauge).
5. To'liq hisobot bloklangan bo'lsa `locked_full_report_card` → so'rash `{report_status:'pending'}`.

## Qabul kriteriyalari (BDD)
- **GIVEN** so'rov detali **WHEN** uy egasi ochadi **THEN** ijarachi Rentmi bali va xulosasi ko'rinadi.
- **GIVEN** to'liq hisobot yopiq **WHEN** uy egasi so'raydi **THEN** REPORT_PENDING oqimi ishga tushadi (ijarachi roziligi kutiladi).

## Kod joylashuvi
- **Modul:** `lib/features/landlord_requests`
- **Sahifa / Widget:** `tenant_scoring_detail_page`; `landlord_detail_scoring_section`, `landlord_detail_payment_discipline_section`, `landlord_detail_rental_history_section`, `compact_score_gauge` (`rental_requests`), `locked_full_report_card`
- **Endpoint:** skoring ma'lumotlari so'rov detalida (`GET /mobile/requests/detail/{id}/`); to'liq hisobot so'rash `PATCH /mobile/requests/update/{id}/` `{report_status:'pending'}`
- **Bog'liq:** skoring modeli va S1 → [`04-skoring/`](../../04-skoring/about.md).

## Konflikt / farqlar
- Farq aniqlanmadi — skoring xulosasi TZ R2 3-qadamiga mos ko'rsatiladi.
- To'liq hisobot (report) rozilik oqimi TZ da alohida yozilmagan, R5 backend'idagi REPORT_* triggerlariga tayanadi (ijarachi tomoni: [`../tenant/oz-sorovlarim.md`](../tenant/oz-sorovlarim.md)).
