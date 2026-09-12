> Manba: [Release 5 17.08.2026 · R5 User storylar: Ijarachi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843840)
>
> Reliz rejasida ([Release 5 17.08.2026 · 3.1. Mobil ilova — Ijarachi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843819)): Uy egasi ommaviy profili: Rentmi'da N vaqt, e'lonlar soni, "Tasdiqlangan uy egasi", tegishlilik, javob vaqti, tegishli e'lonlar; "faqat platforma orqali muloqot" xabari · Guruh: Ishonch · Manba: 14, 15, 16-task

# R5-IJ-08 — Uy egasi ommaviy profili

**User Story:** Ijarachi sifatida men uy egasi haqida tekshirilgan ma'lumotni ko'rishni xohlayman, shunda firibgarlikdan himoyalanaman va ishonch bilan ariza yuboraman.

**Tavsif:** E'lon sahifasidagi uy egasi blokidan ommaviy profil ochiladi: Rentmi'da N vaqt, e'lonlar soni, "Tasdiqlangan uy egasi — shaxsi va hujjatlari Rentmi tomonidan tekshirilgan", javob berish odati, tegishli e'lonlar. Reyting va "Rentmi kafolati" bloklari yashirin (RelizF). Chat/so'rov oqimida "faqat platforma orqali muloqot qiling" xavfsizlik xabari.

**Qabul mezonlari:**

* GIVEN uy egasi identifikatsiyadan o'tgan va mulk tegishliligi tasdiqlangan WHEN profil ochilsa THEN "Tasdiqlangan uy egasi" bloki ko'rinadi
* GIVEN uy egasining boshqa faol e'lonlari bor WHEN profil ochilsa THEN "Tegishli e'lonlar" ro'yxati ko'rinadi
* GIVEN profil ochildi WHEN sahifa yuklansa THEN reyting yulduzi va kafolat bloki ko'rinmaydi
* GIVEN ijarachi chat boshladi WHEN oyna ochilsa THEN xavfsizlik xabari ko'rinadi
