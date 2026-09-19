# Shablon — har bir tugun `about.md` uchun

Har bir "leaf" (ekran/qadam) `about.md` fayli quyidagi tuzilishga amal qiladi. Bu standart butun `tz-mobile/` bo'yicha yagona. Bo'sh bo'limlarni tashlab ketmang — "yo'q" yoki "tegishli emas" deb yozing.

```markdown
# <Ekran / qadam nomi>

**Rollar:** 👤 Ijarachi / 🏠 Uy egasi / 👥 Mehmon    **Holat:** ✅ / 🟡 / ❌ / 💤

## TZ manbai
<Use-case ID (masalan U1) — nomi> · <bo'lim §> · <1–3 jumla qisqacha mazmun>
> Kerakli joyda TZ dan aniq iqtibos.

## Reliz / R5
- **RELIZ:** `<reliz papka / US ID>` — <asosiy qoidalar>
- **R5 o'zgarishi:** <delta, aks holda "yo'q">

## Bajarish tartibi
1. …
2. …

## Qabul kriteriyalari (BDD)
- **GIVEN** … **WHEN** … **THEN** …

## Kod joylashuvi
- **Modul:** `lib/features/<feature>`
- **Sahifa / BLoC:** `<Page>` / `<Bloc/Cubit>`
- **Endpoint:** `<METHOD /mobile/...>`

## Konflikt / farqlar
- ⚠ <TZ↔kod yoki TZ↔reliz farqi> → [`_konfliktlar.md`](../_konfliktlar.md)
- Yo'q bo'lsa: "Farq aniqlanmadi."
```

## Qoidalar

1. **Har bir tugun 4 manbani bog'laydi:** TZ use-case → reliz US → R5 delta → kod (modul/BLoC/endpoint).
2. **Holat majburiy** — ✅/🟡/❌/💤. Kod bilan solishtirib qo'yiladi.
3. **Iqtiboslar aniq** — TZ/reliz matnidan o'zgartirmasdan; uzun matn qisqartiriladi (`…`).
4. **Konflikt bo'lsa ⚠ bilan belgilanadi** va markaziy `_konfliktlar.md` ga havola beriladi.
5. **Papka `about.md`** = o'sha bo'lim indeksi (quyi tugunlar ro'yxati + umumiy oqim); "leaf" `about.md`/`*.md` = to'liq shablon.
6. **Havolalar** nisbatan (relative) markdown link'lar bilan.
