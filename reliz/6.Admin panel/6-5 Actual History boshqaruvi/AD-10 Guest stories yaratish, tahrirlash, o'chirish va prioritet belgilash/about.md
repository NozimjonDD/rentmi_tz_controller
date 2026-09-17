> Manba: [Release 3 07.06.2026 · Admin use cases](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/27721770)
>
> Izoh: R5 da Actual History stories mobil ilovada ko'rsatilmaydi (kod saqlanadi) — [3-1 Asosiy sahifa](<../../../3.Mobil ilova — Ijarachi/3-1 Asosiy sahifa/about.md>).

# AD-10 — Guest stories yaratish, tahrirlash, o'chirish va prioritet belgilash

| **Sseneriy ID** | AD-10 |
| --- | --- |
| **Sseneriy nomi** | Guest stories yaratish, tahrirlash, o'chirish va prioritet belgilash |
| **Guruh** | Actual History boshqaruvi |
| **Aktorlar** | Administrator |
| **Tavsif** | Administrator ro'yxatdan o'tmagan (guest) foydalanuvchilar uchun ko'rsatiladigan Actual storieslarini boshqaradi. Story kontent turlari: skoring tanishtirish, platforma afzalliklari, onboarding. Har bir story rasm + tekst formatida bo'ladi. CTA havolasi qo'lda kiritiladi. Storieslar muddatsiz bo'lib, prioritet raqami orqali tartiblanadi. |
| **Kirish sharti** | Administrator admin panelga kirgan va Actual stories boshqaruvi bo'limini ochgan |
| **Chiqish natijasi** | Guest stories yaratiladi, tahrir qilinadi, o'chiriladi yoki prioriteti o'zgartiriladi; o'zgarishlar darhol ilovada aks etadi |

## Asosiy oqim — Story yaratish

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| **1** | **Administrator** | Actual story boshqaruvi bo'limida 'Guest stories' tabini ochadi |
| **2** | **Administrator** | 'Yangi story yaratish' tugmasini bosadi |
| **3** | **Tizim** | Story yaratish formasi ochiladi: kontent turi (dropdown), rasm yuklash, tekst maydoni, CTA matni, CTA havolasi (URL) |
| **4** | **Administrator** | Kontent turini tanlaydi: Skoring tanishtirish / Platforma afzalliklari / Onboarding |
| **5** | **Administrator** | Rasm yuklaydi (S3 ga yuklanadi); tekst kiritadi; CTA matni va havolasini qo'lda kiritadi |
| **6** | **Administrator** | 'Saqlash' tugmasini bosadi |
| **7** | **Tizim** | Story serverga saqlanadi; guest stories ro'yxatida ko'rsatiladi; holat: faol |
| **8** | **Tizim** | O'zgarishlar darhol ilovada guest foydalanuvchilarga ko'rsatiladi |

## Muqobil oqimlar

| **Holat** | **Oqim** |
| --- | --- |
| **Story tahrirlash** | Administrator mavjud storyni tanlaydi → 'Tahrirlash' → forma ochiladi; mavjud ma'lumotlar to'ldirilgan holda; o'zgartirib 'Saqlash' bosiladi → darhol kuchga kiradi |
| **Story o'chirish** | Administrator storyni tanlaydi → 'O'chirish' → tasdiqlash so'rovi → 'Ha' bosilsa story o'chiriladi; ilovada ko'rsatilmaydi |
| **Prioritet o'zgartirish** | Administrator stories ro'yxatida drag-and-drop yoki prioritet raqamini kiritib tartibni o'zgartiradi → 'Saqlash' → ilovada yangi tartibda ko'rsatiladi |
| **Preview ko'rish** | Administrator 'Preview' tugmasini bosadi — story mobile ko'rinishda simulyatsiya qilinadi |
| **CTA havolasi tekshiruvi** | Saqlashdan oldin CTA URL formati tekshiriladi — noto'g'ri format bo'lsa inline xatolik ko'rsatiladi |

## Xatolik holatlari

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Majburiy maydonlar to'ldirilmagan** | 'Ushbu maydon to'ldirilishi shart' inline xabar; 'Saqlash' disabled |
| **Rasm yuklanmadi (server xatosi)** | 'Rasmni yuklab bo'lmadi, qayta urinib ko'ring' xabari; forma ochiq qoladi |
| **Server xatosi (5xx)** | 'Xatolik yuz berdi, qayta urinib ko'ring' xabari va Retry; kiritilgan ma'lumotlar saqlanib qoladi |

## Biznes qoidalari

| **#** | **Qoida** |
| --- | --- |
| **BQ-1** | Guest stories faqat ro'yxatdan o'tmagan (guest) foydalanuvchilarga ko'rsatiladi — ro'yxatdan o'tgan ijarachilar ko'rmaydi |
| **BQ-2** | Kontent turlari: Skoring tanishtirish, Platforma afzalliklari, Onboarding — uchta kategoriyadan biri tanlanadi |
| **BQ-3** | Story formati: rasm + tekst; video qo'llab-quvvatlanmaydi |
| **BQ-4** | CTA havolasi administrator tomonidan qo'lda kiritiladi — tayyor ro'yxat yo'q |
| **BQ-5** | Stories muddatsiz — ko'rsatish boshlanish/tugash sanasi belgilanmaydi |
| **BQ-6** | Prioritet raqami orqali tartib belgilanadi — kichik raqam birinchi ko'rsatiladi |
| **BQ-7** | O'zgarishlar (yaratish, tahrirlash, prioritet) darhol ilovada aks etadi |
| **BQ-8** | O'chirilgan story qayta tiklanmaydi — arxivga ham saqlanmaydi |
