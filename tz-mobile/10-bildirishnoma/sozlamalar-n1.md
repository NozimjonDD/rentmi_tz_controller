# N1 — Bildirishnoma sozlamalarini boshqarish

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi    **Holat:** ❌ Amalga oshirilmagan (qisman UI)

## TZ manbai
N1 — Push-bildirishnoma sozlamalarini boshqarish · §4.2.1. Foydalanuvchi 'Sozlamalar' → 'Bildirishnomalar' bo'limida bildirishnoma **turlarini** va joriy holatlarini (yoqilgan/o'chirilgan) ko'radi, har birini yoqadi/o'chiradi; tizim saqlaydi va tanlovga muvofiq yuboradi.
> «Foydalanuvchi bildirishnomani yoqadi yoki o'chiradi; Tizim sozlamalarni saqlaydi va keyingi bildirishnomalarni tanlovi asosida yuboradi yoki yubormaydi.»
> Vaqt reglamenti: o'zgarishlarni saqlash — ≤2 s.

## Reliz / R5
- **RELIZ:** N1 — bildirishnoma turlarini boshqarish.
- **R5 o'zgarishi:** `R5-IJ-11` — «N1 sozlamalariga yangi turlar qo'shiladi» (narxi tushdi, yangi e'lonlar). ⚠ Baza N1 sozlamasi bo'lmagani uchun bu ham qo'shilmagan.

## Bajarish tartibi (TZ)
1. 'Sozlamalar' → 'Bildirishnomalar' ochiladi.
2. Bildirishnoma turlari va holatlari ko'rsatiladi.
3. Foydalanuvchi turni yoqadi/o'chiradi.
4. Tizim saqlaydi (≤2 s) va yuborishni tanlovga moslaydi.

## Qabul kriteriyalari (BDD)
- **GIVEN** sozlamalar sahifasi **WHEN** foydalanuvchi turni o'chiradi **THEN** ⚠ kodda **saqlanmaydi** — faqat sahifa hayoti davomida saqlanadi.
- **GIVEN** qurilmada push o'chirilgan **WHEN** foydalanuvchi ochadi **THEN** (TZ) qurilma sozlamalarida ruxsat berish taklifi — kodda alohida taklif yo'q.

## Kod joylashuvi
- **Sahifa:** `lib/features/settings/presentation/pages/app_settings_page.dart` — «Ilova sozlamalari» ichida **bitta** «Bildirishnomalar» toggle (`_NotificationsToggle`).
- **Holat:** `_notificationsEnabled` — **lokal UI holati**; kod izohi: «backend wiring (UpdateNotifications use case) is not implemented yet… persists for the lifetime of the page only».
- **Entity:** `AppSettings.notificationsEnabled` (`notifications_enabled` JSON) mavjud, lekin toggle unga ulanmagan; `UpdateNotifications` use-case yo'q.
- **Endpoint:** yo'q (bildirishnoma sozlamalari uchun mustaqil endpoint aniqlanmagan).

## Konflikt / farqlar
- ⚠ **N1 asosiy funksiyasi amalga oshirilmagan:** TZ **per-tur** yoqish/o'chirish + saqlash (≤2 s) talab qiladi; kodda esa faqat **bitta global toggle**, saqlanmaydi, turlar bo'yicha ajratmaydi. → [`_konfliktlar.md`](../_konfliktlar.md).
- ⚠ Guest'lar uchun toggle yashiriladi (account-scoped) — TZ mehmon holatini ajratmaydi.
- ⚠ R5-IJ-11 «yangi turlar» N1 ga qo'shilishi kerak edi — baza sozlama yo'qligi sabab qo'shilmagan.

---

## Release 5 — R5-IJ-11 — Narx va yangi e'lon bildirishnomalari
**Kod holati:** 🟡 (push bor; N1 sozlamalari amalda yo'q — ❌)

**User Story:** Ijarachi sifatida men saqlangan uy yoki filtrim bo'yicha narx tushganda va yangi e'lon chiqqanda xabar olishni xohlayman, shunda qulay imkoniyatni o'tkazib yubormayman.

**Tavsif:** Ikki yangi bildirishnoma turi: "Narxi tushdi" (saqlangan e'lon/filter) va "Yangi e'lonlar" (saqlangan filter). FCM push + tizim ichi. N1 sozlamalarida boshqariladi.

**Qabul mezonlari:**
- GIVEN ijarachi e'lonni saqlagan WHEN narx belgilangan foizdan ko'p tushsa THEN push va tizim ichi bildirishnoma
- GIVEN saqlangan filter mavjud WHEN unga mos yangi e'lon moderatsiyadan o'tsa THEN push
- GIVEN N1 sozlamalarida tur o'chirilgan WHEN hodisa yuz bersa THEN push kelmaydi, faqat tizim ichi xabar
