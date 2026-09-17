> Manba: [Release 3 07.06.2026 · Admin use cases](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/27721770)

# AD-15 — 'Qiziq emas' ko'p bosilgan e'lonlarni avtomatik review ga yuborish

| **Sseneriy ID** | AD-15 |
| --- | --- |
| **Sseneriy nomi** | 'Qiziq emas' ko'p bosilgan e'lonlarni avtomatik review ga yuborish |
| **Guruh** | E'lonlar moderatsiyasi |
| **Aktorlar** | Tizim (avtomatik), Moderator |
| **Tavsif** | Foydalanuvchilar bitta e'lonni 'Qiziq emas' deb 2 ta yoki undan ko'p marta belgilasa, tizim avtomatik ravishda e'lonni review navbatiga qo'yadi. Review ga tushgan e'lon foydalanuvchilarga ko'rinishda qoladi — faqat moderator bloklasa yashiriladi. Moderator review navbatini ko'radi va qaror qabul qiladi. |
| **Kirish sharti** | Bitta e'lon 2 ta va undan ortiq 'Qiziq emas' belgisini olgan |
| **Chiqish natijasi** | E'lon review navbatiga tushadi; moderator ko'rib chiqadi va qaror qabul qiladi |

## Asosiy oqim — Avtomatik trigger

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| **1** | **Tizim** | Foydalanuvchi e'lonni 'Qiziq emas' deb belgilaydi (IJ-12) — hisoblagich +1 bo'ladi |
| **2** | **Tizim** | E'lonning 'Qiziq emas' hisoblagichi 2 ga yetganda avtomatik trigger ishga tushadi |
| **3** | **Tizim** | E'lon 'Review navbati' ga qo'shiladi; holat: 'Review kutmoqda' |
| **4** | **Tizim** | Moderatorga admin panelda bildirishnoma: '\[E'lon nomi\] 2 ta Qiziq emas belgisini oldi — ko'rib chiqing' |
| **5** | **Moderator** | Review navbatini ochadi — e'lon tafsilotlari, 'Qiziq emas' soni va foydalanuvchilar ro'yxatini ko'radi |
| **6** | **Moderator** | E'lonni ko'rib chiqadi va qaror qabul qiladi: Bloklash (AD-14) / Tozalash ('Qiziq emas' hisoblagichini reset qilish) |
| **7** | **Tizim** | Qarorga qarab e'lon holati yangilanadi; review navbatidan chiqariladi |

## Muqobil oqimlar

| **Holat** | **Oqim** |
| --- | --- |
| **Tozalash (Reset)** | Moderator e'lon asossiz review ga tushgan deb topsa → 'Tozalash' → 'Qiziq emas' hisoblagichi 0 ga qaytadi; e'lon oddiy holga qaytadi; keyingi 2 ta belgida yana trigger ishga tushadi |
| **Review navbatini filtrlash** | Moderator review navbatini sana, kategoriya, 'Qiziq emas' soni bo'yicha filtrlashi mumkin |
| **Bir vaqtda ko'p e'lon review da** | Moderator review navbatida bir nechta e'lonni toplu ko'radi; har biriga alohida qaror qabul qiladi |

## Xatolik holatlari

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Trigger ishlamadi (server xatosi)** | Keyingi sync da qayta tekshiriladi; e'lon review navbatiga qo'shiladi |
| **Moderator bildirishnomasi yuborilmadi** | E'lon review navbatida ko'rinadi; moderator keyingi kirganda ko'radi |

## Biznes qoidalari

| **#** | **Qoida** |
| --- | --- |
| **BQ-1** | Chegara: 2 ta 'Qiziq emas' belgisi → avtomatik review trigger |
| **BQ-2** | Review ga tushgan e'lon foydalanuvchilarga ko'rinishda qoladi — faqat moderator bloklasa yashiriladi |
| **BQ-3** | Moderator bildirishnomasi admin panelda ko'rsatiladi |
| **BQ-4** | Tozalash (Reset) dan keyin hisoblagich 0 ga qaytadi; keyingi 2 ta belgida yana trigger ishga tushadi |
| **BQ-5** | Bir foydalanuvchi bitta e'lonni faqat bir marta 'Qiziq emas' belgilashi mumkin (IJ-12) — hisoblagich duplikat sanalmaydi |
| **BQ-6** | Barcha trigger va moderator qarorlari audit jurnalida qayd etiladi |
