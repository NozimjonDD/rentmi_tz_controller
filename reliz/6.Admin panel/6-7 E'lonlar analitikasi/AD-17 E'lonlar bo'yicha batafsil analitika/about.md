> Manba: [Release 3 07.06.2026 · Admin use cases](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/27721770)

# AD-17 — E'lonlar bo'yicha batafsil analitika

| **Sseneriy ID** | AD-17 |
| --- | --- |
| **Sseneriy nomi** | E'lonlar bo'yicha batafsil analitika — ko'rishlar, ariza, saqlangan monitoring |
| **Guruh** | E'lonlar analitikasi |
| **Aktorlar** | Administrator |
| **Tavsif** | Administrator e'lonlar bo'yicha umumiy dashboard va har bir e'lon bo'yicha qisman alohida analitika ko'radi. Ko'rsatkichlar: ko'rishlar soni, ariza soni, saqlangan soni, 'Qiziq emas' soni, o'xshash e'lonlar bilan solishtirish. Dashboard umumiy holat va trendlarni ko'rsatadi. |
| **Kirish sharti** | Administrator admin panelga kirgan va Analitika → E'lonlar bo'limi ochilgan |
| **Chiqish natijasi** | Umumiy dashboard va alohida e'lon analitikasi ko'rsatiladi |

## Asosiy oqim — Umumiy dashboard

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| **1** | **Administrator** | Analitika bo'limini ochadi → E'lonlar dashboard ko'rsatiladi |
| **2** | **Tizim** | Umumiy ko'rsatkichlar: jami faol e'lonlar, bugungi yangi e'lonlar, jami ko'rishlar, jami arizalar, jami saqlangan |
| **3** | **Tizim** | Trend grafiklari: ko'rishlar, arizalar, saqlangan ko'rsatkichlari vaqt o'qi bo'yicha |
| **4** | **Tizim** | Top e'lonlar jadvali: ko'rishlar, ariza, saqlangan bo'yicha tartiblangan |
| **5** | **Administrator** | Vaqt oralig'ini tanlaydi: bugun / hafta / oy / 3 oy / yil |
| **6** | **Administrator** | E'lonni tanlaydi — alohida e'lon analitikasiga o'tiladi |

## Asosiy oqim — Alohida e'lon analitikasi

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| **1** | **Administrator** | E'lonlar ro'yxatidan bitta e'lonni tanlaydi yoki qidiradi |
| **2** | **Tizim** | E'lon analitika sahifasi ochiladi: e'lon asosiy ma'lumotlari (nom, kategoriya, narx, joylashuv) |
| **3** | **Tizim** | Ko'rsatkichlar bloki: ko'rishlar soni, ariza soni, saqlangan soni, 'Qiziq emas' soni — jami va tanlangan vaqt oralig'ida |
| **4** | **Tizim** | Vaqt bo'yicha dinamika grafigi: har bir ko'rsatkich alohida chiziq sifatida |
| **5** | **Administrator** | Vaqt oralig'ini tanlaydi — ko'rsatkichlar yangilanadi |
| **6** | **Tizim** | Solishtirish bloki: o'xshash kategoriya e'lonlarining o'rtacha ko'rsatkichlari bilan taqqoslash |

## Muqobil oqimlar

| **Holat** | **Oqim** |
| --- | --- |
| **Kategoriya bo'yicha filtrlash** | Dashboard da kategoriya tanlanadi — faqat o'sha kategoriya e'lonlari ko'rsatiladi |
| **Hudud bo'yicha filtrlash** | Tuman yoki viloyat tanlanadi — o'sha hudud e'lonlari analitikasi |
| **E'lon qidirish** | Nom yoki ID bo'yicha qidirib alohida e'lon analitikasiga o'tish mumkin |
| **Ko'rsatkich bo'yicha tartiblash** | Jadvalda ustun sarlavhasiga bosilib ko'rishlar/ariza/saqlangan bo'yicha tartiblash |

## Xatolik holatlari

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Server xatosi** | 'Ma'lumotlarni yuklab bo'lmadi' xabari va Retry |
| **E'lon analitikasi yo'q** | 'Bu e'lon bo'yicha ma'lumotlar mavjud emas' placeholder |

## Biznes qoidalari

| **#** | **Qoida** |
| --- | --- |
| **BQ-1** | Umumiy dashboard: jami faol e'lonlar, ko'rishlar, arizalar, saqlangan — trendlar va top e'lonlar jadvali |
| **BQ-2** | Alohida e'lon analitikasi: ko'rishlar, ariza, saqlangan, 'Qiziq emas' — vaqt dinamikasi va solishtirish |
| **BQ-3** | Ko'rsatkichlar real-time yangilanadi |
| **BQ-4** | Vaqt oralig'i: bugun, hafta, oy, 3 oy, yil |
| **BQ-5** | Solishtirish bloki o'xshash kategoriya e'lonlarining o'rtacha ko'rsatkichlari bilan taqqoslaydi |
| **BQ-6** | Export funksiyasi mavjud emas — faqat ko'rish |
| **BQ-7** | Jadvalda ko'rishlar, ariza, saqlangan bo'yicha tartiblash mumkin |
