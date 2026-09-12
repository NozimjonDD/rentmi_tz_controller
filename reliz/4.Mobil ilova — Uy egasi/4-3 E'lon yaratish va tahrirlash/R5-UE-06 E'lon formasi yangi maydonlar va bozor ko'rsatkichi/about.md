> Manba: [Release 5 17.08.2026 · R5 User storylar: Uy egasi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43712557)
>
> Reliz rejasida ([Release 5 17.08.2026 · 3.2. Mobil ilova — Uy egasi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843819)): E'lon yaratish/tahrirlashda yangi maydonlar: minimal ijara davri, kirish sanasi, minimal skoring talabi; ijarachi skoring qismidagi tekstni olib tashlash; shu hududdagi o'xshash e'lonlar narxi min/max · Guruh: E'lon boshqaruvi · Manba: 21, 23-task; dizayn

# R5-UE-06 — E'lon formasi yangi maydonlar va bozor ko'rsatkichi

**User Story:** Uy egasi sifatida men e'lonimda kirish sanasi, minimal ijara davri va skoring talabini belgilashni, hamda shu hududdagi o'xshash e'lonlar narxini ko'rishni xohlayman, shunda to'g'ri narx qo'yaman va mos ijarachilarni olaman.

**Tavsif:** E'lon yaratish/tahrirlash formasiga maydonlar: minimal ijara davri, kirish sanasi, minimal skoring talabi. Ijarachi skoring qismidagi eski tushuntirish teksti olib tashlanadi. Narx maydonida shu hudud bo'yicha o'xshash faol e'lonlar narxi min–max ko'rsatiladi.

**Qabul mezonlari:**

* GIVEN forma ochildi WHEN hudud va parametrlar kiritilsa THEN "Shu hududda o'xshash uylar: N mln – M mln so'm" ko'rsatkichi chiqadi
* GIVEN o'xshash e'lonlar 3 tadan kam WHEN ko'rsatkich hisoblansa THEN diapazon ko'rsatilmaydi (chalg'itmaslik uchun)
* GIVEN minimal skoring talabi belgilangan WHEN e'lon saqlansa THEN "Sizga mos" va skoring-mos hisob-kitoblarida shu talab ishlatiladi
* GIVEN forma ochildi WHEN skoring bo'limi ko'rsatilsa THEN eski ijarachi-skoring teksti mavjud emas
