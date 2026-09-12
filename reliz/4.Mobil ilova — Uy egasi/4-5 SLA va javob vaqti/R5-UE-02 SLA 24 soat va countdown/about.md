> Manba: [Release 5 17.08.2026 · R5 User storylar: Uy egasi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43712557)
>
> Reliz rejasida ([Release 5 17.08.2026 · 3.2. Mobil ilova — Uy egasi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843819)): SLA 24 soat: "Javob berishingiz kerak: HH:MM:SS" countdown, 7 soatdan kam qolganda qizil; "Diqqat talab qiladi" bloki; muddati o'tganda "ko'rib chiqilmagan" holati va ikki tomonga push · Guruh: So'rov boshqaruvi · Manba: 6-task; dizayn
>
> ❓ Qizil chegarasi: bu yerda 1 soat, R5 asosiy sahifasida 7 soat (N1) — [4-5 SLA va javob vaqti](<../about.md>).

# R5-UE-02 — SLA 24 soat va countdown

**User Story:** Uy egasi sifatida men har so'rovga javob berish uchun qancha vaqt qolganini ko'rishni xohlayman, shunda ijarachini kuttirib qo'ymayman.

**Tavsif:** Har yangi so'rovda "Javob berishingiz kerak: HH:MM:SS" countdown (deadline = so'rov vaqti + 24 soat); 1 soatdan kam qolganda qizil. Asosiy sahifada "Diqqat talab qiladi" bloki: javob kutayotgan arizalar soni va eng eskisiga qolgan vaqt. Muddati o'tsa so'rov "ko'rib chiqilmagan" holatiga o'tadi, ikki tomonga push. Eslatma pushlari 12- va 22-soatlarda. "Ko'rib chiqilmagan" yakuniy rad emas — keyin ham javob berish mumkin.

**Qabul mezonlari:**

* GIVEN yangi so'rov keldi WHEN karta ko'rsatilsa THEN countdown 24:00:00 dan boshlab kamayadi
* GIVEN qolgan vaqt 1 soatdan kam WHEN karta ko'rsatilsa THEN countdown qizil rangda ko'rinadi
* GIVEN 24 soat o'tdi va javob berilmadi WHEN scheduler ishga tushsa THEN so'rov "ko'rib chiqilmagan"ga o'tadi va ikkala tomonga push boradi
* GIVEN so'rov "ko'rib chiqilmagan" WHEN uy egasi qabul qilsa THEN so'rov "qabul qilindi"ga o'tadi va first_response_time yoziladi
* GIVEN javob kutayotgan so'rovlar bor WHEN uy egasi asosiy sahifani ochsa THEN "Diqqat talab qiladi" blokida soni va eng eskisiga qolgan vaqt ko'rinadi
