> Manba: [Release 3 07.06.2026 · Admin use cases](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/27721770)
>
> Izoh: R5 da Actual History stories mobil ilovada ko'rsatilmaydi (kod saqlanadi) — [3-1 Asosiy sahifa](<../../../3.Mobil ilova — Ijarachi/3-1 Asosiy sahifa/about.md>).

# AD-12 — Stories holati boshqaruvi (faol/nofaol, arxiv)

| **Sseneriy ID** | AD-12 |
| --- | --- |
| **Sseneriy nomi** | Stories holati boshqaruvi (faol/nofaol, arxiv) |
| **Guruh** | Actual History boshqaruvi |
| **Aktorlar** | Administrator |
| **Tavsif** | Administrator Actual History storieslarini faol yoki nofaol qiladi. Nofaol qilingan story darhol ilovada ko'rsatilmaydi va arxivga o'tkaziladi. Arxivlangan storyni qayta faol qilish mumkin. Guest va user stories holatlari alohida boshqariladi. |
| **Kirish sharti** | Administrator admin panelda stories ro'yxatini ochgan |
| **Chiqish natijasi** | Story holati o'zgartiriladi; faol/nofaol holat darhol ilovada aks etadi |

## Asosiy oqim — Story nofaol qilish

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| **1** | **Administrator** | Stories ro'yxatida faol storyni tanlaydi |
| **2** | **Administrator** | Story yonidagi toggle ni o'chiradi yoki 'Nofaol qilish' tugmasini bosadi |
| **3** | **Tizim** | Tasdiqlash so'rovi: 'Ushbu storyni nofaol qilmoqchimisiz? U foydalanuvchilarga ko'rsatilmaydi' |
| **4** | **Administrator** | 'Ha' tugmasini bosadi |
| **5** | **Tizim** | Story holati 'Nofaol' ga o'zgaradi; arxiv bo'limiga o'tkaziladi |
| **6** | **Tizim** | Story ilovada foydalanuvchilarga darhol ko'rsatilmaydi |
| **7** | **Tizim** | Stories ro'yxatida story 'Arxivlangan' belgisi bilan ko'rinadi |

## Muqobil oqimlar

| **Holat** | **Oqim** |
| --- | --- |
| **Story faol qilish** | Administrator arxivlangan storyni tanlaydi → toggle yoqadi yoki 'Faol qilish' → tasdiqlash → 'Ha' → story faol holat; ilovada ko'rsatiladi; prioritet ro'yxatiga qaytadi |
| **Bir nechta story bir vaqtda nofaol qilish** | Administrator ro'yxatda bir nechta storyni checkbox bilan tanlaydi → 'Tanlanganlani nofaol qilish' → tasdiqlash → hammasi arxivlanadi |
| **Arxivlangan storieslarni ko'rish** | Administrator 'Arxiv' tabini ochadi — barcha nofaol storieslar ko'rsatiladi; faol qilish yoki o'chirish mumkin |
| **Arxivlangan storyni o'chirish** | Arxivdan storyni tanlaydi → 'O'chirish' → tasdiqlash → story butunlay o'chiriladi |

## Xatolik holatlari

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Server xatosi** | 'Holat o'zgartirib bo'lmadi' xabari va Retry; story oldingi holatda qoladi |
| **Internet yo'q** | Amal amalga oshmaydi; xabar ko'rsatiladi |

## Biznes qoidalari

| **#** | **Qoida** |
| --- | --- |
| **BQ-1** | Nofaol qilingan story darhol arxivga o'tkaziladi — ilovada ko'rsatilmaydi |
| **BQ-2** | Arxivlangan storyni qayta faol qilish mumkin — u prioritet ro'yxatiga oxirgi o'ringa qaytadi |
| **BQ-3** | Stories muddatsiz — vaqt chegarasi yo'q; faqat qo'lda faol/nofaol qilish |
| **BQ-4** | Guest stories va user stories holatlari alohida boshqariladi — bir tabdagi o'zgartirish boshqasiga ta'sir qilmaydi |
| **BQ-5** | Holat o'zgarishi (faol/nofaol) darhol ilovada aks etadi — kesh yangilanadi |
| **BQ-6** | Arxivlangan story ma'lumotlari (rasm, tekst, CTA) saqlanib qoladi — faqat holati o'zgaradi |
