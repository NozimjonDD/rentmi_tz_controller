4.2.1. Mobil ilova quyi tizimi

Mobil ilova quyi tizimi ijarachi va uy egasi uchun iOS va Android platformalarida ishlovchi taqdimot quyi tizimi bo'lib, quyidagi modullardan tashkil topadi.

Foydalanuvchilarni boshqarish moduli

Vazifasi: Foydalanuvchilarni ro'yxatdan o'tkazish, autentifikatsiya va identifikatsiya qilish, profil ma'lumotlarini yuritish, faol qurilmalar va sessiyalarni boshqarish.

Asosiy funksiyalari:

- Telefon raqami va SMS OTP orqali ro'yxatdan o'tkazish
- PIN-kod asosida mobil autentifikatsiya va PIN-kodni tiklash
- Tashqi davlat xizmati (MyID) orqali identifikatsiya
- Profil ma'lumotlarini ko'rish va tahrirlash
- Faol qurilmalarni boshqarish va telefon raqamni o'zgartirish
- Rol (ijarachi/uy egasi) tanlash va o'zgartirish

Ishtirok etuvchi foydalanish ssenariylari: U1, U2, U3, U4, U5

Asosiy talablari:

- Parollar va PIN-kodlar bir tomonlama xeshlash (bcrypt/Argon2) orqali saqlanadi
- 3 ta noto'g'ri urinishdan so'ng hisob 10 daqiqaga vaqtinchalik bloklanadi
- Barcha autentifikatsiya va profil o'zgarishlari audit jurnaliga yoziladi

Skoring moduli

Vazifasi: Ijarachining ishonchlilik darajasini (Rentmi bali, 0–100) baholash, skoring xulosalari va hisobotlarini shakllantirish.

Asosiy funksiyalari:

- Ichki va tashqi ma'lumotlar asosida Rentmi balini hisoblash
- Past/o'rtacha/yuqori ishonchlilik xulosasini shakllantirish
- Rentmi hisobotini PDF formatida taqdim etish
- Tashqi skoring/kredit byurosidan ma'lumot olish

Ishtirok etuvchi foydalanish ssenariylari: S1, S2

Asosiy talablari:

- Rentmi bali hisoblash modeli «RENTME» MChJ intellektual mulki hisoblanadi
- To'liq avtomatik skoring muhim biznes qarorlarga qo'llanilmaydi — faqat ko'maklashuvchi ma'lumot
- Tashqi skoring xizmati mavjud bo'lmasa, bal ichki ma'lumotlar asosida hisoblanadi
- Skoring hisobotini shakllantirish — ≤2 daqiqa

Billing moduli (mobil)

Vazifasi: Skoring hisobotini sotib olish, to'lovlarni amalga oshirish va foydalanuvchi uchun to'lovlar tarixini yuritish.

Asosiy funksiyalari:

- To'lov tizimi (Click/Payme/Uzum) bilan integratsiya orqali to'lov oynasini shakllantirish
- To'lov tranzaksiyasini qayd etish
- To'lovlar tarixini va tranzaksiya tafsilotlarini ko'rsatish

Ishtirok etuvchi foydalanish ssenariylari: B1 (hamda S1 doirasidagi to'lov)

Asosiy talablari:

- Pul summalari tiyin aniqligida butun sonlar sifatida saqlanadi
- To'lov muvaffaqiyatsiz bo'lsa qayta urinish imkoniyati taqdim etiladi
- Tranzaksiyalar timestamp va audit iz bilan mustahkamlanadi
- 1-bosqichda faqat skoring hisoboti xaridi; ijara va kommunal to'lovlar — keyingi bosqichlarda

E'lonlar boshqaruvi moduli

Vazifasi: Ijaraga beriladigan ko'chmas mulk obyektlari bo'yicha e'lonlarni yaratish, tahrirlash, qidirish va filtrlash.

Asosiy funksiyalari:

- Obyekt parametrlari va fotosuratlar bilan e'lon yaratish
- E'lonni tahrirlash, faol/nofaol va boshqa statuslarga olish va o'chirish
- E'lonlarni qidirish va ko'p mezonli filtrlash
- Filtrlarni saqlash va yangi e'lonlar bo'yicha bildirishnoma

Ishtirok etuvchi foydalanish ssenariylari: E1, E2, E3

Asosiy talablari:

- Har bir e'lon kamida 3 ta, ko'pi bilan 15 ta fotosuratga ega bo'lishi
- Yangi va jiddiy tahrirlangan e'lonlar moderatsiyadan o'tadi (E4)
- Obyekt joylashuvi xarita xizmati orqali koordinatalari bilan saqlanadi
- Faqat faol (moderatsiyadan o'tgan) e'lonlar katalogda ko'rsatiladi

So'rovlar boshqaruvi moduli

Vazifasi: Ijarachilar va uy egalari o'rtasidagi ijara so'rovlarini yuborish, ko'rib chiqish va holatini yuritish, chat orqali muloqotni ta'minlash.

Asosiy funksiyalari:

- Ijara so'rovini yuborish (chat imkoniyati bilan)
- Uy egasi tomonidan so'rovni tasdiqlash/rad etish/muhokama qilish
- Tasdiqlangach kontakt ma'lumotlarini ochish
- So'rovlar bo'yicha statistika va tavsiyalar

Ishtirok etuvchi foydalanish ssenariylari: R1, R2

Asosiy talablari:

- So'rov yuborish uchun ijarachida Rentmi bali bo'lishi talab etiladi
- Ayni e'lon bo'yicha takroriy so'rov taqiqlanadi
- 7 kun ko'rib chiqilmagan so'rov avtomatik belgilanadi va uy egasiga bildirishnoma yuboriladi

Bildirishnomalar moduli

Vazifasi: Push va tizim ichidagi bildirishnomalarni yuborish hamda foydalanuvchi bildirishnoma sozlamalarini yuritish.

Asosiy funksiyalari:

- Push-bildirishnoma turlarini yoqish/o'chirish
- So'rov, moderatsiya, skoring va saqlangan filtr bo'yicha bildirishnomalar
- FCM/APNs orqali push yetkazib berish

Ishtirok etuvchi foydalanish ssenariylari: N1

Asosiy talablari:

- Bildirishnomalar foydalanuvchi sozlamalariga muvofiq yuboriladi
- Push o'chirilgan bo'lsa tizim ichidagi xabar ko'rsatiladi
- Sozlamalarni saqlash — ≤2 s

Texnik qo'llab-quvvatlash moduli (mobil)

Vazifasi: Foydalanuvchilarga mobil ilova orqali murojaat (ticket) yuborish imkoniyatini taqdim etish.

Asosiy funksiyalari:

- Kategoriya bo'yicha murojaat yaratish (texnik muammo/shikoyat/taklif)
- Skrinshot yoki fayl biriktirish
- Ticket raqami va taxminiy javob muddatini ko'rsatish

Ishtirok etuvchi foydalanish ssenariylari: T1

Asosiy talablari:

- Murojaat faqat autentifikatsiyadan o'tgan foydalanuvchilar uchun (guest — Telegram orqali)
- Fayl hajmi ruxsat etilgan chegaradan oshmasligi
- Har bir murojaatga noyob ticket raqami beriladi
