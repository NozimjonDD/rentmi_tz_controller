# T1 — Murojaat yuborish (qo'llab-quvvatlash)

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi (👥 mehmon → faqat Telegram)    **Holat:** 🟡 Qisman (statik kontakt)

## TZ manbai
T1 — Murojaat yuborish · §4.2.1 (Texnik qo'llab-quvvatlash moduli). Foydalanuvchi 'Yordam' bo'limini ochadi, kategoriya (texnik muammo / shikoyat / taklif) tanlaydi, mavzu va tavsif kiritadi, ixtiyoriy fayl biriktiradi, yuboradi; tizim **noyob ticket raqami** beradi, murojaat admin panelida support xodimiga ko'rinadi.
> «Tizim saqlaydi, noyob ticket raqami beradi; Foydalanuvchiga tasdiq ko'rsatiladi (ticket raqami va taxminiy javob muddati).»
> «Guest foydalanuvchilar tizim ichidagi murojaat formasidan foydalana olmaydi — ular uchun rasmiy Telegram kanal orqali bog'lanish taqdim etiladi.»

## Reliz / R5
- **RELIZ:** reliz eksportida T1 bo'yicha alohida US yo'q (support xodimi paneli admin tomonda).
- **R5 o'zgarishi:** yo'q.

## Bajarish tartibi (kod)
1. Profil → «Qo'llab-quvvatlash» ochiladi (`SupportPage`, Figma 1:39).
2. Hero karta (tavsif) + «Biz shu yerda» kontakt ro'yxati.
3. Kontakt qatorlari: **Telegram / telefon / email** — har biri `url_launcher` bilan OS handler'ini ochadi (`tel:`, `mailto:`, Telegram URL).
4. Qiymatlar `AppConstants` dan (login «Yordam» sheeti bilan bir xil).

## Qabul kriteriyalari (BDD)
- **GIVEN** foydalanuvchi (yoki guest) **WHEN** «Qo'llab-quvvatlash» ochiladi **THEN** Telegram/telefon/email kontaktlari ko'rsatiladi.
- **GIVEN** Telegram qatori **WHEN** bosiladi **THEN** Telegram ilovasi ochiladi.
- **GIVEN** TZ formasi (kategoriya/mavzu/tavsif/fayl) **WHEN** izlanadi **THEN** ⚠ mavjud emas.

## Kod joylashuvi
- **Modul:** `lib/features/support` — faqat `presentation/pages/support_page.dart` (statik `StatelessWidget`, data/domain qatlami yo'q)
- **Bog'liq:** kontaktlar `AppConstants` (supportTelegramUrl/Handle, supportPhoneDial/Display, supportEmail)
- **Endpoint:** yo'q — hech qanday murojaat/ticket API chaqirilmaydi.

## Konflikt / farqlar
- ⚠ **Chipta (ticket) tizimi yo'q:** TZ T1 kategoriya, mavzu, tavsif, fayl biriktirish va **noyob ticket raqami** bilan formani talab qiladi; kodda esa faqat **statik kontakt sahifasi** (Telegram/telefon/email). Backend murojaat endpointi chaqirilmaydi. → [`_konfliktlar.md`](../_konfliktlar.md).
- Guest holati moslashadi: TZ guest'ni Telegram'ga yo'naltiradi — kodda hamma uchun Telegram/telefon/email (guest ham foydalanadi).
- Chipta-simon (record yaratuvchi) eng yaqin oqimlar boshqa modullarda: shikoyat ([`moderation-shikoyat.md`](moderation-shikoyat.md)) va hisobot tarifi ([`report-service.md`](report-service.md)) — lekin ular T1 murojaat emas.
