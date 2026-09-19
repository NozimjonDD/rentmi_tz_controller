# Profil ko'rish va tahrirlash

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi    **Holat:** ✅ Bajarilgan (⚠ tahrir cubit mock)

## TZ manbai
U4 — Foydalanuvchi profilini boshqarish · §4.1.1.4. Foydalanuvchi profilni ko'radi (shaxsiy, aloqa, Rentmi bali, hisobotlar) va shaxsiy ma'lumotlarni tahrirlaydi.
> «2) Tizim joriy ma'lumotlarni (shaxsiy, aloqa, Rentmi bali, hisobotlar) ko'rsatadi; … 6) Foydalanuvchi o'zgarishlarni saqlaydi; 7) Tizim validatsiya o'tkazadi va ma'lumotlarni bazaga saqlaydi.»

## Reliz / R5
- **RELIZ (R2 · UE-02):** «profil rasmi (yoki boshlang'ich harflar avatar), to'liq ismi, telefon raqami, rol badge, MyID identifikatsiya holati (tasdiqlangan / tasdiqlanmagan), ro'yxatdan o'tgan sana»; ijarachi uchun Rentmi bali/skoring bloki profilga ulanadi; tahrir «Tahrirlash» tugmasi orqali.
- **R5 o'zgarishi:** «tepadagi profil olib tashlanadi» (tenant'da Profil home header avatar orqali) — [`navigatsiya`](../00-umumiy/navigatsiya.md).

## Bajarish tartibi
1. Profil ochiladi → `SettingsDataCubit` profil + skoringni **parallel** yuklaydi (≤3 s).
2. Ekran: avatar (yoki harf-avatar), ism, telefon, rol badge, MyID holati, ro'yxatdan o'tgan sana, Rentmi bali bloki.
3. 'Tahrirlash' → `edit_personal_info_page`; foydalanuvchi shaxsiy ma'lumotni o'zgartiradi.
4. Saqlash → validatsiya → `PUT /mobile/profile/`.
5. Avatar: `avatar_crop_page` da kesiladi → `PATCH /mobile/account/update/` (multipart `profile_picture`).

## Qabul kriteriyalari (BDD)
- **GIVEN** kirgan foydalanuvchi **WHEN** profil ochadi **THEN** shaxsiy ma'lumot + Rentmi bali + avatar ≤3 s ichida ko'rsatiladi.
- **GIVEN** tahrir **WHEN** foydalanuvchi saqlaydi **THEN** validatsiya o'tadi va `PUT /mobile/profile/` chaqiriladi.
- **GIVEN** avatar tanlangan **WHEN** kesib saqlanadi **THEN** `PATCH /mobile/account/update/` multipart bilan yuklanadi.
- **GIVEN** tarmoq uzilgan **WHEN** profil ochiladi **THEN** oxirgi kesh + ogohlantirish banner (UE-02).

## Kod joylashuvi
- **Modul:** `lib/features/settings`
- **Sahifa / Cubit:** `settings_page`, `edit_personal_info_page`, `avatar_crop_page` / `SettingsDataCubit` (profil+skoring parallel), `EditPersonalInfoCubit`
- **Endpoint:** `GET /mobile/account/detail/{userId}/` · `PUT /mobile/profile/` · `PATCH /mobile/account/update/` (multipart `profile_picture`)

## Konflikt / farqlar
- ⚠ `EditPersonalInfoCubit` **mock** — dependency'lar ulanmagan; tahrirlash oxirigacha real backendga bog'lanmagan bo'lishi mumkin. → [`_konfliktlar.md`](../_konfliktlar.md)
- Rentmi bali tafsiloti va hisobot xarid (S1, faqat ijarachi) → [`04-skoring`](../04-skoring/about.md).
