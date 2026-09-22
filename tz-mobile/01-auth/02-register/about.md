# 02 — Ro'yxatdan o'tish (Register)

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi (👥 mehmondan o'tib keladi)    **Holat:** ✅ Bajarilgan
**TZ use-case:** U1 — Foydalanuvchini ro'yxatdan o'tkazish · §4.1.1.4

## Quyi qadamlar

| Qadam | Fayl | TZ |
|---|---|---|
| Telefon + SMS OTP | [`telefon-otp.md`](telefon-otp.md) | U1 (3–5 qadam) |
| PIN yaratish | [`pin-yaratish.md`](pin-yaratish.md) | U1 (7 qadam) |
| Rol bo'yicha keyingi qadam | [`role-post-flow.md`](role-post-flow.md) | U1 (9 qadam), U5 |

## U1 to'liq bajarish tartibi (TZ)

1. 'Ro'yxatdan o'tish' tanlanadi.
2. Telefon raqami kiritiladi.
3. Tizim format va **unikallik**ni tekshiradi.
4. SMS orqali OTP yuboriladi.
5. Foydalanuvchi OTP kiritadi, tizim tekshiradi.
6. Maxfiylik siyosati va Foydalanish shartlariga rozilik (skoring uchun talab).
7. PIN-kod o'rnatiladi.
8. Profil saqlanadi, asosiy oynaga yo'naltiriladi.
9. Identifikatsiya (U5) taklif qilinadi — **IXTIYORIY** ('Keyinroq' mumkin).

## Vaqt reglamenti (TZ)
OTP yuborish ≤30 s · OTP amal muddati **5 daqiqa** · umumiy ≤90 s.

## Kengaytmalar (TZ)
- Raqam mavjud → U2 (login) ga yo'naltirish.
- Noto'g'ri OTP (3 urinish, so'ng 10 daqiqa blok).
- Identifikatsiya 'Keyinroq' → cheklangan rejim (E3 ruxsat, R1 taqiqlangan).
- MyID vaqtincha ishlamasa → 'Keyinroq' rejim.

## Kod joylashuvi
- **Modul:** `lib/features/auth`
- **Sahifa / BLoC:** `LoginPage` (telefon) → `VerifyOtpPage` (OTP) → `RegistrationSuccessPage` / `AuthBloc`
- **Endpoint:** `POST /auth/login/`, `POST /auth/login/confirm/`

## Konflikt / farqlar
- ⚠ Kodda ro'yxatdan o'tish va kirish **bitta OTP oqimi** (`/auth/login/` + `/confirm/`) — TZ ularni U1/U2 alohida ajratadi.
- ⚠ OTP muddati/urinishlari TZ ↔ reliz farqi (quyi fayllarda). → [`_konfliktlar.md`](../../_konfliktlar.md).
