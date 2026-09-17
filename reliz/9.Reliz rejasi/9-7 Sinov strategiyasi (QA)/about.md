# 9-7 Sinov strategiyasi (QA)

**Manba:** [Release 5 17.08.2026 (Confluence)](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/43843819) (11-bo'lim)

| Sinov turi | Maqsad |
| --- | --- |
| Unit / integration | Badge qoidalari (har bir shart alohida), moslik mantig'i, top formula, mediana hisobi, SLA scheduler, narx tarixi trigger, bekor qilish state machine |
| UI/UX funksional | 19 ta use case bo'yicha ssenariylar, iOS va Android; yangi navbar; countdown vizual holatlari |
| Regressiya | R1–R4: login, skoring, e'lon CRUD, qidiruv, so'rov, chat buzilmaganligi; yashirilgan stories ta'sir qilmasligi |
| Performance | Asosiy sahifa ≤3s (badge'lar keshdan), xarita ≤5s, skoring-mos blok ≤3s |
| Edge case | SLA: aynan 24:00:00 chegarasi, vaqt zonasi; bekor qilish poygasi (uy egasi ayni paytda qabul qilsa); badge: tegishlilik ma'lumoti yo'q holati |
| UAT | Pilot ijarachilar (5–10) va uy egalari (3–5) bilan yangi oqimlarni real qurilmalarda sinash |
