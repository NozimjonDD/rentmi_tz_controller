# 06 — Texnik qo'llab-quvvatlash + call-markaz moduli

Foydalanuvchi murojaatlarini ko'rib chiqish, javob berish, eskalatsiya qilish hamda call-markaz orqali ticket yaratish. TZ §4.2.2 (Texnik qo'llab-quvvatlash moduli (admin)). Use-case'lar: **T2**, **T3**.

## Quyi tugunlar

| Tugun | Mazmun | TZ | Holat |
|---|---|---|---|
| [`t2-murojaat-korib-chiqish.md`](t2-murojaat-korib-chiqish.md) | Murojaatni ishlash/javob/eskalatsiya, 24 soat javob | T2 | ✅ |
| [`t3-callmarkaz-ticket.md`](t3-callmarkaz-ticket.md) | Telefon/chat orqali qabul, ticket yaratish, eskalatsiya | T3 | ✅ |
| [`r5-sla-monitoring.md`](r5-sla-monitoring.md) | R5: SLA monitoring (muddati o'tgan so'rovlar) | R5-AD-02 | spec |

## Modul vazifasi va asosiy talablari (TZ §4.2.2)
> «Foydalanuvchi murojaatlarini ko'rib chiqish, javob berish, eskalatsiya qilish hamda call-markaz orqali ticket yaratish.»

- Murojaatlarni **ko'rib chiqish va holatini boshqarish**.
- **Javob berish**, ichki izoh va **eskalatsiya**.
- **Call-markaz operatori** tomonidan ticket yaratish.
- Murojaatga javob maksimal muddati — **24 soat** (ish kuni ichida); 24 soat hal etilmagan ticket **avtomatik eskalatsiya** qilinadi.
- Call-markaz operatori **faqat ko'rish** huquqiga ega.
- Barcha harakatlar **audit jurnaliga** yoziladi.

## Muhim eslatma (rollar)
- **T2** — texnik qo'llab-quvvatlash xodimi: admin web panelida ticket boshqaruvi, javob, ichki izoh, eskalatsiya, holat yangilash.
- **T3** — call-markaz operatori: telefon/chat orqali murojaat qabul qilish, foydalanuvchini topish (faqat ko'rish), yangi ticket yaratish.
- Rollar va RBAC batafsil → [`../07-rollar-va-rbac/about.md`](../07-rollar-va-rbac/about.md).

## ⚠ Konflikt
- **Call-markaz operatori huquqi:** §4.1.3.2 + §4.2.2 operatorni «faqat ko'rish (o'qish) huquqiga ega» deb belgilaydi, T3 esa operator «yangi ticket yaratadi» (yozish amali). → [`_konfliktlar.md`](../_konfliktlar.md) W-A3.

## Backend / API (kutilayotgan)
Web kodbaza yo'q. TZ asosida kutiladi: `GET /admin/tickets/` (filtr), `GET /admin/tickets/{id}/`, `PATCH /admin/tickets/{id}/` (holat/javob/ichki izoh), `POST /admin/tickets/{id}/escalate/`, `POST /admin/tickets/` (call-markaz — yangi ticket). Aniq yo'llar web repo berilganda tasdiqlanadi.
