# R5-AD-01 — Algoritm parametrlari sozlamalari

**Rollar:** 🛡 Administrator    **Holat:** spec (web kod yo'q)    **Manba:** Release 5 (R5-AD-01)

## User Story
Administrator sifatida men badge va tavsiya algoritmlarining parametrlarini sozlashni xohlayman, shunda kod o'zgartirmasdan platforma xatti-harakatini boshqara olaman.

## Tavsif
R3 dagi algoritm sozlamalari moduli kengaytiriladi. Sozlanadigan parametrlar:
- **Top og'irliklari:** w1, w2, w3, oyna, yangilik bonusi, hudud darajasi
- **"Rentmi Maslahat beradi"** mezon ballari
- **"Sizga mos"** moslik mezonlari va qidiruv tarixi oynasi
- **"Narxi tushdi"** foiz chegarasi va oynalari
- **SLA muddati (soat)** va ogohlantirish chegarasi
- **Javob vaqti indikatori** parametrlari (oyna, minimal javoblar soni)

Har o'zgarish audit jurnalida qayd etiladi.

> **Bog'liqlik:** bu parametrlar **mobil** tarafdagi badge'lar (R5-IJ-03), skoring-mos uylar (R5-IJ-02), SLA countdown (R5-UE-02) va javob vaqti indikatorini (R5-UE-03) boshqaradi.

## Qabul mezonlari (BDD)
- **GIVEN** administrator sozlamalar sahifasida **WHEN** Top og'irligi o'zgartirilib saqlansa **THEN** keyingi qayta hisoblashda yangi og'irlik qo'llanadi
- **GIVEN** SLA muddati 24 dan boshqa qiymatga o'zgartirildi **WHEN** yangi so'rov kelsa **THEN** countdown yangi muddat bilan boshlanadi (mavjud so'rovlarning deadline'i o'zgarmaydi)
- **GIVEN** parametr o'zgartirildi **WHEN** audit jurnali ochilsa **THEN** o'zgarish sanasi, mas'ul va eski/yangi qiymat ko'rinadi
- **GIVEN** noto'g'ri qiymat kiritildi (manfiy foiz) **WHEN** saqlash bosilsa **THEN** validatsiya xatosi ko'rsatiladi va qiymat saqlanmaydi

## Backend / API (kutilayotgan)
Web kodbaza yo'q → taxminiy: `GET/PATCH /admin/settings/algorithm/`. Aniq yo'l web repo berilganda tasdiqlanadi (W-K1).

## Konflikt / farqlar
- Farq aniqlanmadi. R3 modulining kengaytmasi; audit majburiy.
