# 01 — Autentifikatsiya moduli

Web qismi quyi tizimi foydalanuvchilari (administrator, moderator, support, call-markaz) uchun **username/parol** asosida kirish va parolni tiklash. TZ §4.2.2 (Autentifikatsiya moduli). Use-case'lar: **U2-veb**, **U2a**.

## Quyi tugunlar

| Tugun | Mazmun | TZ | Holat |
|---|---|---|---|
| [`u2-veb.md`](u2-veb.md) | Web kirish (username + parol, JWT) | U2-veb | ✅ |
| [`u2a-parol-tiklash.md`](u2a-parol-tiklash.md) | Parolni tiklash (faqat superadmin) | U2a | ✅ |

## Modul vazifasi va asosiy talablari (TZ §4.2.2)
> «Web qismi quyi tizimi foydalanuvchilari uchun username/parol asosida kirish va parolni tiklashni ta'minlash.»

- Admin hisoblari **faqat superadmin** tomonidan yaratiladi.
- 3 ta noto'g'ri urinishdan so'ng 10 daqiqaga blok.
- Vaqtinchalik parol amal muddati — 24 soat.
- Barcha kirish va tiklash harakatlari **audit jurnaliga** yoziladi.

## Muhim eslatma (mobil bilan farq)
- Web kirish — **username + parol** (JWT). Mobil esa telefon + OTP + PIN. Ular butunlay boshqa oqim.
- Web sessiya **15 daqiqa faoliyatsizlikdan so'ng** avtomatik yakunlanadi (TZ §4.1.6.1). → [`../07-rollar-va-rbac/about.md`](../07-rollar-va-rbac/about.md).

## ⚠ Konflikt
- **superadmin** roli use-case'larda faol ishlatiladi, lekin §4.1.3.2 rollar ro'yxatida **ta'riflanmagan**. → [`_konfliktlar.md`](../_konfliktlar.md) W-A6.

## Backend / API (kutilayotgan)
Web kodbaza yo'q. TZ asosida kutiladi: `POST /admin/auth/login/` (username/parol → JWT), `POST /admin/auth/password/reset/` (superadmin). Aniq yo'llar web repo berilganda tasdiqlanadi.
