> Manba: [Release 1: 23.05.2026 · US 4 LA: Login Authentication](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/21954605)

# US 4 LA: Login Authentication

## User Story:

Foydalanuvchi sifatida men rol tanlab, telefon raqamim orqali OTP bilan tasdiqlanib, PIN kod yaratib tizimga avtomatik kirishni xohlayman, shunda men platformadan xavfsiz va tez foydalanish imkoniga ega bo‘laman.

## Tavsif:

Foydalanuvchi avval rol (uy egasi, ijarachi, guest) tanlaydi. Keyin telefon raqami (+998 format) kiritilib OTP yuboriladi. OTP 6 xonali bo‘lib 1 daqiqa amal qiladi. OTP muvaffaqiyatli tasdiqlangach, foydalanuvchi 4 xonali PIN kod yaratadi. PIN tasdiqlangandan so‘ng avtomatik login amalga oshiriladi va JWT + refresh token beriladi. User bir nechta device’da login bo‘lishi mumkin. Admin tomonidan bloklangan user OTP stageda to‘xtatiladi

## Shartlar:

* User language tanlangan
* Onboarding yoki choice screen orqali auth flowga kirgan

# Qabul qilish mezonlari (BDD)

## Scenario 1: Role selection

GIVEN user rolni tanlash ekranini ochadi  
WHEN user o'ziga kerakli rolni tanlaydi (uy egasi, ijarachi , guest)  
THEN uning ro'li vaqtinchalik saqlanadi ilova xotirasida

## Scenario 2: OTP yuborish

GIVEN user kerakli telefon raqamni kiritadi  
WHEN OTP kodini so'radydi  
THEN tizim 6 xonali OTP raqamini jo'natadi  
AND 60 sekundli timer ishga tushiriladi

## Scenario 3: OTP verifikatsiyasi

GIVEN user OTP raqaimini qabul qiladi  
WHEN user muddat tugaguniga qadar 1 minut davomida OTP kodni kiritadi  
THEN OTP kod muvaffaqqiyatli tasdilanadi  
AND user PIN kod kiritish sahifasiga yo'naltiriladi

## Scenario 4: OTP timeout

GIVEN OTP userga jo'natilinadi  
WHEN 60 sekund ichida muddati tugaydi  
THEN OTP yaroqsiz bo'ladi  
AND user qayta so'raydi OTP kod jo'natib berilishin

## Scenario 5: OTP kiritishga urinish

GIVEN user OTP kiritishga urinadi  
WHEN user 5 marotaba noto'g'ri otp kodni kiritadi  
THEN system avtomatik ravishda userni muzlatadi  
AND va 5 daqiqagacha userni boshqa funksiyalardan foydalana olmaydigan xolatga qo'yib qo'yad

## Scenario 6: PIN creation

GIVEN OTP muvaffaqqiyatli verifikatsadan o'tadi  
WHEN user 4 xonali PIN kod qo'yadi  
THEN PIN saqlanadi  
AND tizim login qismga o'tib ketad

## Scenario 7: Auto login PIN dan keiyin

GIVEN PIN muvaffaqqiyatli saqlanadi  
WHEN PIN tasdiqlanadi  
THEN tizim userni login sahifasiga yo'naltiradi  
AND JWT va refresh token generatsa qilinad

## Scenario 8: Blocked user access

GIVEN user admin tomonidan bloklangan  
WHEN user telefon raqamini kiritadi  
THEN tizim OTP kod jo'natmaydi  
AND userga bloklanganligi to'g'risida malumot ko'rsatad

## Scenario 9: Multi-device login

GIVEN user bir nechta qurilmalari orqali login qiladi  
WHEN autentifikatsadan muvaffaqqiyatli o'tadi  
THEN tizim bir nechta qurilmalarni saqlab olad

# Business Rules:

*  Role: uy egasi / ijarachi / guest 
*  Role change settings orqali mumkin 
*  Phone format: +998
*  OTP: 6 digit, 1 min validity 
*  Resend cooldown: 30–60 sekund
*  OTP attempt limit: 5 
*  PIN: 4 digit 
*  PIN faqat OTPdan keyin yaratiladi 
*  PINdan keyin avtomatik login 
*  JWT + refresh token ishlatiladi 
*  Multi-device login mavjud
*  Blocked user OTP stageda to‘xtatiladi 

# Functional taalablar:

*  Role selection screen 
*  Phone input validation (+998) 
*  OTP generation & SMS sending 
*  OTP auto-read (SMS autofill support) 
*  OTP verification 
*  Resend OTP with cooldown 
*  PIN creation screen (4 digit) 
*  Secure PIN storage (encrypted) 
*  Auto login after PIN 
*  JWT + refresh token generation 
*  Block user validation 
*  Multi-device session support 

# Non-Functional Requirements:

*  OTP delivery latency minimal (<5 sec ideal) 
*  High security (rate limiting + brute force protection) 
*  PIN encrypted storage 
*  Smooth step-by-step UX (separate screens) 
*  Stable session management 
*  Scalable authentication service 

# Dependencies:

*  SMS gateway service 
*  Authentication service (JWT + refresh token) 
*  User database 
*  Admin block service 
*  Rate limiting service 
*  Session management system 

# Definition of Ready:

*  Full auth flow approved (Role → Phone → OTP → PIN → Login) 
*  OTP rules confirmed (6 digit, 1 min) 
*  PIN requirements approved (4 digit) 
*  Block logic defined 
*  UX separate screens designed 
*  SMS gateway ready 
*  Security rules approved 

# Definition of Done (DoD):

*  Role selection implemented 
*  OTP flow fully working 
*  PIN creation implemented 
*  Auto-login after PIN working 
*  JWT + refresh token integrated 
*  SMS auto-read working 
*  Rate limiting implemented 
*  Blocked user logic working 
*  QA passed (all edge cases) 
*  Security tested 
*  Product Owner approved 

# Out of Scope:

*  MyID integration 
*  Scoring system 
*  Onboarding / language selection 
*  Profile editing 
*  UI redesign beyond auth flow
