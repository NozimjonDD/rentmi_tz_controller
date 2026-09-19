# Uy egasi ommaviy profili

**Rollar:** 👤 Ijarachi / 👥 Mehmon    **Holat:** ❌ Yo'q (R5 rejalashtirilgan)

## TZ manbai
TZ (§4.2.1) da alohida "uy egasi ommaviy profili" ssenariysi yo'q — bu R5 ning ishonch mexanizmi. TZ faqat e'lon egasiga so'rov yuborish (E3 → R1) va identifikatsiya/tegishlilikni (U5) belgilaydi; ommaviy profil shu ma'lumotlarni ijarachiga ko'rsatish uslubidir.
> «Tegishlilik (U5 9-qadam): mulk uy egasining davlat bazasidan yuklangan mulklar ro'yxatida bo'lishi.»

## Reliz / R5
- **RELIZ:** to'g'ridan-to'g'ri manba yo'q (R5 yangiligi).
- **R5 o'zgarishi:** **R5-IJ-08** — e'lon detail'dagi uy egasi blokidan **ommaviy profil** sahifasiga o'tiladi: *Rentmi'da N vaqt*, *e'lonlar soni*, "**Tasdiqlangan uy egasi** — shaxsi va hujjatlari Rentmi tomonidan tekshirilgan", javob berish odati (javob vaqti), tegishli (faol) e'lonlar. Xavfsizlik xabari: "faqat platforma orqali muloqot qiling". Eslatma: reyting va "Rentmi kafolati" bloklari R5 buildida **yashiriladi** (RelizF). Backend: "Uy egasi ommaviy profil endpointi".

## Bajarish tartibi
1. Ijarachi e'lon detail'dagi uy egasi blokini bosadi (kodda `ownerName`/`ownerUserId` mavjud).
2. *(rejalashtirilgan)* Ommaviy profil endpointi chaqiriladi: Rentmi'da vaqt, e'lonlar soni, tasdiqlanganlik (identifikatsiya + tegishlilik), javob vaqti, faol e'lonlar.
3. *(rejalashtirilgan)* "Tasdiqlangan uy egasi" belgisi va "faqat platforma orqali muloqot" xabari ko'rsatiladi.

## Qabul kriteriyalari (BDD)
- **GIVEN** e'lon detail'da uy egasi bloki **WHEN** bosiladi **THEN** *(R5 maqsadi)* ommaviy profil ochiladi: tasdiqlanganlik, Rentmi'da vaqt, javob vaqti, tegishli e'lonlar.
- **GIVEN** R5 build **WHEN** profil ochiladi **THEN** reyting va "Rentmi kafolati" bloklari ko'rinmaydi (yashirilgan — RelizF).
- **GIVEN** tegishlilik ma'lumoti yo'q **WHEN** profil yuklanadi **THEN** "Tasdiqlangan uy egasi" belgisi chiqmaydi (default: ko'rsatmaslik).

## Kod joylashuvi
- **Modul:** — (alohida modul yo'q; kirish nuqtasi `lib/features/announcements` detail'ida)
- **Sahifa / BLoC:** — (ommaviy profil sahifasi/BLoC kodda yo'q); `Announcement` entity'da `ownerName`, `ownerUserId`, `isOwner` maydonlari mavjud (`announcement.dart:58`)
- **Endpoint:** — (R5 backend "uy egasi ommaviy profil endpointi" kutilmoqda; kodda topilmadi). ⚠ `landlord_dashboard` dagi `getLandlordProfile` — uy egasining **o'z** dashboard profili, ommaviy profil emas.

## Konflikt / farqlar
- ⚠ **R5-IJ-08 amalga oshirilmagan:** ommaviy profil ekrani, endpointi va "Tasdiqlangan uy egasi" bloki kodda yo'q — faqat `ownerName`/`ownerUserId` uzatiladi. → [`_konfliktlar.md`](../../_konfliktlar.md) E-K6.
- ⚠ **Adashtirmaslik:** `landlord_dashboard/domain/entities/landlord_profile.dart` uy egasining shaxsiy dashboard profili — ijarachi ko'radigan ommaviy profil bilan bir narsa emas.
