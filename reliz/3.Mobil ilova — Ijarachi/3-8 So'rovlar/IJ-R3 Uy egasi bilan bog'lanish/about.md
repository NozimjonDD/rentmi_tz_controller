> Manba: [Release 4 14.06.2026 · Ijarachi use caselari](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29360144)

**IJ-R3 — Uy egasi bilan bog'lanish**

| **Sseneriy nomi** | Uy egasi bilan bog'lanish (tasdiqlangan so'rovda) |
| --- | --- |
| **Guruh** | So'rov |
| **Aktorlar** | Ijarachi (ro'yxatdan o'tgan) |
| **Tavsif** | So'rov tasdiqlangandan so'ng ijarachi uy egasining kontakt ma'lumotlariga (telefon raqami) kirish imkoniyatiga ega bo'ladi. Modal orqali telefon qilish yoki chat orqali yozish mumkin. |
| **Kirish sharti** | IJ-R2 da tasdiqlangan so'rov kartasi mavjud; yoki xabarnomada (IJ-N1) tasdiqlash xabari bor |
| **Chiqish natijasi** | Ijarachi uy egasiga telefon qiladi yoki chat ekraniga (IJ-C2) o'tadi |
| **Sseneriy ID** | IJ-R3 |

**Asosiy oqim**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Ijarachi** | IJ-R2 da tasdiqlangan so'rov kartasida 'Uy egasi bilan bog'lanish' tugmasini bosadi |
| 2 | **Tizim** | Bottom sheet ochiladi: 'Uy egasi bilan bog'lanish' sarlavhasi; ikki variant: 'Telefon qilish \[raqam\]' + 'Chat orqali yozish' |
| 3 | **Ijarachi** | Variantdan birini tanlaydi |
| 4 | **Tizim** | Telefon tanlansa — qurilma telefon ilovasi ochiladi raqam bilan; Chat tanlansa — IJ-C2 chat ekrani ochiladi |

**Muqobil oqimlar**

| **Holat** | **Oqim** |
| --- | --- |
| **'So'rovingiz qabul qilindi' modal orqali** | IJ-08 da modal ko'ringanida 'Uy egasi bilan bog'lanish' tugmasi bosilganda xuddi shu bottom sheet ochiladi |
| **Xabarnomadan (IJ-N1) kelgan** | Tasdiqlangan so'rov kartasidagi tugmadan xuddi shu oqim |
| **Bottom sheet X bosiladi** | Yopiladi; IJ-R2 ga qaytiladi |

**Xatolik holatlari**

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Telefon ilovasi yo'q** | Qurilma standart xabari ko'rsatiladi |
| **Internet yo'q (chat tanlanganda)** | Chat ekraniga o'tiladi; offline xabari ko'rsatiladi |

**Biznes qoidalari**

| **# Qoida** |   |
| --- | --- |
| **BQ-1** | Uy egasining telefon raqami faqat so'rov tasdiqlangandan so'ng ijarachiga ko'rsatiladi |
| **BQ-2** | Rad etilgan yoki kutmoqda holatlardagi so'rovlarda 'Uy egasi bilan bog'lanish' ko'rinmaydi |
| **BQ-3** | Bog'lanish imkoniyati IJ-R2, IJ-08 modali va IJ-N1 dan ochilishi mumkin |

**Qabul qilish mezonlari (AC)**

| **# Mezon** |   |
| --- | --- |
| **AC-1** | 'Uy egasi bilan bog'lanish' tugmasi faqat tasdiqlangan so'rov kartasida ko'rinadi |
| **AC-2** | Bottom sheet'da uy egasining haqiqiy telefon raqami ko'rsatiladi |
| **AC-3** | 'Telefon qilish' bosilganda qurilma telefon ilovasi raqam bilan ochiladi |
| **AC-4** | 'Chat orqali yozish' bosilganda IJ-C2 chat ekrani ochiladi |
