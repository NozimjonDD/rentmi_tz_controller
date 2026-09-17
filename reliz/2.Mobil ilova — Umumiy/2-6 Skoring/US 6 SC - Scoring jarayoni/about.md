> Manba: [Release 1: 23.05.2026 · US 6 SC: Scoring jarayoni](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/21954624)
>
> ⚠ "Skoring muddatsiz amal qiladi" bandi R4 da o'zgargan — [2-6 Skoring](<../about.md>).

# US 6 SC: Scoring jarayoni

## User Story:

Ijarachi sifatida men skoring xizmatini sotib olib o‘z ishonchlilik darajamni ko‘rishni xohlayman,  
shunda uy egalari oldida ishonchli foydalanuvchi sifatida ko‘rina olaman va tezroq uy topish imkoniyatiga ega bo‘laman.

## Tavsif:

Foydalanuvchi MyID identifikatsiyasidan muvaffaqiyatli o‘tgandan so‘ng avtomatik ravishda skoring bo‘limiga yo‘naltiriladi. Tizim foydalanuvchiga skoring olish zarurligi haqida motivatsion sahifa ko‘rsatadi. Ushbu sahifada skoring narxi, “Ishonchli ijarachiga aylaning” mazmunidagi qiymat taklifi va xizmatning foydalari ko‘rsatiladi.

Foydalanuvchi Payme, Click yoki bank kartasi orqali to‘lovni amalga oshiradi. To‘lov muvaffaqiyatli yakunlangach, skoring hisoblash jarayoni ishga tushadi va foydalanuvchiga skoring natijalari ochiladi.

Skoring natijalarida:

* GREEN / YELLOW / RED band,
* raw score,
* affordability indicator,
* ijobiy va salbiy faktorlar,
* tavsiyalar,
* recommendation screen’lari

ko‘rsatiladi.

Skoring tenantga tegishli bo‘ladi va barcha foydalanuvchi rollari (tenant, landlord, operator) tomonidan qisman va to’liq ko‘rilishi mumkin. Tranzaksiya ma’lumotlari tizimda saqlanadi.

## Shartlar:

* Foydalanuvchi MyID identifikatsiyasidan muvaffaqiyatli o‘tgan bo‘lishi kerak
* Foydalanuvchi tenant rolida bo‘lishi kerak
* Guest user bo‘lmasligi kerak
* Tizimda faol sessiya mavjud bo‘lishi kerak

# Qabul qilish mezonlari 

## Scenario 1: Skoring sotib olish sahifasi ochilishi

GIVEN tenant MyID identifikatsiyasidan muvaffaqiyatli o‘tgan bo‘lsa  
WHEN identifikatsiya yakunlansa  
THEN skoring purchase sahifasi avtomatik ochiladi  
AND foydalanuvchiga skoring narxi va motivatsion ma’lumotlar ko‘rsatiladi

## Scenario 2: Motivatsion sahifa ko‘rinishi

GIVEN foydalanuvchi scoring intro sahifasida bo‘lsa  
WHEN ekran yuklansa  
THEN "Ishonchli ijarachiga aylaning" mazmunidagi kontent ko‘rsatiladi  
AND foydalanuvchiga tezroq uy topish afzalliklari tushuntiriladi

## Scenario 3: To‘lovni amalga oshirish

GIVEN foydalanuvchi "Skoring sotib olish" tugmasini bossa  
WHEN foydalanuvchi Payme, Click yoki karta orqali to‘lov qilsa  
AND to‘lov muvaffaqiyatli yakunlansa  
THEN scoring calculation jarayoni boshlanadi  
AND tranzaksiya tizimga saqlanad

## Scenario 4: Skoring hisoblash jarayoni

GIVEN scoring calculation jarayoni ishlayotgan bo‘lsa  
WHEN foydalanuvchi ilovani yopib yuborsa yoki boshqa sahifaga o‘tsa  
THEN scoring process background rejimida davom etadi  
AND foydalanuvchi ilovadan chiqib ketsa status widget orqali ko‘rsatiladi

## Scenario 5: Skoring natijalarini ko‘rish

GIVEN scoring calculation muvaffaqiyatli yakunlangan bo‘lsa  
WHEN foydalanuvchi scoring result sahifasini ochsa  
THEN foydalanuvchiga band, raw score, affordability indicator va recommendation ma’lumotlari, shaxsiy malumotlari, depozit va predoplata xisobi, kredit tarixi malumotlari, qarzdorliklari, ijara tarixi malumotlari ko‘rsatiladi

## Scenario 6: Push notification yuborilishi

GIVEN scoring calculation muvaffaqiyatli yakunlangan bo‘lsa  
WHEN scoring natijasi tayyor bo‘lsa  
THEN foydalanuvchiga push notification yuboriladi  
AND receipt shakllantirilad

## Scenario 7: Hard reject holati

GIVEN foydalanuvchi hard reject qoidalariga tushsa  
WHEN scoring hisoblanganda  
THEN foydalanuvchiga score va band baribir ko‘rsatiladi, lekin hard reject skore balidan oshibketmasligi kerak bo’ladi

## Scenario 8: Qayta scoring sotib olish

GIVEN foydalanuvchi avval scoring sotib olgan bo‘lsa  
WHEN foydalanuvchi qayta scoring sotib olsa  
THEN yangi scoring calculation ishga tushadi  
AND yangi tranzaksiya tarixga saqlanadi

# Biznes qoidalari:

*  Skoring faqat tenant uchun mavjud 
*  Guest user scoring sotib ola olmaydi 
*  Skoring narxi fixed 
*  Skoring muddatsiz amal qiladi 
*  Tenant scoringni qayta sotib olishi mumkin 
*  To‘lovdan keyin scoring avtomatik hisoblanadi 
*  Hard reject bo‘lsa ham score ko‘rsatiladi 
*  Tranzaksiya tarixi saqlanadi 
*  Push notification yuboriladi 
*  Receipt shakllantiriladi 
*  Scoring barcha rollarga ko‘rinadi 
*  Operator raw scoring faktorlarini ko‘ra oladi 

# Funktsional talablar:

*  Scoring intro/motivation screen 
*  Fixed pricing display 
*  Payment integration (Payme / Click / Card) 
*  Scoring calculation trigger 
*  Background scoring processing 
*  Status widget 
*  Push notification integration 
*  Receipt generation 
*  Scoring result UI 
*  Recommendation screens 
*  Transaction history 
*  Re-purchase flow 
*  Operator scoring visibility 
*  Affordability indicator visualization 

# Nofunktsional talablar:

*  To‘lov xavfsizligi yuqori darajada bo‘lishi kerak 
*  Background calculation barqaror ishlashi kerak 
*  Scoring natijasi kechikmasdan yangilanishi kerak 
*  Push notification ishonchli ishlashi kerak 
*  Transaction ma’lumotlari yo‘qolmasligi kerak 
*  Yuqori yuklamada ham stable ishlashi kerak 

# Bog‘liqliklar:

*  MyID identifikatsiya tizimi 
*  Payment gateway 
*  Scoring calculation service 
*  Push notification service 
*  Transaction storage 
*  Recommendation engine 
*  Operator panel
