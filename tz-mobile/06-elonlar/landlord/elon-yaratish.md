# E'lon yaratish (E1)

**Rollar:** 🏠 Uy egasi    **Holat:** ✅ Bajarilgan

## TZ manbai
E1 — E'lon yaratish · §4.2.1 (9 qadam). Uy egasi obyekt parametrlarini kiritadi, fotosuratlarni yuklaydi (kamida 3, ko'pi 15), tizim validatsiya va joylashuvni xarita orqali tasdiqlaydi, e'lon 'moderatsiya kutmoqda' holatida saqlanadi va moderatsiya navbatiga (E4) qo'shiladi.
> «Uy egasi obyekt parametrlarini kiritadi (obyekt turi, joylashuv, maydon, xonalar soni, ijara narxi, muddati, tavsif, foydalanish shartlari); Fotosuratlarni yuklaydi (kamida 3 ta, ko'pi bilan 15 ta).»

## Reliz / R5
- **RELIZ:** E1 asosiy oqimi — obyekt parametrlari + fotosuratlar bilan e'lon yaratish; ishga tushirish sharti: identifikatsiyadan o'tgan, hisobi faol uy egasi.
- **R5 o'zgarishi:** **R5-UE-06** — yaratish/tahrirlash formasiga yangi maydonlar: **minimal ijara davri**, **kirish sanasi**, **minimal skoring talabi** (`min_tenant_score`); ijarachi skoring qismidagi eski tekst olib tashlanadi; formada shu hududdagi o'xshash e'lonlar narxi min/max ko'rsatiladi. Min skoring auditoriyasi: `GET /mobile/property/tenant-score/audience-count/?min_score=&max_score=`.

## Bajarish tartibi
1. Uy egasi "Yangi e'lon yaratish" ni tanlaydi; forma 5 tab bilan ochiladi (Overview / Basic info / Utilities / Checklist / Rental terms).
2. Ma'lumotnomalar yuklanadi: `/mobile/category/list/`, `/mobile/property/{checklist,entry-requirements,to-whom,nearby-comforts,equipments,utility,rental-rules}/list/`.
3. Foto: har rasm oldin `POST /mobile/attachment/create/` (multipart) orqali yuklanib **id** oladi (kamida 3).
4. Joylashuv xaritada tanlanadi (`select_location_page.dart`), koordinatalar saqlanadi.
5. Saqlash: `POST /mobile/announcements/create/` (**JSON**, `attachments_id[]`, `property_data`, `title`, `price`, `min_rent_period`, `min_tenant_score`, qulayliklar/qoidalar ro'yxatlari).
6. E'lon 'moderatsiya kutmoqda' holatida saqlanadi → E4 (web moderatsiya).

## Qabul kriteriyalari (BDD)
- **GIVEN** uy egasi formani to'ldirdi va ≥3 foto yukladi **WHEN** saqlaydi **THEN** e'lon `attachments_id[]` bilan yaratiladi va moderatsiyaga yuboriladi.
- **GIVEN** 3 tadan kam foto **WHEN** saqlash bosiladi **THEN** validatsiya to'xtatadi (`listing.dart:247` — `totalImageCount >= 3`).
- **GIVEN** min skoring talabi kiritildi **WHEN** auditoriya so'raladi **THEN** `audience-count` mos ijarachilar sonini qaytaradi.

## Kod joylashuvi
- **Modul:** `lib/features/listing`
- **Sahifa / BLoC:** `CreateListingPageNew` (5 tab: `tab_0_overview` … `tab_4_rental_terms`) / `ListingBloc`; `listing_photo_upload.dart`, `tenant_score_slider.dart`, `target_audience_section.dart`
- **Endpoint:** `POST /mobile/attachment/create/` (multipart) → `POST /mobile/announcements/create/` (JSON); ma'lumotnomalar `/mobile/property/*/list/`, `/mobile/category/list/`; `GET /mobile/property/tenant-score/audience-count/?min_score=&max_score=`

## Konflikt / farqlar
- ⚠ **Foto maksimal chegara:** TZ **max 15** ta talab qiladi; kodda faqat **min 3** tekshiriladi (`listing.dart:247/260`), 15 ta yuqori chegara ko'rinmaydi. → [`_konfliktlar.md`](../../_konfliktlar.md).
- ⚠ **Moderatsiya (E4) — web:** yangi e'lon 'moderatsiya kutmoqda' holatiga o'tadi; moderatsiyaning o'zi mobil emas, web/admin (`tz-web/`).
- ⚠ **R5 yangi maydonlar backendga bog'liq:** `min_tenant_score`, kirish sanasi, minimal ijara davri — backend sxema migratsiyasini talab qiladi (R5 dependency).

## Release 5 — R5-UE-06 — E'lon formasi yangi maydonlar va bozor ko'rsatkichi
**Kod holati:** 🟡 (ba'zi maydonlar bor)

**User Story:** Uy egasi sifatida men e'lonimda kirish sanasi, minimal ijara davri va skoring talabini belgilashni, hamda shu hududdagi o'xshash e'lonlar narxini ko'rishni xohlayman, shunda to'g'ri narx qo'yaman va mos ijarachilarni olaman.

**Tavsif:** E'lon formasiga maydonlar: minimal ijara davri, kirish sanasi, minimal skoring talabi. Ijarachi skoring qismidagi eski tushuntirish teksti olib tashlanadi. Narx maydonida shu hudud bo'yicha o'xshash faol e'lonlar narxi min–max ko'rsatiladi.

**Qabul mezonlari:**
- GIVEN forma ochildi WHEN hudud va parametrlar kiritilsa THEN "Shu hududda o'xshash uylar: N mln – M mln so'm" ko'rsatkichi chiqadi
- GIVEN o'xshash e'lonlar 3 tadan kam WHEN ko'rsatkich hisoblansa THEN diapazon ko'rsatilmaydi
- GIVEN minimal skoring talabi belgilangan WHEN e'lon saqlansa THEN "Sizga mos" va skoring-mos hisob-kitoblarda shu talab ishlatiladi
- GIVEN forma ochildi WHEN skoring bo'limi ko'rsatilsa THEN eski ijarachi-skoring teksti mavjud emas
