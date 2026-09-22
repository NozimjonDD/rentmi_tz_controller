# Kadastr — uy egasi mulklarini import

**Rollar:** 🏠 Uy egasi    **Holat:** ✅ Bajarilgan

## TZ manbai
U5 — Foydalanuvchini identifikatsiya qilish · §4.1.1.4 (U5, 9-qadam). Identifikatsiyadan o'tgan uy egasiga tegishli ko'chmas mulklar ro'yxatini yuklab berish taklifi beriladi.
> «Agar foydalanuvchi uy egasi rolida ro'yxatdan o'tsa unga tegishli ko'chmas mulklari ro'yxatini yuklab berish taklifi beriladi, qabul qilsa ro'yxat shakllantiriladi va uy egasining asosiy sahifasiga yo'naltiriladi.»

## Reliz / R5
- **RELIZ:** `2-5 MyID identifikatsiya / US 5` — «Muvaffaqiyatli identifikatsiyadan so'ng … agar foydalanuvchi uy egasi bo'lsa ko'chmas mulklarini import qilib olish sahifasiga o'tadi».
- **R5 o'zgarishi:** «Uy egasining davlat bazasidan mulklar ro'yxatini yuklash integratsiyasi ishlashi — "**Tekshirilgan**" va **tegishlilik** shunga tayanadi» `R5`. R5 §5 da "Tekshirilgan" — uch bayroqli AND: E4 moderatsiya + U5 identifikatsiya + mulk davlat bazasidan yuklangan ro'yxatda.

## Bajarish tartibi
1. Identifikatsiya VERIFIED bo'lgach uy egasiga kadastr onboarding sahifasi ochiladi (`landlord_cadastre_onboarding_page`).
2. `PropertyImportCubit` → `GET /mobile/homeowner-properties/import/preview/` MyID (pinfl + job_id) bo'yicha davlat bazasidagi mulklar ro'yxatini oldindan ko'rsatadi.
3. Foydalanuvchi import qilinadigan obyektlarni belgilaydi.
4. `POST /mobile/homeowner-properties/import/create/` `{selected_objects}` tanlangan mulklarni yaratadi.
5. Ro'yxat shakllantirilgach uy egasining asosiy sahifasiga yo'naltiriladi.

## Qabul kriteriyalari (BDD)
- **GIVEN** uy egasi identifikatsiyadan o'tgan **WHEN** import sahifasi ochiladi **THEN** davlat bazasidagi mulklar preview ko'rinishida ko'rsatiladi.
- **GIVEN** preview ro'yxati ochilgan **WHEN** foydalanuvchi obyektlarni tanlab importni tasdiqlaydi **THEN** tanlangan mulklar hisobga qo'shiladi va dashboard'ga o'tiladi.
- **GIVEN** import MyID (pinfl/job_id) ga bog'liq **WHEN** identifikatsiya ma'lumoti yo'q **THEN** preview shakllanmaydi.

## Kod joylashuvi
- **Modul:** `lib/features/property_import`
- **Sahifa / BLoC:** `LandlordCadastreOnboardingPage` (`lib/features/core_screens/landlord_onboarding/…`) / `PropertyImportCubit`
- **Endpoint:** `GET /mobile/homeowner-properties/import/preview/`; `POST /mobile/homeowner-properties/import/create/` `{selected_objects}`
- Import MyID identifikatsiyasi (pinfl + job_id) natijasiga bog'liq.

## Konflikt / farqlar
- ⚠ **R5 "Tekshirilgan" bog'liqligi:** e'lonning "Tekshirilgan" statusi va mulk tegishliligi aynan shu importga tayanadi (E4 moderatsiya + U5 + davlat bazasi ro'yxati). Import ishlamasa "Tekshirilgan" bayrog'i berilmaydi. → [`_konfliktlar.md`](../_konfliktlar.md).
- TZ importni "taklif" (ixtiyoriy) deb belgilaydi — kodda ham onboarding qadami sifatida o'tkazib yuborilishi mumkin. Boshqa farq aniqlanmadi.
