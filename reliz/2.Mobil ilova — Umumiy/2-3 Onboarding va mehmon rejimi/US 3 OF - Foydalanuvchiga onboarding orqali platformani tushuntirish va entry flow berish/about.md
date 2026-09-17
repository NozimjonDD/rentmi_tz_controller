> Manba: [Release 1: 23.05.2026 · US 3 OF: Foydalanuvchiga onboarding orqali platformani tushuntirish va entry flow berish](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/21626928)

# US 3 OF: Foydalanuvchiga onboarding orqali platformani tushuntirish va entry flow berish

## User Story:

Foydalanuvchi sifatida men onboarding orqali platforma haqida tushunchaga ega bo‘lishni xohlayman,  
shunda men xizmatdan qanday foydalanish kerakligini oson tushunaman

## Tavsif:

Onboarding karusel ko‘rinishida 3–5 ta slide’dan iborat bo‘lsin. Unda platforma maqsdi, skoring tizimi va ijara jarayoni tushuntiriladi. Foydalanuvchi onboardingni skip qilishi mumkin. Tugagach user choice screen (guest / register)ga yo‘naltirilishi kerak bo’ladi

## Old shartlar:

* Language tanlangan
* Splash screen tugagan

# Qabul qilish mezonlari (BDD)

## Scenario 1: Onboarding ko‘rish

GIVEN user onboarding ekraniga o'tadi  
WHEN user slaydlar bilan tanishib chiqadi

## Scenario 2: Onboarding tugatish

GIVEN user onboarding oxirgi slaydida  
WHEN user davom etish knopkasini bosadi  
THEN user ro’yxatdan o’tish yoki guest sifatida foydalanish ekraniga yo’naltiriladi

## Scenario 3: Skip onboarding

GIVEN user onbording ekranida  
WHEN user O’tkazib yuborish knopkasini bosadi  
THEN user ro’yxatdan o’tish ekraniga yo’naltiriladi

## Biznes qoidalari:

*  Onboardingdan o’tish majburiy emas (skip qilish mumkin) 
*  3–5 slaydlardan iborat bo’lgan formatda
*  Content: Rentmi platformasi va ijara tarixi nima, skoring nima,  ijara so’rovi nima
*  Tugagach ro’yxatdan o’tish yoki mexmon sifatida davom etish ekrani ochiladi

## Functional Requirements:

*  Swipe qilsa bo’ladigan karusellar 
*  o’tkazib yuborish knopkasi 
*  davom etish knopkasi 
*  bir nechta tillarni tanlash imkoniyati
*  ro’yxatdan o’tish yoki mexmon sifatida davom etish ekranlari

## Guest:

*  Guest user faqat listings ko‘ra oladi 
*  Full features uchun register kerak

## DoR:

*  Onboarding content tasdiqlangan 
*  UX/UI chizmalari tasdiqlangan
*  user flow (skip + continue) aniqlangan 

## DoD:

*  Onboarding ishlaydi (mobile) 
*  Skip + continue ishlaydi 
*  Navigation choice screenga to‘g‘ri boradi 
*  Localization qo‘llab-quvvatlangan 
*  QA passed
