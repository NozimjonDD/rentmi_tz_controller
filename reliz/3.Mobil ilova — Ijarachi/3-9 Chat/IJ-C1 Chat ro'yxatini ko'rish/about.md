> Manba: [Release 4 14.06.2026 · Ijarachi use caselari](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29360144)
>
> ⚠ Chat kirish joyi R5 da o'zgargan; ❓ kirish sharti bo'yicha ichki nomuvofiqlik — [3-9 Chat](<../about.md>).

**IJ-C1 — Chat ro'yxatini ko'rish**

| **Sseneriy nomi** | Chat ro'yxatini ko'rish |
| --- | --- |
| **Guruh** | Chat |
| **Aktorlar** | Ijarachi (ro'yxatdan o'tgan) |
| **Tavsif** | Ijarachi bottom navigation'dagi chat tabida uy egalari bilan bo'lgan barcha chat suhbatlarini ko'radi. Har bir karta ijarachi muloqot qilayotgan uy egasi va tegishli mulk ma'lumotlarini ko'rsatadi. |
| **Kirish sharti** | Ijarachi tizimga kirgan; kamida bitta tasdiqlangan so'rov mavjud (chat faqat tasdiqlangandan keyin ochiladi) |
| **Chiqish natijasi** | Chat ro'yxati ko'rsatiladi; ijarachi tanlagan chatga kiradi |
| **Sseneriy ID** | IJ-C1 |

**Asosiy oqim**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Ijarachi** | Bottom navigation'dagi chat (pufakcha) ikonasini bosadi |
| 2 | **Tizim** | Chat ro'yxati yuklanadi. Har bir karta: uy egasi avatar + online indikator (yashil nuqta), ism, oxirgi xabar matni, mulk mini-kartasi (nomi + manzil), o'qilmagan xabarlar badge (raqam), vaqt |
| 3 | **Tizim** | Delivery status: ✓ yuborildi (ijarachi xabari), ✓✓ o'qildi |
| 4 | **Ijarachi** | Chat kartasini bosadi → IJ-C2 ga o'tiladi |

**Muqobil oqimlar**

| **Holat** | **Oqim** |
| --- | --- |
| **Chat ro'yxati bo'sh** | 'Hali chat yo'q. So'rov yuborilgandan so'ng chat ochiladi' placeholder ko'rsatiladi |
| **Yangi xabar keldi (push orqali)** | Badge raqami yangilanadi; karta yuqoriga ko'tariladi (eng yangi chat birinchi) |

**Xatolik holatlari**

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | Kesh chat ro'yxati ko'rsatiladi; banner ko'rsatiladi |
| **Server xatosi** | Xabar va Retry |

**Biznes qoidalari**

| **# Qoida** |   |
| --- | --- |
| **BQ-1** | Chat so'rov tasdiqlanmagan bo’lsa xam ochiladi; rad etilgan so'rovlarda chat va telefon qilish yo'q |
| **BQ-2** | Chatlar so'nggi xabar vaqti bo'yicha kamayish tartibida ko'rsatiladi |
| **BQ-3** | Online indikator real-time ko'rsatiladi |
| **BQ-4** | O'qilmagan badge raqami chatga kirganda nolga tushadi |

**Qabul qilish mezonlari (AC)**

| **# Mezon** |   |
| --- | --- |
| **AC-1** | Chat ro'yxati ≤3 s ichida yuklanadi |
| **AC-2** | Har bir kartada uy egasi avatar, ism, oxirgi xabar, mulk nomi va o'qilmagan badge ko'rinadi |
| **AC-3** | O'qilmagan xabar badge raqami chat ochilganda yo'qoladi |
| **AC-4** | Tasdiqlangan so'rovi bo'lmagan ijarachi uchun bo'sh holat placeholder ko'rsatiladi |
