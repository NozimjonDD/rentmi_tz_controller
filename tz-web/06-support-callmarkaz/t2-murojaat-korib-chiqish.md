# T2 — Murojaatni ko'rib chiqish

**Rollar:** 🛠 Texnik qo'llab-quvvatlash xodimi    **Holat:** ✅ (TZ da to'liq)

## TZ manbai
T2 · §4.1.1.4 · Texnik qo'llab-quvvatlash xodimi admin web panelida murojaatlarni ko'rib chiqadi, javob yozadi, ichki izoh qo'shadi, eskalatsiya qiladi va holatni yangilaydi.
> «Xodim murojaatni tanlaydi va tafsilotlarni ko'radi …; murojaatni 'Ishlanmoqda' holatiga o'tkazadi; javob yozadi yoki ichki izoh qo'shadi; zarur bo'lsa boshqa bo'limga yo'naltiradi (eskalatsiya).»

## Reliz / R5
- **RELIZ / R5:** admin panel VueJS'da (R5 — algoritm parametrlari; SLA monitoring esa **so'rovlar** bo'yicha, R3 moduli kengaytmasi). Murojaatni ko'rib chiqish oqimiga o'zgarish yo'q.

## Ishga tushirish shartlari
Texnik qo'llab-quvvatlash xodimi admin web panelida tizimga kirgan; kamida bitta ko'rib chiqilmagan murojaat (ticket) mavjud.

## Bajarish tartibi
1. Xodim admin web panelida 'Murojaatlar' bo'limini ochadi.
2. Tizim murojaatlar ro'yxatini ko'rsatadi (kategoriya, holat, sana, foydalanuvchi bo'yicha filtr).
3. Xodim murojaatni tanlaydi va tafsilotlarni ko'radi (kategoriya, matn, ilovalar, foydalanuvchi profili).
4. Murojaatni 'Ishlanmoqda' holatiga o'tkazadi.
5. Javob yozadi yoki ichki izoh qo'shadi.
6. Zarur bo'lsa boshqa bo'limga yo'naltiradi (eskalatsiya).
7. Muammo hal etilgach 'Hal etildi' holatiga o'tkazadi.
8. Foydalanuvchiga bildirishnoma yuboriladi (push yoqilgan bo'lsa — push; o'chirilgan bo'lsa — tizim ichidagi xabar).
9. Harakatlar audit jurnaliga yoziladi.

## Vaqt reglamenti
Ro'yxatni yuklash — ≤5 s; tafsilotlarni yuklash — ≤3 s; javob saqlash — ≤3 s; bildirishnoma — ≤15 s; **murojaatga javob maksimal muddati — 24 soat** (ish kuni ichida).

## Qabul kriteriyalari (BDD)
- **GIVEN** ko'rib chiqilmagan murojaat bor **WHEN** xodim 'Murojaatlar'ni ochadi **THEN** ro'yxat filtr bilan (kategoriya, holat, sana, foydalanuvchi) ko'rsatiladi.
- **GIVEN** murojaat tanlangan **WHEN** xodim uni ochadi **THEN** kategoriya, matn, ilovalar va foydalanuvchi profili ko'rinadi; holat 'Ishlanmoqda'ga o'tadi.
- **GIVEN** javob yoki ichki izoh yozildi **WHEN** xodim saqlaydi **THEN** foydalanuvchiga bildirishnoma (push yoki tizim ichidagi xabar) yuboriladi.
- **GIVEN** murojaat 24 soat ichida hal etilmadi **WHEN** muddat o'tadi **THEN** avtomatik eskalatsiya va menejerga bildirishnoma yuboriladi.
- **GIVEN** bir vaqtda boshqa xodim ishlamoqda **WHEN** xodim ochadi **THEN** konflikt ogohlantirishi ko'rsatiladi.

## Backend / API (kutilayotgan)
- Kutiladi: `GET /admin/tickets/` (filtr), `GET /admin/tickets/{id}/`, `PATCH /admin/tickets/{id}/` (holat: ishlanmoqda/hal etildi, javob, ichki izoh), `POST /admin/tickets/{id}/escalate/`. Bildirishnoma push/tizim ichida. Aniq yo'llar web repo berilganda tasdiqlanadi.

## Konflikt / farqlar
- Farq aniqlanmadi. Texnik qo'llab-quvvatlash xodimi vakolatlari §4.1.3.2 (ticket boshqaruvi, eskalatsiya, holat yangilash) T2 ssenariysi bilan mos.
