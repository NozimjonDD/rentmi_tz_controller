# Navigatsiya (pastki navbar)

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi / 👥 Mehmon    **Holat:** 🟡 Qisman (R5 targetga nisbatan)

## TZ manbai
§4.1.7.3 — Grafik interfeysga talablar: barcha ekran shakllari yagona dizaynda, interfeys elementlari va navigatsiyaning bir xil joylashuvi bilan bajariladi. Navbar tarkibi TZ da qat'iy sanab o'tilmagan.
> «Barcha ekran shakllari yagona grafik dizaynda, interfeys elementlari va navigatsiyaning bir xil joylashuvi bilan bajariladi.»

## Reliz / R5
- **RELIZ (R5-IJ-01):** «Yangi pastki navbar: **Main, Saved (Saqlanganlar), Lenta (e'lonlar lentasi), So'rovlar, Profil**», «Chat tugmasini tepaga, bildirishnoma tugmasi yoniga chiqarish (unread badge bilan); tepadagi profil olib tashlanadi».
- **R5 o'zgarishi:** navbar to'liq qayta ishlangan (yuqoridagi target); `Saved` tab qo'shilishi ko'zda tutilgan.

## Bajarish tartibi
1. Kod ikki alohida shell'dan iborat (rol bo'yicha ajratilgan).
2. **Landlord shell** (`main_page.dart`, `FloatingPillNavBar`): **Portfelim / Chat / So'rovlar / Profil / +Qo'shish**.
3. **Tenant shell** (`tenant_dashboard_page.dart`): **Home / Chat / Lenta (Feed) / So'rovlar / Filter (detached)**; Profil — home header avatar orqali.
4. Guest tenant shell'dan foydalanadi.

## Qabul kriteriyalari (BDD)
- **GIVEN** uy egasi **WHEN** ilovaga kiradi **THEN** landlord navbar: Portfelim / Chat / So'rovlar / Profil / +Qo'shish.
- **GIVEN** ijarachi yoki guest **WHEN** ilovaga kiradi **THEN** tenant navbar: Home / Chat / Lenta / So'rovlar / Filter; Profil header avatar orqali.
- **GIVEN** R5 talabi **WHEN** navbar tekshiriladi **THEN** 'Saved' tab kutiladi — kodda mavjud emas (⚠).

## Kod joylashuvi
- **Landlord:** `lib/features/main/.../main_page.dart` (`FloatingPillNavBar`)
- **Tenant:** `lib/features/tenant_dashboard/.../tenant_dashboard_page.dart`
- **Endpoint:** yo'q (navigatsiya klient tomonda).

## Konflikt / farqlar
- ⚠ **'Saved' tab yo'q:** R5 «Main / Saved / Lenta / So'rovlar / Profil» ni talab qiladi, kodda tenant shell'da **Saved tab yo'q** (Home / Chat / Lenta / So'rovlar / Filter). → [`_konfliktlar.md`](../_konfliktlar.md)
- ⚠ R5 «Chat tugmasini tepaga» va «tepadagi profil olib tashlanadi» deydi; kodda Chat ikkala navbar'da tab sifatida, Profil tenant'da header avatar orqali.
