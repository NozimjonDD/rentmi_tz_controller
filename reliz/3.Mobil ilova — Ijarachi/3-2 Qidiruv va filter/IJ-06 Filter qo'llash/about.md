> Manba: [Release 3 07.06.2026 · Mobile use cases](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/27656204)

# IJ-06 — Filter qo'llash

| **Sseneriy ID** | IJ-06 |
| --- | --- |
| **Sseneriy nomi** | Filter qo'llash |
| **Guruh** | Qidiruv va filter |
| **Aktorlar** | Ijarachi (ro'yxatdan o'tgan), Mehmon (Guest) |
| **Tavsif** | Foydalanuvchi filter tugmasini bosib parametrlar bo'yicha filtrlaydi. 'Qidirish' bosilganda qo'llaniladi. 'Tozalash' barcha parametrlarni tozalaydi. |
| **Kirish sharti** | Asosiy sahifada yoki IJ-17 da |
| **Chiqish natijasi** | Tanlangan parametrlarga mos e'lonlar IJ-17 da |

## Asosiy oqim

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| **1** | **Foydalanuvchi** | Filter tugmasi → bottom sheet: Ijara turi, Lokatsiya (3 darajali; multi-select), Narx slider (So'm/Dollar), Xonalar/Maydon/Qavat min-max, Mulk turi multi-select, Jonivorlar checkbox |
| **2** | **Foydalanuvchi** | 'Qidirish' → bottom sheet yopiladi; IJ-17 ochiladi |

## Muqobil oqimlar

| **Holat** | **Oqim** |
| --- | --- |
| **Tozalash** | Barcha parametrlar bir vaqtda tozalanadi |
| **X bosiladi** | O'zgartirish qo'llanilmaydi |
| **Kategoriya bilan** | IJ-04 kategoriyasi saqlanadi |
| **Bo'sh natija** | 'Topilmadi' + 'O'zgartirish' |
| **Guest** | Filtrdan foydalana oladi; 'Saqlash' ko'rsatilmaydi |

## Xatolik holatlari

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | Bottom sheet ochiq qoladi |
| **Server xatosi** | Xabar va Retry; parametrlar saqlanadi |
| **Min > max** | Inline xabar; 'Qidirish' disabled |

## Biznes qoidalari

| **#** | **Qoida** |
| --- | --- |
| **BQ-1** | Faqat 'Qidirish' bosilganda qo'llaniladi |
| **BQ-2** | 'Tozalash' barcha parametrlarni bir vaqtda |
| **BQ-3** | Lokatsiya 3 darajali; tuman multi-select |
| **BQ-4** | So'm/Dollar; valyuta o'zgarganda qayta kiritiladi |
| **BQ-5** | Mulk turi multi-select |
| **BQ-6** | Min > max — disabled |
| **BQ-7** | Guest filtrdan foydalana oladi; 'Saqlash' faqat ro'yxatdan o'tganlarga |
| **BQ-8** | Filterlar IJ-17 da chip/badge ko'rinishida |
