# 7-7 SLA countdown

## Ishlash prinsipi

- deadline = so'rov vaqti + 24 soat; countdown real vaqtda; muddati o'tsa holat "ko'rib chiqilmagan" + ikki tomonga push; 7 soatdan kam qolganda qizil. `R5`
  > ❓ Ichki nomuvofiqlik: R5 · R5-UE-02 da — 1 soatdan kam qolganda qizil
  >
  > Izoh: asosiy sahifa qiymati (7 soat) olindi — tasdiqlash kerak (N1). 7 kunlik eski muddat bo'yicha konflikt — [4-5 SLA va javob vaqti](<../../4.Mobil ilova — Uy egasi/4-5 SLA va javob vaqti/about.md>).
- "Ko'rib chiqilmagan" holati yakuniy rad emas — keyin ham javob berish mumkin; push eslatmalar 12 va 22-soatlarda; SLA parametri sozlanadi `R5`
- GIVEN SLA muddati 24 dan boshqa qiymatga o'zgartirildi WHEN yangi so'rov kelsa THEN countdown yangi muddat bilan boshlanadi (mavjud so'rovlarning deadline'i o'zgarmaydi) `R5 · R5-AD-01`

## Sozlanadigan parametrlar

- SLA muddati (soat); ogohlantirish chegarasi `R5`
