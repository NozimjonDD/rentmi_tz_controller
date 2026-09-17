> Manba: [Release 5 17.08.2026 · R5 User storylar: Uy egasi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43712557)
>
> Reliz rejasida ([Release 5 17.08.2026 · 3.2. Mobil ilova — Uy egasi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843819)): "Mulklarim" statuslari: qoralama / ijarada / bo'sh · Guruh: E'lon boshqaruvi · Manba: 26-task

# R5-UE-05 — "Mulklarim" statuslari

**User Story:** Uy egasi sifatida men mulklarimni holati bo'yicha ajratib ko'rishni xohlayman, shunda qaysi uy bo'sh, qaysi ijarada ekanini bir qarashda bilaman.

**Tavsif:** "Mulklarim" bo'limiga qoralama / ijarada / bo'sh statuslari qo'shiladi (mavjud faol / moderatsiyada / rad etilgan / arxiv badge'lariga qo'shimcha). Uy egasi statusni qo'lda o'zgartira oladi.

**Qabul mezonlari:**

* GIVEN e'lon yaratish yakunlanmagan WHEN "Mulklarim" ochilsa THEN e'lon "qoralama" statusida ko'rinadi va tahrirlashni davom ettirish mumkin
* GIVEN uy egasi so'rovni qabul qilib ijaraga berdi WHEN statusni "ijarada"ga o'zgartirsa THEN e'lon katalogda ko'rinmaydi
* GIVEN "ijarada" status WHEN "bo'sh"ga o'zgartirilsa THEN e'lon qayta faollashadi (moderatsiya holati saqlangan bo'lsa qayta moderatsiyasiz)
