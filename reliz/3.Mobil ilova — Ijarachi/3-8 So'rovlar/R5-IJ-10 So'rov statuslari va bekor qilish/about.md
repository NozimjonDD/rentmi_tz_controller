> Manba: [Release 5 17.08.2026 · R5 User storylar: Ijarachi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843840)
>
> Reliz rejasida ([Release 5 17.08.2026 · 3.1. Mobil ilova — Ijarachi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843819)): So'rov statuslari va bekor qilish: "ko'rilmoqda/kutilmoqda" nomlanishi, bekor qilish tugmasi, "bekor qilingan" holati · Guruh: So'rov · Manba: 4, 5-task

# R5-IJ-10 — So'rov statuslari va bekor qilish

**User Story:** Ijarachi sifatida men yuborgan so'rovimni bekor qila olishni xohlayman, shunda fikrim o'zgarganda uy egasini bekorga kuttirmayman.

**Tavsif:** Statuslar yangi nomlanadi: "ko'rilmoqda" / "kutilmoqda" / "qabul qilindi" / "rad etildi" / "bekor qilingan". Bekor qilish tugmasi faqat hali ko'rib chiqilmagan so'rovlarda ko'rinadi; bekor qilingan so'rov ro'yxatda badge bilan turadi.

**Qabul mezonlari:**

* GIVEN so'rov "kutilmoqda" holatida WHEN ijarachi bekor qilishni tasdiqlasa THEN so'rov "bekor qilingan"ga o'tadi va uy egasiga bildirishnoma boradi
* GIVEN so'rov "qabul qilindi" holatida WHEN ro'yxat ochilsa THEN bekor qilish tugmasi ko'rinmaydi
* GIVEN ijarachi bekor qilmoqda VA uy egasi ayni paytda qabul qilmoqda WHEN ikkala amal to'qnashsa THEN birinchi yozilgan amal g'olib bo'ladi, ikkinchi tomonga aktual holat xabari chiqadi
