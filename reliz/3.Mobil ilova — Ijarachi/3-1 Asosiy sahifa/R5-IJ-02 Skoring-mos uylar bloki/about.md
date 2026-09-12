> Manba: [Release 5 17.08.2026 · R5 User storylar: Ijarachi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843840)
>
> Reliz rejasida ([Release 5 17.08.2026 · 3.1. Mobil ilova — Ijarachi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843819)): Skoring-mos uylar bloki: gauge, "Skoringizga mos N ta uy", alohida ro'yxat sahifasi · Guruh: Asosiy sahifa · Manba: Dizayn (F-D1)

# R5-IJ-02 — Skoring-mos uylar bloki

**User Story:** Ijarachi sifatida men skoring balimga mos uylar sonini ko'rishni xohlayman, shunda arizam qabul qilinish ehtimoli yuqori uylarga e'tibor qarata olaman.

**Tavsif:** Asosiy sahifada gauge (ball), "Skoringizga mos N ta uy" matni va "Arizalaringiz ustuvor ko'rib chiqiladi" izohi ko'rsatiladi. Bosilganda mos uylar ro'yxati ochiladi. Moslik: ijarachi bali ≥ e'lonning minimal skoring talabi. Soni soatlik keshda yangilanadi.

**Qabul mezonlari:**

* GIVEN ijarachi skoringdan o'tgan WHEN asosiy sahifa ochilsa THEN blokda joriy bal va mos uylar soni ko'rinadi
* GIVEN ijarachi skoringdan o'tmagan WHEN asosiy sahifa ochilsa THEN blok "Skoringdan o'ting" CTA bilan ko'rinadi (S1 ga yo'naltiradi)
* GIVEN blok ko'rsatilgan WHEN u bosilsa THEN faqat mos e'lonlardan iborat ro'yxat sahifasi ochiladi
* GIVEN mos uy yo'q WHEN blok ochilsa THEN "Hozircha mos uy topilmadi" holati ko'rsatiladi
