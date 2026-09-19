# So'rovni ko'rib chiqish (qabul / rad)

**Rollar:** 🏠 Uy egasi    **Holat:** 🟡 Qisman

## TZ manbai
R2 — Ijara so'rovini ko'rib chiqish · §4.2.1. Uy egasi kiruvchi so'rovlarni holati bo'yicha ko'radi, tafsilotni ochadi va qaror qabul qiladi (tasdiqlash / rad etish / qo'shimcha savol). Tasdiqlangach kontakt ma'lumotlari ochiladi.
> «Uy egasi qaror qabul qiladi: tasdiqlash / rad etish / qo'shimcha savollar berish; Tasdiqlash: so'rov 'tasdiqlangan' holatga o'tadi, ijarachiga bildirishnoma yuboriladi va uy egasining kontakt ma'lumotlari ochib beriladi…»

## Reliz / R5
- **RELIZ:** `R4 · Uy egasi — So'rovlar boshqaruvi` — so'rovlarni ko'rish, qaror qabul qilish.
- **R5 o'zgarishi:** `R5-UE-01` — tab'lar (Barchasi / Yangi / Rad etilgan / Tasdiqlangan), ijarachi kartasida yangi maydonlar (kirish sanasi, byudjet max, ijara muddati, oila tarkibi), "Talablaringizga mos" badge, Qabul qilish / Rad qilish.

## Bajarish tartibi (kod)
1. Global inbox: `GET /mobile/homeowner/requests/list/?tab=new|approved|rejected|contracts` (tab'lar fon'da preload → instant almashuv).
2. Yoki bitta mulk bo'yicha: `GET /mobile/homeowner/rental-requests/list/?property=&status=`.
3. Detal bottom sheet: ijarachi ma'lumotlari + skoring (`tenant_scoring_detail_page`).
4. **Qabul:** `PATCH /mobile/requests/update/{id}/` `{status:'approved', announcement}` → ijarachiga bildirishnoma, kontakt ochiladi.
5. **Rad:** `PATCH … {status:'rejected', announcement}`.
6. **To'liq hisobot so'rash:** `PATCH … {report_status:'pending'}` → ijarachiga REPORT_PENDING bildirishnoma.

## Qabul kriteriyalari (BDD)
- **GIVEN** yangi so'rov **WHEN** uy egasi Qabul qiladi **THEN** `{status:'approved'}` yuboriladi, ijarachiga bildirishnoma va kontakt ochiladi.
- **GIVEN** so'rov **WHEN** uy egasi Rad qiladi **THEN** `{status:'rejected'}` yuboriladi.
- **GIVEN** ijarachi to'liq skoring hisobotini bermagan **WHEN** uy egasi so'raydi **THEN** `{report_status:'pending'}` yuboriladi.

## Kod joylashuvi
- **Modul:** `lib/features/landlord_requests` (global) · `lib/features/rental_requests` (bitta mulk)
- **Sahifa / BLoC:** `LandlordRequestsOverviewPage`, `LandlordRequestsPage` / `LandlordRequestsBloc` (`LandlordRequestsTab{newRequests, approved, rejected, contracts}` → `apiValue` new/approved/rejected/contracts); `landlord_detail_action_buttons`, `request_card_action_buttons`
- **Endpoint:** `GET /mobile/homeowner/requests/list/`, `GET /mobile/homeowner/rental-requests/list/`, `PATCH /mobile/requests/update/{id}/`
- **Nuans:** landlord kartalari `announcement` sifatida sarlavha matnini qaytaradi (int id emas), shuning uchun PATCH oldidan `fetchAnnouncementId` detail endpoint orqali int id ni oladi.

## Konflikt / farqlar
- ⚠ **"Qo'shimcha savol / muhokama" amali yo'q** — kodda faqat Qabul / Rad; TZ 'muhokama davom etmoqda' holati amalga oshirilmagan. → [`_konfliktlar.md`](../../_konfliktlar.md).
- ⚠ Global inbox'da 4-tab **`contracts`** mavjud (uyquda turgan shartnoma funksiyasiga bog'liq) — [`12-contract-dormant/`](../../12-contract-dormant/about.md).
- ⚠ Rad etishda "sabab" kiritish maydoni TZ da ixtiyoriy — kodda alohida sabab formasi yo'q (status faqat `rejected`).
