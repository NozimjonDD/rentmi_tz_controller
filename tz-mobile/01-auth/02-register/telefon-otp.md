# Telefon raqami + SMS OTP

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi / 👥 Mehmon    **Holat:** ✅ Bajarilgan

## TZ manbai
U1 — Foydalanuvchini ro'yxatdan o'tkazish · §4.1.1.4 (3–5 qadam). Telefon raqami (E.164/+998) kiritiladi, tizim format va unikallikni tekshiradi, SMS orqali OTP yuboriladi va tasdiqlanadi.
> «SMS orqali OTP yuboriladi; Foydalanuvchi OTP kiritadi, tizim tekshiradi.»

## Reliz / R5
- **RELIZ:** `2-4 Ro'yxatdan o'tish / US 4 LA` — «Phone format: +998», «OTP: **6 digit, 1 min validity**», «Resend cooldown: 30–60 sekund», «OTP attempt limit: **5**», «SMS auto-read (autofill)», «Blocked user OTP stageda to'xtatiladi».
- **R5 o'zgarishi:** yo'q (auth R5 doirasida faqat U4–U5 doirasida eslatiladi).

## Bajarish tartibi
1. Telefon raqami kiritiladi (`+998`, 9 xona), Maxfiylik siyosati checkbox belgilanadi.
2. `POST /auth/login/` → backend `secret` qaytaradi va SMS OTP yuboradi.
3. 6-xonali OTP kiritiladi (60 sek timer, resend cooldown).
4. `POST /auth/login/confirm/` → `{access, refresh, data:{user}}`; tokenlar secure storage'ga saqlanadi.
5. Muvaffaqiyatda: rol saqlanadi, qurilma FCM ro'yxatdan o'tadi, WebSocket qayta ulanadi.

## Qabul kriteriyalari (BDD)
- **GIVEN** to'g'ri +998 raqam **WHEN** OTP so'raladi **THEN** 6-xonali kod yuboriladi va timer ishga tushadi.
- **GIVEN** OTP muddati tugadi **WHEN** foydalanuvchi kutadi **THEN** kod yaroqsiz, qayta so'rash mumkin.
- **GIVEN** admin bloklagan foydalanuvchi **WHEN** raqam kiritiladi **THEN** OTP yuborilmaydi, bloklanganlik xabari.

## Kod joylashuvi
- **Modul:** `lib/features/auth`
- **Sahifa / BLoC:** `LoginPage`, `VerifyOtpPage` / `AuthBloc` (`SendOtpEvent`, `VerifyOtpEvent`, `ResendOtpEvent`; states `OtpSent(phoneNumber, role, secret)`, `AuthSuccess(user)`)
- **Endpoint:** `POST /auth/login/` `{phone_number, role}` → `secret`; `POST /auth/login/confirm/` `{secret, otp}` → `{access, refresh, data:{user}}`
- Telefon raqamlari log'da maskalanadi (`_maskPhone`).

## Konflikt / farqlar
- ⚠ **OTP amal muddati:** TZ **5 daqiqa** ↔ reliz/kod **1 daqiqa** (60 sek). → [`_konfliktlar.md`](../../_konfliktlar.md) C1.
- ⚠ **Xato urinishlar:** TZ **3 urinish → 10 daqiqa** blok ↔ reliz **5 urinish → 5 daqiqa**. → C2.
