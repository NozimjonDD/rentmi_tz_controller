# Oilaviy holat (marital status)

**Rollar:** 👤 Ijarachi    **Holat:** ✅ Bajarilgan

## TZ manbai
S1 — Rentmi hisobotini xarid qilish · Skoring moduli (15-qadam). Skoring aniqligini oshirish uchun oilaviy holat va tasdiqlovchi ma'lumotlar yuklanadi.
> «(S1, 15-qadam) **Oilaviy holat, farzandlar va daromad** to'g'risida ma'lumot yuklash ... funksionali ochiladi.»

## Reliz / R5
- **RELIZ:** oilaviy holat toggle sifatida kiritiladi (turmush qurgan / qurmagan) va tasdiqlovchi fayllar biriktiriladi. R5 uy egasi so'rovlar kartasida «oila tarkibi» chips sifatida ko'rsatiladi.
- **R5 o'zgarishi:** yo'q (kiritish oqimi o'zgarmaydi; ko'rsatish so'rov kartasida R5 da qo'shiladi).

## Bajarish tartibi
1. Ijarachi oilaviy holat sheet'ini (`MaritalUploadSheet`) ochadi.
2. Holat: `PATCH /mobile/marital-status/update/` `{marital_status}` — `true` = turmush qurmagan (single).
3. Tasdiqlovchi fayllar: `POST /mobile/attachments/marital-status/` (multipart, har fayl `image` maydoni ostida takrorlanadi) → yaratilgan attachment yozuvlari (201).

## Qabul kriteriyalari (BDD)
- **GIVEN** ijarachi holatni tanladi **WHEN** saqlash bosiladi **THEN** `PATCH /mobile/marital-status/update/` `{marital_status}` yuboriladi.
- **GIVEN** bir yoki bir nechta fayl tanlandi **WHEN** yuklash bosiladi **THEN** `POST /mobile/attachments/marital-status/` multipart bilan yuboriladi va attachment ro'yxati qaytadi.

## Kod joylashuvi
- **Modul:** `lib/features/marital_status`
- **Sahifa / BLoC:** `MaritalUploadSheet` / `MaritalUploadCubit`; model `MaritalAttachmentModel`
- **Endpoint:** `PATCH /mobile/marital-status/update/` `{marital_status}`; `POST /mobile/attachments/marital-status/` (multipart `image`)

## Konflikt / farqlar
- ⚠ TZ «oilaviy holat, farzandlar va daromad» ni birga so'raydi; kod 1-bosqichda faqat **oilaviy holat** (bool) + fayllarni qamraydi — farzandlar/daromad alohida strukturalangan maydon sifatida hali yo'q. → [`_konfliktlar.md`](../_konfliktlar.md) B11.
