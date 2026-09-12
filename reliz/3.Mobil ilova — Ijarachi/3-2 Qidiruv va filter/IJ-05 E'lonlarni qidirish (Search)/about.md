> Manba: [Release 3 07.06.2026 · Mobile use cases](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/27656204)

# IJ-05 — E'lonlarni qidirish (Search)

| **Sseneriy ID** | IJ-05 |
| --- | --- |
| **Sseneriy nomi** | E'lonlarni qidirish |
| **Guruh** | Qidiruv va filter |
| **Aktorlar** | Ijarachi (ro'yxatdan o'tgan), Mehmon (Guest) |
| **Tavsif** | Foydalanuvchi qidiruv satriga matn kiritib, e'lonlarni nom va tavsif bo'yicha real-time qidiradi. Natijalar IJ-17 da. Oxirgi qidiruvlar saqlanadi. Bo'sh natijada tavsiyalar chiqadi. |
| **Kirish sharti** | Asosiy sahifada; qidiruv satri ko'rinishda |
| **Chiqish natijasi** | Mos e'lonlar IJ-17 da; yoki bo'sh bo'lsa tavsiyalar |

## Asosiy oqim

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| **1** | **Foydalanuvchi** | Qidiruv satriga bosadi → klaviatura; oxirgi qidiruvlar pastda |
| **2** | **Foydalanuvchi** | So'z yozadi → real-time; debounce 300ms; nom + tavsif; autocomplete |
| **3** | **Foydalanuvchi** | Enter yoki autocomplete → tarixga saqlanadi (maks 10); IJ-17 ochiladi |
| **4** | **Foydalanuvchi** | E'lonni bosadi → IJ-08 |

## Muqobil oqimlar

| **Holat** | **Oqim** |
| --- | --- |
| **Tarixdan foydalanish** | Tanlash → IJ-17 |
| **Bo'sh natija** | 'Topilmadi'; tavsiyalar |
| **Bekor qilish** | X yoki klaviaturani yopish → asosiy sahifa |
| **Guest** | Cheklovsiz |

## Xatolik holatlari

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | Xabar |
| **Server xatosi** | Xabar va Retry |
| **1 harf** | Kamida 2 belgi kerak |

## Biznes qoidalari

| **#** | **Qoida** |
| --- | --- |
| **BQ-1** | Real-time; debounce 300ms |
| **BQ-2** | Nom va tavsif bo'yicha |
| **BQ-3** | Kamida 2 belgi |
| **BQ-4** | Maks 10 ta tarix |
| **BQ-5** | Bo'sh natijada tavsiyalar |
| **BQ-6** | Guest va ro'yxatdan o'tgan uchun bir xil |
