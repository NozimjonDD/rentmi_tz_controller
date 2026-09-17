4.1.1.4. Foydalanish ssenariylari ro'yxati va batafsil tavsifi

Tizimning foydalanish ssenariylari quyi tizimlar va modullar bo'yicha guruhlangan holda taqdim etiladi. Avval umumiy ro'yxat jadvali, so'ngra har bir ssenariyning batafsil tavsifi keltiriladi. Jami 25 ta foydalanish ssenariysi belgilangan (15 ta — Mobil ilovada, 10 ta — Web qismi quyi tizimida).

Foydalanish ssenariylarining umumiy ro'yxati

| ID | Foydalanish ssenariysi nomi | Ishtirokchilar | Turi | Modul |
| --- | --- | --- | --- | --- |
| Mobil ilova quyi tizimi |  |  |  |  |
| U1 | Foydalanuvchini ro'yxatdan o'tkazish | Ro'yxatdan o'tmagan foydalanuvchi (Guest) | Asosiy | Foydalanuvchilarni boshqarish |
| U2 | Tizimga kirish (mobil ilova, PIN) | Ijarachi, uy egasi | Asosiy | Foydalanuvchilarni boshqarish |
| U3 | PIN-kodni tiklash | Ro'yxatdan o'tgan foydalanuvchi | Kengaytma (U2 ga nisbatan) | Foydalanuvchilarni boshqarish |
| U4 | Foydalanuvchi profilini boshqarish | Ijarachi, uy egasi | Asosiy | Foydalanuvchilarni boshqarish |
| U5 | Foydalanuvchini identifikatsiya qilish | Tashqi davlat identifikatsiya xizmati (MyID yoki shunga o'xshash) | Qo'shilish (U1 tarkibida) | Foydalanuvchilarni boshqarish |
| S1 | Rentmi hisobotini xarid qilish | Ijarachi | Asosiy | Skoring |
| S2 | Skoring ma'lumotlarini tashqi manbadan olish | Tashqi skoring/kredit byurosi xizmati | Qo'shilish (S1 tarkibida) | Skoring |
| B1 | To'lovlar tarixini ko'rish | Ijarachi, uy egasi | Asosiy | Billing |
| E1 | E'lon yaratish | Uy egasi | Asosiy | E'lonlar boshqaruvi |
| E2 | E'lonni tahrirlash yoki o'chirish | Uy egasi | Kengaytma (E1 ga nisbatan) | E'lonlar boshqaruvi |
| E3 | E'lonlarni qidirish va filtrlash | Ijarachi, ro'yxatdan o'tmagan foydalanuvchi (guest) | Asosiy | E'lonlar boshqaruvi |
| R1 | Ijara so'rovini yuborish | Ijarachi | Asosiy | So'rovlar boshqaruvi |
| R2 | Ijara so'rovini ko'rib chiqish | Uy egasi | Asosiy | So'rovlar boshqaruvi |
| N1 | Push-bildirishnoma sozlamalarini boshqarish | Ijarachi, uy egasi | Asosiy | Bildirishnomalar |
| T1 | Murojaat yuborish | Ijarachi, uy egasi | Asosiy | Texnik qo'llab-quvvatlash |
| Web qismi quyi tizimi |  |  |  |  |
| U2-veb | Tizimga kirish (web qismi quyi tizimi, parol) | Administrator, moderator, qo'llab-quvvatlash xodimi, call-markaz operatori | Asosiy | Autentifikatsiya |
| U2a | Web parolni tiklash | Administrator (superadmin roliga ega) | Kengaytma (U2-veb ga nisbatan) | Autentifikatsiya |
| E4 | E'lonni moderatsiya qilish | Moderator | Asosiy | Moderatsiya |
| E5 | E'lon kataloglarini boshqarish | Moderator | Asosiy | Moderatsiya |
| A1 | Foydalanuvchini administratsiya qilish | Administrator | Asosiy | Administratorlik |
| A2 | Tizim hisobotlarini shakllantirish | Administrator, texnik qo'llab-quvvatlash xodimi | Asosiy | Administratorlik |
| A4 | To'lovlarni nazorat qilish | Administrator | Asosiy | Billing nazorati |
| A3 | Tashqi integratsiyalarni boshqarish | Administrator | Asosiy | Integratsiya boshqaruvi |
| T2 | Murojaatlarnini ko'rib chiqish | Texnik qo'llab-quvvatlash xodimi | Asosiy | Texnik qo'llab-quvvatlash |
| T3 | Murojaatlarnini qabul qilish va ticket yaratish | Call-markaz operatori | Asosiy | Texnik qo'llab-quvvatlash |

Mobil ilova quyi tizimi

Foydalanuvchilarni boshqarish moduli

| U1 — Foydalanuvchini ro'yxatdan o'tkazish |  |
| --- | --- |
| Aktyor | Ro'yxatdan o'tmagan foydalanuvchi (Guest) |
| Turi | Asosiy |
| Ishga tushirish shartlari | Foydalanuvchi tizimda oldin ro'yxatdan o'tmagan; faol mobil telefon raqamiga ega; ilova qurilmada o'rnatilgan; foydalanuvchi ijarachi asosiy sahifasiga (main page) kirgan yoki birinchi marotaba ilovani ishga tushirmoqda. |
| Bajarish tartibi | 1) Foydalanuvchi 'Ro'yxatdan o'tish' funksiyasini tanlaydi; 2) Telefon raqamini kiritadi; 3) Tizim raqam formatini va unikalligini tekshiradi; 4) SMS orqali OTP yuboriladi; 5) Foydalanuvchi OTP kiritadi, tizim tekshiradi; 6) Foydalanuvchi Maxfiylik siyosati va Foydalanish shartlari bilan tanishib, shaxsiy ma'lumotlarni qayta ishlashga roziligini tasdiqlaydi — skoring xizmatidan foydalanish uchun talab etiladi; 7) Foydalanuvchi PIN-kod o'rnatadi; 8) Tizim profilni saqlaydi va asosiy oynaga yo'naltiradi; 9) Tizim identifikatsiyadan o'tishni taklif qiladi (U5) — bu qadam IXTIYORIY: foydalanuvchi darhol o'tishi yoki 'Keyinroq' deb o'tkazib yuborishi mumkin; ro'yxatdan o'tmagan (guest) yoki identifikatsiyasiz foydalanuvchi e'lonlarni ko'rish va filtrlash (E3) imkoniyatiga ega, lekin ijarachilarga ijara so'rovini yuborishlari (R1) uchun identifikatsiya va skoring xulosasiga ega bo'lish talab etiladi. |
| Vaqt reglamenti | OTP yuborish — ≤30 s; OTP amal muddati — 5 daqiqa; umumiy davomiyligi (foydalanuvchi kiritish vaqtisiz) — ≤90 s. |
| Kiruvchi ma'lumotlar | Telefon raqami (E.164), OTP kodi, U5 talab qilgan identifikatsiya ma'lumotlari, PIN-kod, rol. |
| Chiquvchi ma'lumotlar | Yangi foydalanuvchi profili, autentifikatsiya tokeni, tasdiq xabari. |
| Kengaytmalar | Raqam mavjud → U2 ga yo'naltirish; noto'g'ri OTP (3 urinish, so'ng 10 daq. blok); identifikatsiya (U5) keyinroq o'tkazish tanlansa → foydalanuvchi cheklangan rejimda ishlaydi (E3 ruxsat, R1 taqiqlangan); tashqi xizmat (MyID) vaqtincha ishlamasa → 'Keyinroq' rejim taklif qilinadi. |
| Qo'shilgan ssenariylar | U5 |
| Faoliyat diagrammasi | 4.1.1.4-rasm (U1) |

