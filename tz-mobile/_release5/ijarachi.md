# R5 User storylar — Ijarachi (👤)

Release 5 ning ijarachi bo'yicha to'liq user-storylari (manba: `R5 User storylar Ijarachi.pdf`). Har biri **flow'ga** bog'langan va **kod holati** bilan (tz-mobile kod-o'rganish natijasi). Belgilar: ✅ bajarilgan · 🟡 qisman · ❌ yo'q.

---

## R5-IJ-01 — Yangilangan asosiy sahifa
**Flow:** [06-elonlar/tenant/asosiy-sahifa](../06-elonlar/tenant/asosiy-sahifa.md) · [00-umumiy/navigatsiya](../00-umumiy/navigatsiya.md) · **Kod holati:** 🟡 (navbar'da "Saved" yo'q — K2; stories yashirilishi ↔ kodda faol — E-K2)

**User Story:** Ijarachi sifatida men yangilangan asosiy sahifada kerakli bo'limlarga tez o'tishni xohlayman, shunda uy qidirishni bir ekrandan boshlay olaman.

**Tavsif:** Asosiy sahifa yangi dizaynda: salomlashish headeri, tepada chat va bildirishnoma tugmalari, "Toshkentda uy qidiramizmi?" klikabel shahar tanlovi, xona soni chips filtri, bo'limlar (TOP kvartiralar / Kvartiralar / Rentmi Maslahat beradi / Villa), "Xarita orqali qidirish" banneri. Pastki navbar: Main, Saved, Lenta, So'rovlar, Profil. Actual History stories yashirin qoladi.

**Qabul mezonlari:**
- GIVEN ijarachi tizimga kirgan WHEN asosiy sahifa ochilsa THEN header, chips, barcha bo'limlar va yangi navbar 3 soniya ichida yuklanadi
- GIVEN shahar nomi ko'rsatilgan WHEN "Toshkentda" bosilsa THEN shahar/hudud tanlash oynasi ochiladi va tanlov barcha bo'limlarga qo'llanadi
- GIVEN xona chips'lari WHEN "2 xona" tanlansa THEN bo'limlardagi e'lonlar 2 xonalilarga filtrlanadi
- GIVEN bo'lim mavjud WHEN "Hammasi >" bosilsa THEN shu bo'limning to'liq ro'yxat sahifasi ochiladi
- GIVEN yangi navbar WHEN "Lenta" bosilsa THEN e'lonlar lentasi ochiladi (yangi sahifa emas)

---

## R5-IJ-02 — Skoring-mos uylar bloki
**Flow:** [06-elonlar/tenant/asosiy-sahifa](../06-elonlar/tenant/asosiy-sahifa.md) · [04-skoring](../04-skoring/about.md) · **Kod holati:** 🟡 (skoring-mos endpoint bor)

**User Story:** Ijarachi sifatida men skoring balimga mos uylar sonini ko'rishni xohlayman, shunda arizam qabul qilinish ehtimoli yuqori uylarga e'tibor qarata olaman.

**Tavsif:** Asosiy sahifada gauge (ball), "Skoringizga mos N ta uy" va "Arizalaringiz ustuvor ko'rib chiqiladi" izohi. Bosilganda mos uylar ro'yxati ochiladi. Moslik: ijarachi bali ≥ e'lonning minimal skoring talabi. Soni soatlik keshda.

**Qabul mezonlari:**
- GIVEN ijarachi skoringdan o'tgan WHEN asosiy sahifa ochilsa THEN blokda joriy bal va mos uylar soni ko'rinadi
- GIVEN ijarachi skoringdan o'tmagan WHEN asosiy sahifa ochilsa THEN blok "Skoringdan o'ting" CTA bilan (S1 ga yo'naltiradi)
- GIVEN blok ko'rsatilgan WHEN bosilsa THEN faqat mos e'lonlardan iborat ro'yxat ochiladi
- GIVEN mos uy yo'q WHEN blok ochilsa THEN "Hozircha mos uy topilmadi" ko'rsatiladi

---

## R5-IJ-03 — Badge'lar tizimi
**Flow:** [06-elonlar/tenant/asosiy-sahifa](../06-elonlar/tenant/asosiy-sahifa.md) · [elon-detail](../06-elonlar/tenant/elon-detail.md) · **Kod holati:** 🟡 (badge'lar faqat home endpoint — E-K1)

**User Story:** Ijarachi sifatida men e'lon kartalarida ishonch va moslik belgilarini ko'rishni xohlayman, shunda qaysi uyga ariza berishni tezroq hal qila olaman.

**Tavsif:** To'rt badge: "Sizga mos" (ikki tomonlama moslik), "Top" (og'irlikli ball, hudud kesimida), "Tekshirilgan" (moderatsiya + identifikatsiya + tegishlilik AND), "Narxi tushdi" (narx tarixi). Rasm ustida m²/xona/qavat va kartada ko'rishlar soni.

**Qabul mezonlari:**
- GIVEN e'lon uch shartning barchasiga javob beradi WHEN karta ko'rsatilsa THEN "Tekshirilgan" chiqadi; birorta shart bajarilmasa — chiqmaydi
- GIVEN e'lon ijarachi filtriga mos VA ijarachi e'lon talabiga mos WHEN karta ko'rsatilsa THEN "Sizga mos" chiqadi
- GIVEN narx 7–14 kunda belgilangan foizdan ko'p pasaygan WHEN karta ko'rsatilsa THEN "Narxi tushdi" chiqadi; sun'iy ko'tarib-tushirishda chiqmaydi
- GIVEN tegishlilik ma'lumoti yo'q WHEN karta ko'rsatilsa THEN "Tekshirilgan" ko'rsatilmaydi (default: yashirish)

---

## R5-IJ-04 — Filter yangilanishi
**Flow:** [06-elonlar/tenant/qidiruv-filtr](../06-elonlar/tenant/qidiruv-filtr.md) · **Kod holati:** ✅ (rooms/pets frontend-only — E-K5)

**User Story:** Ijarachi sifatida men narx filtrini qulay qadamlar bilan sozlashni xohlayman, shunda keraksiz aniq raqamlar bilan ovora bo'lmayman.

**Tavsif:** Narx maydonlari va slider so'mda mln qadamga, dollarda 100$ qadamga yaxlitlanadi; so'm/dollar toggle. "Filterni saqlash" va "Filterni tozalash" tugmalari. Saqlangan filtrlar mantig'i qayta ko'rib chiqiladi.

**Qabul mezonlari:**
- GIVEN valyuta so'm WHEN slider surilsa THEN qiymat mln qadam bilan (5 000 000 → 6 000 000)
- GIVEN valyuta dollar WHEN slider surilsa THEN qiymat 100$ qadam bilan
- GIVEN filter to'ldirilgan WHEN "Filterni saqlash" bosilsa THEN filter Saqlanganlar sahifasida paydo bo'ladi
- GIVEN filter to'ldirilgan WHEN "Filterni tozalash" bosilsa THEN barcha maydonlar default holatga qaytadi

---

## R5-IJ-05 — Saqlanganlar sahifasi
**Flow:** [06-elonlar/tenant/favorites](../06-elonlar/tenant/favorites.md) · [qidiruv-filtr](../06-elonlar/tenant/qidiruv-filtr.md) · **Kod holati:** ✅

**User Story:** Ijarachi sifatida men saqlangan uylar va filtrlarimni bitta joyda ko'rishni xohlayman, shunda qidiruvimni davom ettirishim oson bo'ladi.

**Tavsif:** "Saqlanganlar" sahifasi 2 tab: Saqlangan uylar / Saqlangan filterlar. Har filtr kartasida parametrlar, "N ta e'lon bor" va "+N ta yangi" badge.

**Qabul mezonlari:**
- GIVEN saqlangan filtrlar mavjud WHEN sahifa ochilsa THEN har filtr parametrlari va e'lonlar soni bilan ko'rinadi
- GIVEN filtr saqlangandan keyin yangi mos e'lonlar qo'shilgan WHEN sahifa ochilsa THEN "+N ta yangi" badge ko'rinadi
- GIVEN filtr kartasi bosildi WHEN ro'yxat ochilsa THEN yangi e'lonlar birinchi ko'rsatiladi va badge nolga tushadi

---

## R5-IJ-06 — Xarita orqali qidirish
**Flow:** [06-elonlar/tenant/xarita](../06-elonlar/tenant/xarita.md) · **Kod holati:** ✅

**User Story:** Ijarachi sifatida men e'lonlarni xaritada ko'rishni xohlayman, shunda menga qulay joylashuvdagi uylarni tez topa olaman.

**Tavsif:** Xarita ekrani: e'lon pinlari va klasterlar, xarita ustidagi chips (xona soni, Mebelli), "Ro'yhat bo'yicha" toggle, pastda "N ta e'lon topildi" bottom sheet, saralash. Asosiy sahifadagi banner orqali kirish.

**Qabul mezonlari:**
- GIVEN xarita ochilgan WHEN chips tanlansa THEN pinlar va bottom sheet ro'yxati filtrlanadi
- GIVEN pin bosildi WHEN e'lon kartasi ochilsa THEN karta badge'lar va asosiy parametrlar bilan ko'rinadi
- GIVEN "Ro'yhat bo'yicha" bosildi WHEN rejim almashsa THEN ro'yxat ko'rinishiga o'tadi va xaritaga qaytish mumkin
- GIVEN xarita yuklanmoqda WHEN 5 soniyadan oshsa THEN xatolik/retry holati ko'rsatiladi

---

## R5-IJ-07 — E'lon detail yangilanishi
**Flow:** [06-elonlar/tenant/elon-detail](../06-elonlar/tenant/elon-detail.md) · **Kod holati:** ✅

**User Story:** Ijarachi sifatida men e'lon sahifasida qaror uchun zarur barcha ma'lumotni ko'rishni xohlayman, shunda boshqa manbalarga murojaat qilmayman.

**Tavsif:** Yangi maydonlar: minimal ijara davri, kirish sanasi, e'lon joylangan vaqt. Ko'rildi/Ariza/Saqlangan statistika bloki. Badge'lar qatori va javob vaqti indikatori. CTA — "Ariza jo'natish".

**Qabul mezonlari:**
- GIVEN e'lon ochildi WHEN sahifa yuklansa THEN minimal ijara davri, kirish sanasi va joylangan vaqt ko'rinadi
- GIVEN statistika mavjud WHEN sahifa yuklansa THEN Ko'rildi/Ariza/Saqlangan sonlari ko'rinadi
- GIVEN sahifa pastigacha aylantirildi WHEN CTA ko'rinsa THEN tugma "Ariza jo'natish" deb nomlangan

---

## R5-IJ-08 — Uy egasi ommaviy profili
**Flow:** [06-elonlar/tenant/uy-egasi-profil](../06-elonlar/tenant/uy-egasi-profil.md) · **Kod holati:** ❌ (kodda ekran/endpoint yo'q — E-K6)

**User Story:** Ijarachi sifatida men uy egasi haqida tekshirilgan ma'lumotni ko'rishni xohlayman, shunda firibgarlikdan himoyalanaman va ishonch bilan ariza yuboraman.

**Tavsif:** E'lon sahifasidagi uy egasi blokidan ommaviy profil ochiladi: Rentmi'da N vaqt, e'lonlar soni, "Tasdiqlangan uy egasi — shaxsi va hujjatlari Rentmi tomonidan tekshirilgan", javob berish odati, tegishli e'lonlar. Reyting va "Rentmi kafolati" bloklari yashirin (RelizF). Chat/so'rov oqimida "faqat platforma orqali muloqot qiling" xavfsizlik xabari.

**Qabul mezonlari:**
- GIVEN uy egasi identifikatsiyadan o'tgan va mulk tegishliligi tasdiqlangan WHEN profil ochilsa THEN "Tasdiqlangan uy egasi" bloki ko'rinadi
- GIVEN uy egasining boshqa faol e'lonlari bor WHEN profil ochilsa THEN "Tegishli e'lonlar" ro'yxati ko'rinadi
- GIVEN profil ochildi WHEN sahifa yuklansa THEN reyting yulduzi va kafolat bloki ko'rinmaydi
- GIVEN ijarachi chat boshladi WHEN oyna ochilsa THEN xavfsizlik xabari ko'rinadi

---

## R5-IJ-09 — So'rov formasi yangi maydonlar
**Flow:** [07-sorovlar/tenant/ariza-yuborish](../07-sorovlar/tenant/ariza-yuborish.md) · **Kod holati:** ❌ (kodda faqat erkin matn — K4)

**User Story:** Ijarachi sifatida men so'rovda kirish sanasi, byudjet va muddatni ko'rsatishni xohlayman, shunda uy egasi mening shartlarimni oldindan bilib qaror qabul qiladi.

**Tavsif:** So'rov formasiga maydonlar: kirish sanasi, byudjet (max), ijara muddati, to'lov kuni. Bu ma'lumotlar uy egasining ijarachi kartasida ko'rsatiladi.

**Qabul mezonlari:**
- GIVEN forma ochildi WHEN maydonlar to'ldirilmasa THEN majburiy maydonlar bo'yicha validatsiya xabari
- GIVEN forma to'ldirildi WHEN so'rov yuborilsa THEN uy egasi kartasida kirish sanasi / byudjet / muddat ko'rinadi
- GIVEN Rentmi bali yo'q WHEN so'rov yuborilmoqchi bo'lsa THEN S1 (hisobot xarid) taklif etiladi (TZ R1)

---

## R5-IJ-10 — So'rov statuslari va bekor qilish
**Flow:** [07-sorovlar/tenant/oz-sorovlarim](../07-sorovlar/tenant/oz-sorovlarim.md) · **Kod holati:** 🟡 (bekor = rad; alohida "bekor qilingan" status yo'q — K5)

**User Story:** Ijarachi sifatida men yuborgan so'rovimni bekor qila olishni xohlayman, shunda fikrim o'zgarganda uy egasini bekorga kuttirmayman.

**Tavsif:** Statuslar: "ko'rilmoqda" / "kutilmoqda" / "qabul qilindi" / "rad etildi" / "bekor qilingan". Bekor qilish tugmasi faqat hali ko'rib chiqilmagan so'rovlarda; bekor qilingan so'rov ro'yxatda badge bilan turadi.

**Qabul mezonlari:**
- GIVEN so'rov "kutilmoqda" WHEN ijarachi bekor qilishni tasdiqlasa THEN "bekor qilingan"ga o'tadi va uy egasiga bildirishnoma
- GIVEN so'rov "qabul qilindi" WHEN ro'yxat ochilsa THEN bekor qilish tugmasi ko'rinmaydi
- GIVEN ijarachi bekor qilmoqda VA uy egasi ayni paytda qabul qilmoqda WHEN to'qnashsa THEN birinchi yozilgan amal g'olib, ikkinchisiga aktual holat xabari

---

## R5-IJ-11 — Narx va yangi e'lon bildirishnomalari
**Flow:** [10-bildirishnoma](../10-bildirishnoma/about.md) · **Kod holati:** 🟡 (push bor; N1 sozlamalari amalda yo'q — ❌)

**User Story:** Ijarachi sifatida men saqlangan uy yoki filtrim bo'yicha narx tushganda va yangi e'lon chiqqanda xabar olishni xohlayman, shunda qulay imkoniyatni o'tkazib yubormayman.

**Tavsif:** Ikki yangi bildirishnoma turi: "Narxi tushdi" (saqlangan e'lon/filter) va "Yangi e'lonlar" (saqlangan filter). FCM push + tizim ichi. N1 sozlamalarida boshqariladi.

**Qabul mezonlari:**
- GIVEN ijarachi e'lonni saqlagan WHEN narx belgilangan foizdan ko'p tushsa THEN push va tizim ichi bildirishnoma
- GIVEN saqlangan filter mavjud WHEN unga mos yangi e'lon moderatsiyadan o'tsa THEN push
- GIVEN N1 sozlamalarida tur o'chirilgan WHEN hodisa yuz bersa THEN push kelmaydi, faqat tizim ichi xabar
