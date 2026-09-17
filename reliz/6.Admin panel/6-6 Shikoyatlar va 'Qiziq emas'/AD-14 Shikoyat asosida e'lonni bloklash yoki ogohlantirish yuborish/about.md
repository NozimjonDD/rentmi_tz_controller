> Manba: [Release 3 07.06.2026 · Admin use cases](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/27721770)

# AD-14 — Shikoyat asosida e'lonni bloklash yoki ogohlantirish yuborish

| **Sseneriy ID** | AD-14 |
| --- | --- |
| **Sseneriy nomi** | Shikoyat asosida e'lonni bloklash yoki uy egasiga ogohlantirish yuborish |
| **Guruh** | E'lonlar moderatsiyasi |
| **Aktorlar** | Moderator, Administrator |
| **Tavsif** | Moderator shikoyat ko'rib chiqilgandan so'ng qaror qabul qiladi: e'lonni bloklash (foydalanuvchilarga ko'rsatilmaydi) yoki uy egasiga ilova ichida notification ogohlantirish yuborish. Bloklangan e'lon tiklash mumkin. |
| **Kirish sharti** | Moderator AD-13 da shikoyat tafsilotlarini ko'rib chiqib qaror qabul qilishga tayyor |
| **Chiqish natijasi** | E'lon bloklanadi va foydalanuvchilarga ko'rsatilmaydi; yoki uy egasiga ogohlantirish notification yuboriladi |

## Asosiy oqim — E'lonni bloklash

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| **1** | **Moderator** | Shikoyat tafsilotlari sahifasida (AD-13) 'Bloklash' tugmasini bosadi |
| **2** | **Tizim** | Tasdiqlash so'rovi: 'E'lonni bloklashni tasdiqlaysizmi? E'lon foydalanuvchilarga ko'rsatilmaydi' + sabab kiritish maydoni |
| **3** | **Moderator** | Bloklash sababini kiritadi (masalan: 'Yolg'on ma'lumot', 'Qoidabuzarlik') |
| **4** | **Moderator** | 'Bloklash' tugmasini bosadi |
| **5** | **Tizim** | E'lon holati 'Bloklangan' ga o'zgaradi; ilovada foydalanuvchilarga ko'rsatilmaydi |
| **6** | **Tizim** | Uy egasiga ilova ichida notification: 'Sizning e'loningiz bloklanди. Sabab: \[sabab\]. Batafsil ma'lumot uchun qo'llab-quvvatlash bilan bog'laning' |
| **7** | **Tizim** | Shikoyat holati 'Yakunlangan' ga o'tadi; bloklash sababi audit jurnalida qayd etiladi |

## Muqobil oqimlar

| **Holat** | **Oqim** |
| --- | --- |
| **Ogohlantirish yuborish** | Moderator 'Ogohlantirish yuborish' tugmasini bosadi → ogohlantirish matni kiritiladi → 'Yuborish' → uy egasiga ilova ichida notification: 'E'loningiz bo'yicha ogohlantirish keldi: \[matn\]' → shikoyat 'Yakunlangan' |
| **Bloklangan e'lonni tiklash** | Administrator bloklangan e'lonni tanlaydi → 'Tiklash' → sabab kiritadi → e'lon faol holatga qaytadi; uy egasiga notification: 'E'loningiz tiklandi' |
| **Bir vaqtda bloklash + ogohlantirish** | Moderator e'lonni bloklab, bir vaqtda ogohlantirish ham yuborishi mumkin — ikkalasi birga bajariladi |

## Xatolik holatlari

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Bloklash sababi kiritilmagan** | 'Sabab kiritilishi shart' inline xabar; 'Bloklash' disabled |
| **Notification yuborishda xato** | E'lon bloklanadi; notification yuborilmaydi; 'Notification yuborib bo'lmadi, qayta urinib ko'ring' xabari — admin qayta yuborishi mumkin |
| **Server xatosi** | 'Amal amalga oshmadi' xabari va Retry; e'lon holatga ta'sir qilmaydi |

## Biznes qoidalari

| **#** | **Qoida** |
| --- | --- |
| **BQ-1** | Bloklangan e'lon ilovada foydalanuvchilarga ko'rsatilmaydi — o'chirilmaydi, faqat yashiriladi |
| **BQ-2** | Bloklash sababi majburiy maydon — saqlashdan oldin kiritilishi shart |
| **BQ-3** | Ogohlantirish uy egasiga faqat ilova ichida notification orqali yuboriladi |
| **BQ-4** | Bloklangan e'lonni administrator tiklashi mumkin — tiklash ham audit jurnalida qayd etiladi |
| **BQ-5** | Shikoyat asosida bloklash shikoyat holatini avtomatik 'Yakunlangan' ga o'zgartiradi |
| **BQ-6** | Barcha amallar (bloklash, ogohlantirish, tiklash) audit jurnalida sana, mas'ul va sabab bilan qayd etiladi |
