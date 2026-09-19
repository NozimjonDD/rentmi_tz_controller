# Telefon raqamini o'zgartirish

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi    **Holat:** ✅ Bajarilgan

## TZ manbai
U4 · §4.1.1.4 (5-qadam). Telefon raqamini o'zgartirish OTP tasdiq bilan amalga oshiriladi.
> «5) Telefon raqamni o'zgartirishda: yangi raqam kiritiladi — SMS OTP yuboriladi — OTP tasdiqlanadi — raqam yangilanadi.»

Vaqt reglamenti: OTP yuborish ≤30 s; OTP amal muddati 5 daqiqa. Kengaytma: «noto'g'ri OTP (3 urinish, telefon o'zgartirish) → jarayon bekor qilinadi».

## Reliz / R5
- **RELIZ:** telefon o'zgartirish alohida US sifatida ajratilmagan (profil doirasida, R2 · 2-7 Profil).
- **R5 o'zgarishi:** yo'q.

## Bajarish tartibi
1. Profil → telefon o'zgartirish; yangi raqam (+998) kiritiladi.
2. Backend SMS OTP yuboradi (≤30 s).
3. `verify_phone_change_page` da OTP kiritiladi (amal muddati 5 daqiqa).
4. OTP tasdiqlansa — raqam yangilanadi, audit jurnaliga yoziladi.
5. Noto'g'ri OTP (3 urinish) → jarayon bekor qilinadi.

## Qabul kriteriyalari (BDD)
- **GIVEN** yangi raqam **WHEN** OTP so'raladi **THEN** SMS OTP ≤30 s ichida yuboriladi.
- **GIVEN** to'g'ri OTP **WHEN** tasdiqlanadi **THEN** telefon raqami yangilanadi va audit yoziladi.
- **GIVEN** noto'g'ri OTP 3 marta **WHEN** kiritiladi **THEN** jarayon bekor qilinadi.

## Kod joylashuvi
- **Modul:** `lib/features/settings`
- **Sahifa / Cubit:** `verify_phone_change_page` (OTP tasdiq) / `SettingsDataCubit` (profil konteksti)
- **Endpoint:** telefon o'zgartirish + OTP tasdiq endpointi **aniqlanmagan** (berilgan endpoint ro'yxatida yo'q); OTP mexanizmi umumiy auth OTP'ga o'xshash — [`01-auth/02-register/telefon-otp.md`](../01-auth/02-register/telefon-otp.md).

## Konflikt / farqlar
- ⚠ Telefon o'zgartirish OTP endpointi berilmagan — **aniqlanmagan** deb belgilanadi (kodni tasdiqlash kerak).
- OTP amal muddati/urinishlar TZ ↔ reliz farqi (5 daq / 3 urinish ↔ 1 daq / 5 urinish) auth oqimiga ham taalluqli. → [`_konfliktlar.md`](../_konfliktlar.md)
