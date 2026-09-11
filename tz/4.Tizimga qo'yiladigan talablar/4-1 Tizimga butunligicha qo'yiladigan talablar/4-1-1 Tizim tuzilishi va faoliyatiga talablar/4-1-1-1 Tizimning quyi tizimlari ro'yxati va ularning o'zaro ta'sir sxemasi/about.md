4.1.1.1. Tizimning quyi tizimlari ro'yxati va ularning o'zaro ta'sir sxemasi

"Rentmi" AT ikki pog'onali quyi tizimlar tuzilmasiga ega. Yuqori darajada ikkita platforma quyi tizimi — Mobil ilova va Web qismi quyi tizimi — belgilanadi; ularning har biri funksional modullardan tashkil topadi. Quyi tizimlar va modullar quyidagi jadvalda keltirilgan:

| Quyi tizim / modul | Asosiy vazifalari |
| --- | --- |
| MOBIL ILOVA QUYI TIZIMI | Ijarachi va uy egasi uchun mobil ilova (iOS/Android); platforma funksiyalariga kirishni ta'minlovchi taqdimot quyi tizimi. |
| Foydalanuvchilarni boshqarish moduli | Ro'yxatdan o'tkazish, autentifikatsiya, identifikatsiya, profil, faol qurilmalar |
| Skoring moduli | Rentmi balini baholash, skoring xulosalari va hisobotlarini shakllantirish |
| Billing moduli (mobil) | Hisobot xaridi, to'lov, to'lovlar tarixi |
| E'lonlar boshqaruvi moduli | E'lonlarni yaratish, tahrirlash, qidirish, filtrlash |
| So'rovlar boshqaruvi moduli | Ijara so'rovlarini yuborish, ko'rib chiqish, chat, holatini yuritish |
| Bildirishnomalar moduli | Push bildirishnomalar va sozlamalarini boshqarish |
| Texnik qo'llab-quvvatlash moduli (mobil) | Foydalanuvchi murojaatlarini (ticket) yuborish |
| WEB QISMI QUYI TIZIMI | Administrator, moderator, support va call-markaz uchun veb-interfeys; boshqaruv va nazorat quyi tizimi. |
| Autentifikatsiya moduli | Username/parol orqali web kirish, parolni tiklash |
| Moderatsiya moduli | E'lonlarni tekshirish/tasdiqlash, kataloglarni boshqarish, soxta e'lonlarni bloklash |
| Administratorlik moduli | Foydalanuvchilar, RBAC, tizim sozlamalari, hisobotlar |
| Billing nazorati moduli | To'lovlarni nazorat qilish, reconciliation, billing hisobotlari |
| Integratsiya boshqaruvi moduli | Tashqi integratsiyalarni sozlash, monitoring, sinov |
| Texnik qo'llab-quvvatlash moduli (admin) | Murojaatlarni ko'rib chiqish, eskalatsiya, call-markaz ticket |

Quyi tizimlarning o'zaro ta'siri markazlashgan arxitektura tamoyili bo'yicha tashkil etiladi: integratsiya boshqaruvi moduli barcha ichki va tashqi aloqalarni ta'minlovchi asosiy kommunikatsiya qatlami vazifasini bajaradi.

Ijara shartnomalari, Ijara to'lovlari, Kommunal to'lovlar hamda Xizmatlarni boshqarish modullari keyingi loyiha bosqichlarida (2–3-bosqich) alohida texnik topshiriqlar asosida joriy etiladi va mazkur TT doirasiga kirmaydi.
