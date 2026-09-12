# Relizlar — joriy holat

Bu papka Rentmi mahsulot relizlari (Release 1–5) bo'yicha **hozirgi, oxirgi holatni** saqlaydi. Tarix papkalarda emas, git branch'larda: `release-1` — shu holat. Keyingi reliz o'zgarishlari `release-2` da qilinadi va `git diff release-1 release-2` da ko'rinadi.

## Manbalar

| Reliz | Sana | Asosiy sahifa | Use case / user story sahifalari |
| --- | --- | --- | --- |
| Release 1 | 23.05.2026 | [Release 1: 23.05.2026 (Confluence)](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/21823494) | US 1–6 (6 ta sahifa) |
| Release 2 | 01.06.2026 | [Release 2 01.06.2026 (Confluence)](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/25493506) | Use cases: Landlord, Ue cases: Admin |
| Release 3 | 07.06.2026 | [Release 3 07.06.2026 (Confluence)](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/27721729) | Mobile use cases, Admin use cases |
| Release 4 | 14.06.2026 | [Release 4 14.06.2026 (Confluence)](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29425665) | Ijarachi use caselari, Uy egasi, Admin |
| Release 5 | 17.08.2026 | [Release 5 17.08.2026 (Confluence)](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843819) | R5 User storylar: Ijarachi / Uy egasi / Admin; PDF: `doc_files/Release 5 17.08.2026.pdf` |

## Qoidalar

- Har bir talab relizdan **so'zma-so'z** olingan; oxirida manba belgisi: `R3` — reliz sahifasi, `R4 · IJ-R1 BQ-3` — use case va uning bandi.
- Keyingi reliz avvalgi talabni o'zgartirgan bo'lsa — **eng oxirgisi** olinadi, eskisi ostida ko'rsatiladi:
  > ⚠ Konflikt: R4 da — *eski matn*
- Bitta reliz ichida bir-biriga zid gaplar bo'lsa:
  > ❓ Ichki nomuvofiqlik: R4 da — *zid matn*
- `Izoh:` bilan boshlangan qatorlar — tushuntirish, relizda yo'q.
- Zid bo'lmagan (qo'shimcha) talablar hammasi saqlanadi.
- Use case'lar tegishli funksiya papkasida alohida papkada, relizdagi matni o'zgartirilmagan. Boshida manba va, agar bo'lsa, keyingi relizdagi o'zgarish izohi turadi.
- Papka va fayl nomlarida reliz raqami yoki sanasi yo'q. Yangi reliz chiqsa, yangi papka ochilmaydi — shu fayllar yangilanadi va farq `git diff` da ko'rinadi.
- Oxirgi reliz sahifasining funksional bo'limlari (Foydalanuvchilar, Use Cases, Bajariladi, Algoritmlar) 1–8-modullarga birlashtirilgan. Sahifaning har bir qismi qayerga tushgani [9.Reliz rejasi](<9.Reliz rejasi/about.md>) dagi jadvalda.
- Reliz boshqaruvi bo'limlari (Maqsad, Muddat, Prioritetlar, Reliz tayyorligi, Bog'liqliklar, Risklar, QA, KPI) har relizda to'liq almashadi, shuning uchun birlashtirilmaydi: [9.Reliz rejasi](<9.Reliz rejasi/about.md>) da faqat oxirgi relizniki turadi. R1–R4 dagi bu bo'limlar (R3, R4 dagi "Foydalanuvchi tajribasi (Customer Experience)" ham) olinmagan.

## Tuzilma

