> Manba: [Release 3 07.06.2026 · Mobile use cases](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/27656204)
>
> ⚠ Header va Actual History stories R5 da o'zgargan — [3-1 Asosiy sahifa](<../about.md>).

# IJ-01 — Asosiy sahifani ko'rish

| **Sseneriy ID** | IJ-01 |
| --- | --- |
| **Sseneriy nomi** | Asosiy sahifani ko'rish |
| **Guruh** | Asosiy sahifa |
| **Aktorlar** | Ijarachi (ro'yxatdan o'tgan), Mehmon (Guest) |
| **Tavsif** | Foydalanuvchi ilovaga kirganida asosiy sahifani ko'radi. Ro'yxatdan o'tgan ijarachi va mehmon uchun ko'rsatiladigan kontent farqlanadi. |
| **Kirish sharti** | Foydalanuvchi ilovani ishga tushirgan va internet aloqasi mavjud |
| **Chiqish natijasi** | Asosiy sahifa to'liq yuklanadi va foydalanuvchi o'z holatiga mos kontent ko'radi |

## Asosiy oqim — Ro'yxatdan o'tgan ijarachi

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| **1** | **Tizim** | Token tekshiriladi — mavjud va muddati o'tmagan |
| **2** | **Tizim** | Sahifa komponentlari parallel yuklanadi: Actual story, Rentmi Score, e'lonlar bo'limlari |
| **3** | **Tizim** | Actual story doirachalari — backend dinamik prioritet asosida |
| **4** | **Tizim** | Rentmi Score: tugallangan — ball (0–100), yorliq, indikator, ‘Skoringni yaxshilash'; skoringdan xali o’tmagan bo’lsa — 'Skoringdan o'ting' |
| **5** | **Tizim** | Qidiruv satri, ko'rinish tugmasi, filter tugmasi; hot categories; e'lonlar bo'limlari 'Hammasi >' |
| **6** | **Ijarachi** | Pull-to-refresh → barcha komponentlar qayta yuklanadi |

## Muqobil oqim — Guest

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| **1** | **Tizim** | Token yo'q — guest rejimi; marketing Actual story; Score bloki 'Skoringdan o'ting' |
| **2** | **Guest** | 'Skoringdan o'ting' → Ro'yxatdan o'tish; E'lon kartochkasi → IJ-08 |

## Xatolik holatlari

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | Kesh; banner; pull-to-refresh faol |
| **Server xatosi** | Xabar va Retry |
| **Token muddati o'tgan** | Avtomatik logout → login |
| **E'lonlar bo'sh** | Placeholder |

## Biznes qoidalari

| **#** | **Qoida** |
| --- | --- |
| **BQ-1** | Score bloki barcha ro'yxatdan o'tganlarga: tugallangan — rentmi skori ball; tugallanmagan — 'Skoringdan o'ting' |
| **BQ-2** | Guestga faqat 'Skoringdan o'ting'; shaxsiy ball ko'rsatilmaydi |
| **BQ-3** | Guest e'lonlarni ko'ra oladi; so'rov imkonsiz |
| **BQ-4** | Faqat manual pull-to-refresh |
| **BQ-5** | Stories tartibi backend tomonidan dinamik |
| **BQ-6** | ‘Skoringdan o'ting' → ro'yxatdan o'tish sahifasiga yo’naltirilsin, agar user myid identifikatsasidan o’tgan bo’lsa skoring sotib olishga agar o’tmagan bo’lsa identifikatsadan o’tishi shartli |
