> Manba: [Release 4 14.06.2026 · Admin](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29360160)

**AD-A1 — Foydalanuvchini administratsiya qilish**

| **Sseneriy nomi** | Foydalanuvchini administratsiya qilish |
| --- | --- |
| **Guruh** | Foydalanuvchi boshqaruvi |
| **Aktorlar** | Administrator |
| **Tavsif** | Administrator foydalanuvchilar ro'yxatini ko'radi, qidiradi va filtrlaydi. Har bir foydalanuvchining to'liq profilini (shaxsiy ma'lumotlar, Rentmi bali, faoliyat tarixi, audit yozuvlari, so'rovlar, chatlar) ko'rib, kerakli amalni bajaradi: bloklash/aktivatsiya, rol o'zgartirish, blacklist, PIN tiklash, profil tahrirlash. Barcha amallar audit jurnaliga yoziladi. |
| **Kirish sharti** | Administrator admin panel'ga kirgan; 'Foydalanuvchilar' bo'limini ochgan |
| **Chiqish natijasi** | Administrator foydalanuvchi profilini boshqaradi; barcha amallar audit jurnaliga yoziladi |
| **Sseneriy ID** | AD-A1 |

**Asosiy oqim**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Administrator** | 'Foydalanuvchilar' bo'limini ochadi |
| 2 | **Tizim** | Foydalanuvchilar ro'yxati: ism, telefon, rol, ro'yxatdan o'tish sanasi, holat (Faol/Bloklangan); filter va qidiruv paneli |
| 3 | **Administrator** | Qidiruv (ism, telefon) yoki filtr (rol, holat, sana) qo'llaydi |
| 4 | **Administrator** | Foydalanuvchini tanlaydi → to'liq profil sahifasi ochiladi |
| 5 | **Tizim** | Profil sahifasi (read + amallar): shaxsiy ma'lumotlar, Rentmi bali, faoliyat tarixi, audit yozuvlari, so'rovlari, chatlari |
| 6 | **Administrator** | Amalni tanlaydi va bajaradi (quyida batafsil) |
| 7 | **Tizim** | Tanlangan amal bajariladi; foydalanuvchiga bildirishnoma yuboriladi; audit jurnaliga yoziladi |

**Amallar tafsiloti**

| **Amal** | **Tavsif** |
| --- | --- |
| **Bloklash / Aktivatsiya** | Foydalanuvchi hisobi bloklanadi yoki aktivlashtiriladi; sabab kiritish majburiy; audit yozuvi |
| **Rol o'zgartirish** | Ijarachi ↔ Uy egasi roli o'zgartiriladi; foydalanuvchiga bildirishnoma |
| **Profil tahrirlash** | Faqat favqulodda holatlarda: ism, telefon; qo'shimcha tasdiqlash talab qilinadi |
| **Blacklist** | Foydalanuvchi blacklist'ga qo'shiladi — so'rov yuborish taqiqlanadi; olib tashlash ham mumkin; sabab majburiy |
| **PIN tiklash** | Foydalanuvchiga PIN tiklash SMS yuboriladi; foydalanuvchi yangi PIN o'rnatadi |
| **Web parolni tiklash (U2a)** | Admin/moderator/support uchun: vaqtinchalik parol email orqali yuboriladi; 24 soat amal qiladi |

**Muqobil oqimlar**

| **Holat** | **Oqim** |
| --- | --- |
| **Yuqori darajali amal (admin hisobini tahrirlash)** | Qo'shimcha ikki faktorli tasdiqlash talab qilinadi |
| **Bir vaqtda boshqa admin tahrirlamoqda** | Konflikt aniqlanadi → qayta yuklash taklif qilinadi |
| **Blacklist'dagi foydalanuvchining faol so'rovlari bor** | Administrator ogohlantiriladi; mavjud so'rovlar bo'yicha qaror talab qilinadi |
| **Qidiruv natijasi bo'sh** | 'Mos foydalanuvchi topilmadi' placeholder |

**Xatolik holatlari**

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q / server xatosi** | Amal amalga oshmaydi; xabar va Retry; o'zgarishlar saqlanmaydi |

**Biznes qoidalari**

| **# Qoida** |   |
| --- | --- |
| **BQ-1** | Barcha amallar audit jurnaliga: kim, qachon, nima qildi, sababi bilan yoziladi |
| **BQ-2** | Bloklash va blacklist uchun sabab kiritish majburiy |
| **BQ-3** | Profil tahrirlash faqat favqulodda holatlarda ruxsat etiladi; qo'shimcha tasdiqlash talab qilinadi |
| **BQ-4** | Yuqori darajali operatsiyalar (admin hisobini o'zgartirish) ikki faktorli tasdiqlash talab qiladi |
| **BQ-5** | Faol so'rovlari bor foydalanuvchini blacklist'ga qo'shishda ogohlantirish ko'rsatiladi |
| **BQ-6** | Rol o'zgartirilganida foydalanuvchiga push bildirishnoma yuboriladi |

**Qabul qilish mezonlari (AC)**

| **# Mezon** |   |
| --- | --- |
| **AC-1** | Foydalanuvchilar ro'yxati ≤3 s ichida yuklanadi |
| **AC-2** | Bloklash amali bajarilganda foydalanuvchi tizimga kira olmaydi |
| **AC-3** | Blacklist'ga qo'shilganda o'sha foydalanuvchi so'rov yuborish CTA'si disabled bo'ladi |
| **AC-4** | Har bir amal audit jurnalida to'g'ri yozuv bilan aks etadi |
| **AC-5** | Web parolni tiklashda vaqtinchalik parol email'ga ≤60 s ichida yuboriladi |