| U2 — Tizimga kirish (mobil ilova, PIN) |  |
| --- | --- |
| Aktyor | Ijarachi, uy egasi |
| Turi | Asosiy |
| Ishga tushirish shartlari | Foydalanuvchi ilgari ro'yxatdan o'tgan; PIN-kod o'rnatilgan; hisob faol holatda; kirish mobil ilova orqali amalga oshiriladi. |
| Bajarish tartibi | 1) Foydalanuvchi 'Tizimga kirish'ni tanlaydi; 2) Telefon raqamini kiritadi; 3) Tizim raqam va hisob holatini tekshiradi; 4) PIN-kodni kiritadi; 5) Tizim PIN-ni saqlangan xesh bilan taqqoslaydi; 6) Noto'g'ri PIN kiritilsa — urinishlar hisoblagichi oshadi (3 ta noto'g'ri urinishdan so'ng hisob 10 daqiqaga bloklanadi); 7) To'g'ri PIN bo'lsa — sessiya va autentifikatsiya tokeni yaratiladi; 8) Audit jurnaliga yozuv kiritiladi; 9) Foydalanuvchi roliga mos asosiy oynaga yo'naltiriladi. |
| Vaqt reglamenti | Umumiy davomiyligi — ≤5 s; PIN-kodni tekshirish — ≤2 s. |
| Kiruvchi ma'lumotlar | Telefon raqami, PIN-kod. |
| Chiquvchi ma'lumotlar | Foydalanuvchi sessiyasi, autentifikatsiya tokeni, rolga mos asosiy oyna. |
| Kengaytmalar | Raqam topilmadi → U1 ga yo'naltirish; noto'g'ri PIN (3 urinish → 10 daq. blok) → blok davomida U3 orqali PIN tiklash taklif qilinadi; hisob bloklangan (admin tomonidan) → qo'llab-quvvatlashga murojaat. |
| Faoliyat diagrammasi | 4.1.1.4-rasm (U2) |

| U3 — PIN-kodni tiklash |  |
| --- | --- |
| Aktyor | Ro'yxatdan o'tgan foydalanuvchi |
| Turi | Kengaytma (U2 ga nisbatan) |
| Ishga tushirish shartlari | Foydalanuvchi PIN-kodini unutgan yoki hisobi vaqtincha bloklangan; telefon raqami faol. |
| Bajarish tartibi | 1) 'PIN-kodni unutdim' funksiyasini tanlaydi; 2) Telefon raqamini kiritadi; 3) Tizim raqamning mavjudligini tekshiradi; 4) SMS orqali OTP yuboriladi; 5) Foydalanuvchi OTP kiritadi, tizim tekshiradi; 6) Yangi PIN-kod ikki marta kiritiladi; 7) Tizim yangi PIN-ni xeshlab saqlaydi, eski PIN bekor qilinadi; 8) Audit jurnaliga yozuv kiritiladi, bildirishnoma yuboriladi; 9) Foydalanuvchi avtomatik kirgiziladi. |
| Vaqt reglamenti | OTP yuborish — ≤30 s; OTP amal muddati — 5 daqiqa; umumiy davomiyligi — ≤60 s. |
| Kiruvchi ma'lumotlar | Telefon raqami, OTP kodi, yangi PIN-kod. |
| Chiquvchi ma'lumotlar | Yangilangan PIN-kod, bildirishnoma, foydalanuvchi sessiyasi. |
| Kengaytmalar | Noto'g'ri OTP (3 urinish → 10 daq. blok, ssenariy bekor qilinadi; blok tugagach qayta urinish mumkin); yangi PIN eski bilan bir xil → boshqa PIN kiritish so'raladi. |
| Faoliyat diagrammasi | 4.1.1.4-rasm (U3) |

