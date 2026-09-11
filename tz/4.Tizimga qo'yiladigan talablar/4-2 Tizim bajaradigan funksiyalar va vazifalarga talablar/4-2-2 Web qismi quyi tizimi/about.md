4.2.2. Web qismi quyi tizimi

Web qismi quyi tizimi administrator, moderator, texnik qo'llab-quvvatlash xodimi va call-markaz operatori uchun veb-interfeys orqali boshqaruv va nazorat funksiyalarini ta'minlaydi va quyidagi modullardan tashkil topadi.

Autentifikatsiya moduli

Vazifasi: Web qismi quyi tizimi foydalanuvchilari (administrator, moderator, support, call-markaz) uchun username/parol asosida kirish va parolni tiklashni ta'minlash.

Asosiy funksiyalari:

- Username va parol orqali web kirish (JWT)
- Superadmin tomonidan parolni tiklash (vaqtinchalik parol)
- Sessiya va kirish urinishlarini nazorat qilish

Ishtirok etuvchi foydalanish ssenariylari: U2-veb, U2a

Asosiy talablari:

- Admin hisoblari faqat superadmin tomonidan yaratiladi
- 3 ta noto'g'ri urinishdan so'ng 10 daqiqaga blok
- Vaqtinchalik parol amal muddati — 24 soat
- Barcha kirish va tiklash harakatlari audit jurnaliga yoziladi

Moderatsiya moduli

Vazifasi: E'lonlarni tekshirish va tasdiqlash, soxta e'lonlarni bloklash hamda e'lon kataloglari (klassifikatorlar)ni boshqarish.

Asosiy funksiyalari:

- E'lonni tasdiqlash/rad etish/tuzatish talabi
- Soxta yoki qonunga zid e'lonlarni bloklash
- E'lon kataloglarini (obyekt turlari, hududlar, foydalanish shartlari) boshqarish

Ishtirok etuvchi foydalanish ssenariylari: E4, E5

Asosiy talablari:

- Bir e'lonni ko'rib chiqishning maksimal navbat muddati — 24 soat
- Rad etish va tuzatish talabida sabab/izoh majburiy
- Barcha moderatsiya qarorlari audit jurnaliga yoziladi
- Soxta e'lon ulushi 5% dan oshmasligi nazorat qilinadi

Administratorlik moduli

Vazifasi: Foydalanuvchilarni administratsiya qilish, ruxsatlarni boshqarish (RBAC), tizim sozlamalari va tizim hisobotlarini shakllantirish.

Asosiy funksiyalari:

- Foydalanuvchilarni bloklash/aktivatsiya, rol o'zgartirish, blacklist boshqaruvi
- RBAC doirasida ruxsatlarni boshqarish va tizim sozlamalari
- Tizim hisobotlari va analitikani shakllantirish (PDF/CSV)
- Tashqi integratsiyalar holatini monitoring qilish (hisobot doirasida)

Ishtirok etuvchi foydalanish ssenariylari: A1, A2

Asosiy talablari:

- Barcha administrator harakatlari sabab bilan audit jurnaliga yoziladi
- Yuqori darajadagi operatsiyalar ikki faktorli tasdiqlashni talab etadi
- Kritik operatsiyalar qo'shimcha tasdiqlash mexanizmlari bilan himoyalanadi

Billing nazorati moduli

Vazifasi: To'lov tranzaksiyalarini nazorat qilish va billing hisobotlarini shakllantirish.

Asosiy funksiyalari:

- Barcha tranzaksiyalarni ko'rish va filtrlash
- Kunlik/oylik tushum hisoboti

Ishtirok etuvchi foydalanish ssenariylari: A4

Asosiy talablari:

- Pul summalari tiyin aniqligida saqlanadi
- Barcha nazorat harakatlari audit jurnaliga yoziladi

Integratsiya boshqaruvi moduli

Vazifasi: Tashqi axborot tizimlari bilan ulanishlarni sozlash, holatini monitoring qilish va sinovdan o'tkazish.

Asosiy funksiyalari:

- Ulangan tashqi xizmatlar ro'yxati va real vaqtdagi holati
- Integratsiya parametrlarini (endpoint, kalit, timeout, retry) sozlash
- Sinov so'rovi orqali integratsiyani tekshirish
- Integratsiyani vaqtincha yoqish/o'chirish

Ishtirok etuvchi foydalanish ssenariylari: A3

Asosiy talablari:

- Integratsiya kalitlari shifrlangan holda saqlanadi
- Barcha tashqi so'rovlar tizim log jurnalida qayd etiladi
- Qayta urinish (retry) va circuit breaker mexanizmlari qo'llaniladi
- O'zgarishlar audit jurnaliga yoziladi

Texnik qo'llab-quvvatlash moduli (admin)

Vazifasi: Foydalanuvchi murojaatlarini ko'rib chiqish, javob berish, eskalatsiya qilish hamda call-markaz orqali ticket yaratish.

Asosiy funksiyalari:

- Murojaatlarni ko'rib chiqish va holatini boshqarish
- Javob berish, ichki izoh va eskalatsiya
- Call-markaz operatori tomonidan ticket yaratish
- Foydalanuvchiga bildirishnoma yuborish

Ishtirok etuvchi foydalanish ssenariylari: T2, T3

Asosiy talablari:

- Murojaatga javob maksimal muddati — 24 soat (ish kuni ichida)
- 24 soat hal etilmagan ticket avtomatik eskalatsiya qilinadi
- Call-markaz operatori faqat ko'rish huquqiga ega
- Barcha harakatlar audit jurnaliga yoziladi
