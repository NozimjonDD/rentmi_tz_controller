> Manba: [Release 5 17.08.2026 · R5 User storylar: Ijarachi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843840)
>
> Reliz rejasida ([Release 5 17.08.2026 · 3.1. Mobil ilova — Ijarachi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843819)): Yangilangan asosiy sahifa: salomlashish header, bo'limlar (TOP kvartiralar / Kvartiralar / Rentmi Maslahat beradi / Villa, "Hammasi >"), xona soni chips, chat tugmasi tepada, yangi navbar (Main, Saved, Lenta, So'rovlar, Profil) · Guruh: Asosiy sahifa · Manba: Dizayn; 8, 11-task

# R5-IJ-01 — Yangilangan asosiy sahifa

**User Story:** Ijarachi sifatida men yangilangan asosiy sahifada kerakli bo'limlarga tez o'tishni xohlayman, shunda uy qidirishni bir ekrandan boshlay olaman.

**Tavsif:** Asosiy sahifa yangi dizaynda quriladi: salomlashish headeri, tepada chat va bildirishnoma tugmalari, "Toshkentda uy qidiramizmi?" klikabel shahar tanlovi, xona soni chips filtri, bo'limlar (TOP kvartiralar / Kvartiralar / Rentmi Maslahat beradi / Villa) va "Xarita orqali qidirish" banneri. Pastki navbar: Main, Saved, Lenta, So'rovlar, Profil. Actual History stories yashirin qoladi.

**Qabul mezonlari:**

* GIVEN ijarachi tizimga kirgan WHEN asosiy sahifa ochilsa THEN header, chips, barcha bo'limlar va yangi navbar 3 soniya ichida yuklanadi
* GIVEN shahar nomi ko'rsatilgan WHEN ijarachi "Toshkentda" so'zini bossa THEN shahar/hudud tanlash oynasi ochiladi va tanlov barcha bo'limlarga qo'llanadi
* GIVEN xona chips'lari ko'rsatilgan WHEN "2 xona" tanlansa THEN bo'limlardagi e'lonlar 2 xonalilarga filtrlanadi
* GIVEN bo'lim mavjud WHEN "Hammasi >" bosilsa THEN shu bo'limning to'liq ro'yxat sahifasi ochiladi
* GIVEN yangi navbar ko'rsatilgan WHEN "Lenta" bosilsa THEN e'lonlar lentasi ochiladi (yangi sahifa emas)
