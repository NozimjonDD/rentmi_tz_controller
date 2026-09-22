# T3 — Murojaatni qabul qilish va ticket yaratish

**Rollar:** 🎧 Call-markaz operatori    **Holat:** ✅ (TZ da to'liq)

## TZ manbai
T3 · §4.1.1.4 · Call-markaz operatori telefon/chat orqali murojaatni qabul qiladi, foydalanuvchini topadi (faqat ko'rish), yangi ticket yaratadi va zaruratda texnik qo'llab-quvvatlashga eskalatsiya qiladi.
> «Operator web qismi quyi tizimida foydalanuvchini topadi (telefon raqami yoki identifikatori bo'yicha) — faqat ko'rish huquqida; … tizimda yangi ticket yaratadi (kategoriya, mavzu, tavsif).»

## Reliz / R5
- **RELIZ / R5:** o'zgarish yo'q.

## Ishga tushirish shartlari
Call-markaz operatori web qismi quyi tizimiga kirgan; foydalanuvchidan telefon yoki chat orqali murojaat kelgan.

## Bajarish tartibi
1. Operator foydalanuvchi murojaatini telefon/chat orqali qabul qiladi.
2. Operator web qismi quyi tizimida foydalanuvchini topadi (telefon raqami yoki identifikatori bo'yicha) — **faqat ko'rish huquqida**.
3. Murojaat mazmunini aniqlaydi va kategoriyalaydi (texnik muammo / shikoyat / taklif).
4. Tizimda **yangi ticket yaratadi** (kategoriya, mavzu, tavsif).
5. Zaruratga ko'ra ticketni texnik qo'llab-quvvatlash xodimiga yo'naltiradi (eskalatsiya).
6. Foydalanuvchiga ticket raqami va taxminiy javob muddati aytiladi.
7. Harakat audit jurnaliga yoziladi.

## Vaqt reglamenti
Foydalanuvchini topish — ≤5 s; ticket yaratish — ≤5 s.

## Qabul kriteriyalari (BDD)
- **GIVEN** telefon/chat orqali murojaat keldi **WHEN** operator foydalanuvchini qidiradi **THEN** foydalanuvchi faqat ko'rish rejimida topiladi.
- **GIVEN** murojaat kategoriyalandi **WHEN** operator ticket yaratadi **THEN** yangi ticket noyob raqam bilan saqlanadi (kategoriya, mavzu, tavsif).
- **GIVEN** murojaat texnik yordam talab qiladi **WHEN** operator eskalatsiya qiladi **THEN** ticket support xodimiga yo'naltiriladi va unga bildirishnoma boradi.
- **GIVEN** foydalanuvchi tizimda topilmadi **WHEN** operator ticket yaratadi **THEN** murojaat umumiy murojaat sifatida yoziladi.

## Backend / API (kutilayotgan)
- Kutiladi: `GET /admin/users/?search=<telefon|id>` (faqat ko'rish), `POST /admin/tickets/` (yangi ticket), `POST /admin/tickets/{id}/escalate/` (support xodimiga). Aniq yo'llar web repo berilganda tasdiqlanadi.

## Konflikt / farqlar
- ⚠ **Call-markaz operatori huquqi:** §4.1.3.2 + §4.2.2 operatorni «faqat ko'rish (o'qish) huquqiga ega» deb belgilaydi, T3 da esa operator «yangi ticket yaratadi» — bu **yozish amali**. → [`_konfliktlar.md`](../_konfliktlar.md) W-A3.
