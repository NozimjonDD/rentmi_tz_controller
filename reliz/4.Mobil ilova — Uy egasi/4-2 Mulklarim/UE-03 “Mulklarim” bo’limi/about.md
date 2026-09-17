> Manba: [Release 2 01.06.2026 · Use cases: Landlord](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/25493538) · Ustuvorlik: Yuqori (P1)
>
> ❓ Sarlavhadagi raqam jadval ichidagidan farq qiladi (N6) — [4-2 Mulklarim](<../about.md>).

# UE-03 — “Mulklarim” bo’limi

| **UE-04 — “Mulklarim” bo’limi — to’liq e’lonlar ro’yxati** |
| --- |
| **Aktyor** | Uy egasi |
| **Turi** | Asosiy |
| **Ishga tushirish shartlari** | Foydalanuvchi tizimga kirgan va uy egasi roliga ega. |
| **Bajarish tartibi** | Foydalanuvchi “Mulklarim” bo’limini home page yoki profil navigatsiyadan ochadi; 2) Tizim foydalanuvchiga tegishli barcha e’lonlarni ro’yxatlaydi; 3) Har bir e’lon kartochkasida: mulk nomi va manzili, mulk turi, narx, xonalar soni, e’lon holati (badge: Faol, Moderatsiya kutmoqda, Tuzatish kutmoqda, Rad etildi, Arxivda, Bloklangan), yaratilgan sana ko’rsatiladi; 4) Ro’yxat yaratilgan sana bo’yicha kamayib tartiblanadi (eng yangi birinchi); 5) Filtr tugmasi orqali UE-05 filterlash ekrani ochiladi; 6) Har bir kartochkaga bosib e’lon tafsilotiga o’tish mumkin; 7) Pastki o’ngda “+” tugmasi — yangi e’lon yaratish (UE-06); 8) E’lon yo’q bo’lsa — empty state ko’rsatiladi. |
| **Vaqt reglamenti** | Ro’yxat yuklanish ≤ 3 sek; 20 tadan ortiq e’londa pagination yoki lazy load qo’llaniladi. |
| **Kiruvchi ma'lumotlar** | Foydalanuvchi identifikatori. |
| **Chiquvchi ma'lumotlar** | Foydalanuvchiga tegishli barcha e’lonlar ro’yxati holat, sana va asosiy parametrlar bilan. |
| **Kengaytmalar** | Filtr qo’llanilgan bo’lsa — faol filtr indikatori ko’rsatiladi va “Filtrni tozalash” havolasi chiqadi; internet yo’q bo’lsa — oxirgi kesh ko’rsatiladi. |
