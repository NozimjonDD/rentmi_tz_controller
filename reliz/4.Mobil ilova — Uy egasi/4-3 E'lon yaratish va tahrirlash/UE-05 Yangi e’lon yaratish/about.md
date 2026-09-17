> Manba: [Release 2 01.06.2026 · Use cases: Landlord](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/25493538) · Ustuvorlik: Yuqori (P1)
>
> ❓ Sarlavhadagi raqam jadval ichidagidan farq qiladi (N6) — [4-2 Mulklarim](<../../4-2 Mulklarim/about.md>).

# UE-05 — Yangi e’lon yaratish

| **UE-06 — Yangi e’lon yaratish** |
| --- |
| **Aktyor** | Uy egasi |
| **Turi** | Asosiy |
| **Ishga tushirish shartlari** | Foydalanuvchi tizimga kirgan, uy egasi roliga ega va MyID orqali identifikatsiyadan o’tgan. |
| **Bajarish tartibi** | Foydalanuvchi “+” tugmasini bosadi; 2) E’lon yaratish ekrani ochiladi — ko’p qadam shakli (multi-step form); 3) 1-qadam — Asosiy ma’lumotlar: mulk turi tanlash, xonalar soni, umumiy maydon (kv.m), qavat, umumiy qavatlar soni; 4) 2-qadam — Joylashuv: Google Maps orqali joylashuvni belgilash yoki manzil kiritish (ko’cha, uy raqami, tuman, shahar), koordinatalar avtomatik saqlanadi; 5) 3-qadam — Narx va shartlar: oylik ijara narxi (UZS), kommunal to’lovlar holati (kiritilgan / alohida), qo’shimcha shartlar (matn maydoni); 6) 4-qadam — Foto va tavsif: kamida 1 ta, maksimal 10 ta foto yuklash (S3 ga); asosiy foto belgilash; tavsif matni (majburiy, kamida 50 belgi); 7) 5-qadam — Ko’rib chiqish: barcha kiritilgan ma’lumotlar ko’rsatiladi, tahrirlash imkoniyati har qadam uchun; 8) “E’lonni yuborish” tugmasi bosilganda e’lon “Moderatsiya kutmoqda” holatiga o’tadi; 9) Muvaffaqiyat xabari ko’rsatiladi: “E’loningiz moderatsiyaga yuborildi. Natija haqida bildirishnoma olasiz.”; 10) Foydalanuvchi “Mulklarim” sahifasiga qaytariladi. |
| **Vaqt reglamenti** | Har bir qadam yuklanish ≤ 1 sek; foto yuklash (har biri) ≤ 5 sek; e’lonni saqlash ≤ 3 sek. |
| **Kiruvchi ma'lumotlar** | Mulk turi, maydon, xonalar, qavat, joylashuv (koordinatalar + manzil), narx, shartlar, fotolar (S3), tavsif. |
| **Chiquvchi ma'lumotlar** | Yangi e’lon “Moderatsiya kutmoqda” holatida; muvaffaqiyat xabari; push bildirishnoma yuboriladi. |
| **Kengaytmalar** | Identifikatsiyadan o’tmagan uy egasi e’lon yarata olmaydi — MyID ga yo’naltirish banneri ko’rsatiladi; majburiy maydon to’ldirilmasa — “Yuborish” tugmasi faol bo’lmaydi; foto 5 MB dan oshsa — xatolik xabari; internet uzilsa — qoralama (draft) saqlanadi va foydalanuvchi ogohlantirish oladi; Google Maps yuklanmasa — qo’lda manzil kiritish imkoniyati ko’rsatiladi. |
