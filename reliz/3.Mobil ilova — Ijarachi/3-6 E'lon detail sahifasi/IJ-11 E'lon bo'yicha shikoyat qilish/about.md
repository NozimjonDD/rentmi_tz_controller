> Manba: [Release 3 07.06.2026 · Mobile use cases](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/27656204)

# IJ-11 — E'lon bo'yicha shikoyat qilish

| **Sseneriy ID** | IJ-11 |
| --- | --- |
| **Sseneriy nomi** | E'lon bo'yicha shikoyat qilish |
| **Guruh** | E'lon ko'rish |
| **Aktorlar** | Ijarachi (ro'yxatdan o'tgan) |
| **Tavsif** | Ro'yxatdan o'tgan ijarachi 3 nuqta menyusidan 'Shikoyat qilish' ni tanlaydi. Matn kiritib yuboradi. Bir foydalanuvchi bitta e'lon bo'yicha faqat bir marta shikoyat qila oladi. |
| **Kirish sharti** | IJ-08 sahifasida; ro'yxatdan o'tgan; avval shikoyat qilinmagan |
| **Chiqish natijasi** | Shikoyat adminga yuboriladi; 'Shikoyatingiz yuborildi' xabari ko'rsatiladi |

## Asosiy oqim

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| **1** | **Foydalanuvchi** | 3 nuqta (⋮) → 'Shikoyat qilish' |
| **2** | **Tizim** | Bottom sheet: icon, sarlavha, textarea, 'Ariza jo'natish' tugmasi |
| **3** | **Foydalanuvchi** | Shikoyat matnini kiritadi, yoki varyantlardan tanlash |
| **4** | **Foydalanuvchi** | 'Ariza jo'natish' → serverga yuboriladi; admin panelda (AD-13) ko'rinadi |
| **5** | **Tizim** | 'Shikoyatingiz yuborildi' xabari; bottom sheet yopiladi; IJ-08 ga qaytiladi |
| **6** | **Tizim** | 3 nuqta menyusida 'Shikoyat yuborilgan' (disabled) |

## Muqobil oqimlar

| **Holat** | **Oqim** |
| --- | --- |
| **X bosiladi** | Bottom sheet yopiladi; yuborilmaydi |
| **Bo'sh textarea** | 'Matnini kiriting'; 'Ariza jo'natish' disabled |
| **Avval shikoyat qilingan** | 'Shikoyat yuborilgan' (disabled); bottom sheet ochilmaydi |
| **Guest** | Ko'rinmaydi |

## Xatolik holatlari

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | Yuborilmaydi; xabar; matn saqlanadi |
| **Server xatosi** | Xabar va Retry; matn saqlanadi |

## Biznes qoidalari

| **#** | **Qoida** |
| --- | --- |
| **BQ-1** | Faqat ro'yxatdan o'tganlarga |
| **BQ-2** | Bitta e'lon bo'yicha faqat bir marta |
| **BQ-3** | Yuborilgandan keyin 'Shikoyat yuborilgan' (disabled) |
| **BQ-4** | Bo'sh textarea → 'Ariza jo'natish' disabled |
| **BQ-5** | 'Shikoyatingiz yuborildi' xabari |
| **BQ-6** | Admin panelida (AD-13) moderatorga uzatiladi |
| **BQ-7** | Xatolikda matn saqlanib qoladi |
