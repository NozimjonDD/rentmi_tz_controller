# 04 — Billing nazorati moduli

Administrator tomonidan **to'lov tranzaksiyalarini nazorat qilish** va billing hisobotlarini shakllantirish. TZ §4.2.2 (Billing nazorati moduli). Use-case: **A4**.

## Quyi tugunlar

| Tugun | Mazmun | TZ | Holat |
|---|---|---|---|
| [`a4-tolovlar-nazorati.md`](a4-tolovlar-nazorati.md) | Tranzaksiyalarni ko'rish/filtr, reconciliation, refund, kunlik/oylik hisobot | A4 | ✅ |

## Modul vazifasi va asosiy talablari (TZ §4.2.2)
> «To'lov tranzaksiyalarini nazorat qilish va billing hisobotlarini shakllantirish.»

- Barcha tranzaksiyalarni **ko'rish va filtrlash** (sana, foydalanuvchi, tur, summa, holat, to'lov tizimi).
- **Kunlik/oylik tushum** hisoboti (muvaffaqiyat darajasi).
- Pul summalari **tiyin (minimal birlik) aniqligida** saqlanadi.
- Barcha nazorat harakatlari **audit jurnaliga** yoziladi.

## Muhim eslatma
- Bo'lim **faqat administrator** uchun (§4.1.3.2 — barcha operatsiyalar va ma'lumotlarga kirish). → [`../07-rollar-va-rbac/about.md`](../07-rollar-va-rbac/about.md).
- Nomuvofiqlikda **reconciliation**, talab bo'lsa **refund** tegishli to'lov tizimi orqali amalga oshiriladi.
- R5 admin panelida (algoritm parametrlari, SLA monitoring) billing nazoratiga **o'zgarish yo'q**.

## ⚠ Konflikt
- **Hisobot vaqti:** A4 ssenariysida hisobot ≤30 s, §2.2/§4.1.4.1 da ≤10 s. → [`_konfliktlar.md`](../_konfliktlar.md) W-A1.
- **Ssenariylar tartibi:** ro'yxatda A4 (to'lovlar) A3 (integratsiya) dan oldin kelgan. → [`_konfliktlar.md`](../_konfliktlar.md) W-B3.

## Backend / API (kutilayotgan)
Web kodbaza yo'q. TZ asosida kutiladi: `GET /admin/billing/transactions/` (filtr/qidiruv), `GET /admin/billing/transactions/{id}/` (tafsilot + webhook holati), `POST /admin/billing/transactions/{id}/reconcile/`, `POST /admin/billing/transactions/{id}/refund/`, `GET /admin/billing/reports/` (kunlik/oylik). Aniq yo'llar web repo berilganda tasdiqlanadi.
