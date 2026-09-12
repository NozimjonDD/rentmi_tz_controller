> Manba: [Release 4 14.06.2026 · Uy egasi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29392915)

**UE-C1 — Chat orqali ijarachi bilan xabarlashish**

| **Sseneriy nomi** | Chat orqali ijarachi bilan xabarlashish |
| --- | --- |
| **Guruh** | Chat |
| **Aktorlar** | Uy egasi (ro'yxatdan o'tgan) |
| **Tavsif** | Uy egasi ijarachi bilan chat orqali matn va rasm almashadi. Chat UE-R2 kartasidagi chat ikonasi yoki UE-R3 header'dan ochiladi. Uy egasi faqat o'zi yuborgan xabarlarni tahrirlashi va o'chirishi mumkin. Ijarachini bloklash imkoniyati ham mavjud. |
| **Kirish sharti** | UE-R2 yoki UE-R3 dan chat ikona bosilgan; so'rov pending yoki tasdiqlangan holatda (rad etilganda chat yo'q) |
| **Chiqish natijasi** | Uy egasi ijarachi bilan xabar almashadi |
| **Sseneriy ID** | UE-C1 |

**Asosiy oqim — Chat ro'yxati**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Uy egasi** | Bottom navigation'dagi chat (pufakcha) ikonasini bosadi |
| 2 | **Tizim** | Chat ro'yxati yuklanadi. Har bir karta: ijarachi avatar + online indikator (yashil nuqta), ism, oxirgi xabar matni, mulk mini-kartasi (nomi + manzil), o'qilmagan badge (raqam), vaqt |
| 3 | **Uy egasi** | Chat kartasini bosadi → chat detail ekrani ochiladi |

**Asosiy oqim — Xabarlashish**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Tizim** | Chat ekrani: yuqorida mulk mini-kartasi; sarlavhada ijarachi ismi + online holati; qidiruv va 3-nuqta ikonalari |
| 2 | **Tizim** | Xabar tarixi: sana separator; uy egasi xabarlari o'ngda (yashil), ijarachi xabarlari chapda (oq); delivery status ✓/✓✓ |
| 3 | **Uy egasi** | Matn yozadi va yuborish tugmasini bosadi |
| 4 | **Tizim** | Xabar threadga qo'shiladi; ✓ (yuborildi) → ijarachi o'qigach ✓✓ |

**Muqobil oqimlar**

| **Holat** | **Oqim** |
| --- | --- |
| **Rasm yuborish** | Paperclip → galereya → rasm tanlanadi → 2-ustun grid preview → yuborish |
| **O'z xabarini tahrirlash** | Uzun bosish → 'Tahrirlash' → matn maydoni to'ldiriladi → saqlash |
| **O'z xabarini o'chirish** | Uzun bosish → 'O'chirish' → tasdiqlash modali → o'chiriladi |
| **Nusxa olish** | Uzun bosish → 'Nusxa olish' → bufer xotiraga |
| **Qaytarish (Reply)** | Uzun bosish → 'Qaytarish' → quote bilan yangi xabar |
| **Multi-select** | Bitta xabar uzun bosiladi → checkbox rejimi → mass copy/delete |
| **Xabarda qidiruv** | Header search → qidiruv satri → mos xabarga scroll |
| **3-nuqta menyu** | 'Telefon qilish' → ijarachiga qo'ng'iroq; 'Block qilish' → bloklash bottom sheet |
| **Chat ro'yxati bo'sh** | 'Hali chat yo'q. So'rov yuboring — chat darhol ochiladi' placeholder |

**Bloklash oqimi**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Uy egasi** | 3-nuqta (⋮) → 'Block qilish' tanlaydi |
| 2 | **Tizim** | Bloklash bottom sheet: ijarachi avatar + ism; ogohlantirish matni; sabab checkboxlari: 'Uy rasmda ko'rsatilganday emas' / 'Narx e'londa ko'rsatilganday emas' / 'Boshqa' (+ textarea) |
| 3 | **Uy egasi** | Kamida bitta sabab belgilaydi → 'Ushbu shaxsning e'lonlarini ko'rmoqchimasman' tugmasini bosadi |
| 4 | **Tizim** | Bloklash saqlanadi; ijarachi feeddan chiqarilmaydi (uy egasi tomonidan bloklash faqat chatni yopadi); chat arxivga o'tadi |

**Xatolik holatlari**

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | Xabar saqlanmaydi; matn saqlanib qoladi; banner |
| **Rasm hajmi >5 MB** | 'Fayl hajmi ruxsat etilganidan katta'; yuklanmaydi |
| **Server xatosi** | Xabar yuborilmadi belgisi; Retry |

**Biznes qoidalari**

| **# Qoida** |   |
| --- | --- |
| **BQ-1** | Chat pending va tasdiqlangan so'rovlarda ochiladi; faqat rad etilgan so'rovlarda chat disabled |
| **BQ-2** | Uy egasi faqat o'zi yuborgan xabarlarni tahrirlashi va o'chirishi mumkin; ijarachi xabarlariga bu amallar qo'llanilmaydi |
| **BQ-3** | Delivery status: ✓ — yuborildi, ✓✓ — ijarachi o'qidi |
| **BQ-4** | Rasm formati: jpg, png, pdf; hajm: ≤5 MB |
| **BQ-5** | Chatlar so'nggi xabar vaqti bo'yicha kamayish tartibida ko'rsatiladi |
| **BQ-6** | Uy egasi tomonidan bloklash chat o'tkazishini to'xtatadi; ijarachi e'lonlari uy egasi feedidan chiqarilmaydi (bu ijarachi tomonidan bloklashdan farqi) |

**Qabul qilish mezonlari (AC)**

| **# Mezon** |   |
| --- | --- |
| **AC-1** | Xabar yuborilgandan ≤1 s ichida threadda ko'rsatiladi |
| **AC-2** | Faqat uy egasining o'z xabarida 'Tahrirlash' va 'O'chirish' ko'rinadi; ijarachi xabarida 'Nusxa olish' va 'Qaytarish' ko'rsatiladi |
| **AC-3** | Rad etilgan so'rov chatida chat input disabled va 3-nuqta menyu ko'rsatilmaydi |
| **AC-4** | Bloklash bottom sheet'da sabab tanlanmagan holda tugma disabled ko'rinadi |
| **AC-5** | 3-nuqta 'Telefon qilish' bosilganda qurilma telefon ilovasi ijarachi raqami bilan ochiladi |
