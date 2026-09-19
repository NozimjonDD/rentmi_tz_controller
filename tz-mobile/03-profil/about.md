# 03 — Profil va sozlamalar

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi    **Holat:** ✅ Bajarilgan (⚠ ba'zi qismlar mock / TZ tashqarisi)
**TZ use-case:** U4 — Foydalanuvchi profilini boshqarish · §4.1.1.4

Foydalanuvchi o'z profilini ko'radi va tahrirlaydi, Rentmi balini ko'radi, telefon raqamini (OTP bilan) o'zgartiradi, manzillar va parolni boshqaradi, faol qurilmalarni ko'radi.

## Quyi qadamlar

| Qadam | Fayl | TZ (U4) | Holat |
|---|---|---|---|
| Ko'rish + tahrir + avatar | [`profil-korish-tahrir.md`](profil-korish-tahrir.md) | 1–3, 6–7 | ✅ |
| Telefon o'zgartirish (OTP) | [`telefon-ozgartirish.md`](telefon-ozgartirish.md) | 5 | ✅ |
| Rol almashtirish | [`rol-almashtirish.md`](rol-almashtirish.md) | — (U4 da yo'q) | ✅ ⚠ |
| Manzillar (CRUD) | [`manzillar.md`](manzillar.md) | 3 (aloqa ma'lumoti) | ✅ |
| Parol / qurilmalar / til / chiqish | [`parol-va-boshqa.md`](parol-va-boshqa.md) | 4 | 🟡 |

## U4 bajarish tartibi (TZ)

> «1) 'Mening profilim' bo'limini tanlaydi; 2) Tizim joriy ma'lumotlarni (shaxsiy, aloqa, Rentmi bali, hisobotlar) ko'rsatadi; 3) Foydalanuvchi harakatni tanlaydi: shaxsiy ma'lumotlarni tahrirlash / Rentmi bali tafsilotini ko'rish / hisobot xarid qilish — faqat ijarachi uchun (S1) / … / faol qurilmalarni ko'rish va boshqarish / telefon raqamni o'zgartirish; … 8) Audit jurnaliga yozuv kiritiladi.»

**Vaqt reglamenti (TZ):** Profil yuklash ≤3 s · saqlash ≤3 s · OTP yuborish ≤30 s · OTP amal muddati 5 daqiqa.

## Kod moduli

`lib/features/settings`. Sahifalar: `settings_page`, `edit_personal_info_page`, `verify_phone_change_page`, `addresses_page`, `add_edit_address_page`, `change_password_page`, `role_switch_page`, `app_settings_page`, `language_settings_page`, `about_app_page`, `terms_security_page`, `privacy_page`, `avatar_crop_page`.
Cubitlar: `SettingsDataCubit` (profil+skoring parallel), `AddressesCubit`, `AppSettingsCubit`, `ChangePasswordCubit`, `EditPersonalInfoCubit` (⚠ mock — deps yo'q), `LogoutCubit`.

## Endpointlar

| Amal | Endpoint |
|---|---|
| Profil detali | `GET /mobile/account/detail/{userId}/` |
| Profil yangilash | `PUT /mobile/profile/` |
| Avatar / qisman yangilash | `PATCH /mobile/account/update/` (multipart `profile_picture`) |
| Parol o'zgartirish | `POST /mobile/profile/change-password/` |
| Manzillar | `GET/POST /mobile/addresses/` · `PUT/DELETE /mobile/addresses/{id}/` · `POST /mobile/addresses/{id}/set-default/` |
| Telefon o'zgartirish OTP | aniqlanmagan |
| Faol qurilmalar | aniqlanmagan |

## Konflikt / farqlar

- ⚠ Rol almashtirish (`role_switch_page`) TZ U4 da yo'q — modul va'da qilgan (**B4**). → [`_konfliktlar.md`](../_konfliktlar.md)
- ⚠ `EditPersonalInfoCubit` mock (deps ulanmagan) — [`profil-korish-tahrir.md`](profil-korish-tahrir.md).
- ⚠ Faol qurilmalar boshqaruvi (U4 4-qadam) — kodda alohida sahifa/endpoint aniqlanmadi.
- Rentmi bali ko'rish va hisobot xarid (S1) → [`04-skoring`](../04-skoring/about.md).
