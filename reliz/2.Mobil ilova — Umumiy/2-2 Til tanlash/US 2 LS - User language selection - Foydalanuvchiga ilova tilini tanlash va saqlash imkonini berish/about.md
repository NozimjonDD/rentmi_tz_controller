> Manba: [Release 1: 23.05.2026 · US 2 LS: User language selection - Foydalanuvchiga ilova tilini tanlash va saqlash imkonini berish](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/21823527)

# US 2 LS: User language selection - Foydalanuvchiga ilova tilini tanlash va saqlash imkonini berish

## User Story:

Foydalanuvchi sifatida men ilovaga kirishda tilni tanlashni xohlayman, shunda men platformani o‘zim tushunadigan tilda ishlata olaman

## Tavsif:

Foydalanuvchi splash screendan keyin alohida full screen orqali ilova tilini tanlaydi. Tanlangan til backend profileda saqlanadi va keyingi sessiyalarda ham qo‘llaniladi. Tilni keyinchalik settings orqali o‘zgartirish mumkin bo’ladi

## Shartlar:

* Foydalanuvchi ilovani ochgan
* Splash screen tugagan

# Qabul qilish mezonlari

## Scenario 1: Til tanlash

GIVEN user opens language selection screen  
WHEN user selects a language (uzb lotin, rus, uzb kiril, english)  
THEN selected language is applied in UI  
AND saved to backend profile

## Scenario 2: Default language

GIVEN user tilni tanlamaydi  
WHEN tizim ishlashda davom etadi  
THEN default o’zbek tili tanlanadi (lotin)

## Scenario 3: Language change later

GIVEN user nastroykiga kiradi  
WHEN user tilni o’zgartiradi  
THEN tizim ilova UI qismini yangilaydi  
AND bekend malumotlarini yangilaydi

## Biznes qoidalari:

*  Language selection majburiy bosqich 
*  Default language: Uzbek Latin 
*  Tanlov backend profile qismida saqlanadi 
*  Keyinchalik settingsdan o‘zgartiriladi 

## Functional Requirements:

*  UI va UX til tanlash stranitsalarini ishlab chiqish 
*  4 ta til qo‘llab-quvvatlash
*  Backendga language update request metodini ishlab chiqish
*  UIda tilni tanlash qismini ishlab chiqish

## DoR:

*  Supported languages aniq belgilangan 
*  UI dizayn tasdiqlangan 
*  Backend endpoint tayyor 
*  Default language qaror qilingan 

## DoD:

*  Language selection ishlaydi 
*  Backend save ishlaydi 
*  UI translation ishlaydi 
*  Settings change qo‘llab-quvvatlangan 
*  QA testdan o‘tgan
