# 9-4 Reliz tayyorligi kriteriyalari

**Manba:** [Release 5 17.08.2026 (Confluence)](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843819) (8-bo'lim)

Ushbu reliz quyidagi shartlar bajarilganida muvaffaqiyatli ishlab chiqilgan deb qabul qilinadi:

* Ijarachi yangilangan asosiy sahifani ko'radi: bo'limlar, chips, skoring-mos blok, yangi navbar (Main/Saved/Lenta/So'rovlar/Profil) to'g'ri ishlaydi
* Badge'lar to'g'ri chiqadi: "Tekshirilgan" faqat uch shart birga bajarilganda; "Sizga mos" ikki tomonlama moslikda; "Top" hudud kesimida; "Narxi tushdi" faqat real pasayishda
* Skoring-mos uylar bloki to'g'ri sonni ko'rsatadi va ro'yxatga olib boradi
* Filter narx qiymatlari mln so'm / 100$ ga yaxlitlanadi; filter saqlanadi va Saqlanganlar sahifasida "+N ta yangi" badge ishlaydi
* Xarita ekranida pinlar, chips, ro'yxat toggle va bottom sheet to'g'ri ishlaydi
* E'lon detailda yangi maydonlar va Ko'rildi/Ariza/Saqlangan statistikasi ko'rinadi
* Uy egasi ommaviy profili ochiladi: tasdiqlanganlik, Rentmi'da vaqt, javob vaqti, tegishli e'lonlar; reyting va kafolat bloklari ko'rinmaydi (yashirilgan)
* Ijarachi so'rov yuborishda yangi maydonlarni to'ldiradi; so'rovni bekor qila oladi; statuslar yangi nomlanishda
* Uy egasida countdown ishlaydi: 24 soat, 7 soatdan kam qolganda qizil; muddati o'tsa so'rov "ko'rib chiqilmagan" bo'ladi va ikki tomonga push keladi
* "Odatda N soatda javob beradi" faqat kamida 3 ta javobdan keyin, mediana asosida chiqadi
* "Talablaringizga mos" badge uy egasi kartasida to'g'ri ishlaydi; so'rovlar sahifasida statistika grafigi ko'rinadi
* Uy egasi asosiy sahifasida Analitika (7/30 kun) real sonlarni, Daromadlarim va Xizmatlar bloklari "Tez kunda" ni ko'rsatadi
* "Mulklarim"da qoralama/ijarada/bo'sh statuslari ishlaydi; e'lon formasida o'xshash e'lonlar min/max ko'rinadi
* Bildirishnomalar: narx tushganda va saqlangan filter bo'yicha yangi e'londa push keladi; N1 sozlamalarida yangi turlar boshqariladi
* Terminologiya barcha ekranlarda yagona: "kirish sanasi", "bron", "Ariza jo'natish"
* RelizF elementlari buildda ko'rinmaydi: reyting, Rentmi kafolati, bo'shash sanasi badge'lari, "uy bo'shadi" bildirishnomasi
* Regressiya: R1–R4 funksionalliklari buzilmagan; kritik bug yo'q; barcha 19 ta use case (11 ijarachi + 6 uy egasi + 2 admin) sinovdan o'tgan
