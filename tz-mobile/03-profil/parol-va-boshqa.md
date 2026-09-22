# Parol, qurilmalar, til va chiqish

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi    **Holat:** 🟡 Qisman (faol qurilmalar aniqlanmagan)

## TZ manbai
U4 · §4.1.1.4 (4-qadam) — faol qurilmalarni ko'rish va boshqarish. Parol/chiqish/til — umumiy xavfsizlik va §4.3.3 til talablari doirasida.
> «4) Faol qurilmalarni boshqarishda: barcha faol sessiyalar ro'yxati ko'rsatiladi, kerakmas qurilmadan chiqish imkoniyati mavjud.»

## Reliz / R5
- **RELIZ (R2 · UE-02):** «'Chiqish' tugmasi pastda joylashgan». Til — `2-2 US 2` (settingsdan o'zgartirish).
- **R5 o'zgarishi:** yo'q.

## Bajarish tartibi
1. **Parol:** `change_password_page` → eski + yangi parol → `POST /mobile/profile/change-password/` (`ChangePasswordCubit`).
2. **Til:** `language_settings_page` → 4 tildan tanlash → `LocaleProvider` + `SharedPreferences` — [`til-tanlash`](../00-umumiy/til-tanlash.md).
3. **App sozlamalari:** `app_settings_page` (`AppSettingsCubit`); ma'lumot: `about_app_page`, `terms_security_page`, `privacy_page`.
4. **Faol qurilmalar:** U4 barcha faol sessiyalar ro'yxati + qurilmadan chiqishni talab qiladi — kodda alohida sahifa aniqlanmadi.
5. **Chiqish:** `LogoutCubit` → sessiya tokenlari tozalanadi → login/guest.

## Qabul kriteriyalari (BDD)
- **GIVEN** eski + yangi parol **WHEN** saqlaydi **THEN** `POST /mobile/profile/change-password/` chaqiriladi.
- **GIVEN** til sozlamasi **WHEN** o'zgartiriladi **THEN** UI yangilanadi va tanlov saqlanadi.
- **GIVEN** foydalanuvchi **WHEN** 'Chiqish' ni tasdiqlaydi **THEN** sessiya tozalanadi.
- **GIVEN** faol qurilmalar (U4) **WHEN** talab qilinadi **THEN** ⚠ kodda ro'yxat/chiqish sahifasi aniqlanmadi.

## Kod joylashuvi
- **Modul:** `lib/features/settings`
- **Sahifa / Cubit:** `change_password_page` (`ChangePasswordCubit`), `app_settings_page` (`AppSettingsCubit`), `language_settings_page`, `about_app_page`, `terms_security_page`, `privacy_page`, chiqish (`LogoutCubit`)
- **Endpoint:** `POST /mobile/profile/change-password/`; faol qurilmalar endpointi **aniqlanmagan**; chiqish (sessiya) → [`01-auth/05-sessiya`](../01-auth/05-sessiya/about.md).

## Konflikt / farqlar
- ⚠ **Faol qurilmalar boshqaruvi** (U4 4-qadam: faol sessiyalar ro'yxati + qurilmadan chiqish) — kodda alohida sahifa/endpoint **aniqlanmadi**. → [`_konfliktlar.md`](../_konfliktlar.md)
