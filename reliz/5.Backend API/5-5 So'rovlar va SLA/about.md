# 5-5 So'rovlar va SLA

**Manba:** [Release 4 14.06.2026 (Confluence)](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29425665) · [Release 5 17.08.2026 (Confluence)](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843819)

- So'rov yaratish endpointi: POST /requests — ijarachi tomonidan, e'lon identifikatori + xabar `R4`
- Rentmi bali tekshiruvi (S1 trigger): so'rov yuborishda ball tekshiriladi, yo'q bo'lsa xarid taklifi qaytariladi `R4`
- Duplikat so'rov bloklash: bir e'lon bo'yicha faol so'rov mavjud bo'lsa yangi so'rov rad etiladi `R4`
- Blacklist tekshiruvi: ijarachi blacklist'da bo'lsa so'rov bloklash `R4`
- So'rovlar ro'yxati (ijarachi): GET /requests?role=tenant — holat, sana filtrlari `R4`
- So'rovlar ro'yxati (uy egasi): GET /requests?role=landlord&listing_id=X — e'lon bo'yicha, tabs `R4`
- So'rov tafsiloti: GET /requests/{id} — Rentmi skore, to'lov intizomi, ijara tarixi `R4`
- Qaror endpointi: PATCH /requests/{id}/decision — approve | reject `R4`
- Tasdiqlashda kontakt ochilish: ijarachiga uy egasining telefon raqami qaytariladi `R4`
- SLA mexanizmi: so'rov holati state machine'iga "bekor qilingan" qo'shiladi; 24 soatlik deadline maydoni; scheduler — muddati o'tganlarni "ko'rib chiqilmagan"ga o'tkazish va push; first_response_time yozuvi `R5`
  > ⚠ Konflikt: R4 da — 7-kun auto-expire: scheduler — ko'rib chiqilmagan so'rovlar avtomatik 'ko'rib chiqilmagan' holatga o'tadi, ikki tomonga FCM push
- So'rov holati state machine: pending → approved | rejected | expired `R4`
  > Izoh: R5 da state machine'ga "bekor qilingan" holati qo'shiladi (yuqorida).
- Javob vaqti agregati: uy egasi bo'yicha oxirgi 30 kun mediana; kamida 3 ta javob bo'lsagina ko'rsatiladi; soatlik pog'onalarga yaxlitlash `R5`
