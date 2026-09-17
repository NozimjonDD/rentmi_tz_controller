> Manba: [Release 1: 23.05.2026 · US 1 SS: Splash screen va boshlang‘ich initialization jarayonini ko‘rsatish](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/21626893)

# US 1 SS: Splash screen va boshlang‘ich initialization jarayonini ko‘rsatish

## User Story:

Foydalanuvchi sifatida men ilovani ochganimda splash screenni ko‘rmoqchiman, shunda tizim kerakli ma’lumotlarni yuklab, meni to‘g‘ri sahifaga avtomatik yo‘naltira oladi

## Tavsif:

Mobil ilova ishga tushirilganda splash screen (logo bilan) ko‘rsatiladi. Shu vaqt ichida fonda tizimni ishga tayyorlash jarayoni bajariladi: autentifikatsiya tekshiruvi, foydalanuvchi sessiyasi holati, konfiguratsiyalar yuklanadi. Jarayon natijasiga qarab foydalanuvchi tegishli sahifaga yo‘naltiriladi (onboarding, Pincode tekshiruvi, home yoki error ekranlariga)

## Shartlar:

* Ilova mobil qurilmaga o‘rnatilgan bo‘lishi kerak
* Foydalanuvchi ilovani ochishi kerak

# Qabul qilish kriteriyalari

## Scenario 1: Yangi foydalanuvchi4

GIVEN foydalanuvchi ilovani ochdi  
WHEN splash screen ko‘rsatiladi  
AND initialization muvaffaqiyatli tugaydi  
AND foydalanuvchi autentifikatsiyadan o‘tmagan bo‘lsa  
THEN foydalanuvchi onboarding sahifasiga yo‘naltiriladi

## Scenario 2: Tizimga kirgan foydalanuvchi

GIVEN foydalanuvchi ilovani ochdi  
WHEN splash screen initialization tugaydi  
AND foydalanuvchi aktiv tokenga ega bo‘lsa  
THEN foydalanuvchidan pin kodini kiritish so’raladi, va muvaffaqqiyatli pin kod kiritilganidan so’ng asosiy sahifaga yo’nltiriladi

## Scenario 3: Xatolik holati

GIVEN foydalanuvchi ilovani ochdi  
WHEN initialization jarayoni tarmoq yoki server xatosi sababli muvaffaqiyatsiz bo‘lsa  
THEN error ekrani ko‘rsatiladi  
AND foydalanuvchi qayta urinish (retry) qilish yoki mobil qurilma cash xotirasida saqlangan malumotlarni foydalanuvchiga ko’rsatish

## Scenario 4: Splash ekranni chetlab o‘tish mumkin emas

GIVEN splash screen ishlamoqda  
WHEN initialization jarayoni davom etmoqda  
THEN foydalanuvchi splash screenni o‘tkazib yubora olmaydi

# Biznes qoidalari:

* Splash screen har doim ilova ochilganda ko‘rsatiladi
* Routing faqat initialization tugagandan keyin amalga oshiriladi
* Foydalanuvchi splash screenni skip qila olmaydi
* Error holatida retry imkoniyati bo‘lishi kerak
* Foydalanuvchiga cashda saqlangan malumotlar internetga qayt ulanguniga qadar ko’rsatilinishi kerak

# Funktsional talablar:

* Splash screenda logo ko‘rsatish
* Background initialization jarayonini ishga tushirish
* Token orqali autentifikatsiyani tekshirish
* Dastlabki konfiguratsiyani yuklash
* User state bo‘yicha routing:

    * yangi user → onboarding
    * login bo‘lgan user → Pincode → home
    * xatolik → Cash asosida malumotlarni ochib berish → error ekran
    

# Nofunktsional talablar:

* Splash screen tez va silliq yuklanishi kerak
* UI bloklanmasligi kerak
* Past internet tezligida ham ishlashi kerak
* Android va iOS platformalarini qo‘llab-quvvatlash
* Ekran qotib qolmasligi kerak

# Bog‘liqliklar:

* Autentifikatsiya servisi
* Backend apilar
* Routing/navigation moduli
* Network status tekshiruvi
* Konfiguratsiya servisi
* UI|UX dizayn

# Definition of Ready:

* Initialization flow aniq belgilangan
* Routing logika tasdiqlangan
* UX dizayn tayyor
* Error holatlari aniqlangan

# Definition of Done:

* Splash screen ishlab chiqilgan
* Initialization integratsiya qilingan
* Auth tekshiruvi ishlaydi
* Routing to‘liq ishlaydi
* Error handling mavjud
* QA testdan o‘tgan
* Android va iOS’da sinovdan o‘tgan
