# Moderatsiya / shikoyat (UGC report)

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi    **Holat:** ✅ Bajarilgan

## TZ manbai
TZ mobil use-case'larida foydalanuvchi shikoyati alohida yozilmagan — moderatsiya asosan web (E4) va admin/moderator tomonida. Mobil ilovada foydalanuvchi kontenti (e'lon, foydalanuvchi) ustidan **shikoyat yuborish** App Store Guideline 1.2 va UGC talablari uchun qo'shilgan.
> Reliz: «Shikoyat kelganda moderator e'lonni ko'rib chiqadi, bloklaydi yoki ogohlantirish yuboradi» (`R3` moderator, admin veb).

## Reliz / R5
- **RELIZ:** `R3` — foydalanuvchi shikoyati (report), moderator ko'rib chiqadi (admin veb).
- **R5 o'zgarishi:** yo'q.

## Bajarish tartibi (kod)
1. E'lon/foydalanuvchi ustida «Shikoyat» → `report_bottom_sheet`.
2. Sabablar: `GET /mobile/moderation/report-reasons/?applies_to=` (kontent turiga qarab).
3. Foydalanuvchi sabab tanlaydi + ixtiyoriy izoh.
4. Yuborish: `POST /mobile/moderation/report/` `{content_type, object_id, reason_code, description?}`.
5. Natija: `SubmittedReport`; xatolar — `DuplicateReport` (409/`duplicate_report`), `Throttled` (429), `NotFound` (404).

## Qabul kriteriyalari (BDD)
- **GIVEN** e'lon **WHEN** foydalanuvchi shikoyat qiladi **THEN** sabab tanlash sheeti ochiladi va report yuboriladi.
- **GIVEN** ayni kontent bo'yicha takroriy shikoyat **WHEN** yuboriladi **THEN** `DuplicateReportException` (ko'p yuborishning oldi olinadi).
- **GIVEN** juda tez-tez shikoyat **WHEN** yuboriladi **THEN** `ThrottledException`.

## Kod joylashuvi
- **Modul:** `lib/features/moderation` — `ReportBloc` (`ReportEvent`/`ReportState`); `report_bottom_sheet`
- **Endpoint:** `GET /mobile/moderation/report-reasons/`, `POST /mobile/moderation/report/`
- **Entity:** `ReportReason`, `ReportableContent` (`content_type` + `object_id`), `SubmittedReport`
- **Ko'rilgan shikoyatlar:** `/settings/my-reports` route.

## Konflikt / farqlar
- Farq aniqlanmadi — mobil shikoyat oqimi backend moderatsiya (E4/R3) ni to'ldiradi.
- Moderatsiya natijasi bildirishnomasi (uy egasiga) → [`10-bildirishnoma/push-fcm.md`](../10-bildirishnoma/push-fcm.md) (`announcements/list/` route).