| U4 — Foydalanuvchi profilini boshqarish |  |
| --- | --- |
| Aktyor | Ijarachi, uy egasi |
| Turi | Asosiy |
| Ishga tushirish shartlari | Foydalanuvchi tizimga muvaffaqiyatli kirgan; ijarachi yoki uy egasi roliga ega. |
| Bajarish tartibi | 1) 'Mening profilim' bo'limini tanlaydi; 2) Tizim joriy ma'lumotlarni (shaxsiy, aloqa, Rentmi bali, hisobotlar) ko'rsatadi; 3) Foydalanuvchi harakatni tanlaydi: shaxsiy ma'lumotlarni tahrirlash / Rentmi bali tafsilotini ko'rish / hisobot xarid qilish — faqat ijarachi uchun (S1) / xarid qilingan hisobotni PDF formatida yuklab olish — faqat ijarachi uchun / faol qurilmalarni ko'rish va boshqarish / telefon raqamni o'zgartirish; 4) Faol qurilmalarni boshqarishda: barcha faol sessiyalar ro'yxati ko'rsatiladi, kerakmas qurilmadan chiqish imkoniyati mavjud; 5) Telefon raqamni o'zgartirishda: yangi raqam kiritiladi — SMS OTP yuboriladi — OTP tasdiqlanadi — raqam yangilanadi; 6) Foydalanuvchi o'zgarishlarni saqlaydi; 7) Tizim validatsiya o'tkazadi va ma'lumotlarni bazaga saqlaydi; 8) Audit jurnaliga yozuv kiritiladi. |
| Vaqt reglamenti | Profil yuklash — ≤3 s; o'zgarishlarni saqlash — ≤3 s; OTP yuborish (tel. raqam o'zgartirish) — ≤30 s; OTP amal muddati — 5 daqiqa. |
| Kiruvchi ma'lumotlar | Yangilangan shaxsiy va aloqa ma'lumotlari, tanlangan harakat turi, yangi telefon raqami (o'zgartirish holatida), OTP kodi (o'zgartirish holatida). |
| Chiquvchi ma'lumotlar | Yangilangan profil, Rentmi bali va xulosasi, xarid qilingan hisobotlar ro'yxati (faqat ijarachi), faol qurilmalar ro'yxati, yangilangan telefon raqami. |
| Kengaytmalar | Validatsiya xatoligi → aniq xabar ko'rsatish; hisobot xarid qilish (faqat ijarachi) → S1 ga yo'naltirish; noto'g'ri OTP (3 urinish, telefon o'zgartirish) → jarayon bekor qilinadi. |
| Faoliyat diagrammasi | 4.1.1.4-rasm (U4) |

| U5 — Foydalanuvchini identifikatsiya qilish |  |
| --- | --- |
| Aktyor | Tashqi davlat identifikatsiya xizmati (MyID yoki shunga o'xshash) |
| Turi | Qo'shilish (U1 tarkibida) |
| Ishga tushirish shartlari | Foydalanuvchi telefon raqamini muvaffaqiyatli tasdiqlagan; tashqi xizmat ulanishga tayyor. |
| Bajarish tartibi | 1) Tizim tashqi xizmat bilan integratsiyani ishga tushiradi; 2) Foydalanuvchi tashqi xizmat interfeysiga yo'naltiriladi (OAuth 2.0); 3) Foydalanuvchi shaxsini tasdiqlash jarayonidan o'tadi; 4) Tashqi xizmat foydalanuvchi ma'lumotlarini (ism, JShShIR, pasport, tug'ilgan sana) qaytaradi; 5) Tizim ma'lumotlar to'g'riligi va to'liqligini tekshiradi; 6) Foydalanuvchi profili identifikatsiyadan o'tgan deb belgilanadi; 7) Audit jurnaliga yozuv kiritiladi; 8) U1 ga qaytiladi; 9) Agar foydalanuvchi uy egasi rolida ro'yxatdan o'tsa unga tegishli ko'chmas mulklari ro'yxatini yuklab berish taklifi beriladi, qabul qilsa ro'yxat shakllantiriladi va uy egasining asosiy sahifasiga yo'naltiriladi; 10) Agar foydalanuvchi ijarachi bo'lsa unga skoringdan o'tish taklif beriladi (ixtiyoriy), xohlasa ijarachi asosiy sahifasiga o'tib ketadi. |
| Vaqt reglamenti | Tashqi xizmatga so'rov — ≤5 s; umumiy davomiyligi (foydalanuvchi kirish vaqtisiz) — ≤60 s. |
| Kiruvchi ma'lumotlar | Telefon raqami, tashqi xizmat talab qilgan identifikatsiya ma'lumotlari. |
| Chiquvchi ma'lumotlar | Tasdiqlangan shaxsiy ma'lumotlar, identifikatsiya holati, noyob identifikator. |
| Kengaytmalar | Tashqi xizmat mavjud emas → foydalanuvchiga xabar, identifikatsiya keyinroq taklif qilinadi; identifikatsiya muvaffaqiyatsiz (farqli ma'lumotlar) → qo'llab-quvvatlashga murojaat; shaxs bazada mavjud bo'lsa → mavjud hisob haqida xabar va kirish (U2) taklif qilinadi (yangi hisob yaratilmaydi). |
| Faoliyat diagrammasi | 4.1.1.4-rasm (U5) |

Skoring moduli

| S1 — Rentmi hisobotini xarid qilish |  |
| --- | --- |
| Aktyor | Ijarachi |
| Turi | Asosiy |
| Ishga tushirish shartlari | Foydalanuvchi identifikatsiyadan o'tgan va tizimga kirgan; Rentmi hisobotini xarid qilishni tanlagan. |
| Bajarish tartibi | 1) Foydalanuvchi profil yoki ijarachi ma'lumotlari oynasida 'Rentmi hisobotini xarid qilish'ni tanlaydi; 2) Tizim mavjud hisobot ma'lumotlarini va narxlarini ko'rsatadi; 3) Foydalanuvchi hisobotni xarid qilishni tanlaydi; 4) Tizim to'lov tizimi bilan integratsiya orqali to'lov oynasini shakllantiradi; 5) Foydalanuvchi to'lovni amalga oshiradi; 6) Tizim foydalanuvchi bo'yicha ichki ma'lumotlarni yig'adi (shaxsiy, ijara tarixi, to'lovlar tarixi, tizim faoliyati); 7) Tashqi manbalardan foydalanuvchining ma'lumotlari (kredit tarixi, soliq qarzdorligi, ish joyi) olinadi (S2); 8) Tizim skoring algoritmi asosida Rentmi skoring balini (0–100) hisoblaydi; 9) Bal asosida umumiy xulosa shakllantiriladi (past/o'rtacha/yuqori ishonchlilik); 10) Natija foydalanuvchi profiliga saqlanadi; 11) Tizim hisobotni ko'rish ekraniga yo'naltiradi; 12) Hisobot 'Xarid qilingan hisobotlar' bo'limiga saqlanadi; foydalanuvchi skoring balini ijarachi asosiy sahifasi va profili orqali ko'rishi mumkin; 13) Bildirishnoma yuboriladi; 14) PDF formatida yuklab olish imkoniyati ochiladi; 15) Oilaviy holat, farzandlar va daromad to'g'risida ma'lumot yuklash hamda tavsiyanoma qo'shish funksionali ochiladi. |
| Vaqt reglamenti | To'lov oynasini shakllantirish — ≤5 s; to'lov tasdig'i — ≤15 s; hisobotni shakllantirish — ≤2 daqiqa. |
| Kiruvchi ma'lumotlar | Hisobot olinadigan foydalanuvchi identifikatori, hisobot ma'lumotlari, to'lov ma'lumotlari. |
| Chiquvchi ma'lumotlar | PDF hisobot, xarid tranzaksiyasi yozuvi. |
| Kengaytmalar | To'lov muvaffaqiyatsiz → xatolik va qayta urinish; tashqi to'lov tizimi mavjud emas → keyinroq urinish taklifi; ball qayta hisoblanayotgan bo'lsa → foydalanuvchi ogohlantiriladi. |
| Faoliyat diagrammasi | 4.1.1.4-rasm (S1) |

| S2 — Skoring ma'lumotlarini tashqi manbadan olish |  |
| --- | --- |
| Aktyor | Tashqi skoring/kredit byurosi xizmati |
| Turi | Qo'shilish (S1 tarkibida) |
| Ishga tushirish shartlari | Foydalanuvchi identifikatsiyadan o'tgan; tashqi skoring xizmati ulanishga tayyor; foydalanuvchi shaxsiy ma'lumotlarni qayta ishlashga rozilik bergan. |
| Bajarish tartibi | 1) Tizim tashqi skoring xizmatiga autentifikatsiyalangan so'rov jo'natadi (foydalanuvchi identifikatori va zarur ma'lumotlar); 2) So'rov jurnaliga yozuv kiritiladi; 3) Tashqi xizmat javob qaytaradi (kredit reytingi, tarix, soliq qarzdorligi va boshqa ko'rsatkichlar); 4) Tizim olingan ma'lumotlar formatini va to'liqligini tekshiradi; 5) Ma'lumotlar S1 ga uzatiladi; 6) Javob jurnaliga yozuv kiritiladi. |
| Vaqt reglamenti | So'rov yuborish — ≤2 s; javob kutish — ≤8 s; umumiy davomiyligi — ≤10 s. |
| Kiruvchi ma'lumotlar | Foydalanuvchi identifikatori, JShShIR, zarur shaxsiy ma'lumotlar. |
| Chiquvchi ma'lumotlar | Kredit reytingi, moliyaviy tarix ko'rsatkichlari, so'rov holati, javob timestamp. |
| Kengaytmalar | Tashqi xizmat mavjud emas → 'ma'lumot olinmadi' holati, S1 faqat ichki ma'lumotlar asosida davom etadi; javob vaqti oshib ketishi → timeout bo'yicha uzish; noto'g'ri/to'liq bo'lmagan javob → xato jurnaliga yozuv, 'ma'lumot olinmadi' qaytariladi. |
| Faoliyat diagrammasi | 4.1.1.4-rasm (S2) |

Billing moduli (mobil)

| B1 — To'lovlar tarixini ko'rish |  |
| --- | --- |
| Aktyor | Ijarachi, uy egasi |
| Turi | Asosiy |
| Ishga tushirish shartlari | Foydalanuvchi tizimga kirgan; kamida bitta skoring xisobobitni sotib olish bo'yicha to'lov tranzaksiyasi mavjud. 1-bosqichda faqat skoring hisoboti xaridi tranzaksiyalari ko'rsatiladi; keyingi bosqichlarda ijara to'lovlari (3-bosqich), xizmatlar va kommunal to'lovlar (2-bosqich) ham ushbu bo'limda aks ettiriladi. |
| Bajarish tartibi | 1) Foydalanuvchi 'Mening hisobotlarim' yoki profil bo'limida 'To'lovlar tarixi'ni tanlaydi; 2) Tizim barcha tranzaksiyalar ro'yxatini ko'rsatadi (sana, tur, summa, holat); 3) Foydalanuvchi tranzaksiyani tanlaydi va batafsil ma'lumotlarni ko'radi; 4) Ixtiyoriy: saqlangan hisobotni qayta ko'rish mumkin. |
| Vaqt reglamenti | To'lovlar ro'yxatini yuklash — ≤3 s. |
| Kiruvchi ma'lumotlar | Foydalanuvchi identifikatori, filtr parametrlari (sana oralig'i, tur — ixtiyoriy). |
| Chiquvchi ma'lumotlar | To'lovlar tarixi ro'yxati, tranzaksiya tafsilotlari. |
| Kengaytmalar | To'lovlar tarixi bo'sh → 'Hali to'lovlar amalga oshirilmagan' xabari. |
| Faoliyat diagrammasi | 4.1.1.4-rasm (B1) |

