> Manba: [Release 3 07.06.2026 · Mobile use cases](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/27656204)

# IJ-15 — Top e'lonlarni ko'rish

| **Sseneriy ID** | IJ-15 |
| --- | --- |
| **Sseneriy nomi** | Top e'lonlarni ko'rish |
| **Guruh** | Top va tavsiyalar |
| **Aktorlar** | Ijarachi (ro'yxatdan o'tgan), Mehmon (Guest) |
| **Tavsif** | Foydalanuvchi asosiy sahifadagi 'Kvartiralar' yoki boshqa kategoriyaga tegishli bo'limida top e'lonlarni ko'radi. Top e'lonlar ko'rishlar soni, ariza soni va saqlangan soni kombinatsiyasi asosida algoritm tomonidan belgilanadi. Ko'rsatkichlar pasayganda 'Top 👑' badge avtomatik tushiriladi. 'Hammasi >' bosilganda to'liq ro'yxat IJ-17 da ochiladi. |
| **Kirish sharti** | Foydalanuvchi asosiy sahifada (IJ-01); kamida bitta top e'lon mavjud |
| **Chiqish natijasi** | Top e'lonlar ko'rsatiladi; 'Hammasi >' bosilsa IJ-17 da to'liq top e'lonlar ro'yxati ochiladi |

## Asosiy oqim

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| **1** | **Tizim** | Asosiy sahifada 'Kvartiralar' bo'limi yuklanadi — algoritm top e'lonlarni hisoblaydi: ko'rishlar soni + ariza soni + saqlangan soni kombinatsiyasi |
| **2** | **Tizim** | Top e'lonlar gorizontal scroll kartochkalarda ko'rsatiladi; har bir top e'lon kartochkasining chap yuqori burchagida 'Top' (ko'k) badge ko'rsatiladi |
| **3** | **Foydalanuvchi** | E'lon kartochkasini bosadi |
| **4** | **Tizim** | IJ-08 ga o'tiladi — detail sahifasida ham 'Top' badge ko'rsatiladi |
| **5** | **Foydalanuvchi** | Asosiy sahifaga qaytadi va 'Hammasi >' tugmasini bosadi |
| **6** | **Tizim** | IJ-17 sahifasi ochiladi — sarlavha: 'Top e'lonlar'; faqat top e'lonlar ro'yxati ko'rsatiladi |
| **7** | **Foydalanuvchi** | Ro'yxatdan e'lonni tanlaydi → IJ-08 ga o'tiladi |

## Muqobil oqimlar

| **Holat** | **Oqim** |
| --- | --- |
| **Top e'lon ko'rsatkichlari pasayadi** | Algoritm avtomatik hisoblaydi — ko'rsatkichlar belgilangan chegaradan pastga tushganda 'Top' badge olib tashlanadi; e'lon oddiy e'lon sifatida ko'rsatiladi |
| **Top e'lon yo'q** | 'Kvartiralar' bo'limida top badge ko'rsatilmaydi; 'Hammasi >' sahifasida top bo'limi bo'sh ko'rsatiladi |
| **Guest foydalanuvchi** | Guest ham top e'lonlarni to'liq ko'ra oladi — cheklov yo'q |

## Xatolik holatlari

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | Kesh top e'lonlar ko'rsatiladi; 'Internet aloqasi yo'q' banner |
| **Server xatosi** | 'Ma'lumotlarni yuklab bo'lmadi' xabari va Retry; bo'lim bo'sh ko'rsatiladi |

## Biznes qoidalari

| **#** | **Qoida** |
| --- | --- |
| **BQ-1** | Top e'lonlar ko'rishlar soni, ariza soni va saqlangan soni kombinatsiyasi asosida algoritm tomonidan belgilanadi |
| **BQ-2** | 'Top' badge ko'rsatkichlar pasayganda avtomatik tushiriladi — admin qo'lda boshqarmaydi |
| **BQ-3** | 'Top' badge e'lon kartochkasida va IJ-08 detail sahifasida ham ko'rsatiladi |
| **BQ-4** | 'Hammasi >' bosilganda IJ-17 ochiladi — sarlavhada 'Top e'lonlar' |
| **BQ-5** | Top e'lonlar ro'yxati asosiy sahifada va alohida sahifada ham ko'rsatiladi |
| **BQ-6** | Guest va ro'yxatdan o'tgan foydalanuvchi uchun top e'lonlar bir xil ko'rsatiladi |
