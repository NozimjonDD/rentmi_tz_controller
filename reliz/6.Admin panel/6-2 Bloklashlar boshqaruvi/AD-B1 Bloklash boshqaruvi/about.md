> Manba: [Release 4 14.06.2026 · Admin](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29360160)

**AD-B1 — Bloklash boshqaruvi**

| **Sseneriy nomi** | Bloklash boshqaruvi (ko'rish va unblock) |
| --- | --- |
| **Guruh** | Foydalanuvchi boshqaruvi |
| **Aktorlar** | Administrator |
| **Tavsif** | Administrator barcha bloklashlarni (ijarachi → uy egasi va uy egasi → ijarachi) ro'yxatda ko'radi. Har bir bloklashning sababini, kim bloklagan va qachon bloklanganligi ko'rsatiladi. Administrator bloklashni olib tashlash (unblock) imkoniyatiga ega. |
| **Kirish sharti** | Administrator admin panel'da 'Bloklashlar' bo'limini ochgan; kamida bitta bloklash mavjud |
| **Chiqish natijasi** | Administrator bloklashlar ro'yxatini ko'radi va zarur hollarda unblock qiladi |
| **Sseneriy ID** | AD-B1 |

**Asosiy oqim — Ko'rish**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Administrator** | Admin panel'da 'Bloklashlar' bo'limini ochadi |
| 2 | **Tizim** | Jadval ko'rsatiladi. Ustunlar: Bloklagan (ism + rol) \| Bloklangan (ism + rol) \| Sabab \| Bloklash sanasi \| Holat (Faol/Olib tashlangan) |
| 3 | **Tizim** | Filter: Bloklash turi (Barchasi / Ijarachi bloklagan / Uy egasi bloklagan); Sana oralig'i |
| 4 | **Administrator** | Qidiruv: foydalanuvchi ismi yoki telefon bo'yicha |
| 5 | **Administrator** | Bloklash qatorini bosadi → tafsilot panel (yoki modal) ochiladi: to'liq sabab matni, bloklash sanasi/vaqti, bloklagan foydalanuvchi profili havolasi |

**Asosiy oqim — Unblock qilish**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Administrator** | Tafsilot panelida 'Bloklashni olib tashlash' tugmasini bosadi |
| 2 | **Tizim** | Tasdiqlash modali: 'Haqiqatan ham bloklashni olib tashlamoqchimisiz?' + Sabab maydoni (majburiy) |
| 3 | **Administrator** | Sabab kiritadi va 'Tasdiqlash' tugmasini bosadi |
| 4 | **Tizim** | Bloklash 'Olib tashlangan' holatiga o'tadi; ikkala foydalanuvchi uchun chat va ko'rish imkoniyati qayta tiklanadi |
| 5 | **Tizim** | Audit jurnaliga yoziladi: administrator ID, sana/vaqt, sabab |

**Muqobil oqimlar**

| **Holat** | **Oqim** |
| --- | --- |
| **Tasdiqlash modal 'Bekor qilish'** | Modal yopiladi; bloklash o'zgarmaydi |
| **Bloklashlar ro'yxati bo'sh** | 'Hozircha bloklash yo'q' placeholder |
| **Allaqachon olib tashlangan blok** | 'Bloklashni olib tashlash' tugmasi disabled ko'rsatiladi |

**Xatolik holatlari**

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q / server xatosi** | Unblock amalga oshmaydi; xabar va Retry; holat o'zgarmaydi |

**Biznes qoidalari**

| **# Qoida** |   |
| --- | --- |
| **BQ-1** | Jadval ustunlari: Bloklagan (ism + rol), Bloklangan (ism + rol), Sabab, Bloklash sanasi, Holat |
| **BQ-2** | Ikki turdagi bloklash ko'rsatiladi: ijarachi → uy egasi va uy egasi → ijarachi |
| **BQ-3** | Unblock qilishda sabab kiritish majburiy — audit uchun |
| **BQ-4** | Unblock qilinganida ikki foydalanuvchi uchun chat va ko'rish imkoniyati avtomatik tiklanadi |
| **BQ-5** | Barcha unblock amallari audit jurnaliga administrator ID, sana/vaqt va sabab bilan yoziladi |

**Qabul qilish mezonlari (AC)**

| **# Mezon** |   |
| --- | --- |
| **AC-1** | Bloklashlar ro'yxati ≤3 s ichida yuklanadi |
| **AC-2** | Filter va qidiruv ≤2 s ichida natija ko'rsatadi |
| **AC-3** | Unblock tasdiqlash modali sabab maydoni bo'sh bo'lsa 'Tasdiqlash' tugmasi disabled ko'rsatiladi |
| **AC-4** | Unblock muvaffaqiyatli bo'lgandan so'ng jadvalda holat 'Olib tashlangan' ga o'zgaradi |
| **AC-5** | Audit jurnaliga unblock yozuvi kiritilganligi tekshiriladi |