E'lonlar boshqaruvi moduli

| E1 — E'lon yaratish |  |
| --- | --- |
| Aktyor | Uy egasi |
| Turi | Asosiy |
| Ishga tushirish shartlari | Foydalanuvchi tizimga kirgan va uy egasi roliga ega; identifikatsiyadan o'tgan; hisobi faol. |
| Bajarish tartibi | 1) Uy egasi 'Yangi e'lon yaratish' funksiyasini tanlaydi; 2) Tizim e'lon yaratish formasini ko'rsatadi; 3) Uy egasi obyekt parametrlarini kiritadi (obyekt turi, joylashuv, maydon, xonalar soni, ijara narxi, muddati, tavsif, foydalanish shartlari); 4) Fotosuratlarni yuklaydi (kamida 3 ta, ko'pi bilan 15 ta); 5) Tizim ma'lumotlarni validatsiyadan o'tkazadi; 6) Tizim obyekt joylashuvini xarita xizmati orqali tasdiqlaydi va koordinatalarni saqlaydi; 7) E'lon 'moderatsiya kutmoqda' holatida saqlanadi; 8) E'lon moderatsiya navbatiga qo'shiladi (moderator E4 asosida ko'rib chiqadi); 9) Moderatsiya tasdiqlangach e'lon faol holatga o'tkaziladi va uy egasiga bildirishnoma yuboriladi. |
| Vaqt reglamenti | Forma yuklash — ≤3 s; validatsiya — ≤2 s; fotosuratlarni yuklash — ≤15 s; saqlash — ≤3 s. |
| Kiruvchi ma'lumotlar | Obyekt parametrlari (turi, manzil, maydon, xonalar, narx, muddat), tavsif, foydalanish shartlari, fotosuratlar, joylashuv koordinatalari. |
| Chiquvchi ma'lumotlar | Yangi e'lon yozuvi (noyob identifikator bilan), e'lon holati, moderatsiyaga yuborilganligi haqida bildirishnoma. |
| Kengaytmalar | Validatsiya xatoligi → aniq xabar va tuzatish so'ralishi; fotosurat hajmi/formati noto'g'ri → qayta yuklash taklifi; moderatsiya rad etilsa (E4 dan) → sabab bilan xabar va E2 ga o'tish imkoniyati. |
| Qo'shilgan ssenariylar | E4 |
| Faoliyat diagrammasi | 4.1.1.4-rasm (E1) |

| E2 — E'lonni tahrirlash yoki o'chirish |  |
| --- | --- |
| Aktyor | Uy egasi |
| Turi | Kengaytma (E1 ga nisbatan) |
| Ishga tushirish shartlari | Uy egasi tizimga kirgan; e'lon mavjud va ushbu uy egasiga tegishli. |
| Bajarish tartibi | 1) Uy egasi 'Mening e'lonlarim' bo'limidan e'lonni tanlaydi; 2) Tizim e'lon tafsilotlarini ko'rsatadi va mumkin bo'lgan harakatlarni taqdim etadi (tahrirlash, faol/nofaol qilish, o'chirish); 3) Uy egasi harakatni tanlaydi; 4) Tahrirlash holatida: o'zgartirishlar kiritiladi, validatsiya o'tkaziladi, jiddiy o'zgarishlar (joylashuv manzili, mulk turi, maydon, xonalar soni) bo'lsa e'lon qayta moderatsiyaga yuboriladi; narx o'zgarishi qayta moderatsiyani talab etmaydi (E4); 5) Faol/nofaol holatida: e'lon holati o'zgartiriladi; 6) O'chirish holatida: tizim tasdiq so'raydi, tasdiqlangandan so'ng e'lon arxivga ko'chiriladi; 7) Operatsiya audit jurnaliga yoziladi. |
| Vaqt reglamenti | E'lon yuklash — ≤3 s; o'zgarishlarni saqlash — ≤3 s; o'chirish — ≤2 s. |
| Kiruvchi ma'lumotlar | E'lon identifikatori, tanlangan harakat, yangi qiymatlar (tahrirlash holatida). |
| Chiquvchi ma'lumotlar | Yangilangan e'lon, audit yozuvi, tegishli bildirishnoma. |
| Kengaytmalar | Faol ijara so'rovlari mavjud e'lonni o'chirish urinishi → ogohlantirish va tasdiq so'rash; tahrirlash validatsiyadan o'tmasa → xatolik xabari; jiddiy o'zgarish aniqlansa → qayta moderatsiya. |
| Faoliyat diagrammasi | 4.1.1.4-rasm (E2) |

| E3 — E'lonlarni qidirish va filtrlash |  |
| --- | --- |
| Aktyor | Ijarachi, ro'yxatdan o'tmagan foydalanuvchi (guest) |
| Turi | Asosiy |
| Ishga tushirish shartlari | Foydalanuvchi tizimga kirgan yoki guest holatida; kamida bitta faol (moderatsiyadan o'tgan) e'lon mavjud. |
| Bajarish tartibi | 1) Foydalanuvchi e'lonlar katalogini ochadi; 2) Tizim faol e'lonlarni oldindan belgilangan tartibda ko'rsatadi (sana bo'yicha kamayib, va ijarachining skoring bali asosida); 3) Foydalanuvchi qidiruv yoki filtr parametrlarini kiritadi (hudud, narx oralig'i, obyekt turi, maydon, xonalar soni va boshqalar); 4) Tizim filtrlarga mos e'lonlarni shakllantiradi va ko'rsatadi; 5) Foydalanuvchi e'lonni tanlaydi yoki filtrlarni o'zgartiradi; 6) Qo'shimcha: ro'yxatdan o'tgan foydalanuvchi filtrlarni saqlashi mumkin; saqlangan filtrlarga mos yangi e'lonlar paydo bo'lganda tizim bildirishnoma yuboradi; 7) Foydalanuvchi e'lon egasiga ijara so'rovi yuborishi, e'lonni bloklashi (qiziq bo'lmasa qayta ko'rmaydi), ulashishi va shikoyat qilishi mumkin. |
| Vaqt reglamenti | Katalogni yuklash — ≤3 s; filtrlash natijalarini shakllantirish — ≤5 s. |
| Kiruvchi ma'lumotlar | Qidiruv va filtr parametrlari, saqlash buyrug'i (ixtiyoriy). |
| Chiquvchi ma'lumotlar | Filtrlarga mos e'lonlar ro'yxati, saqlangan filtr (agar talab qilingan bo'lsa). |
| Kengaytmalar | Filtrlarga e'lon mos kelmasa → 'mos e'lon topilmadi' va filtrlarni yumshatish taklifi; guest filtrni saqlamoqchi bo'lsa → ro'yxatdan o'tish (U1) taklif qilinadi; saqlangan filtr bo'yicha yangi e'lon → push-bildirishnoma yuboriladi. |
| Faoliyat diagrammasi | 4.1.1.4-rasm (E3) |

