> Manba: [Release 5 17.08.2026 · R5 User storylar: Admin](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43712577)
>
> Reliz rejasida ([Release 5 17.08.2026 · 3.3. Admin panel](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843819)): Algoritm parametrlari sozlamalari: Top og'irliklari, Sizga mos/tavsiya ballari, "Narxi tushdi" foiz chegarasi, SLA muddati · Guruh: Algoritm sozlamalari · Manba: R3 moduli kengaytmasi

# R5-AD-01 — Algoritm parametrlari sozlamalari

**User Story:** Administrator sifatida men badge va tavsiya algoritmlarining parametrlarini sozlashni xohlayman, shunda kod o'zgartirmasdan platforma xatti-harakatini boshqara olaman.

**Tavsif:** R3 dagi algoritm sozlamalari moduli kengaytiriladi: Top og'irliklari (w1, w2, w3, oyna, yangilik bonusi, hudud darajasi), "Rentmi Maslahat beradi" mezon ballari, "Sizga mos" moslik mezonlari va qidiruv tarixi oynasi, "Narxi tushdi" foiz chegarasi va oynalari, SLA muddati (soat) va ogohlantirish chegarasi, javob vaqti indikatori parametrlari (oyna, minimal javoblar soni). Har o'zgarish audit jurnalida qayd etiladi.

**Qabul mezonlari:**

* GIVEN administrator sozlamalar sahifasida WHEN Top og'irligi o'zgartirilib saqlansa THEN keyingi qayta hisoblashda yangi og'irlik qo'llanadi
* GIVEN SLA muddati 24 dan boshqa qiymatga o'zgartirildi WHEN yangi so'rov kelsa THEN countdown yangi muddat bilan boshlanadi (mavjud so'rovlarning deadline'i o'zgarmaydi)
* GIVEN parametr o'zgartirildi WHEN audit jurnali ochilsa THEN o'zgarish sanasi, mas'ul va eski/yangi qiymat ko'rinadi
* GIVEN noto'g'ri qiymat kiritildi (masalan manfiy foiz) WHEN saqlash bosilsa THEN validatsiya xatosi ko'rsatiladi va qiymat saqlanmaydi
