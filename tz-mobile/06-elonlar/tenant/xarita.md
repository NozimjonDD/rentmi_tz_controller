# Xarita orqali qidirish

**Rollar:** 👤 Ijarachi / 👥 Mehmon    **Holat:** ✅ Bajarilgan

## TZ manbai
E3 — E'lonlarni qidirish va filtrlash · §4.2.1. Xarita — E3 ning muqobil ko'rinishi: e'lon joylashuvi xarita xizmati orqali koordinatalari bilan saqlanadi (§4.2.1 asosiy talab) va foydalanuvchi e'lonlarni geografik kesimda qidiradi.
> «Obyekt joylashuvi xarita xizmati orqali koordinatalari bilan saqlanadi.»

## Reliz / R5
- **RELIZ:** E3 doirasida katalogning muqobil ko'rinishi.
- **R5 o'zgarishi:** **R5-IJ-06** — Xarita ekrani: e'lon pinlari va klasterlar, xarita ustidagi chips (xona soni, Mebelli), "Ro'yhat bo'yicha" toggle, "N ta e'lon topildi" bottom sheet, saralash, banner-kirish; kartada qulayliklar ko'rsatiladi. QA talabi: xarita ≤5 s.

## Bajarish tartibi
1. Foydalanuvchi asosiy sahifadagi "Xarita orqali qidirish" bannerdan xaritani ochadi.
2. Kamera harakati/zoom o'zgarganda `GET /mobile/map/locations/` chaqiriladi: `zoom`, `ne_lat`, `ne_lng`, `sw_lat`, `sw_lng` + faol filtr paramlari.
3. Backend **klaster** yoki **property** ro'yxatini qaytaradi (`clusters`, `properties`, `total_count`); klasterlash server tomonida.
4. Zoom **≥16** da property rejimi — alohida e'lon pinlari; kichik zoom'da klasterlar.
5. Pin bosilsa `PropertyBottomSheet` e'lon kartasini ko'rsatadi; "N ta e'lon topildi" bottom sheet ro'yxat/saralash beradi.

## Qabul kriteriyalari (BDD)
- **GIVEN** xarita ochilgan **WHEN** kamera hududi o'zgaradi **THEN** joriy `bounds` va `zoom` bo'yicha pin/klaster ≤5 s ichida yangilanadi.
- **GIVEN** zoom ≥16 **WHEN** hudud yuklanadi **THEN** klaster o'rniga alohida e'lon pinlari ko'rinadi.
- **GIVEN** faol filtr **WHEN** xarita so'rovi yuboriladi **THEN** filtr paramlari (`category`, `min/max_price`, `districts`, `regions`, `is_furniture`) so'rovga qo'shiladi.

## Kod joylashuvi
- **Modul:** `lib/features/map`
- **Sahifa / BLoC:** `MapPage` / `MapCubit`; `map_marker_service.dart`, `property_bottom_sheet.dart`
- **Endpoint:** `GET /mobile/map/locations/` (`zoom`, `ne_lat/ne_lng/sw_lat/sw_lng`, filtr); kategoriyalar `GET /mobile/category/list/`

## Konflikt / farqlar
- ⚠ **Klasterlash — backend:** klaster hisobi va zoom bo'yicha rejim server tomonida; mobil faqat `bounds/zoom` yuboradi. TZ da klasterlash aniq belgilanmagan. → [`_konfliktlar.md`](../../_konfliktlar.md).
- ⚠ **Filtr to'liq emas:** xarita so'rovi filtrning bir qismini (narx, hudud, kategoriya, mebel) uzatadi; katalog filtridagi `area/floor/period/comfort` xaritaga o'tmaydi.