So'rovlar boshqaruvi moduli

| R1 — Ijara so'rovini yuborish |  |
| --- | --- |
| Aktyor | Ijarachi |
| Turi | Asosiy |
| Ishga tushirish shartlari | Foydalanuvchi tizimga kirgan va ijarachi roliga ega; identifikatsiyadan o'tgan; tanlangan e'lon faol holatda. |
| Bajarish tartibi | 1) Ijarachi e'lon tafsilotlari oynasida 'So'rov yuborish'ni tanlaydi; 2) Tizim so'rov formasini ko'rsatadi (qo'shimcha savol va malumotlar — uy egasi bilan chat qilish imkoniyati ochiladi); 3) Ijarachi ma'lumotlarni kiritadi; 4) Tizim ijarachining Rentmi balini tekshiradi; ball mavjud bo'lmasa, S1 (Rentmi hisobotini xarid qilish) taklif qilinadi; 5) Tizim so'rovni 'ko'rib chiqish kutmoqda' holatida saqlaydi; 6) Uy egasiga push va tizim ichidagi bildirishnoma yuboriladi; 7) Ijarachiga so'rov yuborilganligi haqida tasdiq ko'rsatiladi. |
| Vaqt reglamenti | Forma yuklash — ≤3 s; so'rovni saqlash — ≤3 s; uy egasiga bildirishnoma — ≤10 s. |
| Kiruvchi ma'lumotlar | E'lon identifikatori, ko'chib kelish sanasi, budjet malumoti, ijara muddati, qo'shimcha xabar (ixtiyoriy). |
| Chiquvchi ma'lumotlar | Yangi ijara so'rovi yozuvi (noyob identifikator bilan), uy egasiga bildirishnoma, ijarachiga tasdiq. |
| Kengaytmalar | Ayni e'lon bo'yicha takroriy so'rov mavjud → yangi so'rov taqiqlanadi, mavjud holatni ko'rish taklif qilinadi; ijarachi blacklist'da → so'rov taqiqlanadi; e'lon yuborish paytida nofaol bo'lib qolsa → ijarachiga xabar va so'rov bekor qilinadi. |
| Qo'shilgan ssenariylar | S1 (Rentmi bali mavjud bo'lmasa — xarid taklif etiladi) |
| Faoliyat diagrammasi | 4.1.1.4-rasm (R1) |

| R2 — Ijara so'rovini ko'rib chiqish |  |
| --- | --- |
| Aktyor | Uy egasi |
| Turi | Asosiy |
| Ishga tushirish shartlari | Uy egasi tizimga kirgan; uning e'loniga kamida bitta ko'rib chiqish kutayotgan so'rov mavjud. |
| Bajarish tartibi | 1) Uy egasi 'Kiruvchi so'rovlar' bo'limini ochadi va e'lonlaridan birini tanlaydi; 2) Tizim so'rovlar ro'yxatini holati bo'yicha ko'rsatadi; 3) Uy egasi so'rovni tanlaydi va tafsilotlarni ko'rib chiqadi (ijarachi ma'lumotlari, Rentmi bali va xulosa, so'rov xabari va chat orqali xabarlashish imkoniyati); 4) Uy egasi qaror qabul qiladi: tasdiqlash / rad etish / qo'shimcha savollar berish; 5) Tasdiqlash: so'rov 'tasdiqlangan' holatga o'tadi, ijarachiga bildirishnoma yuboriladi va uy egasining kontakt ma'lumotlari ochib beriladi; mazkur TT doirasida ssenariy shu yerda yakunlanadi (keyingi bosqich — elektron ijara shartnomasi — 3-bosqichda); 6) Rad etish: uy egasi sabab kiritishi mumkin, so'rov 'rad etildi' holatga o'tadi, ijarachiga bildirishnoma yuboriladi; 7) Qo'shimcha savol: uy egasi xabar qoldiradi, so'rov 'muhokama davom etmoqda' holatga o'tadi; 8) Qaror audit jurnaliga yoziladi; 9) Uy egasi e'lonlar so'rovlari bo'yicha statistik ma'lumotlar va tavsiyalarni ko'radi. |
| Vaqt reglamenti | So'rovlar ro'yxatini yuklash — ≤3 s; tafsilotlarni yuklash — ≤3 s; qarorni saqlash — ≤3 s; ijarachiga bildirishnoma — ≤10 s. |
| Kiruvchi ma'lumotlar | So'rov identifikatori, uy egasi qarori, sabab yoki qo'shimcha xabar (ixtiyoriy). |
| Chiquvchi ma'lumotlar | So'rovning yangilangan holati, ijarachiga bildirishnoma, audit yozuvi. |
| Kengaytmalar | So'rov 7 kun davomida ko'rib chiqilmasa → avtomatik 'ko'rib chiqilmagan' deb belgilanadi va uy egasiga push-bildirishnoma yuboriladi; bir vaqtda bir nechta so'rov tasdiqlansa → uy egasiga eslatma ko'rsatiladi. |
| Faoliyat diagrammasi | 4.1.1.4-rasm (R2) |

Bildirishnomalar moduli

| N1 — Push-bildirishnoma sozlamalarini boshqarish |  |
| --- | --- |
| Aktyor | Ijarachi, uy egasi |
| Turi | Asosiy |
| Ishga tushirish shartlari | Foydalanuvchi tizimga kirgan; mobil ilovaga push-bildirishnomalar uchun qurilma ruxsati berilgan. |
| Bajarish tartibi | 1) Foydalanuvchi 'Sozlamalar' → 'Bildirishnomalar' bo'limini ochadi; 2) Tizim bildirishnoma turlarini va joriy holatlarini (yoqilgan/o'chirilgan) ko'rsatadi; 3) Bildirishnoma turlari: yangi ijara so'rovi keldi (uy egasi); so'rov holati o'zgarganda (ijarachi — tasdiqlandi/rad etildi/muhokama); e'lon moderatsiya natijasi (uy egasi); Rentmi bali yangilanganda (S1 muvaffaqiyatli bajarilgach); saqlangan filtr bo'yicha yangi e'lon (ijarachi); 4) Foydalanuvchi bildirishnomani yoqadi yoki o'chiradi; 5) Tizim sozlamalarni saqlaydi va keyingi bildirishnomalarni tanlovi asosida yuboradi yoki yubormaydi. |
| Vaqt reglamenti | Sozlamalar sahifasini yuklash — ≤3 s; o'zgarishlarni saqlash — ≤2 s. |
| Kiruvchi ma'lumotlar | Foydalanuvchi identifikatori, bildirishnomalarni yoqish/o'chirish holati. |
| Chiquvchi ma'lumotlar | Yangilangan bildirishnoma sozlamalari, tasdiqlash xabari. |
| Kengaytmalar | Qurilmada push ruxsati o'chirilgan → qurilma sozlamalarida ruxsat berish taklifi; bildirishnomalar o'chirilsa → foydalanuvchi ogohlantiriladi, tasdiqlash so'raladi. |
| Faoliyat diagrammasi | 4.1.1.4-rasm (N1) |

Texnik qo'llab-quvvatlash moduli (mobil)

