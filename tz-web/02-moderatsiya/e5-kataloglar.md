# E5 — E'lon kataloglarini boshqarish

**Rollar:** 🔍 Moderator    **Holat:** ✅ (TZ da to'liq)

## TZ manbai
E5 · §4.1.1.4 · Moderator obyekt turlari, hududlar/tumanlar, foydalanish shartlari va boshqa **klassifikatorlarni** (kataloglarni) qo'shadi, tahrirlaydi yoki nofaol qiladi.
> «Tizim mavjud katalog ma'lumotnomalarini ko'rsatadi (obyekt turlari, hududlar/tumanlar, foydalanish shartlari va boshqa klassifikatorlar).»

## Reliz / R5
- **RELIZ / R5:** R5 da e'lon kataloglariga **yangi maydonlar** (minimal ijara davri, minimal skoring talabi) qo'shiladi va shu uchun moderatsiya ko'rinishi yangilanadi. Algoritm parametrlari (R5-AD-01) alohida administrator sozlamasi — bu tugunga kirmaydi. reliz admin bo'limi to'liq emas → W-K2.

## Ishga tushirish shartlari
Moderator web qismi quyi tizimiga kirgan va **moderator roliga** ega.

## Bajarish tartibi
1. Moderator 'Kataloglar' bo'limini ochadi.
2. Tizim mavjud katalog ma'lumotnomalarini ko'rsatadi (obyekt turlari, hududlar/tumanlar, foydalanish shartlari va boshqa klassifikatorlar).
3. Moderator yangi yozuv qo'shadi, mavjudini tahrirlaydi yoki nofaol qiladi.
4. Tizim o'zgarishlarni validatsiyadan o'tkazadi (**takrorlanmaslik tekshiruvi**).
5. O'zgarishlar saqlanadi va **e'lon yaratish (E1)** hamda **qidirish/filtrlash (E3)** formalarida darhol aks etadi.
6. Harakat audit jurnaliga yoziladi.

## Vaqt reglamenti
Katalogni yuklash — ≤3 s; o'zgarishlarni saqlash — ≤2 s.

## Qabul kriteriyalari (BDD)
- **GIVEN** moderator 'Kataloglar' bo'limida **WHEN** yangi yozuv qo'shadi **THEN** validatsiyadan o'tadi, saqlanadi va E1/E3 formalarida darhol ko'rinadi.
- **GIVEN** mavjud takroriy yozuv **WHEN** moderator qo'shmoqchi **THEN** tizim rad etadi (takrorlanmaslik tekshiruvi).
- **GIVEN** foydalanilayotgan katalog yozuvi **WHEN** moderator o'chirmoqchi **THEN** ogohlantirish chiqadi, faqat **nofaol qilish** taklif etiladi.

## Backend / API (kutilayotgan)
Web kodbaza yo'q → TZ asosida taxminiy (`/admin/...`):
- `GET /admin/catalogs/` — klassifikatorlar ro'yxati (obyekt turlari, hududlar, foydalanish shartlari).
- `POST /admin/catalogs/{type}/entries/` — yangi yozuv (takrorlanmaslik tekshiruvi bilan).
- `PATCH /admin/catalogs/{type}/entries/{id}/` — tahrirlash / nofaol qilish.
- Aniq yo'llar web repo berilganda tasdiqlanadi.

## Konflikt / farqlar
- ⚠ **Uzilgan havola:** §4.3.2 klassifikatorlar «batafsil 4.1.11 bandida» deydi, biroq **§4.1.11 TZ da mavjud emas** — klassifikatorlar aslida shu E5 (kataloglar boshqaruvi)da ta'riflangan. → [`_konfliktlar.md`](../_konfliktlar.md) W-B2.
