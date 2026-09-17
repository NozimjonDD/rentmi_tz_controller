> Manba: [Release 3 07.06.2026 · Admin use cases](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/27721770)
>
> Izoh: R5 da Actual History stories mobil ilovada ko'rsatilmaydi (kod saqlanadi) — [3-1 Asosiy sahifa](<../../../3.Mobil ilova — Ijarachi/3-1 Asosiy sahifa/about.md>).

# AD-11 — User stories yaratish, tahrirlash, o'chirish va prioritet belgilash

| **Sseneriy ID** | AD-11 |
| --- | --- |
| **Sseneriy nomi** | User stories yaratish, tahrirlash, o'chirish va prioritet belgilash |
| **Guruh** | Actual History boshqaruvi |
| **Aktorlar** | Administrator |
| **Tavsif** | Administrator ro'yxatdan o'tgan ijarachilar uchun ko'rsatiladigan Actual storieslarini boshqaradi. Kontent personallashtirilgan: skoring maslahat, ijara tarixi, xizmatlar tanishtirish, Rentmi yangiliklari. Interface va yaratish jarayoni guest stories bilan bir xil. Storieslar muddatsiz, prioritet raqami orqali tartiblanadi. |
| **Kirish sharti** | Administrator admin panelga kirgan va Actual story boshqaruvi bo'limini ochgan |
| **Chiqish natijasi** | User stories yaratiladi, tahrir qilinadi, o'chiriladi yoki prioriteti o'zgartiriladi; o'zgarishlar darhol ro'yxatdan o'tgan ijarachilar ilovasida aks etadi va notification ko’rinishida xam qabul qilinadi |

## Asosiy oqim — Story yaratish

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| **1** | **Administrator** | Actual story boshqaruvi bo'limida 'User stories' tabini ochadi |
| **2** | **Administrator** | 'Yangi story yaratish' tugmasini bosadi |
| **3** | **Tizim** | Story yaratish formasi ochiladi: kontent turi (dropdown), rasm yuklash, tekst maydoni, CTA matni, CTA havolasi (URL) |
| **4** | **Administrator** | Kontent turini tanlaydi: Skoring maslahat / Ijara tarixi / Xizmatlar / Rentmi yangiligi |
| **5** | **Administrator** | Rasm yuklaydi; tekst kiritadi; CTA matni va havolasini qo'lda kiritadi |
| **6** | **Administrator** | 'Saqlash' tugmasini bosadi |
| **7** | **Tizim** | Story serverga saqlanadi; user stories ro'yxatida ko'rsatiladi; holat: faol |
| **8** | **Tizim** | O'zgarishlar darhol ro'yxatdan o'tgan ijarachilar ilovasida aks etadi |

## Muqobil oqimlar

| **Holat** | **Oqim** |
| --- | --- |
| **Story tahrirlash** | Mavjud storyni tanlaydi → 'Tahrirlash' → forma ochiladi; mavjud ma'lumotlar to'ldirilgan; o'zgartirib 'Saqlash' → darhol kuchga kiradi |
| **Story o'chirish** | Storyni tanlaydi → 'O'chirish' → tasdiqlash so'rovi → 'Ha' → story o'chiriladi; arxivlanmaydi |
| **Prioritet o'zgartirish** | Drag-and-drop yoki prioritet raqami orqali tartib o'zgartiriladi → 'Saqlash' → ilovada yangi tartibda |
| **Preview ko'rish** | 'Preview' tugmasi → story mobile ko'rinishda simulyatsiya qilinadi |

## Xatolik holatlari

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Majburiy maydonlar to'ldirilmagan** | Inline xabar; 'Saqlash' disabled |
| **Rasm yuklanmadi** | 'Rasmni yuklab bo'lmadi' xabari; forma ochiq |
| **Server xatosi** | Xabar va Retry; kiritilgan ma'lumotlar saqlanib qoladi |

## Biznes qoidalari

| **#** | **Qoida** |
| --- | --- |
| **BQ-1** | User stories faqat ro'yxatdan o'tgan ijarachilar uchun — guest foydalanuvchilar ko'rmaydi |
| **BQ-2** | Kontent turlari: Skoring maslahat, Ijara tarixi, Xizmatlar, Rentmi yangiligi — aniq belgilangan kategoriyalar yo'q, administrator erkin tanlaydi |
| **BQ-3** | Story formati: rasm + tekst; video qo'llab-quvvatlanmaydi |
| **BQ-4** | CTA havolasi qo'lda kiritiladi |
| **BQ-5** | Stories muddatsiz — ko'rsatish muddati belgilanmaydi |
| **BQ-6** | Prioritet raqami orqali tartib — kichik raqam birinchi; mobil ilovada backend dinamik tartibni qayta hisoblaydi (ijarachi holati asosida) |
| **BQ-7** | O'zgarishlar darhol ilovada aks etadi va notification ko’rinishida xabarlanadi |
| **BQ-8** | AD-10 (guest) va AD-11 (user) stories yaratish interfeysi bir xil — faqat kontent turi va maqsad auditoriyasi farqli |
