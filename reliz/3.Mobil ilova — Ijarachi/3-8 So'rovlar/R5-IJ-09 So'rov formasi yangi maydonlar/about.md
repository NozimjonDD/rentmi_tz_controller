> Manba: [Release 5 17.08.2026 · R5 User storylar: Ijarachi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843840)
>
> Reliz rejasida ([Release 5 17.08.2026 · 3.1. Mobil ilova — Ijarachi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843819)): So'rov formasi yangi maydonlar: kirish sanasi, byudjet (max), ijara muddati, to'lov kuni · Guruh: So'rov · Manba: 19-task; dizayn

# R5-IJ-09 — So'rov formasi yangi maydonlar

**User Story:** Ijarachi sifatida men so'rovda kirish sanasi, byudjet va muddatni ko'rsatishni xohlayman, shunda uy egasi mening shartlarimni oldindan bilib qaror qabul qiladi.

**Tavsif:** So'rov formasiga maydonlar qo'shiladi: kirish sanasi, byudjet (max), ijara muddati, to'lov kuni. Bu ma'lumotlar uy egasining ijarachi kartasida ko'rsatiladi.

**Qabul mezonlari:**

* GIVEN forma ochildi WHEN maydonlar to'ldirilmasa THEN majburiy maydonlar bo'yicha validatsiya xabari chiqadi
* GIVEN forma to'ldirildi WHEN so'rov yuborilsa THEN uy egasi kartasida kirish sanasi / byudjet / muddat ko'rinadi
* GIVEN Rentmi bali yo'q WHEN so'rov yuborilmoqchi bo'lsa THEN S1 (hisobot xarid qilish) taklif etiladi (TZ R1)
