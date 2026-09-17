4.1.5.2. Avariyaviy holatlar ro'yxati va ularga qo'yiladigan talablar

Tizim quyidagi avariyaviy holatlar bo'yicha ishlash qobiliyatini saqlab qolish va tiklash imkoniyatini ta'minlashi lozim:

| Avariyaviy holat | Ishonchlilik talabi |
| --- | --- |
| Dasturiy ta'minot xatoliklari | Dasturiy xatolik yuz berganda tizim tranzaksiyalarni to'liq bajarilganga qadar rollback qilish yoki tiklash imkoniyatini ta'minlashi; foydalanuvchiga xatolik haqida aniq ma'lumot berilishi |
| Ma'lumotlar bazasi bilan bog'liq nosozliklar | Ma'lumotlar bazasi kundalik va oylik zahira nusxalari orqali tiklanishi; tranzaksiya jurnalidan (transaction log) foydalanib oxirgi muvaffaqiyatli holatga tiklash imkoniyati |
| Tashqi tizimlar bilan aloqaning uzilishi | Qayta urinish (retry) va circuit breaker mexanizmlari qo'llanilishi; foydalanuvchi operatsiyalarining to'g'ri yakunlanishi ta'minlanishi |
