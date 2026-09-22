# 05 — Integratsiya boshqaruvi moduli

Administrator tomonidan **tashqi axborot tizimlari bilan ulanishlarni sozlash**, holatini monitoring qilish va sinovdan o'tkazish. TZ §4.2.2 (Integratsiya boshqaruvi moduli). Use-case: **A3**.

## Quyi tugunlar

| Tugun | Mazmun | TZ | Holat |
|---|---|---|---|
| [`a3-integratsiyalar.md`](a3-integratsiyalar.md) | Tashqi xizmatlar holati, endpoint/kalit/timeout sozlash, sinov so'rovi | A3 | ✅ |

## Modul vazifasi va asosiy talablari (TZ §4.2.2)
> «Tashqi axborot tizimlari bilan ulanishlarni sozlash, holatini monitoring qilish va sinovdan o'tkazish.»

- Ulangan tashqi xizmatlar ro'yxati va **real vaqtdagi holati** (identifikatsiya, skoring byurosi, to'lov tizimlari, SMS, push, xarita).
- Integratsiya parametrlarini (**endpoint, kalit, timeout, retry**) sozlash.
- **Sinov so'rovi** orqali integratsiyani tekshirish; vaqtincha yoqish/o'chirish.
- Integratsiya **kalitlari shifrlangan** holda saqlanadi.
- Barcha tashqi so'rovlar log jurnalida, o'zgarishlar audit jurnaliga yoziladi.
- Qayta urinish (retry) va **circuit breaker** mexanizmlari qo'llaniladi.

## Muhim eslatma
- Bo'lim **faqat administrator** uchun. → [`../07-rollar-va-rbac/about.md`](../07-rollar-va-rbac/about.md).
- Tashqi xizmatlar ro'yxati §4.1.2.3 da (8 xizmat turi); protokollar §4.1.2.1 (HTTPS/REST/webhook/SMPP).
- R5 admin panelida (algoritm parametrlari, SLA monitoring) integratsiya boshqaruviga **o'zgarish yo'q**.

## ⚠ Konflikt
- **Ssenariylar tartibi:** ro'yxatda A4 (to'lovlar) A3 (integratsiya) dan oldin kelgan (tartib buzilgan). → [`_konfliktlar.md`](../_konfliktlar.md) W-B3.

## Backend / API (kutilayotgan)
Web kodbaza yo'q. TZ asosida kutiladi: `GET /admin/integrations/` (ro'yxat + holat), `GET /admin/integrations/{id}/` (statistika/javob vaqti), `PATCH /admin/integrations/{id}/` (endpoint/kalit/timeout/retry — kalit shifrlangan), `POST /admin/integrations/{id}/test/` (sinov so'rovi), `POST /admin/integrations/{id}/toggle/` (yoqish/o'chirish). Aniq yo'llar web repo berilganda tasdiqlanadi.