| # | Modul | Funksiyalar |
| --- | --- | --- |
| 1 | [1.Foydalanuvchilar](<1.Foydalanuvchilar/about.md>) | Rollar va platformalar |
| 2 | [2.Mobil ilova — Umumiy](<2.Mobil ilova — Umumiy/about.md>) | Splash, til, onboarding, kirish, MyID, skoring, profil |
| 3 | [3.Mobil ilova — Ijarachi](<3.Mobil ilova — Ijarachi/about.md>) | Asosiy sahifa, qidiruv, xarita, saqlanganlar, top/badge, e'lon detail, ommaviy profil, so'rovlar, chat, bildirishnomalar |
| 4 | [4.Mobil ilova — Uy egasi](<4.Mobil ilova — Uy egasi/about.md>) | Asosiy sahifa, Mulklarim, e'lon formasi, so'rovlar boshqaruvi, SLA, statistika/AI, chat, bildirishnomalar |
| 5 | [5.Backend API](<5.Backend API/about.md>) | Endpointlar va servislar |
| 6 | [6.Admin panel](<6.Admin panel/about.md>) | Foydalanuvchilar, bloklashlar, dashboard, moderatsiya, stories, shikoyatlar, analitika, algoritm sozlamalari, so'rovlar monitoringi |
| 7 | [7.Algoritmlar](<7.Algoritmlar/about.md>) | 11 ta algoritm |
| 8 | [8.Nofunksional talablar va integratsiyalar](<8.Nofunksional talablar va integratsiyalar/about.md>) | Unumdorlik, integratsiyalar |
| 9 | [9.Reliz rejasi](<9.Reliz rejasi/about.md>) | Oxirgi relizning maqsadi, muddati, prioritetlari, tayyorlik kriteriyalari, bog'liqliklari, risklari, QA va KPI |

## Konfliktlar (eng oxirgisi olingan)

