> Manba: [Release 2 01.06.2026 · Ue cases: Admin](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/25591819) · Ustuvorlik: Yuqori (P1)

**ADMINISTRATOR USE CASELARI**

AD-01 — Ijarachilar ro’yxati va boshqaruvi

| **AD-01 — Ijarachilar ro’yxati va boshqaruvi** |
| --- |
| **Aktyor** | Administrator |
| **Turi** | Asosiy |
| **Ishga tushirish shartlari** | Administrator admin veb-ilovasiga kirgan va administrator roliga ega. |
| **Bajarish tartibi** | Administrator “Foydalanuvchilar” → “Ijarachilar” bo’limini ochadi; 2) Tizim barcha ijarachi rolida ro’yxatdan o’tgan foydalanuvchilarni jadval ko’rinishida chiqaradi; 3) Jadvalda har bir ijarachi uchun quyidagi ma’lumotlar ko’rsatiladi:    — Tartib raqami;    — To’liq ismi;    — Telefon raqami;    — MyID identifikatsiya holati (tasdiqlangan / tasdiqlanmagan — badge bilan);    — Rentmi ball (0–100, rangli ko’rsatgich: 0–40 qizil, 41–70 sariq, 71–100 yashil);    — Ro’yxatdan o’tgan sana;    — Hisob holati (Faol / Bloklangan / Blacklist — badge bilan);    — Oxirgi faollik sanasi;    — Jami ijara so’rovlari soni; 4) Qidiruv maydoni mavjud: ism/familiya, telefon raqami bo’yicha; 5) Filtr imkoniyatlari:    — Identifikatsiya holati (tasdiqlangan / tasdiqlanmagan);    — Hisob holati (faol / bloklangan / blacklist);    — Rentmi ball oralig’i (slider);    — Ro’yxatdan o’tgan sana oralig’i; 6) Saralash: ism, sana, ball, so’rovlar soni bo’yicha o’sib yoki kamayib; 7) Ijarachi qatoriga bosib AD-05 (Foydalanuvchini boshqarish amallari) use casega o’tiladi; 8) Eksport: ko’rinayotgan ro’yxatni XLSX yoki CSV formatida yuklab olish. |
| **Vaqt reglamenti** | Ro’yxat yuklanishi ≤ 3 sek; qidiruv natijasi ≤ 2 sek; filtr qo’llash ≤ 2 sek; eksport ≤ 15 sek. |
| **Kiruvchi ma'lumotlar** | Filtr parametrlari, qidiruv so’zi, saralash tartibi. |
| **Chiquvchi ma'lumotlar** | Ijarachilar ro’yxati barcha ko’rsatkichlar bilan; eksport fayli (XLSX/CSV). |
| **Kengaytmalar** | Hech qanday foydalanuvchi topilmasa — “Natija topilmadi” va filtrni tozalash havolasi; ma’lumotlar 1000 tadan oshsa — pagination (100 ta sahifada); eksport faqat joriy filterlangan ro’yxatni chiqaradi. |
