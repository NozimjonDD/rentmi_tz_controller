> Manba: [Release 4 14.06.2026 · Ijarachi use caselari](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29360144)

**IJ-C3 — Uy egasini bloklash (chat ichidan)**

| **Sseneriy nomi** | Uy egasini bloklash |
| --- | --- |
| **Guruh** | Chat |
| **Aktorlar** | Ijarachi (ro'yxatdan o'tgan) |
| **Tavsif** | Ijarachi chat ichidagi 3-nuqta menyusidan uy egasini bloklaydi. Bloklash sababini ko'rsatadi. Bloklangandan so'ng o'sha uy egasiga tegishli barcha e'lonlar ijarachi feedidan chiqariladi. |
| **Kirish sharti** | Ijarachi IJ-C2 chat ekranida; 3-nuqta menyu mavjud |
| **Chiqish natijasi** | Uy egasi bloklanadi; uy egasining e'lonlari feeddan chiqariladi; chat arxivga o'tadi |
| **Sseneriy ID** | IJ-C3 |

**Asosiy oqim**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Ijarachi** | Chat ekranida (IJ-C2) 3-nuqta (⋮) menyusini bosadi → 'Block qilish' tanlaydi |
| 2 | **Tizim** | Bloklash bottom sheet ochiladi: uy egasi avatar + ism; 'Siz rostdan ham \[Ism\]ni blok qilmoqchimisiz?' matni; ogohlantirish: 'Agar siz uy egasini blok qilsangiz, \[Ism\]ga tegishli boshqa e'lonlarni ko'ra olmaysiz' |
| 3 | **Tizim** | Sabab checkboxlari ko'rsatiladi: 'Uy rasmda ko'rsatilganday emas' / 'Narx e'londa ko'rsatilganday emas' / 'Boshqa' (+ textarea) |
| 4 | **Ijarachi** | Kamida bitta sababni belgilaydi ('Boshqa' tanlansa textarea majburiy to'ldiriladi) |
| 5 | **Ijarachi** | 'Ushbu shaxsning e'lonlarini ko'rmoqchimasman' (qizil) tugmasini bosadi |
| 6 | **Tizim** | Bloklash serverga saqlanadi; uy egasining barcha e'lonlari ijarachi feedidan darhol chiqariladi |
| 7 | **Tizim** | Chat arxivga o'tadi; ijarachi IJ-C1 ga qaytadi |

**Muqobil oqimlar**

| **Holat** | **Oqim** |
| --- | --- |
| **X bosiladi yoki bottom sheet yopiladi** | Bloklash amalga oshmaydi; IJ-C2 ga qaytiladi |
| **'Boshqa' belgilangan, textarea bo'sh** | 'Ushbu shaxsning e'lonlarini ko'rmoqchimasman' disabled; textarea to'ldirish talab qilinadi |
| **Hech bir sabab tanlanmagan** | Tugma disabled qoladi |

**Xatolik holatlari**

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | Bloklash amalga oshmaydi; xabar ko'rsatiladi |
| **Server xatosi** | Xabar va Retry; feeddan olib tashlanmaydi |

**Biznes qoidalari**

| **# Qoida** |   |
| --- | --- |
| **BQ-1** | Kamida bitta sabab tanlanishi shart; 'Boshqa' tanlansa textarea ham to'ldirilishi majburiy |
| **BQ-2** | Bloklash qaytarib bo'lmaydi — undo yo'q (faqat admin orqali olib tashlash mumkin) |
| **BQ-3** | Bloklangan uy egasining barcha e'lonlari qidiruv va tavsiya natijalaridan ham chiqariladi |
| **BQ-4** | Bloklangandan so'ng chat arxivga o'tadi; IJ-C1 da ko'rinmaydi |

**Qabul qilish mezonlari (AC)**

| **# Mezon** |   |
| --- | --- |
| **AC-1** | Sabab tanlanmagan holda 'Ushbu shaxsning e'lonlarini ko'rmoqchimasman' tugmasi disabled ko'rinadi |
| **AC-2** | 'Boshqa' tanlanganda textarea paydo bo'ladi va bo'sh qoldirib tugma bosilmaydi |
| **AC-3** | Bloklangandan ≤3 s ichida uy egasining e'lonlari feeddan yo'qoladi |
| **AC-4** | Bloklangandan so'ng IJ-C1 da o'sha chat ko'rinmaydi |
| **AC-5** | Bloklangan uy egasining e'lonlari IJ-17 qidiruv natijalarida ham ko'rsatilmaydi |
