# 01 — Autentifikatsiya (Auth)

Foydalanuvchini telefon raqami + SMS-OTP orqali ro'yxatdan o'tkazish va kirish, 4-xonali PIN gate, JWT sessiya boshqaruvi. TZ use-case'lari: **U1** (ro'yxatdan o'tkazish), **U2** (kirish, PIN), **U3** (PIN tiklash).

## Quyi tugunlar

| Tugun | Mazmun | TZ | Holat |
|---|---|---|---|
| [`01-rol-tanlash/`](01-rol-tanlash/about.md) | Ijarachi / Uy egasi / Mehmon tanlash | — (reliz US4) | 🟡 |
| [`02-register/`](02-register/about.md) | Ro'yxatdan o'tish: telefon → OTP → PIN → rol post-flow | U1 | ✅ |
| [`03-login/`](03-login/about.md) | Kirish: telefon + PIN | U2 | ✅ |
| [`04-pincode/`](04-pincode/about.md) | PIN yaratish / tekshirish / tiklash / biometrika | U2, U3 | ✅ |
| [`05-sessiya/`](05-sessiya/about.md) | JWT, refresh, multi-device, sessiya tugashi | — | ✅ |

## Umumiy oqim (kod'dagi haqiqiy holat)

```
splash → til → onboarding → MEHMON (ijarachi) dashboard
   [talab bo'yicha auth] → rol tanlash → telefon → OTP(6) → PIN yaratish → JWT
       → MyID (02) → rol dashboard
       → skoring (04) / kadastr import (02) — TALAB BO'YICHA
```

> ⚠ **Kod TZ'dan farq qiladi:** TZ (U1/U2) "rol tanlash → telefon → OTP → PIN → identifikatsiya" majburiy ketma-ketligini nazarda tutadi. Kodda oqim **guest-first**: majburiy rol tanlash yo'q, auth talab bo'yicha ochiladi; login'dan keyin majburiy zanjir faqat **PIN → MyID → dashboard** (orkestrator: `lib/core/services/onboarding_flow_service.dart`, `OnboardingStep{auth, pincode, identification, scoring, payment, cadastre, main}`). Batafsil: [`_konfliktlar.md`](../_konfliktlar.md).

## Umumiy xavfsizlik qoidalari (TZ §4.1.6)

- Parollar va PIN-kodlar bir tomonlama xeshlanadi (TZ: bcrypt/Argon2; **kodda: PBKDF2-HMAC-SHA256**, 10 000 iteratsiya + salt).
- 3 ta noto'g'ri urinishdan so'ng 10 daqiqaga blok (TZ). ⚠ reliz US4: 5 urinish → 5 daqiqa.
- Barcha autentifikatsiya harakatlari audit jurnaliga yoziladi.
- Aloqa HTTPS (TLS 1.2+); API tokenlari JWT/OAuth2.

## Kod modullari

`lib/features/auth` · `lib/features/role_selection` · `lib/features/pincode` · `lib/features/onboarding` · orkestrator `lib/core/services/onboarding_flow_service.dart` · token `lib/core/services/token_manager.dart`, `token_storage_service.dart`, `pincode_storage_service.dart`.

## Asosiy endpointlar

| Amal | Endpoint |
|---|---|
| OTP so'rash | `POST /auth/login/` — `{phone_number, role}` → `secret` |
| OTP tasdiq | `POST /auth/login/confirm/` — `{secret, otp}` → `{access, refresh, data:{user}}` |
| Token refresh | `POST /auth/token/refresh/` — `{refresh}` → `{access, refresh}` |
| Chiqish | `POST /auth/logout/` |
| Qurilma ro'yxati | `POST /mobile/device/register/` — `{fcm_token, device_id, name, device_type}` |
