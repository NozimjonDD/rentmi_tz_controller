# R5 User storylar — Uy egasi (🏠)

Release 5 ning uy egasi bo'yicha to'liq user-storylari (manba: `R5 User storylar Uy egasi.pdf`). Flow + kod holati bilan. Belgilar: ✅ · 🟡 · ❌.

---

## R5-UE-01 — So'rovlar sahifasi yangilanishi
**Flow:** [07-sorovlar/landlord/korib-chiqish](../07-sorovlar/landlord/korib-chiqish.md) · **Kod holati:** 🟡 (ijarachi kartasidagi strukturalangan maydonlar to'liq emas — K4 ga bog'liq)

**User Story:** Uy egasi sifatida men so'rovlarni ijarachining shartlari va mosligi bilan birga ko'rishni xohlayman, shunda tez va asosli qaror qabul qila olaman.

**Tavsif:** So'rovlar sahifasida tablar (Barchasi / Yangi / Rad etilgan / Tasdiqlangan), statistika minigrafigi (jami so'rovlar, trend %). Ijarachi kartasi: Rentmi gauge (ball/100 + label), oila tarkibi chips, kirish sanasi / byudjet (max) / ijara muddati maydonlari, "Talablaringizga mos" badge, Qabul qilish / Rad qilish tugmalari.

**Qabul mezonlari:**
- GIVEN yangi so'rov keldi WHEN "Yangi so'rovlar" tabi ochilsa THEN kartada ijarachining kirish sanasi, byudjeti va muddati ko'rinadi
- GIVEN ijarachi e'lon talablariga mos WHEN karta ko'rsatilsa THEN "Talablaringizga mos" badge ko'rinadi
- GIVEN sahifa ochildi WHEN statistika bloki yuklansa THEN jami so'rovlar soni va trend grafigi ko'rinadi
- GIVEN "Qabul qilish" bosildi WHEN tasdiq modali yopilsa THEN ijarachiga kontakt ochiladi va so'rov "Tasdiqlangan" tabiga o'tadi

---

## R5-UE-02 — SLA 24 soat va countdown
**Flow:** [07-sorovlar/landlord/sla-va-statistika](../07-sorovlar/landlord/sla-va-statistika.md) · **Kod holati:** ❌ (24h countdown kodda yo'q — K3/C3)

**User Story:** Uy egasi sifatida men har so'rovga javob berish uchun qancha vaqt qolganini ko'rishni xohlayman, shunda ijarachini kuttirib qo'ymayman.

**Tavsif:** Har yangi so'rovda "Javob berishingiz kerak: HH:MM:SS" countdown (deadline = so'rov vaqti + 24 soat); **1 soatdan kam qolganda qizil**. Asosiy sahifada "Diqqat talab qiladi" bloki: javob kutayotgan arizalar soni va eng eskisiga qolgan vaqt. Muddati o'tsa so'rov "ko'rib chiqilmagan"ga o'tadi, ikki tomonga push. Eslatma pushlari 12- va 22-soatlarda. "Ko'rib chiqilmagan" yakuniy rad emas — keyin ham javob berish mumkin.

> ⚠ **R5 ichida ziddiyat:** bu batafsil story «**1 soatdan** kam qolganda qizil» deydi; `Release 5 17.08.2026.pdf` xulosasi esa «**7 soatdan** kam qolganda qizil». → [`about.md`](about.md), [`_konfliktlar.md`](../_konfliktlar.md).

**Qabul mezonlari:**
- GIVEN yangi so'rov keldi WHEN karta ko'rsatilsa THEN countdown 24:00:00 dan boshlab kamayadi
- GIVEN qolgan vaqt 1 soatdan kam WHEN karta ko'rsatilsa THEN countdown qizil rangda
- GIVEN 24 soat o'tdi va javob berilmadi WHEN scheduler ishga tushsa THEN so'rov "ko'rib chiqilmagan"ga o'tadi va ikkala tomonga push
- GIVEN so'rov "ko'rib chiqilmagan" WHEN uy egasi qabul qilsa THEN "qabul qilindi"ga o'tadi va first_response_time yoziladi
- GIVEN javob kutayotgan so'rovlar bor WHEN uy egasi asosiy sahifani ochsa THEN "Diqqat talab qiladi" blokida soni va eng eskisiga qolgan vaqt ko'rinadi

---