| T1 — Murojaat yuborish |  |
| --- | --- |
| Aktyor | Ijarachi, uy egasi |
| Turi | Asosiy |
| Ishga tushirish shartlari | Foydalanuvchi tizimga kirgan; mobil ilova orqali murojaat yuboriladi; texnik qo'llab-quvvatlash xizmati faol. Eslatma: guest foydalanuvchilar tizim ichidagi murojaat formasidan foydalana olmaydi — ular uchun rasmiy Telegram kanal orqali bog'lanish taqdim etiladi. |
| Bajarish tartibi | 1) Foydalanuvchi mobil ilovada 'Yordam' yoki 'Qo'llab-quvvatlash' bo'limini ochadi; 2) Tizim murojaat kategoriyalarini ko'rsatadi: texnik muammo / shikoyat / taklif; 3) Foydalanuvchi kategoriyani tanlaydi; 4) Murojaat mavzusini va tavsifini kiritadi; 5) Ixtiyoriy: skrinshot yoki fayl biriktiradi; 6) Murojaatni yuboradi; 7) Tizim saqlaydi, noyob ticket raqami beradi; 8) Foydalanuvchiga tasdiq ko'rsatiladi (ticket raqami va taxminiy javob muddati); 9) Murojaat admin web panelida support xodimiga ko'rinadi. |
| Vaqt reglamenti | Forma yuklash — ≤3 s; murojaatni yuborish — ≤5 s; tasdiq ko'rsatish — ≤3 s. |
| Kiruvchi ma'lumotlar | Kategoriya, mavzu, tavsif matni, ilovalar (ixtiyoriy), foydalanuvchi identifikatori. |
| Chiquvchi ma'lumotlar | Murojaat yozuvi (noyob ticket raqami bilan), foydalanuvchiga tasdiq, support xodimiga bildirishnoma. |
| Kengaytmalar | Fayl hajmi ruxsat etilganidan katta → yuklanishdan rad etiladi; tizim yuklamasi yuqori → foydalanuvchiga kechikish haqida ogohlantirish. |
| Faoliyat diagrammasi | 4.1.1.4-rasm (T1) |

Web qismi quyi tizimi

Autentifikatsiya moduli

| U2-veb — Tizimga kirish (Web qismi quyi tizimi, parol) |  |
| --- | --- |
| Aktyor | Administrator, moderator, qo'llab-quvvatlash xodimi, call-markaz operatori |
| Turi | Asosiy |
| Ishga tushirish shartlari | Foydalanuvchi hisobi superadmin tomonidan oldindan yaratilgan (username va parol berilgan); hisob faol holatda; kirish web interfeys orqali amalga oshiriladi. |
| Bajarish tartibi | 1) Foydalanuvchi web sahifada 'Kirish'ni bosadi; 2) Username va parolni kiritadi; 3) Tizim ma'lumotlarni tekshiradi (3 ta noto'g'ri urinishdan so'ng hisob 10 daqiqaga bloklanadi); 4) To'g'ri ma'lumotlar bo'lsa — JWT tokeni yaratiladi; 5) Audit jurnaliga yozuv kiritiladi; 6) Foydalanuvchi roliga mos web qismi quyi tizimiga yo'naltiriladi. |
| Vaqt reglamenti | Umumiy davomiyligi — ≤5 s; parolni tekshirish — ≤2 s. |
| Kiruvchi ma'lumotlar | Username, parol. |
| Chiquvchi ma'lumotlar | Foydalanuvchi sessiyasi, JWT tokeni, rolga mos web qismi quyi tizimi. |
| Kengaytmalar | Username topilmadi → kirish rad etiladi; parol unutilgan → U2a (faqat superadmin tomonidan tiklash); hisob bloklangan → superadminga murojaat. |
| Faoliyat diagrammasi | 4.1.1.4-rasm (U2-veb) |

| U2a — Web parolni tiklash |  |
| --- | --- |
| Aktyor | Administrator (superadmin roliga ega) |
| Turi | Kengaytma (U2-veb ga nisbatan) |
| Ishga tushirish shartlari | Web interfeys foydalanuvchisi (admin/moderator/support) hisobi superadmin tomonidan oldindan yaratilgan; foydalanuvchi parolini unutgan yoki hisobi bloklangan. |
| Bajarish tartibi | 1) Ta'sirlangan foydalanuvchi superadminga murojaat qiladi; 2) Superadmin web qismi quyi tizimida 'Foydalanuvchilarni boshqarish'ga kiradi; 3) Foydalanuvchini topadi va 'Parolni tiklash'ni tanlaydi; 4) Tizim yangi vaqtinchalik parol yaratadi; 5) Vaqtinchalik parolni superadmin korxona emaili orqali foydalanuvchiga yuboriladi; 6) Foydalanuvchi vaqtinchalik parol bilan kirganda tizim yangi parol o'rnatishni talab qiladi; 7) Foydalanuvchi yangi parolni ikki marta kiritib tasdiqlaydi; 8) Yangi parol saqlangach, sessiya yaratiladi; 9) Barcha harakatlar audit jurnaliga yoziladi. |
| Vaqt reglamenti | Vaqtinchalik parol yuborish — ≤60 s; parolning amal muddati — 24 soat. |
| Kiruvchi ma'lumotlar | Ta'sirlangan foydalanuvchi identifikatori, superadmin autentifikatsiya tokeni. |
| Chiquvchi ma'lumotlar | Yangilangan parol (xeshlangan), audit yozuvi. |
| Kengaytmalar | Superadmin parolni xavfsiz kanal orqali uzatadi; vaqtinchalik parol muddati o'tdi → qayta tiklash so'rash talab etiladi. |
| Faoliyat diagrammasi | 4.1.1.4-rasm (U2a) |

Moderatsiya moduli

| E4 — E'lonni moderatsiya qilish |  |
| --- | --- |
| Aktyor | Moderator |
| Turi | Asosiy |
| Ishga tushirish shartlari | Yangi yoki tahrirlangan e'lon 'moderatsiya kutmoqda' holatida; moderator tizimga kirgan. |
| Bajarish tartibi | 1) Moderator moderatsiya navbati oynasini ochadi; 2) Tizim kutayotgan e'lonlar ro'yxatini ko'rsatadi (eng eski avvalroq); 3) Moderator e'lonni tanlaydi va tafsilotlarni ko'rib chiqadi (parametrlar, fotosuratlar, uy egasi ma'lumotlari); 4) Moderator qaror qabul qiladi: tasdiqlash / rad etish / tuzatish talabi; 5) Tasdiqlash: e'lon 'faol' holatga o'tadi, uy egasiga bildirishnoma yuboriladi; 6) Rad etish: moderator sabab kiritadi, e'lon 'rad etildi' holatga o'tadi, uy egasiga sabab bilan bildirishnoma; 7) Tuzatish talabi: moderator izoh kiritadi, e'lon 'tuzatish kutmoqda' holatga o'tadi; 8) Qaror audit jurnaliga yoziladi. |
| Vaqt reglamenti | Moderatsiya navbatini yuklash — ≤3 s; qarorni saqlash — ≤2 s; uy egasiga bildirishnoma — ≤10 s; bir e'lonni ko'rib chiqishning maksimal kutish muddati (navbatda) — 24 soatdan ko'p emas. |
| Kiruvchi ma'lumotlar | E'lon identifikatori, moderator qarori, sabab yoki izoh (rad etish/tuzatish holatida). |
| Chiquvchi ma'lumotlar | E'lonning yangi holati, moderator audit yozuvi, uy egasiga bildirishnoma. |
| Kengaytmalar | Soxta yoki qonunga zid e'lon → e'lon bloklanadi va uy egasi hisobi 'tekshiruv ostida' belgilanadi; ayni obyekt uchun takroriy e'lon → avtomatik rad etish va sabab; fotosuratlar tavsifga mos kelmasligi → tuzatish talabi. |
| Faoliyat diagrammasi | 4.1.1.4-rasm (E4) |

