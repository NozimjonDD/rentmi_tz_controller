# Daromad va oilaviy holat hujjatlarini yuklash

**Rollar:** 👤 Ijarachi    **Holat:** ✅ Bajarilgan

## TZ manbai
S1 — Rentmi hisobotini xarid qilish · §4.1.1.4 (S1, 15-qadam). Hisobotdan so'ng oilaviy holat, farzandlar va daromad ma'lumotini yuklash funksionali ochiladi (affordability/ishonchlilik uchun kiruvchi ma'lumot).
> «Oilaviy holat, farzandlar va daromad to'g'risida ma'lumot yuklash hamda tavsiyanoma qo'shish funksionali ochiladi.»

## Reliz / R5
- **RELIZ:** `2-6 Skoring / US 6` — «**affordability indicator**» natijada ko'rsatiladi; daromad/oila ma'lumoti uning kirish manbai.
- **R5 o'zgarishi:** yo'q.

## Bajarish tartibi
1. Natija/hisobotdan daromad yuklash sheet'i ochiladi (`scoring_income_upload_sheet`).
2. Norasmiy (tasdiqlanmagan) daromad davri: `PATCH /mobile/unconfirmed_income-period/update/` `{unconfirmed_income_period: <oy>}` (idempotent).
3. Daromadni tasdiqlovchi hujjat(lar): `POST /mobile/attachments/income-status/` (multipart fayl yuklash).
4. Oilaviy holat: `PATCH /mobile/marital-status/update/` `{marital_status}`; tasdiqlovchi hujjat `POST /mobile/attachments/marital-status/` (multipart).
5. Yuklangan ma'lumot affordability faktoriga kiritiladi va keyingi qayta hisoblashda hisobga olinadi.

## Qabul kriteriyalari (BDD)
- **GIVEN** foydalanuvchi daromad davrini kiritadi **WHEN** saqlanadi **THEN** `PATCH /unconfirmed_income-period/update/` chaqiriladi va qiymat saqlanadi.
- **GIVEN** daromad hujjati tanlangan **WHEN** yuklanadi **THEN** `POST /attachments/income-status/` orqali multipart yuklanadi.
- **GIVEN** oilaviy holat/hujjat kiritilgan **WHEN** saqlanadi **THEN** marital-status endpointlari chaqiriladi va affordability inputiga qo'shiladi.

## Kod joylashuvi
- **Modul:** `lib/features/scoring` (income) + `lib/features/marital_status`
- **Sahifa / BLoC:** `scoring_income_upload_sheet` / `ScoringIncomeUploadCubit`; `marital_upload_sheet` / `MaritalUploadCubit`
- **Endpoint:** `PATCH /mobile/unconfirmed_income-period/update/` `{unconfirmed_income_period}`; `POST /mobile/attachments/income-status/` (multipart); `PATCH /mobile/marital-status/update/` `{marital_status}`; `POST /mobile/attachments/marital-status/` (multipart)

## Konflikt / farqlar
- Daromad + oilaviy holat + farzandlar ma'lumoti TZ 15-qadam bilan mos. Farq aniqlanmadi.
