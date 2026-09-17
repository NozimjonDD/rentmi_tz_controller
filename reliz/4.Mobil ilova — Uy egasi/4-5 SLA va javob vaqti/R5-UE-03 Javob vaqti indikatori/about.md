> Manba: [Release 5 17.08.2026 · R5 User storylar: Uy egasi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43712557)
>
> Reliz rejasida ([Release 5 17.08.2026 · 3.2. Mobil ilova — Uy egasi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843819)): Javob vaqti indikatori: "Odatda N soatda javob beradi" (e'londa va profilda), SLA ma'lumotidan mediana asosida · Guruh: Ishonch · Manba: 13-task

# R5-UE-03 — Javob vaqti indikatori

**User Story:** Uy egasi sifatida men tez javob berishim ijarachilarga ko'rinishini xohlayman, shunda e'lonlarim ko'proq ariza oladi.

**Tavsif:** Har so'rov bo'yicha first_response_time yoziladi. Ko'rsatkich — oxirgi 30 kun medianasi, soatlik pog'onaga yaxlitlanadi ("odatda 1 soat ichida javob beradi", "odatda 2 soatda"...). Kamida 3 ta javob bo'lsagina e'lon sahifasida va ommaviy profilda chiqadi. Uy egasiga onboarding tooltip orqali tushuntiriladi.

**Qabul mezonlari:**

* GIVEN uy egasida kamida 3 ta javob yozuvi bor WHEN e'lon yoki profil ochilsa THEN indikator mediana asosida ko'rinadi
* GIVEN javoblar 3 tadan kam WHEN sahifa ochilsa THEN indikator ko'rsatilmaydi
* GIVEN bitta so'rovga juda kech javob berilgan WHEN mediana hisoblansa THEN bitta chetlanish ko'rsatkichni keskin buzib yubormaydi (mediana, o'rtacha emas)
* GIVEN uy egasi birinchi marta So'rovlar sahifasini ochdi WHEN sahifa yuklansa THEN tez javob berish foydasi haqidagi tooltip ko'rsatiladi