| E5 — E'lon kataloglarini boshqarish |  |
| --- | --- |
| Aktyor | Moderator |
| Turi | Asosiy |
| Ishga tushirish shartlari | Moderator web qismi quyi tizimiga kirgan va moderator roliga ega. |
| Bajarish tartibi | 1) Moderator 'Kataloglar' bo'limini ochadi; 2) Tizim mavjud katalog ma'lumotnomalarini ko'rsatadi (obyekt turlari, hududlar/tumanlar, foydalanish shartlari va boshqa klassifikatorlar); 3) Moderator yangi yozuv qo'shadi, mavjudini tahrirlaydi yoki nofaol qiladi; 4) Tizim o'zgarishlarni validatsiyadan o'tkazadi (takrorlanmaslik tekshiruvi); 5) O'zgarishlar saqlanadi va e'lon yaratish (E1) hamda qidirish/filtrlash (E3) formalarida darhol aks etadi; 6) Harakat audit jurnaliga yoziladi. |
| Vaqt reglamenti | Katalogni yuklash — ≤3 s; o'zgarishlarni saqlash — ≤2 s. |
| Kiruvchi ma'lumotlar | Katalog turi, yozuv qiymati, harakat turi (qo'shish/tahrirlash/nofaol qilish). |
| Chiquvchi ma'lumotlar | Yangilangan katalog, audit yozuvi. |
| Kengaytmalar | Foydalanilayotgan katalog yozuvini o'chirish urinishi → ogohlantirish, faqat nofaol qilish taklif etiladi; takroriy yozuv → rad etiladi. |
| Faoliyat diagrammasi | 4.1.1.4-rasm (E5) |

Administratorlik moduli

| A1 — Foydalanuvchini administratsiya qilish |  |
| --- | --- |
| Aktyor | Administrator |
| Turi | Asosiy |
| Ishga tushirish shartlari | Administrator tizimga kirgan va administrator roliga ega; tizimda kamida bitta boshqariladigan foydalanuvchi mavjud. |
| Bajarish tartibi | 1) Administrator 'Foydalanuvchilarni boshqarish' bo'limini ochadi; 2) Tizim foydalanuvchilar ro'yxatini taqdim etadi (filtr va qidiruv: rol, holat, ro'yxatdan o'tish sanasi va boshqalar); 3) Administrator foydalanuvchini tanlaydi va to'liq profilini ko'radi (shaxsiy ma'lumotlar, Rentmi bali, faoliyat tarixi, audit yozuvlari, so'rovlari, chatlari); 4) Quyidagi harakatlardan birini tanlaydi: a) bloklash/aktivatsiya; b) rol o'zgartirish; c) profil ma'lumotlarini tahrirlash (favqulodda holatda); d) blacklist'ga qo'shish/chiqarish; e) PIN-kodni majburiy tiklashga yo'naltirish; shuningdek RBAC doirasida ruxsatlarni boshqarish va tizim sozlamalariga kirish; 5) Tanlangan harakatni tasdiqlaydi va sabab kiritadi (audit uchun majburiy); 6) Tizim o'zgarishlarni saqlaydi va foydalanuvchiga bildirishnoma yuboradi; 7) Barcha harakatlar audit jurnaliga batafsil yoziladi (kim, qachon, nima, sababi bilan). |
| Vaqt reglamenti | Foydalanuvchilar ro'yxatini yuklash — ≤5 s; profil yuklash — ≤3 s; o'zgarishlarni saqlash — ≤3 s; bildirishnoma — ≤10 s. |
| Kiruvchi ma'lumotlar | Foydalanuvchi identifikatori, tanlangan harakat, sabab, yangi qiymatlar (tahrirlash holatida). |
| Chiquvchi ma'lumotlar | Yangilangan foydalanuvchi profili yoki holati, audit yozuvi, foydalanuvchiga bildirishnoma. |
| Kengaytmalar | Blacklist'ga qo'shilgan foydalanuvchining faol so'rovlari mavjud → administrator ogohlantiriladi; bir foydalanuvchi boshqa administrator tomonidan tahrirlanayotgan bo'lsa → konflikt aniqlanadi va qayta yuklash taklif qilinadi; yuqori darajadagi operatsiyalar → qo'shimcha tasdiqlash (ikki faktorli) talab etiladi. |
| Faoliyat diagrammasi | 4.1.1.4-rasm (A1) |

| A2 — Tizim hisobotlarini shakllantirish |  |
| --- | --- |
| Aktyor | Administrator, texnik qo'llab-quvvatlash xodimi |
| Turi | Asosiy |
| Ishga tushirish shartlari | Foydalanuvchi tizimga kirgan va administrator yoki texnik qo'llab-quvvatlash roliga ega; hisobot uchun yetarli ma'lumotlar mavjud. |
| Bajarish tartibi | 1) Foydalanuvchi 'Hisobotlar va analitika' bo'limini ochadi; 2) Tizim hisobot turlarini ko'rsatadi: foydalanuvchilar, e'lonlar, so'rovlar, to'lovlar, skoring, moderatsiya faoliyati, tizim monitoring, tashqi integratsiyalar holati; 3) Foydalanuvchi hisobot turi va parametrlarni (davr, filtrlar) tanlaydi; 4) Tizim hisobotni ma'lumotlar bazasidan yig'adi va jadval/grafik ko'rinishida ko'rsatadi; 5) Integratsiya monitoringi rejimida: tashqi xizmatlar holati real vaqtda ko'rsatiladi; 6) PDF, XLSX yoki CSV formatida yuklab olish mumkin; 7) Audit jurnaliga yozuv kiritiladi. |
| Vaqt reglamenti | Hisobot sahifasini yuklash — ≤5 s; hisobot shakllantirish — ≤30 s; eksport faylini tayyorlash — ≤15 s. |
| Kiruvchi ma'lumotlar | Hisobot turi, davr (sana oralig'i), filtrlar, guruhlash mezonlari, eksport formati. |
| Chiquvchi ma'lumotlar | Tayyor hisobot (jadval/grafik), eksport fayli (PDF/XLSX/CSV), audit yozuvi. |
| Kengaytmalar | Hisobot vaqti chegaradan oshsa → ogohlantirish va davrni kamaytirish taklifi; ma'lumot yo'q → 'ma'lumot topilmadi' xabari. |
| Faoliyat diagrammasi | 4.1.1.4-rasm (A2) |

Billing nazorati moduli

