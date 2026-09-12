> Manba: [Release 5 17.08.2026 · R5 User storylar: Ijarachi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843840)
>
> Reliz rejasida ([Release 5 17.08.2026 · 3.1. Mobil ilova — Ijarachi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843819)): Bildirishnomalar: saqlangan filter/e'lon bo'yicha "Narxi tushdi" va "Yangi e'lonlar" · Guruh: Bildirishnomalar · Manba: 10-task

# R5-IJ-11 — Narx va yangi e'lon bildirishnomalari

**User Story:** Ijarachi sifatida men saqlangan uy yoki filtrim bo'yicha narx tushganda va yangi e'lon chiqqanda xabar olishni xohlayman, shunda qulay imkoniyatni o'tkazib yubormayman.

**Tavsif:** Ikki yangi bildirishnoma turi: "Narxi tushdi" (saqlangan e'lon/filter bo'yicha) va "Yangi e'lonlar" (saqlangan filter bo'yicha). FCM push + tizim ichi. N1 sozlamalarida boshqariladi.

**Qabul mezonlari:**

* GIVEN ijarachi e'lonni saqlagan WHEN e'lon narxi belgilangan foizdan ko'p tushsa THEN push va tizim ichi bildirishnoma keladi
* GIVEN saqlangan filter mavjud WHEN unga mos yangi e'lon moderatsiyadan o'tsa THEN push keladi
* GIVEN N1 sozlamalarida tur o'chirilgan WHEN hodisa yuz bersa THEN push kelmaydi, faqat tizim ichi xabar ko'rinadi
