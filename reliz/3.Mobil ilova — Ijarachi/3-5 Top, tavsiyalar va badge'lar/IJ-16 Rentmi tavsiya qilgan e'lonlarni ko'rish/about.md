> Manba: [Release 3 07.06.2026 · Mobile use cases](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/27656204)
>
> ⚠ Tavsiya mezonlari R5 da o'zgargan — [7-4 Rentmi Maslahat beradi](<../../../7.Algoritmlar/7-4 Rentmi Maslahat beradi/about.md>).

# IJ-16 — Rentmi tavsiya qilgan e'lonlarni ko'rish

| **Sseneriy ID** | IJ-16 |
| --- | --- |
| **Sseneriy nomi** | Rentmi tavsiya qilgan e'lonlarni ko'rish |
| **Guruh** | Top va tavsiyalar |
| **Aktorlar** | Ijarachi (ro'yxatdan o'tgan), Mehmon (Guest) |
| **Tavsif** | Foydalanuvchi asosiy sahifadagi 'Rentmi Maslahat beradi' bo'limida personallashtirilgan tavsiya e'lonlarini ko'radi. Tavsiyalar ijarachining skoring bali, qidiruv tarixi va sevimli kategoriyalari asosida belgilanadi. Guest uchun umumiy mashhur e'lonlar ko'rsatiladi. 'Hammasi >' bosilganda to'liq ro'yxat IJ-17 da ochiladi. |
| **Kirish sharti** | Foydalanuvchi asosiy sahifada (IJ-01); kamida bitta tavsiya e'lon mavjud |
| **Chiqish natijasi** | Tavsiya e'lonlar ko'rsatiladi; 'Hammasi >' bosilsa IJ-17 da to'liq tavsiyalar ro'yxati ochiladi |

## Asosiy oqim — Ro'yxatdan o'tgan ijarachi

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| **1** | **Tizim** | Asosiy sahifada 'Rentmi Maslahat beradi' bo'limi yuklanadi — algoritm ijarachining skoring bali, qidiruv tarixi va sevimli kategoriyalari asosida tavsiyalarni hisoblaydi |
| **2** | **Tizim** | Tavsiya e'lonlari katta kartochkalarda (Rentmi Maslahat beradi uslubida) gorizontal scroll ko'rinishida ko'rsatiladi |
| **3** | **Foydalanuvchi** | Tavsiya e'lon kartochkasini bosadi |
| **4** | **Tizim** | IJ-08 ga o'tiladi |
| **5** | **Foydalanuvchi** | Asosiy sahifaga qaytadi va 'Hammasi >' tugmasini bosadi |
| **6** | **Tizim** | IJ-17 sahifasi ochiladi — sarlavha: 'Rentmi Maslahat beradi'; to'liq tavsiyalar ro'yxati ko'rsatiladi |
| **7** | **Foydalanuvchi** | Ro'yxatdan e'lonni tanlaydi → IJ-08 ga o'tiladi |

## Muqobil oqimlar

| **Holat** | **Oqim** |
| --- | --- |
| **Guest foydalanuvchi** | Personallashtirilgan tavsiya yo'q — o'rniga umumiy mashhur e'lonlar (ko'p ko'rilgan, ko'p saqlangan) ko'rsatiladi; 'Rentmi Maslahat beradi' bo'limi mavjud bo'lib qoladi |
| **Ijarachi yangi (qidiruv tarixi yo'q)** | Skoring bali va kategoriya bo'yicha umumiy tavsiyalar ko'rsatiladi — qidiruv tarixi to'planguncha |
| **Tavsiya e'lon yo'q** | Bo'lim ko'rsatilmaydi yoki 'Hozircha tavsiyalar mavjud emas' placeholder ko'rsatiladi |
| **Ijarachi 'Qiziq emas' belgilagan** | 'Qiziq emas' belgilangan e'lonlar tavsiyalar ro'yxatidan ham chiqarib tashlanadi |

## Xatolik holatlari

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | Kesh tavsiyalar ko'rsatiladi; 'Internet aloqasi yo'q' banner |
| **Server xatosi** | 'Ma'lumotlarni yuklab bo'lmadi' xabari va Retry; bo'lim bo'sh ko'rsatiladi |
| **Algoritm natijasi bo'sh** | Umumiy mashhur e'lonlar fallback sifatida ko'rsatiladi |

## Biznes qoidalari

| **#** | **Qoida** |
| --- | --- |
| **BQ-1** | Tavsiyalar algoritmi ijarachining skoring bali, qidiruv tarixi va sevimli kategoriyalari kombinatsiyasi asosida ishlaydi |
| **BQ-2** | Guest uchun personallashtirilgan tavsiya yo'q — o'rniga umumiy mashhur e'lonlar ko'rsatiladi |
| **BQ-3** | 'Qiziq emas' belgilangan e'lonlar tavsiyalar ro'yxatidan ham chiqarib tashlanadi |
| **BQ-4** | Tavsiya algoritmi natijasi bo'sh bo'lganda umumiy mashhur e'lonlar fallback sifatida ko'rsatiladi |
| **BQ-5** | 'Hammasi >' bosilganda IJ-17 ochiladi — sarlavhada 'Rentmi Maslahat beradi' |
| **BQ-6** | Yangi ijarachida qidiruv tarixi yo'q bo'lganda skoring bali va kategoriya bo'yicha umumiy tavsiyalar ko'rsatiladi |
| **BQ-7** | Admin panelidan (AD-18) algoritm parametrlarini sozlash mumkin — skoring, kategoriya, narx og'irliklarini belgilash |