| A4 — To'lovlarni nazorat qilish |  |
| --- | --- |
| Aktyor | Administrator |
| Turi | Asosiy |
| Ishga tushirish shartlari | Administrator web qismi quyi tizimiga kirgan; tizimda kamida bitta to'lov tranzaksiyasi mavjud. |
| Bajarish tartibi | 1) Administrator 'To'lovlar nazorati' bo'limini ochadi; 2) Tizim barcha tranzaksiyalar ro'yxatini ko'rsatadi (sana, foydalanuvchi, tur, summa, holat, to'lov tizimi) filtr va qidiruv bilan; 3) Administrator tranzaksiyani tanlaydi va batafsil ma'lumotlarni ko'radi (to'lov tizimi javobi, webhook holati); 4) Muammoli tranzaksiyani aniqlaydi (muvaffaqiyatsiz, kutilmoqda, qaytarilishi kerak); 5) Zaruratga ko'ra qo'lda holatni moslashtirish yoki to'lov tizimi bilan solishtirish (reconciliation) amalga oshiriladi; 6) Statistik hisobot shakllantiriladi (kunlik/oylik tushum, muvaffaqiyat darajasi); 7) Harakatlar audit jurnaliga yoziladi. |
| Vaqt reglamenti | Ro'yxatni yuklash — ≤5 s; tranzaksiya tafsilotlari — ≤3 s; hisobot shakllantirish — ≤30 s. |
| Kiruvchi ma'lumotlar | Filtr parametrlari, tranzaksiya identifikatori, qo'lda moslashtirish buyrug'i (ixtiyoriy). |
| Chiquvchi ma'lumotlar | Tranzaksiyalar ro'yxati, tranzaksiya tafsilotlari, billing hisoboti, audit yozuvi. |
| Kengaytmalar | To'lov tizimi bilan nomuvofiqlik aniqlansa → reconciliation jarayoni ishga tushiriladi; qaytarish (refund) talab qilinsa → tegishli to'lov tizimi orqali amalga oshiriladi. |
| Faoliyat diagrammasi | 4.1.1.4-rasm (A4) |

Integratsiya boshqaruvi moduli

| A3 — Tashqi integratsiyalarni boshqarish |  |
| --- | --- |
| Aktyor | Administrator |
| Turi | Asosiy |
| Ishga tushirish shartlari | Administrator web qismi quyi tizimga kirgan; tizimga kamida bitta tashqi integratsiya ulangan. |
| Bajarish tartibi | 1) Administrator 'Integratsiyalar' bo'limini ochadi; 2) Tizim ulangan tashqi xizmatlar ro'yxatini va real vaqtdagi holatini ko'rsatadi (identifikatsiya, skoring byurosi, to'lov tizimlari, SMS, push, xarita); 3) Administrator xizmatni tanlaydi va tafsilotlarni ko'radi (holat, oxirgi muvaffaqiyatli so'rov, xatoliklar statistikasi, javob vaqti); 4) Integratsiya parametrlarini sozlaydi (endpoint, kalit/token muddati, qayta urinish va timeout sozlamalari) — kalitlar shifrlangan saqlanadi; 5) Integratsiyani sinov so'rovi orqali tekshiradi; 6) Zaruratga ko'ra integratsiyani vaqtincha o'chiradi yoki yoqadi; 7) Barcha o'zgarishlar audit jurnaliga yoziladi. |
| Vaqt reglamenti | Ro'yxatni yuklash — ≤5 s; sinov so'rovi natijasi — ≤15 s; sozlamalarni saqlash — ≤3 s. |
| Kiruvchi ma'lumotlar | Integratsiya identifikatori, sozlama qiymatlari, sinov so'rovi buyrug'i. |
| Chiquvchi ma'lumotlar | Yangilangan integratsiya sozlamalari, holat, sinov natijasi, audit yozuvi. |
| Kengaytmalar | Tashqi xizmat javob bermasa → 'mavjud emas' holati va ogohlantirish; noto'g'ri kalit → sinov rad etiladi va xato ko'rsatiladi. |
| Faoliyat diagrammasi | 4.1.1.4-rasm (A3) |

Texnik qo'llab-quvvatlash moduli (admin)

| T2 — Murojaatni ko'rib chiqish |  |
| --- | --- |
| Aktyor | Texnik qo'llab-quvvatlash xodimi |
| Turi | Asosiy |
| Ishga tushirish shartlari | Texnik qo'llab-quvvatlash xodimi admin web panelida tizimga kirgan; kamida bitta ko'rib chiqilmagan murojaat (ticket) mavjud. |
| Bajarish tartibi | 1) Xodim admin web panelida 'Murojaatlar' bo'limini ochadi; 2) Tizim murojaatlar ro'yxatini ko'rsatadi (kategoriya, holat, sana, foydalanuvchi bo'yicha filtr); 3) Xodim murojaatni tanlaydi va tafsilotlarni ko'radi (kategoriya, matn, ilovalar, foydalanuvchi profili); 4) Murojaatni 'Ishlanmoqda' holatiga o'tkazadi; 5) Javob yozadi yoki ichki izoh qo'shadi; 6) Zarur bo'lsa boshqa bo'limga yo'naltiradi (eskalatsiya); 7) Muammo hal etilgach 'Hal etildi' holatiga o'tkazadi; 8) Foydalanuvchiga bildirishnoma yuboriladi (push yoqilgan bo'lsa — push; o'chirilgan bo'lsa — tizim ichidagi xabar); 9) Harakatlar audit jurnaliga yoziladi. |
| Vaqt reglamenti | Ro'yxatni yuklash — ≤5 s; tafsilotlarni yuklash — ≤3 s; javob saqlash — ≤3 s; bildirishnoma — ≤15 s; murojaatga javob maksimal muddati — 24 soat (ish kuni ichida). |
| Kiruvchi ma'lumotlar | Ticket identifikatori, xodim qarori, javob matni yoki ichki izoh, yangi holat. |
| Chiquvchi ma'lumotlar | Yangilangan ticket holati, foydalanuvchiga javob/bildirishnoma, audit yozuvi. |
| Kengaytmalar | Bir vaqtda boshqa xodim ishlamoqda → konflikt ogohlantirishi; 24 soat o'tib hal etilmagan ticket → avtomatik eskalatsiya va menejerga bildirishnoma. |
| Qo'shilgan ssenariylar | T1 |
| Faoliyat diagrammasi | 4.1.1.4-rasm (T2) |

| T3 — Murojaatni qabul qilish va ticket yaratish |  |
| --- | --- |
| Aktyor | Call-markaz operatori |
| Turi | Asosiy |
| Ishga tushirish shartlari | Call-markaz operatori web qismi quyi tizimiga kirgan; foydalanuvchidan telefon yoki chat orqali murojaat kelgan. |
| Bajarish tartibi | 1) Operator foydalanuvchi murojaatini telefon/chat orqali qabul qiladi; 2) Operator web qismi quyi tizimida foydalanuvchini topadi (telefon raqami yoki identifikatori bo'yicha) — faqat ko'rish huquqida; 3) Murojaat mazmunini aniqlaydi va kategoriyalaydi (texnik muammo / shikoyat / taklif); 4) Tizimda yangi ticket yaratadi (kategoriya, mavzu, tavsif); 5) Zaruratga ko'ra ticketni texnik qo'llab-quvvatlash xodimiga yo'naltiradi (eskalatsiya); 6) Foydalanuvchiga ticket raqami va taxminiy javob muddati aytiladi; 7) Harakat audit jurnaliga yoziladi. |
| Vaqt reglamenti | Foydalanuvchini topish — ≤5 s; ticket yaratish — ≤5 s. |
| Kiruvchi ma'lumotlar | Foydalanuvchi identifikatori/telefon raqami, kategoriya, mavzu, tavsif. |
| Chiquvchi ma'lumotlar | Yangi ticket yozuvi (noyob raqam bilan), eskalatsiya yo'nalishi (zarur bo'lsa), support xodimiga bildirishnoma. |
| Kengaytmalar | Foydalanuvchi tizimda topilmasa → umumiy murojaat sifatida yoziladi; murojaat darhol hal etilsa → ticket 'hal etildi' holatida yopiladi. |
| Qo'shilgan ssenariylar | T2 (eskalatsiya) |
| Faoliyat diagrammasi | 4.1.1.4-rasm (T3) |
