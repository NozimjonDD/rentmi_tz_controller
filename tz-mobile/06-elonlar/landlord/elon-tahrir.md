# E'lonni tahrirlash / o'chirish (E2)

**Rollar:** 🏠 Uy egasi    **Holat:** ✅ Bajarilgan

## TZ manbai
E2 — E'lonni tahrirlash yoki o'chirish · §4.2.1 (7 qadam, E1 ga kengaytma). Uy egasi "Mening e'lonlarim" dan e'lonni tanlaydi; tahrirlash, faol/nofaol qilish yoki o'chirish mumkin. Jiddiy o'zgarish (joylashuv, mulk turi, maydon, xonalar soni) qayta moderatsiyaga yuboradi; narx o'zgarishi qayta moderatsiya talab qilmaydi. O'chirishda arxivga ko'chiriladi.
> «Jiddiy o'zgarishlar (joylashuv manzili, mulk turi, maydon, xonalar soni) bo'lsa e'lon qayta moderatsiyaga yuboriladi; narx o'zgarishi qayta moderatsiyani talab etmaydi.»

## Reliz / R5
- **RELIZ:** E2 asosiy oqimi — tahrir / faol-nofaol / o'chirish; audit jurnaliga yozish.
- **R5 o'zgarishi:** tahrirlash formasi R5-UE-06 yangi maydonlarini (minimal ijara davri, kirish sanasi, min skoring) o'z ichiga oladi — yaratish bilan bir forma. Lifecycle statuslari (**bron** — "rezerv" o'rniga) R5 terminologiyasiga mos.

## Bajarish tartibi
1. Uy egasi "Mening e'lonlarim" dan e'lonni tanlaydi ([`mulklarim.md`](mulklarim.md)).
2. E'lon menyusi mumkin bo'lgan amallarni beradi (`announcement_detail_menu.dart`, `property_actions_menu.dart`).
3. **Tahrir:** `PUT /mobile/announcements/update/{id}/` — o'zgartirishlar, validatsiya; jiddiy o'zgarishlarda qayta moderatsiya.
4. **Lifecycle (faol/nofaol va h.k.):** `POST /mobile/property/announcements/{id}/{archive|unarchive|paused|reserved}/`.
5. **O'chirish:** tasdiq so' raladi → `DELETE /mobile/announcements/delete/{id}/` → arxivga ko'chiriladi.

## Qabul kriteriyalari (BDD)
- **GIVEN** uy egasi narxni o'zgartiradi **WHEN** saqlaydi **THEN** e'lon qayta moderatsiyasiz yangilanadi.
- **GIVEN** joylashuv/xonalar o'zgardi **WHEN** saqlaydi **THEN** e'lon qayta moderatsiyaga yuboriladi.
- **GIVEN** faol ijara so'rovlari mavjud e'lon **WHEN** o'chirish bosiladi **THEN** ogohlantirish va tasdiq so'raladi, so'ng arxivlanadi.

## Kod joylashuvi
- **Modul:** `lib/features/listing` (tahrir) + `lib/features/announcements` (o'chirish, lifecycle)
- **Sahifa / BLoC:** `CreateListingPageNew` (edit rejimi) / `ListingBloc`; `announcement_detail_menu.dart`, `property_actions_menu.dart`; usecase'lar `delete_announcement`, `archive_announcement`, `unarchive_announcement`, `pause_announcement`, `reserve_announcement`
- **Endpoint:** `PUT /mobile/announcements/update/{id}/`; `DELETE /mobile/announcements/delete/{id}/`; `POST /mobile/property/announcements/{id}/{archive\|unarchive\|paused\|reserved}/`

## Konflikt / farqlar
- ⚠ **Amal ikki modulda:** tahrir `listing` da (`listing_remote_data_source.dart:535`), o'chirish/lifecycle `announcements` da (`announcements_remote_data_source.dart`) — bitta E2 use-case, ikki modul. → [`_konfliktlar.md`](../../_konfliktlar.md) E-K7.
- ⚠ **Qayta moderatsiya mantiqi backendda:** "jiddiy o'zgarish" aniqlanishi (joylashuv/tur/maydon/xonalar) server tomonida; mobil faqat `PUT update` yuboradi.
- ⚠ **Terminologiya:** lifecycle `reserved` ↔ R5 UI "bron" (avval "rezerv").
