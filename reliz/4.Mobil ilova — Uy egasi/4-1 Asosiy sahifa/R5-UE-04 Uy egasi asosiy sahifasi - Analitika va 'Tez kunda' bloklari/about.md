> Manba: [Release 5 17.08.2026 · R5 User storylar: Uy egasi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43712557)
>
> Reliz rejasida ([Release 5 17.08.2026 · 3.2. Mobil ilova — Uy egasi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843819)): Uy egasi asosiy sahifasi: Analitika (7/30 kun: Ko'rishlar, So'rovlar, Yoqtirishlar, Qo'ng'iroqlar); Daromadlarim va Xizmatlar bloklari — soddalashtirilgan, raqamlar o'rnida "Tez kunda" · Guruh: Statistika · Manba: 20-task; dizayn

# R5-UE-04 — Uy egasi asosiy sahifasi: Analitika va "Tez kunda" bloklari

**User Story:** Uy egasi sifatida men mulklarim bo'yicha faollik ko'rsatkichlarini bir ekranda ko'rishni xohlayman, shunda e'lonlarim samarasini baholay olaman.

**Tavsif:** Analitika bloki: 7 kun / 30 kun switch; Ko'rishlar, So'rovlar, Yoqtirishlar, Qo'ng'iroqlar counterlari (o'zgarish belgisi bilan). Daromadlarim va Xizmatlar bloklari UI to'liq quriladi, lekin raqamlar/kontent o'rnida "Tez kunda" ko'rsatiladi (2–3-bosqich funksionaliga tayyorgarlik).

**Qabul mezonlari:**

* GIVEN uy egasi asosiy sahifada WHEN "7 kun" tanlansa THEN barcha counterlar 7 kunlik davr bo'yicha yangilanadi
* GIVEN davr almashtirildi WHEN "30 kun" tanlansa THEN counterlar 30 kunlik davrga o'tadi
* GIVEN Daromadlarim bloki ko'rsatilgan WHEN sahifa yuklansa THEN raqamlar o'rnida "Tez kunda" matni ko'rinadi, blok bosilganda ham to'lov funksionali ochilmaydi
* GIVEN Xizmatlar bloki ko'rsatilgan WHEN sahifa yuklansa THEN kontent o'rnida "Tez kunda" ko'rinadi
