> Manba: [Release 5 17.08.2026 · R5 User storylar: Admin](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43712577)
>
> Reliz rejasida ([Release 5 17.08.2026 · 3.3. Admin panel](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843819)): SLA monitoring: muddati o'tgan (ko'rib chiqilmagan) so'rovlar ro'yxati va statistikasi · Guruh: So'rovlar monitoring · Manba: 6-task

# R5-AD-02 — SLA monitoring

**User Story:** Administrator sifatida men muddati o'tgan so'rovlar va uy egalarining javob berish intizomini kuzatishni xohlayman, shunda platforma xizmat sifatini nazorat qila olaman.

**Tavsif:** So'rovlar monitoring bo'limiga SLA ko'rinishi qo'shiladi: "ko'rib chiqilmagan" (muddati o'tgan) so'rovlar ro'yxati (ijarachi, uy egasi, e'lon, o'tgan vaqt), uy egasi kesimida o'rtacha/mediana javob vaqti hisoboti, davr bo'yicha filtrlash va eksport.

**Qabul mezonlari:**

* GIVEN muddati o'tgan so'rovlar mavjud WHEN SLA monitoring ochilsa THEN ro'yxat sana bo'yicha (eng eskisi birinchi) ko'rinadi
* GIVEN davr filtri qo'llandi WHEN hisobot yuklansa THEN faqat tanlangan davr so'rovlari va statistikasi ko'rinadi
* GIVEN uy egasi kesimi ochildi WHEN hisobot yuklansa THEN har uy egasi bo'yicha so'rovlar soni, javob berilganlar ulushi va mediana javob vaqti ko'rinadi
* GIVEN ro'yxat ko'rsatilgan WHEN so'rov satri bosilsa THEN so'rov tafsilotlari sahifasi (read-only) ochiladi
