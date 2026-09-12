> Manba: [Release 4 14.06.2026 · Ijarachi use caselari](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29360144)
>
> ⚠ Holat nomlari va 7 kunlik muddat R5 da o'zgargan — [3-8 So'rovlar](<../about.md>), [4-5 SLA va javob vaqti](<../../../4.Mobil ilova — Uy egasi/4-5 SLA va javob vaqti/about.md>).

**IJ-R2 — Mening so'rovlarim — holat ro'yxati va filter**

| **Sseneriy nomi** | Mening so'rovlarim — holat ro'yxati va filter |
| --- | --- |
| **Guruh** | So'rov |
| **Aktorlar** | Ijarachi (ro'yxatdan o'tgan) |
| **Tavsif** | Ijarachi bottom navigation'dagi 'So'rovlar' tabida o'zi yuborgan barcha so'rovlarni holati bo'yicha ko'radi. Holat tablar, sort va filter imkoniyatlari mavjud. Rad etilgan so'rov uchun e'lon sahifasiga kirganida modal ko'rsatiladi. |
| **Kirish sharti** | Ijarachi tizimga kirgan; kamida bitta so'rov yuborilgan |
| **Chiqish natijasi** | So'rovlar ro'yxati holat bo'yicha ko'rsatiladi; ijarachi so'rov tafsilotiga yoki uy egasiga bog'lanishga o'ta oladi |
| **Sseneriy ID** | IJ-R2 |

**Asosiy oqim**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Ijarachi** | Bottom navigation'dagi 'So'rovlar' tabini bosadi |
| 2 | **Tizim** | Sahifa yuklanadi: sarlavha 'So'rovlar', filter ikona; tabs: Barchasi \| Yangi so'rovlar \| Rad etilganlar \| Tasdiqlanganlar; sort: 'Eng oxirgi so'rovlar' |
| 3 | **Tizim** | Har bir so'rov kartasi ko'rsatiladi: e'lon rasmi + nomi + manzil + maydon + qavat + narx + yuborilgan sana + holat badge |
| 4 | **Tizim** | Holat badge'lari: Uy egasi arizangizni qabul qildi' (yashil) / 'Uy egasi arizangizni qabul qilmadi' (qizil) / 'Arizangiz tekshirish jarayonida' (sariq) |
| 5 | **Ijarachi** | Tab tanlab filtrlaydi (Yangi so'rovlar / Rad etilganlar / Tasdiqlanganlar) |
| 6 | **Ijarachi** | Sort yoki filter ikonasini bosadi — sana, lokatsiya, narx bo'yicha filter bottom sheet ochiladi |
| 7 | **Ijarachi** | So'rov kartasini bosadi → so'rov tafsilotini ko'radi |

**Muqobil oqimlar**

| **Holat** | **Oqim** |
| --- | --- |
| **Tasdiqlangan so'rov kartasi** | 'Uy egasi bilan bog'lanish' ko'k tugmasi ko'rinadi → bosish → IJ-R3 modal (Telefon qilish / Chat orqali yozish) |
| **Rad etilgan so'rov** | Karta holati ko'rsatiladi; ijarachi e'lon sahifasiga (IJ-08) kirganida 'So'rovingiz qabul qilinmadi' modal avtomatik ko'rsatiladi |
| **So'rovlar ro'yxati bo'sh** | 'Hali so'rov yo'q. E'lonlarni ko'rish' placeholder va havola ko'rsatiladi |
| **Muddati o'tgan so'rov (7 kun)** | Holat badge: 'Ko'rib chiqilmadi' (kulrang); ijarachiga xabarnoma allaqachon yuborilgan |

**Xatolik holatlari**

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | Kesh; 'Internet aloqasi yo'q' banner; pull-to-refresh faol |
| **Server xatosi** | Xabar va Retry |

**Biznes qoidalari**

| **# Qoida** |   |
| --- | --- |
| **BQ-1** | Tabs: Barchasi \| Yangi so'rovlar \| Rad etilganlar \| Tasdiqlanganlar |
| **BQ-2** | Sort default: 'Eng oxirgi so'rovlar' (sana kamayish tartibida) |
| **BQ-3** | Rad etilgan so'rovda darhol modal ko'rsatilmaydi — ijarachi keyingi safar o'sha e'lon (IJ-08) sahifasiga kirganida modal avtomatik ochiladi |
| **BQ-4** | 7 kun ko'rib chiqilmagan so'rov 'Ko'rib chiqilmadi' holatiga o'tadi; faqat uy egasiga push yuboriladi |
| **BQ-5** | Tasdiqlangan so'rovda 'Uy egasi bilan bog'lanish' tugmasi ko'rinadi |
| **BQ-6** | Pull-to-refresh bilan holat yangilanadi |

**Qabul qilish mezonlari (AC)**

| **# Mezon** |   |
| --- | --- |
| **AC-1** | So'rovlar ro'yxati ≤3 s ichida yuklanadi |
| **AC-2** | Tab filtri bosilganda ro'yxat ≤2 s ichida yangilanadi |
| **AC-3** | Tasdiqlangan so'rov kartasida 'Uy egasi bilan bog'lanish' tugmasi ko'rinadi; boshqa holatlarda ko'rinmaydi |
| **AC-4** | Rad etilgan so'rovdan so'ng ijarachi o'sha e'lon sahifasiga (IJ-08) kirganida modal avtomatik ko'rsatiladi |
| **AC-5** | 7 kun o'tib ko'rib chiqilmagan so'rov 'Ko'rib chiqilmadi' badge bilan ko'rsatiladi |
| **AC-6** | Bo'sh holat placeholder'da e'lonlarga o'tish havolasi mavjud |
