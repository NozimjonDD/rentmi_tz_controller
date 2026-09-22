# Tashqi platformadan import

**Rollar:** 🏠 Uy egasi    **Holat:** ✅ Bajarilgan

## TZ manbai
E1 — E'lon yaratish · §4.2.1. Tashqi import TZ da alohida ssenariy sifatida yozilmagan — bu E1 yaratish formasini boshqa platformadagi e'lon ma'lumotlari bilan **oldindan to'ldirish** qulayligi. Yakuniy e'lon baribir E1 oqimi bo'yicha saqlanadi va moderatsiyaga (E4) yuboriladi.
> «Uy egasi obyekt parametrlarini kiritadi … tizim ma'lumotlarni validatsiyadan o'tkazadi.»

## Reliz / R5
- **RELIZ:** to'g'ridan-to'g'ri manba yo'q — kod qulayligi.
- **R5 o'zgarishi:** yo'q (R5 e'lon formasi maydonlariga tegishli, importga emas).

## Bajarish tartibi
1. Uy egasi e'lon yaratishda "Import" bottom sheet'ini ochadi (`import_bottom_sheet.dart`).
2. Platforma tanlanadi: **OLX** (`olx.uz`), **Uybor** (`uybor.uz`), **Joyme** (`joyme.uz`) — `ImportPlatform` enum.
3. E'lon havolasi kiritiladi (`import_link_sheet.dart`).
4. `POST /mobile/platform/link/` `{link}` — backend havolani parse qiladi va `ParsedListingResponse` qaytaradi.
5. Parse natijasi yaratish formasini oldindan to'ldiradi; uy egasi tekshiradi/tahrirlaydi va E1 bo'yicha saqlaydi.

## Qabul kriteriyalari (BDD)
- **GIVEN** to'g'ri e'lon havolasi **WHEN** import so'raladi **THEN** `POST /mobile/platform/link/` parse qilingan maydonlarni qaytaradi va forma to'ldiriladi.
- **GIVEN** noto'g'ri/parse bo'lmaydigan havola **WHEN** yuboriladi **THEN** xatolik ko'rsatiladi, forma bo'sh qoladi.
- **GIVEN** parse qilingan e'lon **WHEN** saqlanadi **THEN** oddiy E1 oqimi (attachment + create + moderatsiya) qo'llanadi.

## Kod joylashuvi
- **Modul:** `lib/features/listing`
- **Sahifa / BLoC:** `import_bottom_sheet.dart`, `import_link_sheet.dart`, `import_platform_sheet.dart`, `ImportPlatform` (`import_platform.dart`) / `ListingBloc`
- **Endpoint:** `POST /mobile/platform/link/` `{link}` → `ParsedListingResponse`

## Konflikt / farqlar
- ⚠ **Platforma identifikatori yuborilmaydi:** parse so'roviga faqat `link` boradi, tanlangan platforma backendga uzatilmaydi (`import_platform.dart` izohi). → [`_konfliktlar.md`](../../_konfliktlar.md).
- ⚠ **Manba nomlari:** kodda OLX/Uybor/Joyme (uch platforma); "Uysot"/"Joymee" varianti kodda yo'q — hujjatlarda kodga mos nomlash ishlatilsin.
