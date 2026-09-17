> Manba: [Release 3 07.06.2026 · Mobile use cases](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/27656204)

# IJ-03 — E'lonlarni grid/list ko'rinishida ko'rish

| **Sseneriy ID** | IJ-03 |
| --- | --- |
| **Sseneriy nomi** | E'lonlarni grid/list ko'rinishida ko'rish |
| **Guruh** | Qidiruv va filter |
| **Aktorlar** | Ijarachi (ro'yxatdan o'tgan), Mehmon (Guest) |
| **Tavsif** | Foydalanuvchi e'lonlarni uchta ko'rinishdan birida (Single card, Grid, List) ko'radi. Default — Single card. |
| **Kirish sharti** | Asosiy sahifada yoki IJ-17 da; kamida bitta e'lon mavjud |
| **Chiqish natijasi** | E'lonlar tanlangan ko'rinishda; seans davomida saqlanadi |

## Asosiy oqim

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| **1** | **Tizim** | Default — Single card: rasm, nom, manzil, maydon, qavat, narx, ko'rishlar, 'Top' badge |
| **2** | **Foydalanuvchi** | Ko'rinish tugmasi: Single card → Grid → List → Single card sikli |
| **3** | **Foydalanuvchi** | E'lonni bosadi → IJ-08 |

## Muqobil oqimlar

| **Holat** | **Oqim** |
| --- | --- |
| **Ilova qayta ochiladi** | Default Single card |
| **IJ-17** | Xuddi shu sikl |
| **Guest** | Cheklovsiz |

## Xatolik holatlari

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Bo'sh ro'yxat** | Placeholder; tugma faol |
| **Rasm yuklanmadi** | Placeholder; ma'lumotlar davom etadi |

## Biznes qoidalari

| **#** | **Qoida** |
| --- | --- |
| **BQ-1** | Default — Single card (seans boshida) |
| **BQ-2** | Sikl: Single card → Grid → List → Single card |
| **BQ-3** | Faqat joriy seans — ilova yopilganda default |
| **BQ-4** | Asosiy sahifa va IJ-17 ikkalasida |
| **BQ-5** | E'lon bosish → IJ-08 |
| **BQ-6** | Guest va ro'yxatdan o'tgan uchun bir xil |
