> Manba: [Release 1: 23.05.2026 · US 5 MyID: Identifikatsa](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/21823547)

# US 5 MyID: Identifikatsa

## User Story:

Foydalanuvchi sifatida men MyID SDK orqali shaxsiy identifikatsiyadan o‘tishni xohlayman,  
shunda men platformada tasdiqlangan foydalanuvchi bo‘lib, skoring tizimidan foydalanish imkoniga ega bo‘laman.

## Tavsif:

Foydalanuvchi muvaffaqiyatli login jarayonidan (Rol → Telefon → OTP → PIN → Login) o‘tgandan so‘ng avtomatik ravishda MyID identifikatsiya ekraniga yo‘naltiriladi. MyID SDK ilova ichida (embedded) ishlaydi va foydalanuvchidan PINFL, pasport ma’lumotlari hamda selfi orqali identifikatsiyani amalga oshiradi. Ma’lumotlar backendga yuboriladi va foydalanuvchining identifikatsiya holati aniqlanadi. Muvaffaqiyatli identifikatsiyadan so‘ng foydalanuvchi agar ijarachi bo’lsa skoring jarayoniga o‘tadi, agar foydalanuvchi uy egasi bo’lsa ko’chmas mulklarini import qilib olish sahifasiga o’tadi

## Shartlar:

* Foydalanuvchi tizimga muvaffaqiyatli kirgan bo‘lishi kerak
* JWT sessiya faol bo‘lishi kerak
* Kamera ruxsati berilgan bo‘lishi kerak

# Qabul qilish mezonlari 

## Scenario 1: MyID jarayonining boshlanishi

GIVEN foydalanuvchi tizimga muvaffaqiyatli kirgan bo‘lsa  
WHEN login jarayoni yakunlansa  
THEN MyID SDK identifikatsiya ekrani avtomatik ochiladi  
AND foydalanuvchidan identifikatsiya talab qilinad

## Scenario 2: Muvaffaqiyatli identifikatsiya

GIVEN foydalanuvchi MyID jarayonini yakunlasa  
WHEN SDK "VERIFIED" holatini qaytarsa  
THEN foydalanuvchining ma’lumotlari saqlanadi  
AND u ro’lican kelib chiqib skoring jarayoniga yoki uy import qilish strnitsasiga yo‘naltiriladi

## Scenario 3: Xatolik yoki muvaffaqiyatsiz identifikatsiya

GIVEN foydalanuvchi MyID jarayonida bo‘lsa  
WHEN SDK "REJECTED" yoki "ERROR" holatini qaytarsa  
THEN foydalanuvchiga qayta urinish imkoniyati berilad

## Scenario 4: Qayta urinish cheklovi

GIVEN foydalanuvchi identifikatsiyadan o‘ta olmagan bo‘lsa  
WHEN 3 martadan ortiq qayta urinish amalga oshirilsa  
THEN tizim vaqtinchalik cheklov qo‘yadi  
AND keyingi urinishlar ma’lum vaqt o‘tib ruxsat etiladi

## Scenario 5: Sessiyani tiklash

GIVEN foydalanuvchi identifikatsiyani to‘liq yakunlamagan bo‘lsa  
WHEN u ilovaga qayta kirsa  
THEN tizim MyID jarayonini davom ettirishga yo‘naltirad

## Scenario 6: Kamera ruxsati

GIVEN foydalanuvchi MyID jarayonini boshlasa  
WHEN kamera ruxsati berilmagan bo‘lsa  
THEN tizim ruxsat so‘raydi  
AND ruxsat berilmaguncha jarayon davom etmayd

# Biznes qoidalari:

*  MyID jarayoni login dan keyin avtomatik boshlanadi 
*  SDK ilova ichida (embedded) ishlaydi 
*  PINFL, pasport va selfi ma’lumotlari olinadi 
*  Identifikatsiya natijasi: VERIFIED / REJECTED / ERROR 
*  Qayta urinish cheklovi: 3 marta 
*  Muvaffaqiyatli identifikatsiya → skoring jarayoniga o‘tish 
*  Identifikatsiya jarayoni to‘liq sessiya davomida saqlsh

# Funktsional talablar:

*  MyID SDK integratsiyasi 
*  Login tugagandan so‘ng avtomatik yo‘naltirish 
*  Kamera ruxsatini boshqarish 
*  PINFL va pasport ma’lumotlarini olish 
*  Selfi orqali tekshirish 
*  Backendga ma’lumot yuborish 
*  Qayta urinish mexanizmi (3 martagacha) 
*  SDK ichida ishlaydigan UI flow 
*  Identifikatsiya holatini boshqarish 

# Nofunktsional talablar:

*  Yuqori xavfsizlik (shifrlangan ma’lumot uzatish) 
*  Barqaror SDK ishlashi 
*  Tezkor identifikatsiya jarayoni 
*  Kamera ishlash optimizatsiyasi 
*  Sessiya barqarorligi 
*  Ma’lumotlar maxfiyligini ta’minlash 

# Bog‘liqliklar:

*  MyID SDK 
*  Backend identifikatsiya servisi 
*  JWT autentifikatsiya tizimi 
*  Kamera ruxsat tizimi 
*  Xavfsiz ma’lumot saqlash 
*  Skoring tizimi (keyingi bosqich) 

# Definition of Ready (DoR):

*  MyID SDK hujjatlari mavjud 
*  Identifikatsiya maydonlari tasdiqlangan (PINFL, pasport, selfi) 
*  Statuslar aniqlangan (VERIFIED / REJECTED / ERROR) 
*  Qayta urinish qoidalari tasdiqlangan 
*  UX dizayn tayyor 
*  Kamera ruxsati flow’i aniqlangan 
*  Xavfsizlik talablari tasdiqlangan 

# Definition of Done (DoD):

*  MyID SDK muvaffaqiyatli integratsiya qilingan 
*  Embedded flow ishlaydi 
*  Kamera ruxsati boshqariladi 
*  Muvaffaqiyatli va muvaffaqiyatsiz holatlar ishlaydi 
*  Qayta urinish mexanizmi ishlaydi 
*  Backend integratsiya qilingan 
*  Ma’lumotlar xavfsiz saqlanadi 
*  QA testdan o‘tgan 
*  Xavfsizlik tekshiruvi muvaffaqiyatli 

# Scope tashqarisida:

*  Skoring hisoblash logikasi 
*  Ro‘yxatdan o‘tish (OTP, PIN) 
*  Admin panelda tekshiruv 
*  Qo‘lda operator tomonidan tekshirish
