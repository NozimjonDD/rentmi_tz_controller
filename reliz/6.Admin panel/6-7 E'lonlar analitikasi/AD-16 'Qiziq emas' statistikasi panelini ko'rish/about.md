> Manba: [Release 3 07.06.2026 · Admin use cases](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/27721770)

# AD-16 — 'Qiziq emas' statistikasi panelini ko'rish

| **Sseneriy ID** | AD-16 |
| --- | --- |
| **Sseneriy nomi** | 'Qiziq emas' statistikasi panelini ko'rish |
| **Guruh** | E'lonlar analitikasi |
| **Aktorlar** | Administrator, Moderator |
| **Tavsif** | Administrator va moderator 'Qiziq emas' statistikasi panelini ko'radi. Panel barcha vaqt oraliqlarini qamrab oladi. Eng ko'p rad etilgan e'lonlar reytingi, trend grafigi, sabab tahlili ko'rsatiladi. Export funksiyasi mavjud emas. |
| **Kirish sharti** | Administrator/Moderator admin panelga kirgan va Analitika → 'Qiziq emas' bo'limini ochgan |
| **Chiqish natijasi** | 'Qiziq emas' statistikasi to'liq ko'rsatiladi |

## Asosiy oqim

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| **1** | **Administrator** | Analitika bo'limidan 'Qiziq emas' statistikasi sahifasini ochadi |
| **2** | **Tizim** | Asosiy ko'rsatkichlar ko'rsatiladi: jami 'Qiziq emas' soni, bugungi soni, o'tgan hafta/oy bilan solishtirish |
| **3** | **Tizim** | Eng ko'p 'Qiziq emas' olgan e'lonlar reytingi ko'rsatiladi: e'lon nomi, kategoriya, soni, so'nggi sana |
| **4** | **Tizim** | Trend grafigi ko'rsatiladi: vaqt o'qi bo'yicha 'Qiziq emas' dinamikasi |
| **5** | **Administrator** | Vaqt oralig'ini tanlaydi: bugun / hafta / oy / 3 oy / yil / barcha vaqt |
| **6** | **Tizim** | Tanlangan vaqt oralig'i bo'yicha statistika yangilanadi |
| **7** | **Administrator** | E'lonni bosadi — o'sha e'lon bo'yicha batafsil 'Qiziq emas' tarixi ko'rsatiladi: sana, foydalanuvchi soni |

## Muqobil oqimlar

| **Holat** | **Oqim** |
| --- | --- |
| **Kategoriya bo'yicha filtrlash** | Administrator kategoriyani tanlaydi — o'sha kategoriya e'lonlari bo'yicha statistika ko'rsatiladi |
| **Review ga yuborilgan e'lonlar** | 'Review ga yuborilgan' filtri — chegara (2 ta) ga yetib review navbatiga tushgan e'lonlar alohida ko'rsatiladi |
| **Statistika bo'sh** | 'Hozircha ma'lumotlar mavjud emas' placeholder ko'rsatiladi |

## Xatolik holatlari

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Server xatosi** | 'Ma'lumotlarni yuklab bo'lmadi' xabari va Retry |
| **Internet yo'q** | Xabar ko'rsatiladi; sahifa yuklanmaydi |

## Biznes qoidalari

| **#** | **Qoida** |
| --- | --- |
| **BQ-1** | Statistika barcha vaqt oraliqlarini qamrab oladi: bugun, hafta, oy, 3 oy, yil, barcha vaqt |
| **BQ-2** | Export funksiyasi mavjud emas — faqat ko'rish mumkin |
| **BQ-3** | Statistika real-time yangilanadi — yangi 'Qiziq emas' belgisi qo'shilganda darhol aks etadi |
| **BQ-4** | Eng ko'p 'Qiziq emas' olgan e'lonlar reytingi o'sish tartibida (ko'pdan kamga) ko'rsatiladi |
| **BQ-5** | Har bir e'lon bo'yicha batafsil tarix (sana bo'yicha dinamika) ko'rish mumkin |