## R5-UE-03 — Javob vaqti indikatori
**Flow:** [07-sorovlar/landlord](../07-sorovlar/landlord/about.md) · [06-elonlar/tenant/uy-egasi-profil](../06-elonlar/tenant/uy-egasi-profil.md) · **Kod holati:** ❌ (first_response_time / indikator kodda yo'q)

**User Story:** Uy egasi sifatida men tez javob berishim ijarachilarga ko'rinishini xohlayman, shunda e'lonlarim ko'proq ariza oladi.

**Tavsif:** Har so'rov bo'yicha first_response_time yoziladi. Ko'rsatkich — oxirgi 30 kun medianasi, soatlik pog'onaga yaxlitlanadi ("odatda 1 soat ichida javob beradi"...). Kamida 3 ta javob bo'lsagina e'lon sahifasida va ommaviy profilda chiqadi. Uy egasiga onboarding tooltip orqali tushuntiriladi.

**Qabul mezonlari:**
- GIVEN uy egasida kamida 3 ta javob yozuvi bor WHEN e'lon yoki profil ochilsa THEN indikator mediana asosida ko'rinadi
- GIVEN javoblar 3 tadan kam WHEN sahifa ochilsa THEN indikator ko'rsatilmaydi
- GIVEN bitta so'rovga juda kech javob berilgan WHEN mediana hisoblansa THEN bitta chetlanish ko'rsatkichni keskin buzmaydi (mediana, o'rtacha emas)
- GIVEN uy egasi birinchi marta So'rovlar sahifasini ochdi WHEN sahifa yuklansa THEN tez javob foydasi haqida tooltip ko'rsatiladi

---

## R5-UE-04 — Asosiy sahifa: Analitika va "Tez kunda" bloklari
**Flow:** [06-elonlar/landlord/statistika](../06-elonlar/landlord/statistika.md) · **Kod holati:** 🟡 (analitika qisman/mock; "Tez kunda" placeholder'lar bor)

**User Story:** Uy egasi sifatida men mulklarim bo'yicha faollik ko'rsatkichlarini bir ekranda ko'rishni xohlayman, shunda e'lonlarim samarasini baholay olaman.

**Tavsif:** Analitika bloki: 7 kun / 30 kun switch; Ko'rishlar, So'rovlar, Yoqtirishlar, Qo'ng'iroqlar counterlari (o'zgarish belgisi bilan). Daromadlarim va Xizmatlar bloklari UI to'liq quriladi, lekin raqamlar/kontent o'rnida "Tez kunda" (2–3-bosqichga tayyorgarlik).

**Qabul mezonlari:**
- GIVEN uy egasi asosiy sahifada WHEN "7 kun" tanlansa THEN barcha counterlar 7 kunlik davr bo'yicha yangilanadi
- GIVEN davr almashtirildi WHEN "30 kun" tanlansa THEN counterlar 30 kunlik davrga o'tadi
- GIVEN Daromadlarim bloki WHEN sahifa yuklansa THEN raqamlar o'rnida "Tez kunda", blok bosilganda ham to'lov funksionali ochilmaydi
- GIVEN Xizmatlar bloki WHEN sahifa yuklansa THEN kontent o'rnida "Tez kunda"

---

## R5-UE-05 — "Mulklarim" statuslari
**Flow:** [06-elonlar/landlord/mulklarim](../06-elonlar/landlord/mulklarim.md) · **Kod holati:** 🟡 (kod statuslari R5 ga to'liq mos emas — E-K10)

**User Story:** Uy egasi sifatida men mulklarimni holati bo'yicha ajratib ko'rishni xohlayman, shunda qaysi uy bo'sh, qaysi ijarada ekanini bir qarashda bilaman.

**Tavsif:** "Mulklarim" bo'limiga qoralama / ijarada / bo'sh statuslari qo'shiladi (mavjud faol / moderatsiyada / rad etilgan / arxiv badge'lariga qo'shimcha). Uy egasi statusni qo'lda o'zgartira oladi.

**Qabul mezonlari:**
- GIVEN e'lon yaratish yakunlanmagan WHEN "Mulklarim" ochilsa THEN e'lon "qoralama" statusida ko'rinadi va tahrirlashni davom ettirish mumkin
- GIVEN uy egasi so'rovni qabul qilib ijaraga berdi WHEN statusni "ijarada"ga o'zgartirsa THEN e'lon katalogda ko'rinmaydi
- GIVEN "ijarada" WHEN "bo'sh"ga o'zgartirilsa THEN e'lon qayta faollashadi (moderatsiya holati saqlangan bo'lsa qayta moderatsiyasiz)

---

## R5-UE-06 — E'lon formasi yangi maydonlar va bozor ko'rsatkichi
**Flow:** [06-elonlar/landlord/elon-yaratish](../06-elonlar/landlord/elon-yaratish.md) · **Kod holati:** 🟡 (ba'zi maydonlar bor)

**User Story:** Uy egasi sifatida men e'lonimda kirish sanasi, minimal ijara davri va skoring talabini belgilashni, hamda shu hududdagi o'xshash e'lonlar narxini ko'rishni xohlayman, shunda to'g'ri narx qo'yaman va mos ijarachilarni olaman.

**Tavsif:** E'lon formasiga maydonlar: minimal ijara davri, kirish sanasi, minimal skoring talabi. Ijarachi skoring qismidagi eski tushuntirish teksti olib tashlanadi. Narx maydonida shu hudud bo'yicha o'xshash faol e'lonlar narxi min–max ko'rsatiladi.

**Qabul mezonlari:**
- GIVEN forma ochildi WHEN hudud va parametrlar kiritilsa THEN "Shu hududda o'xshash uylar: N mln – M mln so'm" ko'rsatkichi chiqadi
- GIVEN o'xshash e'lonlar 3 tadan kam WHEN ko'rsatkich hisoblansa THEN diapazon ko'rsatilmaydi
- GIVEN minimal skoring talabi belgilangan WHEN e'lon saqlansa THEN "Sizga mos" va skoring-mos hisob-kitoblarda shu talab ishlatiladi
- GIVEN forma ochildi WHEN skoring bo'limi ko'rsatilsa THEN eski ijarachi-skoring teksti mavjud emas
