# Konfliktlar va farqlar (web qismi)

Web qismi quyi tizimiga tegishli ziddiyatlar. Har bir `about.md`/leaf shu yerdagi **W-** ID'larga havola qiladi. To'liq spec-tahlil (mobil bilan birga): loyiha ildizidagi `TZ_konflikt_report.html`.

## TZ ichidagi ziddiyatlar (web use-case'larga tegishli)

| ID | Mavzu | Bir joyda | Boshqa joyda | Flow |
|---|---|---|---|---|
| **W-A1** | Hisobot shakllantirish vaqti | §2.2 va §4.1.4.1: **≤10 sek** | **A2** va **A4** ssenariylari: **≤30 sek** | [03](03-administratorlik/about.md), [04](04-billing-nazorati/about.md) |
| **W-A3** | Call-markaz operatori huquqi | §4.1.3.2 + §4.2.2: **«Faqat ko'rish (o'qish) huquqiga ega»** | **T3** ssenariysi: operator **«yangi ticket yaratadi»** (yozish amali) | [06](06-support-callmarkaz/about.md) |
| **W-A4** | Support xodimi ma'lumot doirasi | §4.1.3.2: **«anonimlashtirilgan analitikaga cheklangan kirish»** | **A2**: support «foydalanuvchilar, to'lovlar, skoring» hisobotlarini shakllantiradi (shaxsiy/moliyaviy) | [03](03-administratorlik/about.md), [07](07-rollar-va-rbac/about.md) |
| **W-A6** | «superadmin» roli ta'riflanmagan | U2-veb, U2a, §4.2.2 da faol ishlatiladi | §4.1.3.2 rollar ro'yxatida **yo'q** (faqat «Administrator») | [01](01-autentifikatsiya/about.md), [07](07-rollar-va-rbac/about.md) |
| **W-B2** | §4.1.11 ga uzilgan havola | §4.3.2: «klassifikatorlar… batafsil **4.1.11 bandida**» | §4.1.11 **mavjud emas** (klassifikatorlar E5 — kataloglar boshqaruvida) | [02](02-moderatsiya/about.md) |
| **W-B3** | A3/A4 tartibi buzilgan | Ssenariylar ro'yxatida **A4** (to'lovlar) **A3** (integratsiya) dan oldin | — | [04](04-billing-nazorati/about.md), [05](05-integratsiya/about.md) |

## Kod / spetsifikatsiya holati

| ID | Mavzu | Izoh |
|---|---|---|
| **W-K1** | Web kodbaza yo'q | VueJS admin panel kodi taqdim etilmagan → barcha «Backend/API» bo'limlari TZ asosida **taxminiy**; endpointlar aniq emas |
| **W-K2** | reliz admin bo'limi to'liq emas | `reliz/` eksportida "6. Admin panel" bo'limi to'liq yo'q; R5 PDF faqat qisman (algoritm parametrlari, SLA monitoring) beradi |
| **W-C3** | So'rov SLA (mobil bilan bog'liq) | R5 admin panelda **SLA monitoring** (24 soat) qo'shilgan (R5-AD-02); TZ R2 da 7 kun — mobil tomonda ham konflikt (C3) | 

## Umumiy tavsiya
1. **superadmin** rolini §4.1.3.2 ga rasman qo'shish (W-A6).
2. **RBAC matritsasini** TZ ichiga kiritish — W-A3, W-A4 shundan kelib chiqadi ([07](07-rollar-va-rbac/about.md)).
3. Hisobot vaqti (W-A1) va A3/A4 tartibini (W-B3) yagona qilish.
4. Web repo berilsa — "Backend/API" bo'limlarini real endpoint bilan to'ldirish (W-K1).
