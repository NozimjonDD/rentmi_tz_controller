# Saqlangan uylar (Favorites / wishlist)

**Rollar:** 👤 Ijarachi    **Holat:** ✅ Bajarilgan

## TZ manbai
E3 — E'lonlarni qidirish va filtrlash · §4.2.1. TZ E3 filtrni **saqlash** imkoniyatini beradi; e'lonning o'zini saqlash (wishlist) — reliz Saqlanganlar sahifasining bir tabidir ("Saqlangan uylar"), E3 saqlash mantiqining kengaytmasi.
> «Qo'shimcha: ro'yxatdan o'tgan foydalanuvchi filtrlarni saqlashi mumkin.»

## Reliz / R5
- **RELIZ:** navbarda **Saved (Saqlanganlar)** bo'limi.
- **R5 o'zgarishi:** **R5-IJ-05** — Saqlanganlar sahifasi **2 tab**: *Saqlangan uylar* (wishlist) / *Saqlangan filterlar*. Ushbu tugun birinchi tabni (uylar) qamraydi; ikkinchisi — [`qidiruv-filtr.md`](qidiruv-filtr.md).

## Bajarish tartibi
1. Foydalanuvchi navbardan Saqlanganlar → "Saqlangan uylar" tabini ochadi.
2. `GET /mobile/wishlist/` — saqlangan e'lonlar va kategoriyalar (`categories` / `category_counts`) keladi (`page/page_size=20`).
3. E'lonni saqlash/olib tashlash (toggle): `GET /mobile/wishlist/update/?announcement_id={id}`.
4. Kategoriya tab'lari bo'yicha ro'yxat filtrlanadi (`favorites_tab_bar.dart`).

## Qabul kriteriyalari (BDD)
- **GIVEN** ijarachi kartadagi yurakcha bosadi **WHEN** toggle chaqiriladi **THEN** e'lon wishlist'ga qo'shiladi/olib tashlanadi va ro'yxat yangilanadi.
- **GIVEN** bo'sh wishlist **WHEN** sahifa ochiladi **THEN** empty-state (`favorites_empty_state.dart`) ko'rsatiladi.
- **GIVEN** kategoriyali javob **WHEN** tab tanlanadi **THEN** shu kategoriyaga tegishli e'lonlar ko'rinadi.

## Kod joylashuvi
- **Modul:** `lib/features/favorites`
- **Sahifa / BLoC:** `FavoritesPage` / `FavoritesBloc`; `favorite_item_card.dart`, `favorites_tab_bar.dart`, `favorites_empty_state.dart`
- **Endpoint:** `GET /mobile/wishlist/`; `GET /mobile/wishlist/update/?announcement_id=`

## Konflikt / farqlar
- ⚠ **GET-mutatsiya:** wishlist o'zgarishi holat o'zgartiruvchi bo'lsa-da `GET /mobile/wishlist/update/` orqali bajariladi (POST/DELETE emas) — REST semantikasiga zid. → [`_konfliktlar.md`](../../_konfliktlar.md) E-K4.
- ⚠ **`isFavorite` doim `false`:** lokal tekshiruv `isFavorite()` har doim `false` qaytaradi (`favorites_remote_data_source.dart:171`) — saqlangan holat home/list javobidagi `is_favorited` ga tayanadi.

---

## Release 5 — R5-IJ-05 — Saqlanganlar sahifasi
**Kod holati:** ✅

**User Story:** Ijarachi sifatida men saqlangan uylar va filtrlarimni bitta joyda ko'rishni xohlayman, shunda qidiruvimni davom ettirishim oson bo'ladi.

**Tavsif:** "Saqlanganlar" sahifasi 2 tab: Saqlangan uylar / Saqlangan filterlar. Har filtr kartasida parametrlar, "N ta e'lon bor" va "+N ta yangi" badge.

**Qabul mezonlari:**
- GIVEN saqlangan filtrlar mavjud WHEN sahifa ochilsa THEN har filtr parametrlari va e'lonlar soni bilan ko'rinadi
- GIVEN filtr saqlangandan keyin yangi mos e'lonlar qo'shilgan WHEN sahifa ochilsa THEN "+N ta yangi" badge ko'rinadi
- GIVEN filtr kartasi bosildi WHEN ro'yxat ochilsa THEN yangi e'lonlar birinchi ko'rsatiladi va badge nolga tushadi
