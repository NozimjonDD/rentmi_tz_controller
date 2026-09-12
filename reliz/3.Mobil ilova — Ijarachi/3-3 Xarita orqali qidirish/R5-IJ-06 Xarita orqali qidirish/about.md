> Manba: [Release 5 17.08.2026 · R5 User storylar: Ijarachi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843840)
>
> Reliz rejasida ([Release 5 17.08.2026 · 3.1. Mobil ilova — Ijarachi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843819)): Xarita orqali qidirish: pinlar, xarita ustidagi chips (xona soni, Mebelli), "Ro'yhat bo'yicha" toggle, "N ta e'lon topildi" bottom sheet, saralash, banner-kirish · Guruh: Qidiruv va filter · Manba: 9, 12-task

# R5-IJ-06 — Xarita orqali qidirish

**User Story:** Ijarachi sifatida men e'lonlarni xaritada ko'rishni xohlayman, shunda menga qulay joylashuvdagi uylarni tez topa olaman.

**Tavsif:** Xarita ekrani: e'lon pinlari va klasterlar, xarita ustidagi chips (xona soni, Mebelli), "Ro'yhat bo'yicha" toggle, pastda "N ta e'lon topildi" bottom sheet, saralash. Asosiy sahifadagi banner orqali kirish.

**Qabul mezonlari:**

* GIVEN xarita ochilgan WHEN chips tanlansa THEN pinlar va bottom sheet ro'yxati filtrlanadi
* GIVEN pin bosildi WHEN e'lon kartasi ochilsa THEN karta badge'lar va asosiy parametrlar bilan ko'rinadi
* GIVEN "Ro'yhat bo'yicha" bosildi WHEN rejim almashsa THEN ro'yxat ko'rinishiga o'tadi va xaritaga qaytish mumkin
* GIVEN xarita yuklanmoqda WHEN 5 soniyadan oshsa THEN xatolik/retry holati ko'rsatiladi