| # | Mavzu | Eski | Joriy | Qayerda |
| --- | --- | --- | --- | --- |
| K1 | So'rovni ko'rib chiqish muddati | R4: 7 kun | R5: 24 soat (SLA) | [4-5 SLA va javob vaqti](<4.Mobil ilova — Uy egasi/4-5 SLA va javob vaqti/about.md>), [5-5 So'rovlar va SLA](<5.Backend API/5-5 So'rovlar va SLA/about.md>), [6-9 So'rovlar monitoring va SLA](<6.Admin panel/6-9 So'rovlar monitoring va SLA/about.md>) |
| K2 | Muddat o'tganda push kimga | R4 · UE-R4, IJ-R2: faqat uy egasiga | R5: ikki tomonga | [4-5 SLA va javob vaqti](<4.Mobil ilova — Uy egasi/4-5 SLA va javob vaqti/about.md>) |
| K3 | So'rov statuslari nomlanishi | R4: qabul qilindi / qabul qilinmadi / tekshirish jarayonida | R5: ko'rilmoqda / kutilmoqda / qabul qilindi / rad etildi / bekor qilingan | [3-8 So'rovlar](<3.Mobil ilova — Ijarachi/3-8 So'rovlar/about.md>) |
| K4 | CTA nomi | R3, R4: So'rov jo'natish | R5: Ariza jo'natish | [3-6 E'lon detail sahifasi](<3.Mobil ilova — Ijarachi/3-6 E'lon detail sahifasi/about.md>) |
| K5 | "rezerv" atamasi | R2 · UE-04: "Rezervda" statusi | R5: "bron" | [4-2 Mulklarim](<4.Mobil ilova — Uy egasi/4-2 Mulklarim/about.md>) |
| K6 | Actual History stories | R3: asosiy sahifada ko'rsatiladi | R5: yashirin (kod saqlanadi) | [3-1 Asosiy sahifa](<3.Mobil ilova — Ijarachi/3-1 Asosiy sahifa/about.md>) |
| K7 | Asosiy sahifa header tugmalari | R3: bildirishnoma va sevimlilar | R5: chat va bildirishnoma; tepadagi profil olib tashlanadi | [3-1 Asosiy sahifa](<3.Mobil ilova — Ijarachi/3-1 Asosiy sahifa/about.md>) |
| K8 | Ijarachi chat joylashuvi | R4: pastki navbar tab | R5: tepada, bildirishnoma yonida | [3-1 Asosiy sahifa](<3.Mobil ilova — Ijarachi/3-1 Asosiy sahifa/about.md>), [3-9 Chat](<3.Mobil ilova — Ijarachi/3-9 Chat/about.md>) |
| K9 | Tavsiya algoritmi mezonlari | R3: skoring, qidiruv tarixi, sevimli kategoriyalar | R5: saqlangan filtr, hudud, narx, skoring, ko'rish tarixi (ball yig'indisi) | [7-4 Rentmi Maslahat beradi](<7.Algoritmlar/7-4 Rentmi Maslahat beradi/about.md>), [5-2 Top, tavsiya, badge va moslik](<5.Backend API/5-2 Top, tavsiya, badge va moslik/about.md>), [6-8 Algoritm sozlamalari](<6.Admin panel/6-8 Algoritm sozlamalari/about.md>), [3-5 Top, tavsiyalar va badge'lar](<3.Mobil ilova — Ijarachi/3-5 Top, tavsiyalar va badge'lar/about.md>) |
| K10 | Skoring amal qilish muddati | R1 · US 6: muddatsiz | R4 · IJ-R1: muddati o'tishi mumkin (muddat belgilanmagan) | [2-6 Skoring](<2.Mobil ilova — Umumiy/2-6 Skoring/about.md>) |
| K11 | So'rovlar monitoringida eksport | R4 · AD-R1: yo'q | R5 · R5-AD-02: SLA ko'rinishida bor | [6-9 So'rovlar monitoring va SLA](<6.Admin panel/6-9 So'rovlar monitoring va SLA/about.md>) |

## Ichki nomuvofiqliklar (bitta reliz ichida)

Bitta reliz ichidagi ziddiyatda keyinroq tahrirlangan Confluence sahifasi olindi. Ziddiyat bitta sahifaning o'zida bo'lsa — hal qilinmagan deb qoldirildi.

| # | Reliz | Mavzu | Holat | Qayerda |
| --- | --- | --- | --- | --- |
| N1 | R5 | SLA countdown qizil chegarasi: 7 soat (asosiy sahifa) — 1 soat (R5-UE-02) | Asosiy sahifa olindi (16.08 12:29 > 12:01) — **tasdiqlash kerak** | [4-5 SLA va javob vaqti](<4.Mobil ilova — Uy egasi/4-5 SLA va javob vaqti/about.md>), [7-7 SLA countdown](<7.Algoritmlar/7-7 SLA countdown/about.md>) |
| N2 | R4 | AI maslahat kartochkasi: shartli (asosiy sahifa) — doim (UE-S1) | UE-S1 olindi (14.06 12:28 > 11:04) | [4-6 Statistika va AI maslahat](<4.Mobil ilova — Uy egasi/4-6 Statistika va AI maslahat/about.md>) |
| N3 | R3 | Stories ko'rsatish muddati: bor (asosiy sahifa) — muddatsiz (AD-10/11/12) | Use case olindi (07.06 13:52 > 09:08) | [6-5 Actual History boshqaruvi](<6.Admin panel/6-5 Actual History boshqaruvi/about.md>) |
| N4 | R4 | Chat qachon ochiladi: faqat tasdiqlangandan keyin (IJ-C1 kirish sharti) — tasdiqlanmagan bo'lsa ham (IJ-C1 BQ-1, UE-C1 BQ-1, IJ-R1 BQ-7) | **Hal qilinmagan** | [3-9 Chat](<3.Mobil ilova — Ijarachi/3-9 Chat/about.md>) |
| N5 | R4 | Ruxsat toggle: majburiy (IJ-R1 3, 6-qadam) — yoqmasdan ham yuborish mumkin (IJ-R1 BQ-3, AC-2; UE-R3) | **Hal qilinmagan** | [3-8 So'rovlar](<3.Mobil ilova — Ijarachi/3-8 So'rovlar/about.md>) |
| N6 | R2 | Use case raqamlari: sarlavhalarda UE-01…UE-06, jadvallar ichida UE-04…UE-07 | **Hal qilinmagan** (raqamlash) | [4-2 Mulklarim](<4.Mobil ilova — Uy egasi/4-2 Mulklarim/about.md>) |
| N7 | R2 / R5 | "ijarada" (R5) va "Ijaraga berilgan" (R2) bitta statusmi | **Aniqlashtirish kerak** | [4-2 Mulklarim](<4.Mobil ilova — Uy egasi/4-2 Mulklarim/about.md>) |
