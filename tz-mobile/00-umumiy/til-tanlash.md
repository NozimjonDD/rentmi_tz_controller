# Til tanlash

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi / 👥 Mehmon    **Holat:** ✅ Bajarilgan

## TZ manbai
§4.3.3 — Lingvistik ta'minotga talablar. Interfeys 4 tilni qo'llab-quvvatlaydi; til birinchi kirishda tanlanadi va keyinchalik sozlamalarda o'zgartiriladi.
> «o'zbek tili (lotin alifbosida); o'zbek tili (kirill alifbosida); rus tili; ingliz tili.»
> «Foydalanuvchi birinchi kirishda interfeys tilini tanlaydi va keyinchalik sozlamalarda o'zgartirishi mumkin.»

## Reliz / R5
- **RELIZ:** `2-2 Til tanlash / US 2 LS` — «Language selection majburiy bosqich», «Default language: Uzbek Latin», «Tanlov backend profile qismida saqlanadi», «Keyinchalik settingsdan o'zgartiriladi», «4 ta til qo'llab-quvvatlash» (uzb lotin, rus, uzb kiril, english).
- **R5 o'zgarishi:** yo'q.

## Bajarish tartibi
1. Splashdan keyin full-screen til tanlash ochiladi (`/language-selection`).
2. Foydalanuvchi 4 tildan birini tanlaydi: **uz (lotin) / uz (kirill) / ru / en**.
3. `LocaleProvider` orqali UI darhol shu tilga o'tadi.
4. Tanlov `SharedPreferences` (`language`) ga saqlanadi; default — uz-latin.
5. Keyinchalik profil sozlamalari (`language_settings_page`) orqali o'zgartiriladi.

## Qabul kriteriyalari (BDD)
- **GIVEN** til tanlash ekrani **WHEN** foydalanuvchi til tanlaydi **THEN** UI shu tilda ko'rsatiladi va tanlov saqlanadi.
- **GIVEN** foydalanuvchi til tanlamaydi **WHEN** tizim davom etadi **THEN** default o'zbek (lotin) qo'llaniladi.
- **GIVEN** sozlamalar **WHEN** foydalanuvchi tilni o'zgartiradi **THEN** UI qismi yangilanadi.

## Kod joylashuvi
- **Modul:** `lib/features/core_screens/language`
- **Sahifa / BLoC:** `language_selection_page` / `LanguageBloc` + `LocaleProvider` (Provider — TZ da yagona Provider ishlatilishi shu; qolgan hammasi BLoC/Cubit)
- **Route:** `/language-selection`
- **Saqlash:** `SharedPreferences` kalit `language` (default uz-latin)
- **Endpoint:** aniqlanmagan (kodda mahalliy saqlash).

## Konflikt / farqlar
- ⚠ Reliz «tanlov backend profile qismida saqlanadi» deydi; kodda til **mahalliy** `SharedPreferences` (`language`) da saqlanadi — backend profilga sinxron aniqlanmadi (guest uchun backend hisobi ham yo'q). → [`_konfliktlar.md`](../_konfliktlar.md)
