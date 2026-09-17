> Manba: [Release 2 01.06.2026 · Use cases: Landlord](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/25493538) · Ustuvorlik: O’rta (P2)
>
> ⚠ "Rezervda" → "bron" (R5); ❓ "ijarada" statusi — [4-2 Mulklarim](<../about.md>). ❓ Sarlavhadagi raqam jadval ichidagidan farq qiladi (N6) — [4-2 Mulklarim](<../about.md>).

# UE-04 — “Mulklarim” filterlash

| **UE-05 — “Mulklarim” filterlash** |
| --- |
| **Aktyor** | Uy egasi |
| **Turi** | Asosiy |
| **Ishga tushirish shartlari** | Foydalanuvchi “Mulklarim” ro’yxatida (UE-04) va filtr tugmasini bosgan. |
| **Bajarish tartibi** | Filtr panel pastdan yuqorilab chiqadi (bottom sheet); 2) Foydalanuvchi quyidagi parametrlar bo’yicha filtr qo’llashi mumkin:    — Mulk turi(dropdown, bir tanlash);    — Ko’chmas mulk statusi: Qoralama (Draft), Moderatsiya kutmoqda, Tuzatish kutmoqda, Rad etildi, E’lon berishga tayyor, Faol, Ijaraga berilgan, Vaqtincha yopiq, Rezervda, Bloklangan, Arxivlangan (multi-select chips, bir nechtasini tanlash mumkin);    — Narx oralig’i: minimum va maksimum qiymat kiritish (range slider, UZS);    — Lokatsiya: Toshkent tumanlari ro’yxati (multi-select, har bir tumanda soni ko’rsatiladi);    — Sana bo’yicha: e’lon yaratilgan sana oralig’i (date range picker); 3) “Qo’llash” tugmasi bosilganda filtr natijalari ro’yxatga qo’llaniladi; 4) Filtr panel yopiladi va ro’yxat yangilanadi; 5) Faol filtr bo’lsa — ro’yxat tepasida faol parametrlar ko’rsatiladi; 6) “Filtrni tozalash” barcha filtrlarni olib tashlaydi. |
| **Vaqt reglamenti** | Filtr qo’llash ≤ 2 sek; natijalar yangilanishi ≤ 1 sek. |
| **Kiruvchi ma'lumotlar** | Mulk turi, holat (bir yoki bir nechta), narx oralig’i, tuman(lar), sana oralig’i. |
| **Chiquvchi ma'lumotlar** | Filterlangan e’lonlar ro’yxati; faol filtr ko’rsatkichi. |
| **Kengaytmalar** | Filtr qo’llanganida hech narsa topilmasa — “Bu filtr bo’yicha mulk topilmadi” xabari va “Filtrni tozalash” havolasi ko’rsatiladi; narx minimumi maksimumdan katta bo’lsa — validatsiya xatosi ko’rsatiladi. |
