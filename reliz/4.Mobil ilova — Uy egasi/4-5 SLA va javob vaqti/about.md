# 4-5 SLA va javob vaqti

**Manba:** [R4 · 4. Bajariladi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29425665) · [R5 · 4. Bajariladi](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843819) · [R5-UE-02](<R5-UE-02 SLA 24 soat va countdown/about.md>) · [R5-UE-03](<R5-UE-03 Javob vaqti indikatori/about.md>)

## Joriy talablar

- SLA 24 soat: har yangi so'rovda "Javob berishingiz kerak: HH:MM:SS" countdown; 7 soatdan kam qolganda qizil; muddati o'tsa so'rov "ko'rib chiqilmagan" holatiga o'tadi va ikki tomonga push (TZ dagi 7 kun o'rniga 24 soat — ichki qaror sifatida hujjatlashtiriladi) `R5`
  > ⚠ Konflikt: R4 da — 7 kun davomida ko'rib chiqilmagan so'rovlar avtomatik 'Ko'rib chiqilmagan' deb belgilanadi, ikki tomonga FCM push yuboriladi
  >
  > ⚠ Konflikt: R4 · UE-R4 BQ-3 da — 7 kun ko'rib chiqilmagan so'rov avtomatik 'ko'rib chiqilmagan' holatga o'tadi; faqat uy egasiga push yuboriladi (ijarachiga emas)
  >
  > ⚠ Konflikt: R4 · IJ-R2 BQ-4 da — 7 kun ko'rib chiqilmagan so'rov 'Ko'rib chiqilmadi' holatiga o'tadi; faqat uy egasiga push yuboriladi
  >
  > ❓ Ichki nomuvofiqlik: R5 · R5-UE-02 da — 1 soatdan kam qolganda qizil
  >
  > Izoh: R5 asosiy sahifasida (4 joyda) "7 soatdan kam qolganda qizil", R5-UE-02 user story'da "1 soatdan kam". Asosiy sahifa keyinroq tahrirlangan (16.08.2026 12:29; user story — 12:01), shuning uchun 7 soat olindi — tasdiqlash kerak (N1).
- "Diqqat talab qiladi" bloki asosiy sahifada: javob kutayotgan arizalar soni, eng eskisiga qolgan vaqt `R5`
- Eslatma pushlari 12- va 22-soatlarda. `R5 · R5-UE-02`
- "Ko'rib chiqilmagan" yakuniy rad emas — keyin ham javob berish mumkin. `R5 · R5-UE-02`
- Har so'rov bo'yicha first_response_time yoziladi. `R5 · R5-UE-03`
- Ko'rsatkich — oxirgi 30 kun medianasi, soatlik pog'onaga yaxlitlanadi ("odatda 1 soat ichida javob beradi", "odatda 2 soatda"...). `R5 · R5-UE-03`
- Kamida 3 ta javob bo'lsagina e'lon sahifasida va ommaviy profilda chiqadi. `R5 · R5-UE-03`
- Javob vaqti indikatori uy egasiga tushuntiriladi: onboarding tooltip — tez javob berish arizalar sonini oshirishi haqida `R5`

Algoritmlar: [7-6 Javob vaqti indikatori](<../../7.Algoritmlar/7-6 Javob vaqti indikatori/about.md>), [7-7 SLA countdown](<../../7.Algoritmlar/7-7 SLA countdown/about.md>).

## Use case'lar

| ID | Nomi | Reliz | Holati |
| --- | --- | --- | --- |
| [UE-R4](<../4-4 So'rovlar boshqaruvi/UE-R4 So'rovni qabul qilish yoki rad etish/about.md>) | So'rovni qabul qilish yoki rad etish (7 kun) | R4 | ⚠ R5 bilan almashtirilgan |
| [R5-UE-02](<R5-UE-02 SLA 24 soat va countdown/about.md>) | SLA 24 soat va countdown | R5 | Joriy; ❓ qizil chegarasi |
| [R5-UE-03](<R5-UE-03 Javob vaqti indikatori/about.md>) | Javob vaqti indikatori | R5 | Joriy |
