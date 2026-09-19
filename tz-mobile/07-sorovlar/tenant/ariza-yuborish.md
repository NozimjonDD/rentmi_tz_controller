# Ariza yuborish (ijara so'rovi)

**Rollar:** 👤 Ijarachi    **Holat:** 🟡 Qisman

## TZ manbai
R1 — Ijara so'rovini yuborish · §4.2.1. Ijarachi (tizimga kirgan, ijarachi roli, identifikatsiyadan o'tgan) faol e'lon uchun so'rov formasini to'ldiradi; tizim Rentmi balini tekshiradi, so'rovni 'ko'rib chiqish kutmoqda' holatida saqlaydi va uy egasiga bildirishnoma yuboradi.
> «Tizim so'rov formasini ko'rsatadi (qo'shimcha savol va malumotlar…); … Tizim ijarachining Rentmi balini tekshiradi; ball mavjud bo'lmasa, S1 … taklif qilinadi.»
> Kiruvchi ma'lumotlar: «E'lon identifikatori, ko'chib kelish sanasi, budjet malumoti, ijara muddati, qo'shimcha xabar (ixtiyoriy).»

## Reliz / R5
- **RELIZ:** `IJ-R1 — Ijara so'rovini yuborish` `R4` — Rentmi bali tekshiriladi: mavjud va muddati o'tmagan bo'lsa davom etadi, aks holda S1 (Rentmi hisobotini xarid qilish) taklif qilinadi; CTA `R5-IJ-08`: «Ariza jo'natish» (terminologiya).
- **R5 o'zgarishi:** `R5-IJ-09` — so'rov formasiga yangi maydonlar qo'shilishi kerak: **kirish sanasi, byudjet (max), ijara muddati, to'lov kuni**. ⚠ Kodda bu maydonlar amalga oshirilmagan.

## Bajarish tartibi (kod)
1. E'lon detalida "Ariza jo'natish" bosiladi.
2. Identifikatsiya tekshiriladi — o'tmagan bo'lsa `verification_required_sheet` ko'rsatiladi (R1 identifikatsiya talabi).
3. Rentmi bali tekshiriladi — yo'q bo'lsa `purchase_required_dialog` (S1 taklif).
4. `RentalRequestDialog` bottom sheet ochiladi: e'lon kartasi (rasm, narx, xonalar) + **bitta erkin matn maydoni**.
5. Yuborish → `POST /mobile/rental-request/create/` `{property, announcement, text}`.
6. Muvaffaqiyatda tasdiq ko'rsatiladi; ro'yxat yangilanadi.

## Qabul kriteriyalari (BDD)
- **GIVEN** identifikatsiyadan o'tmagan ijarachi **WHEN** "Ariza jo'natish" bosiladi **THEN** identifikatsiya talab sheeti chiqadi, forma ochilmaydi.
- **GIVEN** Rentmi bali yo'q ijarachi **WHEN** ariza boshlanadi **THEN** S1 (hisobot xarid) taklif dialogi chiqadi.
- **GIVEN** to'g'ri holat **WHEN** matn kiritilib yuboriladi **THEN** so'rov `pending` holatda yaratiladi va uy egasiga bildirishnoma ketadi.

## Kod joylashuvi
- **Modul:** `lib/features/tenant_requests`
- **Sahifa / BLoC:** `RentalRequestDialog`, `TenantRequestsPage` / `TenantRequestsBloc` (`CreateRentalRequestEvent`); gate widgetlari `verification_required_sheet`, `purchase_required_dialog`
- **Endpoint:** `POST /mobile/rental-request/create/` `{property, announcement, text}` → 201
- Rentmi bal tekshiruvi mijoz tomonida amalga oshiriladi (S1 oqimi → [`04-skoring/`](../../04-skoring/about.md)).

## Konflikt / farqlar
- ⚠ **Tuzilgan maydonlar yo'q:** TZ (kirish sanasi, byudjet, ijara muddati) va R5-IJ-09 (kirish sanasi, byudjet max, ijara muddati, to'lov kuni) maydonlarini forma **to'plamaydi** — faqat `text` erkin matn yuboriladi. → [`_konfliktlar.md`](../../_konfliktlar.md).
- Chat imkoniyati (TZ 2-qadam) so'rov formasida emas, alohida chat modulida — [`08-chat/`](../../08-chat/about.md).
- Takroriy so'rov taqiqi va blacklist tekshiruvi backend zimmasida (mijozda alohida oqim yo'q).
