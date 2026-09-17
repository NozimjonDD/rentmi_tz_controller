> Manba: [Release 5 17.08.2026 · R5 User storylar: Uy egasi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43712557)
>
> Reliz rejasida ([Release 5 17.08.2026 · 3.2. Mobil ilova — Uy egasi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843819)): So'rovlar sahifasi yangilanishi: tablar, statistika mini-grafigi, ijarachi kartasida yangi maydonlar (kirish sanasi, byudjet, muddat, oila tarkibi), "Talablaringizga mos" badge · Guruh: So'rov boshqaruvi · Manba: 22-task; dizayn

# R5-UE-01 — So'rovlar sahifasi yangilanishi

**User Story:** Uy egasi sifatida men so'rovlarni ijarachining shartlari va mosligi bilan birga ko'rishni xohlayman, shunda tez va asosli qaror qabul qila olaman.

**Tavsif:** So'rovlar sahifasida tablar (Barchasi / Yangi / Rad etilgan / Tasdiqlangan), statistika mini-grafigi (jami so'rovlar, trend %). Ijarachi kartasi: Rentmi gauge (ball/100 + label), oila tarkibi chips, kirish sanasi / byudjet (max) / ijara muddati maydonlari, "Talablaringizga mos" badge, Qabul qilish / Rad qilish tugmalari.

**Qabul mezonlari:**

* GIVEN yangi so'rov keldi WHEN "Yangi so'rovlar" tabi ochilsa THEN kartada ijarachining kirish sanasi, byudjeti va muddati ko'rinadi
* GIVEN ijarachi e'lon talablariga mos WHEN karta ko'rsatilsa THEN "Talablaringizga mos" badge ko'rinadi
* GIVEN sahifa ochildi WHEN statistika bloki yuklansa THEN jami so'rovlar soni va trend grafigi ko'rinadi
* GIVEN "Qabul qilish" bosildi WHEN tasdiq modali yopilsa THEN ijarachiga kontakt ochiladi va so'rov "Tasdiqlangan" tabiga o'tadi
