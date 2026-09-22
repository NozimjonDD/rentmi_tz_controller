# Qidiruv va filtr (+ saqlangan filtrlar)

**Rollar:** 👤 Ijarachi / 👥 Mehmon    **Holat:** ✅ Bajarilgan

## TZ manbai
E3 — E'lonlarni qidirish va filtrlash · §4.2.1 (3–6 qadam). Foydalanuvchi qidiruv/filtr parametrlarini kiritadi (hudud, narx oralig'i, obyekt turi, maydon, xonalar soni va boshqalar), tizim mos e'lonlarni shakllantiradi; ro'yxatdan o'tgan foydalanuvchi filtrlarni saqlashi, mos yangi e'lon paydo bo'lganda bildirishnoma olishi mumkin.
> «Foydalanuvchi qidiruv yoki filtr parametrlarini kiritadi (hudud, narx oralig'i, obyekt turi, maydon, xonalar soni va boshqalar); Tizim filtrlarga mos e'lonlarni shakllantiradi va ko'rsatadi.»

## Reliz / R5
- **RELIZ:** E3 asosiy oqimi — katalog + ko'p mezonli filtr; guest filtr saqlamoqchi bo'lsa U1 (ro'yxatdan o'tish) taklif qilinadi; saqlangan filtr bo'yicha yangi e'lon → push.
- **R5 o'zgarishi:** **R5-IJ-04** — narx qiymatlarini yaxlitlash (so'mda mln qadam, dollarda 100$ qadam), so'm/dollar toggle, «Filterni saqlash» va «Filterni tozalash» tugmalari. **R5-IJ-05** — Saqlanganlar sahifasi 2 tab (Saqlangan uylar / Saqlangan filterlar), har filtr kartasida "N ta e'lon bor" va "+N ta yangi" badge.

## Bajarish tartibi
1. Katalog ochiladi: `GET /mobile/announcements/tenant/list/` (filtr paramsiz — barcha faol e'lonlar, `page/page_size=5`).
2. Filtr opsiyalari yuklanadi: `GET /mobile/regions/`, `/category/list/`, `/property/equipments/list/`, `/property/nearby-comforts/list/`.
3. Foydalanuvchi filtrni to'ldiradi; `AnnouncementFilter.toQueryParams()` query paramlarni shakllantiradi (`districts`, `regions`, `min_price/max_price` yoki `min_price_usd/max_price_usd`, `category`, `period`, `created_at`, `comfort_equipment_ids`, `nearby_comfort_ids`, `is_furniture`, `search`, `area_from/to`, `floor_from/to`).
4. Ro'yxat qayta yuklanadi; "load more" URL asosida keyingi sahifani oladi.
5. Ro'yxatdan o'tgan foydalanuvchi filtrni saqlaydi: `POST /mobile/saved-filters/` (`FilterSessionCubit`); saqlanganlar ro'yxati `GET /mobile/saved-filters/list/`, yangilash `PUT …/update/{id}/`, o'chirish `DELETE …/delete/{id}/`.

## Qabul kriteriyalari (BDD)
- **GIVEN** faol filtr (hudud + narx) **WHEN** qo'llaniladi **THEN** mos e'lonlar ≤5 s ichida shakllanadi va ro'yxat yangilanadi.
- **GIVEN** hech bir e'lon mos kelmadi **WHEN** natija bo'sh **THEN** 'mos e'lon topilmadi' va filtrlarni yumshatish taklifi.
- **GIVEN** ro'yxatdan o'tgan ijarachi **WHEN** filtrni saqlaydi **THEN** Saqlanganlar → "Saqlangan filterlar" tabida karta paydo bo'ladi; guest bo'lsa U1 taklif qilinadi.

## Kod joylashuvi
- **Modul:** `lib/features/announcements`
- **Sahifa / BLoC:** `AnnouncementsListPage`, `AnnouncementFilterPage` / `AnnouncementsBloc`, `FilterCubit`, `FilterSessionCubit`; filtr entity `AnnouncementFilter`
- **Endpoint:** `GET /mobile/announcements/tenant/list/`; opsiyalar `/mobile/regions/`, `/category/list/`, `/property/{equipments,nearby-comforts}/list/`; saqlangan filtr `GET/POST /mobile/saved-filters/list/`, `/saved-filters/`, `PUT …/update/{id}/`, `DELETE …/delete/{id}/`

## Konflikt / farqlar
- ⚠ **Clean Arch chetlab:** `FilterSessionCubit` `DioClient` ni to'g'ridan-to'g'ri chaqiradi (repository/usecase qatlamisiz) — modul ichidagi boshqa oqimlardan farq qiladi. → [`_konfliktlar.md`](../../_konfliktlar.md) E-K3.
- ⚠ **rooms/pets faqat frontend:** filtr `rooms_min`, `rooms_max`, `pets` yuboradi, ammo backend spec kutilmoqda (`announcement_filter.dart:381` — "backend ignores unknown params harmlessly"). → E-K5.
- ⚠ **Sahifalash:** `page_size=5` — TZ da sahifa hajmi ko'rsatilmagan.

---

## Release 5 — R5-IJ-04 — Filter yangilanishi
**Kod holati:** ✅ (rooms/pets frontend-only — E-K5)

**User Story:** Ijarachi sifatida men narx filtrini qulay qadamlar bilan sozlashni xohlayman, shunda keraksiz aniq raqamlar bilan ovora bo'lmayman.

**Tavsif:** Narx maydonlari va slider so'mda mln qadamga, dollarda 100$ qadamga yaxlitlanadi; so'm/dollar toggle. "Filterni saqlash" va "Filterni tozalash" tugmalari. Saqlangan filtrlar mantig'i qayta ko'rib chiqiladi.

**Qabul mezonlari:**
- GIVEN valyuta so'm WHEN slider surilsa THEN qiymat mln qadam bilan (5 000 000 → 6 000 000)
- GIVEN valyuta dollar WHEN slider surilsa THEN qiymat 100$ qadam bilan
- GIVEN filter to'ldirilgan WHEN "Filterni saqlash" bosilsa THEN filter Saqlanganlar sahifasida paydo bo'ladi
- GIVEN filter to'ldirilgan WHEN "Filterni tozalash" bosilsa THEN barcha maydonlar default holatga qaytadi
