> Manba: [Release 3 07.06.2026 · Mobile use cases](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/27656204)

# IJ-12 — E'lonni 'Qiziq emas'/Bloklash deb belgilash

| **Sseneriy ID** | IJ-12 |
| --- | --- |
| **Sseneriy nomi** | E'lonni 'Qiziq emas' deb belgilash |
| **Guruh** | E'lon ko'rish |
| **Aktorlar** | Ijarachi (ro'yxatdan o'tgan) |
| **Tavsif** | Ro'yxatdan o'tgan ijarachi 3 nuqta menyusidan 'Blok qilish' ni tanlaydi. Tasdiqdan keyin e'lon feeddan darhol olib tashlanadi. Qaytarib bo'lmaydi. Statistika AD-16 da aks etadi. |
| **Kirish sharti** | IJ-08 sahifasida; ro'yxatdan o'tgan |
| **Chiqish natijasi** | E'lon feeddan darhol olib tashlanadi; kontekstga qarab asosiy sahifaga yoki IJ-17 ga yo'naltiriladi |

## Asosiy oqim

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| **1** | **Foydalanuvchi** | 3 nuqta (⋮) → 'Blok qilish' |
| **2** | **Tizim** | Tasdiqlash bottom sheet: icon, 'Qiziq emas' sarlavhasi, 'Ha, qiziq emas' (qizil) / 'Yo'q, qiziq' (ko'k) |
| **3** | **Foydalanuvchi** | 'Ha, qiziq emas' tugmasini bosadi |
| **4** | **Tizim** | Serverga yuboriladi; e'lon bloklanadi |
| **5** | **Tizim** | E'lon feeddan darhol olib tashlanadi |
| **6** | **Tizim** | Kontekstga qarab: IJ-17 dan kelgan → IJ-17 ga; asosiy sahifadan → asosiy sahifaga |
| **7** | **Tizim** | 'Qiziq emas' statistikasi AD-16 da yangilanadi |

## Muqobil oqimlar

| **Holat** | **Oqim** |
| --- | --- |
| **'Yo'q, qiziq' yoki X** | Bottom sheet yopiladi; IJ-08 da qoliladi |
| **Guest** | 'Blok qilish' ko'rinmaydi |

## Xatolik holatlari

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | Serverga yuborilmaydi; xabar; bottom sheet ochiq |
| **Server xatosi** | 'Amalga oshmadi'; Retry; feeddan olib tashlanmaydi |

## Biznes qoidalari

| **#** | **Qoida** |
| --- | --- |
| **BQ-1** | Faqat ro'yxatdan o'tganlarga |
| **BQ-2** | 'Ha, qiziq emas' bosilgandan so'ng darhol feeddan olib tashlanadi |
| **BQ-3** | Qaytarib bo'lmaydi — undo yo'q |
| **BQ-4** | Kontekstga qarab yo'naltirish: IJ-17 dan → IJ-17; asosiy → asosiy |
| **BQ-5** | Statistika AD-16 da real-time yangilanadi |
| **BQ-6** | E'lon qidiruv va tavsiya natijalaridan ham chiqariladi |
| **BQ-7** | 'Yo'q, qiziq' yoki X — hech qanday amal bajarilmaydi |
