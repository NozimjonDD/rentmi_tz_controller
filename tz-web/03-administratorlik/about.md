# 03 — Administratorlik moduli

Web qismi quyi tizimida **administrator** foydalanuvchilarni administratsiya qiladi, ruxsatlarni (RBAC) va tizim sozlamalarini boshqaradi hamda tizim hisobotlarini shakllantiradi. TZ §4.2.2 (Administratorlik moduli). Use-case'lar: **A1**, **A2** (A2 support bilan birga).

## Quyi tugunlar

| Tugun | Mazmun | TZ | Holat |
|---|---|---|---|
| [`a1-foydalanuvchi-admin.md`](a1-foydalanuvchi-admin.md) | Foydalanuvchi: bloklash/rol/blacklist/PIN tiklash, RBAC, ikki faktorli tasdiq | A1 | ✅ |
| [`a2-hisobotlar.md`](a2-hisobotlar.md) | Hisobotlar (foydalanuvchilar…integratsiya), PDF/XLSX/CSV | A2 | 🟡 |
| [`r5-algoritm-parametrlari.md`](r5-algoritm-parametrlari.md) | R5: algoritm parametrlari sozlamalari | R5-AD-01 | spec |

## Modul vazifasi va asosiy talablari (TZ §4.2.2)
> «Foydalanuvchilarni administratsiya qilish, ruxsatlarni boshqarish (RBAC), tizim sozlamalari va tizim hisobotlarini shakllantirish.»

- Barcha administrator harakatlari **sabab bilan** audit jurnaliga yoziladi.
- **Yuqori darajadagi operatsiyalar — ikki faktorli** tasdiqlashni talab etadi.
- **Kritik operatsiyalar** qo'shimcha tasdiqlash mexanizmlari bilan himoyalanadi.

## Muhim eslatma
- **RBAC** — modulning o'zagi; lekin ruxsatlar matritsasi §4.1.3.2 da to'liq ta'riflanmagan (→ [`07-rollar-va-rbac`](../07-rollar-va-rbac/about.md)).
- A2 hisobotlarini **support** ham shakllantiradi — bu support rolining ma'lumot doirasi bilan ziddiyatga olib keladi (W-A4).

## ⚠ Konflikt
- **W-A1** — hisobot vaqti: A2 da ≤30 s, §2.2/§4.1.4.1 da ≤10 s. → [`_konfliktlar.md`](../_konfliktlar.md).
- **W-A4** — support ma'lumot doirasi: A2 shaxsiy/moliyaviy hisobotlar vs §4.1.3.2 «anonimlashtirilgan analitikaga cheklangan kirish». → [`_konfliktlar.md`](../_konfliktlar.md).

## Backend / API (kutilayotgan)
Web kodbaza yo'q. TZ asosida kutiladi: `GET /admin/users/`, `POST /admin/users/{id}/block|role|blacklist|pin/reset/`, `GET /admin/reports/`, `POST /admin/reports/generate/`, `GET /admin/reports/{id}/export/?format=…`. reliz admin bo'limi to'liq emas (W-K2) → aniq yo'llar web repo berilganda tasdiqlanadi.
