> Manba: [Release 5 17.08.2026 · R5 User storylar: Ijarachi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843840)
>
> Reliz rejasida ([Release 5 17.08.2026 · 3.1. Mobil ilova — Ijarachi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843819)): Filter yangilanishi: narxni mln so'm / 100$ ga yaxlitlash, so'm/dollar toggle, filterni saqlash va tozalash · Guruh: Qidiruv va filter · Manba: 1, 27-task

# R5-IJ-04 — Filter yangilanishi

**User Story:** Ijarachi sifatida men narx filtrini qulay qadamlar bilan sozlashni xohlayman, shunda keraksiz aniq raqamlar bilan ovora bo'lmayman.

**Tavsif:** Narx maydonlari va slider so'mda mln qadamga, dollarda 100$ qadamga yaxlitlanadi; so'm/dollar toggle. "Filterni saqlash" va "Filterni tozalash" tugmalari. Saqlangan filtrlar mantig'i qayta ko'rib chiqiladi.

**Qabul mezonlari:**

* GIVEN valyuta so'm WHEN slider surilsa THEN qiymat mln qadam bilan o'zgaradi (masalan 5 000 000 → 6 000 000)
* GIVEN valyuta dollar WHEN slider surilsa THEN qiymat 100$ qadam bilan o'zgaradi
* GIVEN filter to'ldirilgan WHEN "Filterni saqlash" bosilsa THEN filter Saqlanganlar sahifasida paydo bo'ladi
* GIVEN filter to'ldirilgan WHEN "Filterni tozalash" bosilsa THEN barcha maydonlar default holatga qaytadi
