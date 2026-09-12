> Manba: [Release 3 07.06.2026 · Admin use cases](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/27721770)

# AD-13 — Shikoyatlar ro'yxatini ko'rish va ko'rib chiqish

| **Sseneriy ID** | AD-13 |
| --- | --- |
| **Sseneriy nomi** | Shikoyatlar ro'yxatini ko'rish va ko'rib chiqish |
| **Guruh** | E'lonlar moderatsiyasi |
| **Aktorlar** | Moderator, Administrator |
| **Tavsif** | Moderator ijarachi tomonidan yuborilgan shikoyatlarni ko'radi va ko'rib chiqadi. Har bir shikoyat uchta bosqichda boshqariladi: Yangi → Ko'rilmoqda → Yakunlangan. Moderator shikoyatni ko'rib chiqishda izoh qoldira oladi. Shikoyat tafsilotlarida e'lon ma'lumotlari va ijarachi matni ko'rsatiladi. |
| **Kirish sharti** | Moderator/Administrator admin panelga kirgan va Shikoyatlar bo'limini ochgan |
| **Chiqish natijasi** | Shikoyat ko'rib chiqiladi; holati yangilanadi; izoh qo'shiladi |

## Asosiy oqim

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| **1** | **Moderator** | Shikoyatlar bo'limini ochadi — barcha shikoyatlar ro'yxati ko'rsatiladi: e'lon nomi, shikoyatchi, sana, holat (Yangi / Ko'rilmoqda / Yakunlangan) |
| **2** | **Moderator** | Shikoyatni filtrlaydi: holat, sana, e'lon bo'yicha |
| **3** | **Moderator** | Shikoyatni bosadi — tafsilotlar sahifasi ochiladi: e'lon ma'lumotlari, ijarachi shikoyat matni, shikoyat sanasi, holat |
| **4** | **Moderator** | 'Ko'rilmoqda' holatiga o'tkazadi — shikoyatni o'rganish boshlanganligini belgilaydi |
| **5** | **Moderator** | E'lonni ko'rib chiqadi — kerak bo'lsa e'lonni tizimda ochadi |
| **6** | **Moderator** | Izoh kiritadi — masalan: 'E'lon tekshirildi, qoidabuzarlik aniqlandi' yoki 'Shikoyat asossiz' |
| **7** | **Moderator** | Qaror qabul qiladi: AD-14 (bloklash / ogohlantirish) yoki shikoyatni rad etish |
| **8** | **Tizim** | Shikoyat holati 'Yakunlangan' ga o'zgaradi; izoh saqlanadi; audit jurnalida qayd etiladi |

## Muqobil oqimlar

| **Holat** | **Oqim** |
| --- | --- |
| **Shikoyatni rad etish** | Moderator shikoyat asossiz deb topsa → 'Rad etish' tugmasi → izoh kiritadi → holat 'Yakunlangan'; e'longa hech qanday ta'sir qilmaydi |
| **Shikoyatlarni toplu ko'rish** | Moderator bir nechta shikoyatni tanlaydi → umumiy statistikani ko'radi (qaysi e'longa ko'p shikoyat kelgan) |
| **Bir e'lon bo'yicha barcha shikoyatlar** | E'lon nomini bosib o'sha e'lon bo'yicha barcha shikoyatlarni ko'rish mumkin |

## Xatolik holatlari

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Server xatosi** | 'Ma'lumotlarni yuklab bo'lmadi' xabari va Retry |
| **Holat yangilashda xato** | 'Holat o'zgartirib bo'lmadi' xabari; shikoyat oldingi holatda qoladi |

## Biznes qoidalari

| **#** | **Qoida** |
| --- | --- |
| **BQ-1** | Shikoyat holatlari: Yangi → Ko'rilmoqda → Yakunlangan; faqat oldinga o'tish mumkin |
| **BQ-2** | Moderator har bir shikoyat uchun izoh qoldira oladi — izoh majburiy emas, ixtiyoriy |
| **BQ-3** | Yangi shikoyat kelganda moderatorga admin panelda bildirishnoma ko'rsatiladi |
| **BQ-4** | Shikoyat tafsilotlarida: e'lon nomi, ijarachi ID, shikoyat matni, sana, holat ko'rsatiladi |
| **BQ-5** | Barcha moderator amallari (holat o'zgartirish, izoh) audit jurnalida sana va mas'ul bilan qayd etiladi |
| **BQ-6** | Rad etilgan shikoyat 'Yakunlangan' holatga o'tadi — e'longa hech qanday ta'sir qilmaydi |
