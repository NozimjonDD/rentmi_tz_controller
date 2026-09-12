> Manba: [Release 4 14.06.2026 · Uy egasi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29392915)

**UE-AI1 — AI maslahat**

| **Sseneriy nomi** | AI maslahat (narx tahlili va e'lon to'liqlik baholash) |
| --- | --- |
| **Guruh** | AI maslahat |
| **Aktorlar** | Uy egasi (ro'yxatdan o'tgan) |
| **Tavsif** | Uy egasi AI maslahat modalida ikkita tab bo'yicha tavsiyalar ko'radi: 'AI bo'yicha' tabida bozor narx tahlili va joylashuv maslahatlari; 'E'lon bo'yicha' tabida e'lon to'ldirilganlik foizi va har bir bo'lim bo'yicha tavsiyalar. 'Tahrirlash' tugmasi to'g'ridan-to'g'ri tegishli e'lon bo'limiga olib boradi. |
| **Kirish sharti** | UE-S1 da AI maslahat kartochkasi yoki E'lon badge bosilgan |
| **Chiqish natijasi** | Uy egasi tavsiyalar asosida e'lonni yaxshilashi yoki narxni moslashtirishi mumkin |
| **Sseneriy ID** | UE-AI1 |

**Asosiy oqim — 'AI bo'yicha' tabi**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Tizim** | AI maslahat modali ochiladi: 'AI maslahat' sarlavhasi + X tugmasi; 2 tab: 'AI bo'yicha' (default) \| 'E'lon bo'yicha' |
| 2 | **Tizim** | Shaxsiylashtirilgan murojaat: 'Boy aka! Siz uchun, Bozorni analitika qilgan holatda, \[E'lon nomi\] uyingiz uchun maslahatlar tayyorlab qo'ydik' |
| 3 | **Tizim** | Narx gauge: chiziqli o'q (juda arzon ← yaxshi narx → qimmat narx); joriy narx pozitsiyasi marker bilan ko'rsatiladi |
| 4 | **Tizim** | Narx bo'yicha maslahat kartalari (ikonali): hudud o'rtacha narxi va tavsiya diapazon; mebel premium ta'siri (N%); jonivor ruxsati ta'siri (+N%) |
| 5 | **Tizim** | Joylashuv bo'yicha maslahat kartalari: e'lon sarlavhasiga qo'shilishi tavsiya etiladigan kalit so'zlar (metro yaqinligi va boshqalar) va ularning qidiruv ko'rsatkichiga ta'siri |

**Asosiy oqim — 'E'lon bo'yicha' tabi**

| **#** | **Aktyor** | **Amal** |
| --- | --- | --- |
| 1 | **Uy egasi** | 'E'lon bo'yicha' tabini bosadi |
| 2 | **Tizim** | E'lon statusi bloki: doira progress (N%), 'E'lon N% To'ldirilgan' + holat label (O'rtacha/Yaxshi/A'lo) |
| 3 | **Tizim** | 4 ta baholash bloki, har birida: ikona, nom, progress bar (qizil/sariq/yashil), 'Tahrirlash' tugmasi, tavsiya matni: |
| 4 | **Tizim** | Rasmlar — 'E'loningizda rasmlar yetarli emas. Planirovka va Oshxona rasmi mavjud emas' (progress: sariq) |
| 5 | **Tizim** | Tavsif — 'Tavsif juda qisqa. Tavsifni 200 tagacha so'zdan iborat text yozing' (progress: qizil) |
| 6 | **Tizim** | Uy qulayliklari — 'Uy qulayliklari yaxshi. Yana 2 tagacha qulaylik qo'shishingiz mumkin' (progress: yashil) |
| 7 | **Tizim** | Kommunal to'lovlar — 'Kommunal to'lovlarni kim to'lashi kerakligini ko'rsatmagansiz' (progress: qizil) |
| 8 | **Uy egasi** | 'Tahrirlash' tugmasini bosadi → to'g'ridan-to'g'ri tegishli bo'limning tahrirlash ekraniga o'tiladi |

**Muqobil oqimlar**

| **Holat** | **Oqim** |
| --- | --- |
| **X bosiladi** | Modal yopiladi; UE-S1 ga qaytiladi |
| **'AI bo'yicha' → 'E'lon bo'yicha' tab almashtirish** | Tab tarkibi almashadi; scroll pozitsiyasi saqlanmaydi |
| **Rasmlar 'Tahrirlash'** | E'lon rasmlari tahrirlash ekrani ochiladi |
| **Tavsif 'Tahrirlash'** | E'lon tavsif maydoni tahrirlash ekrani ochiladi |
| **Qulayliklar 'Tahrirlash'** | E'lon qulayliklari tahrirlash ekrani ochiladi |
| **Kommunal 'Tahrirlash'** | E'lon kommunal to'lovlar bo'limi tahrirlash ekrani ochiladi |

**Xatolik holatlari**

| **Holat** | **Tizim munosabati** |
| --- | --- |
| **Internet yo'q** | AI maslahat yuklanmaydi; 'Internet aloqasi yo'q' xabari; modal ochilmaydi |
| **AI servisi xatosi** | 'Maslahat hozircha mavjud emas' xabari; qayta urinish tugmasi |

**Biznes qoidalari**

| **# Qoida** |   |
| --- | --- |
| **BQ-1** | AI maslahat ma'lumotlari tanlangan mulk va joriy bozor ma'lumotlari asosida shakllantiriladi |
| **BQ-2** | Narx gauge ijarachining joriy narxini bozor o'rtachasi bilan taqqoslaydi |
| **BQ-3** | E'lon to'ldirilganlik foizi UE-S1 badge'i bilan bir xil qiymatda ko'rsatiladi |
| **BQ-4** | 'Tahrirlash' tugmasi to'g'ridan-to'g'ri tegishli bo'limning tahrirlash ekraniga olib boradi (umumiy tahrirlash emas) |
| **BQ-5** | Baholash bloklari rangi: <50% — qizil; 50–79% — sariq; 80%+ — yashil |

**Qabul qilish mezonlari (AC)**

| **# Mezon** |   |
| --- | --- |
| **AC-1** | AI maslahat modali ≤3 s ichida yuklanadi |
| **AC-2** | Narx gauge joriy e'lon narxini to'g'ri pozitsiyada ko'rsatadi |
| **AC-3** | E'lon to'ldirilganlik foizi UE-S1 dagi badge foizi bilan bir xil |
| **AC-4** | Har bir 'Tahrirlash' tugmasi bosilganda tegishli bo'lim tahrirlash ekrani ochiladi (boshqa bo'limga emas) |
| **AC-5** | Tab almashtirganda content ≤1 s ichida ko'rsatiladi |
