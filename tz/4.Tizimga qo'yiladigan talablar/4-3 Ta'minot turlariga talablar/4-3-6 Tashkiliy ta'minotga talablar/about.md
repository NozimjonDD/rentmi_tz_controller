4.3.6. Tashkiliy ta'minotga talablar

Tizim faoliyatida ishtirok etuvchi bo'linmalar tuzilishi va funksiyalari:

Tizim faoliyati "RENTME" MChJ tarkibidagi quyidagi bo'linmalar va ish o'rinlari tomonidan ta'minlanadi:

| Bo'linma yoki ish o'rni | Asosiy funksiyasi |
| --- | --- |
| Tizim administratori | Tizim konfiguratsiyasini boshqarish, foydalanuvchi hisoblarini administratsiya qilish, tizim xavfsizligini nazorat qilish |
| Ma'lumotlar bazasi administratori | Ma'lumotlar bazasi ishlashini ta'minlash, unumdorlikni optimallashtirish, zahira nusxalarni nazorat qilish |
| DevOps/infratuzilma muhandisi | Server infratuzilmasini boshqarish, monitoring, CI/CD pipeline va ishga tushirishlar |
| Texnik qo'llab-quvvatlash xodimlari | Foydalanuvchi shikoyatlari va texnik muammolarni ko'rib chiqish, birinchi darajadagi qo'llab-quvvatlash |
| Moderatorlar | E'lonlarni tekshirish va tasdiqlash, soxta e'lonlarni bloklash, foydalanuvchi shikoyatlarini ko'rib chiqish |
| Call-markaz operatorlari | Foydalanuvchi murojaatlarini qabul qilish, umumiy ma'lumot berish |
| Dasturchilar (ishlab chiqish jamoasi) | Tizimni rivojlantirish, xatoliklarni bartaraf etish, yangi funksiyalarni joriy etish |

Tizim faoliyati va xodimlar o'rtasidagi o'zaro aloqa tartibi:

- Xodimlar o'rtasidagi o'zaro aloqa ichki korporativ kanallar (elektron pochta, tezkor xabar almashish tizimlari, ichki issue tracker) orqali amalga oshiriladi;
- Foydalanuvchilar shikoyatlari quyidagi zanjir bo'yicha qayta ishlanadi: call-markaz → texnik qo'llab-quvvatlash → (zaruratga ko'ra) administrator yoki dasturchilar;
- Har bir murojaat ichki issue tracker tizimida qayd etiladi va uning hal qilinishi nazorat qilinadi;
- Kritik muammolar (tizim mavjud emasligi, xavfsizlik hodisalari) bo'yicha eskalatsiya mexanizmi belgilanadi.

Xodimlarning xatolardan himoyasi:

- Kritik operatsiyalar (foydalanuvchi ma'lumotlarini o'chirish, katta hajmli administratsiya harakatlari) qo'shimcha tasdiqlash mexanizmlari orqali himoyalanadi;
- Barcha administrator harakatlari audit jurnaliga yoziladi;
- Test va production muhitlari ajratilgan, test ma'lumotlari bilan ish faqat test muhitida amalga oshiriladi;
- Xodimlarga rollarga muvofiq kirish huquqlari beriladi va vaqti-vaqti bilan qayta ko'rib chiqiladi;
- Yangi xodimlar ishga qabul qilingandan so'ng tizimdan foydalanish bo'yicha o'qitishdan o'tkaziladi.
