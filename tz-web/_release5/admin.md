# R5 User storylar — Admin (🛡)

Release 5 ning admin panel bo'yicha to'liq user-storylari (manba: `R5 User storylar Admin.pdf`). Web (VueJS) kodbaza yo'q → **kod holati spec-only** (implementatsiya noma'lum).

---

## R5-AD-01 — Algoritm parametrlari sozlamalari
**Flow:** [03-administratorlik](../03-administratorlik/about.md) · [05-integratsiya](../05-integratsiya/about.md) · **Kod holati:** spec (web kod yo'q)

**User Story:** Administrator sifatida men badge va tavsiya algoritmlarining parametrlarini sozlashni xohlayman, shunda kod o'zgartirmasdan platforma xatti-harakatini boshqara olaman.

**Tavsif:** R3 dagi algoritm sozlamalari moduli kengaytiriladi: **Top og'irliklari** (w1, w2, w3, oyna, yangilik bonusi, hudud darajasi), **"Rentmi Maslahat beradi"** mezon ballari, **"Sizga mos"** moslik mezonlari va qidiruv tarixi oynasi, **"Narxi tushdi"** foiz chegarasi va oynalari, **SLA muddati (soat)** va ogohlantirish chegarasi, **javob vaqti indikatori** parametrlari (oyna, minimal javoblar soni). Har o'zgarish audit jurnalida qayd etiladi.

**Qabul mezonlari:**
- GIVEN administrator sozlamalar sahifasida WHEN Top og'irligi o'zgartirilib saqlansa THEN keyingi qayta hisoblashda yangi og'irlik qo'llanadi
- GIVEN SLA muddati 24 dan boshqa qiymatga o'zgartirildi WHEN yangi so'rov kelsa THEN countdown yangi muddat bilan boshlanadi (mavjud so'rovlar deadline'i o'zgarmaydi)
- GIVEN parametr o'zgartirildi WHEN audit jurnali ochilsa THEN o'zgarish sanasi, mas'ul va eski/yangi qiymat ko'rinadi
- GIVEN noto'g'ri qiymat (manfiy foiz) WHEN saqlash bosilsa THEN validatsiya xatosi, qiymat saqlanmaydi

---

## R5-AD-02 — SLA monitoring
**Flow:** [06-support-callmarkaz](../06-support-callmarkaz/about.md) · **Kod holati:** spec (web kod yo'q)

**User Story:** Administrator sifatida men muddati o'tgan so'rovlar va uy egalarining javob berish intizomini kuzatishni xohlayman, shunda platforma xizmat sifatini nazorat qila olaman.

**Tavsif:** So'rovlar monitoring bo'limiga SLA ko'rinishi qo'shiladi: **"ko'rib chiqilmagan" (muddati o'tgan) so'rovlar ro'yxati** (ijarachi, uy egasi, e'lon, o'tgan vaqt), **uy egasi kesimida o'rtacha/mediana javob vaqti** hisoboti, davr bo'yicha filtrlash va eksport.

**Qabul mezonlari:**
- GIVEN muddati o'tgan so'rovlar mavjud WHEN SLA monitoring ochilsa THEN ro'yxat sana bo'yicha (eng eskisi birinchi) ko'rinadi
- GIVEN davr filtri qo'llandi WHEN hisobot yuklansa THEN faqat tanlangan davr so'rovlari va statistikasi ko'rinadi
- GIVEN uy egasi kesimi ochildi WHEN hisobot yuklansa THEN har uy egasi bo'yicha so'rovlar soni, javob berilganlar ulushi va mediana javob vaqti ko'rinadi
- GIVEN ro'yxat ko'rsatilgan WHEN so'rov satri bosilsa THEN so'rov tafsilotlari sahifasi (readonly) ochiladi

---

> **Bog'liqlik:** R5-AD-01 dagi SLA muddati (24 soat) va javob vaqti parametrlari — mobil tomondagi R5-UE-02/UE-03 ni boshqaradi ([`../../tz-mobile/_release5/uy-egasi.md`](../../tz-mobile/_release5/uy-egasi.md)). R5-AD-02 monitoring esa o'sha so'rovlar SLA'sini kuzatadi.
