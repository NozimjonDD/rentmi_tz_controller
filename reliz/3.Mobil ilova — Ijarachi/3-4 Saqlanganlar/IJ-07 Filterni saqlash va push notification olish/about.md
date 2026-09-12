> Manba: [Release 3 07.06.2026 · Mobile use cases](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/27656204)

# IJ-07 — Filterni saqlash va push notification olish

| **Sseneriy ID** | IJ-07 |
| --- | --- |
| **Sseneriy nomi** | Filterni saqlash va push notification olish |
| **Guruh** | Qidiruv va filter |
| **Aktorlar** | Ijarachi (ro'yxatdan o'tgan) |
| **Tavsif** | Ro'yxatdan o'tgan ijarachi filter parametrlarini saqlab qo'yadi. Yangi mos e'londa FCM push notification keladi. Notification istalgan vaqtda yoqib/o'chiriladi. |
| **Kirish sharti** | IJ-06 da kamida bitta parametr; ro'yxatdan o'tgan |
| **Chiqish natijasi** | Filter saqlanadi; notification yoqilgan bo'lsa yangi mos e'londa push notification keladi |

## Asosiy oqim

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| **1** | **Ijarachi** | 'Filterni saqlash' → filter serverga saqlanadi; default nom: parametrlar qisqacha tavsifi |
| **2** | **Tizim** | Notification so'rovi: Ruxsat / Rad etish |
| **3** | **Ijarachi** | 'Ruxsat berish' → FCM token; 'Filter saqlandi va bildirishnomalar yoqildi' |
| **4** | **Tizim** | Yangi mos e'londa push: '\[Tuman\]da yangi \[mulk turi\]: \[narx\] so'm/oyiga' → bosilganda IJ-08 |

## Muqobil oqimlar

| **Holat** | **Oqim** |
| --- | --- |
| **Notification rad** | Filter saqlanadi; 'O'chirilgan' |
| **Toggle** | Yoqib/o'chirish → server darhol yangilanadi |
| **O'chirish** | Tasdiqlash → filter va notification o'chiriladi |
| **Saqlangan filtrni qo'llash** | Filtrni bosish → IJ-17 |
| **Guest** | 'Saqlash' ko'rinmaydi |

## Xatolik holatlari

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | Filter saqlanmaydi |
| **FCM xato** | Filter saqlanadi; notification yoqilmaydi |
| **Server xatosi** | Filter saqlanmaydi; Retry |

## Biznes qoidalari

| **#** | **Qoida** |
| --- | --- |
| **BQ-1** | Faqat ro'yxatdan o'tganlarga |
| **BQ-2** | Filtrlar soni cheksiz |
| **BQ-3** | Notification matni: '\[Tuman\]da yangi \[mulk turi\]: \[narx\] so'm/oyiga' |
| **BQ-4** | Barcha filter uchun notification bir tugma orqali yoqib o’chirilishi kerak |
| **BQ-5** | O'chirishdan oldin tasdiqlash |
| **BQ-6** | Notification → to'g'ridan-to'g'ri IJ-08 |
| **BQ-7** | Faqat to'liq mos e'londa notification |
| **BQ-8** | Filter o'chirilganda notification ham o'chiriladi |
