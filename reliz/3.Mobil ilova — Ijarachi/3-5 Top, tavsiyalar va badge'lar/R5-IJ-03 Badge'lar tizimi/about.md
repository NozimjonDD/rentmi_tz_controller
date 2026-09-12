> Manba: [Release 5 17.08.2026 · R5 User storylar: Ijarachi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843840)
>
> Reliz rejasida ([Release 5 17.08.2026 · 3.1. Mobil ilova — Ijarachi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843819)): Badge'lar tizimi: Sizga mos, Top, Tekshirilgan, Narxi tushdi · Guruh: Qidiruv va e'lon · Manba: 2-task; F-D3

# R5-IJ-03 — Badge'lar tizimi

**User Story:** Ijarachi sifatida men e'lon kartalarida ishonch va moslik belgilarini ko'rishni xohlayman, shunda qaysi uyga ariza berishni tezroq hal qila olaman.

**Tavsif:** To'rt badge joriy etiladi: "Sizga mos" (ikki tomonlama moslik), "Top" (og'irlikli ball, hudud kesimida), "Tekshirilgan" (moderatsiya + identifikatsiya + tegishlilik AND), "Narxi tushdi" (narx tarixi asosida). Rasm ustida parametrlar (m², xona, qavat) va kartada ko'rishlar soni ko'rsatiladi.

**Qabul mezonlari:**

* GIVEN e'lon uch shartning barchasiga javob beradi WHEN karta ko'rsatilsa THEN "Tekshirilgan" badge chiqadi; birorta shart bajarilmasa — chiqmaydi
* GIVEN e'lon ijarachi filtriga mos VA ijarachi e'lon talabiga mos WHEN karta ko'rsatilsa THEN "Sizga mos" chiqadi
* GIVEN e'lon narxi 7–14 kunda belgilangan foizdan ko'p pasaygan WHEN karta ko'rsatilsa THEN "Narxi tushdi" chiqadi; sun'iy ko'tarib-tushirishda chiqmaydi
* GIVEN tegishlilik ma'lumoti mavjud emas WHEN karta ko'rsatilsa THEN "Tekshirilgan" badge ko'rsatilmaydi (default: yashirish)
