# Web / admin API xaritasi (kutilayotgan)

> ⚠ **Muhim:** Web (VueJS admin panel) kodbazasi taqdim etilmagan. Quyidagi endpointlar **TZ use-case'lari asosida mantiqan kutiladi** — aniq yo'llar (namespace, nom) web repo berilganda tasdiqlanishi kerak. Bular tayyor kontrakt emas, **taxminiy xarita**. (Mobil endpointlar tasdiqlangan: [`../tz-mobile/_endpointlar.md`](../tz-mobile/_endpointlar.md).)

Namespace ehtimoli: `/admin/...` yoki umumiy `/api/v1/...` (mobil `/mobile/...` dan farqli).

## 01 — Autentifikatsiya
| Amal | Kutilayotgan endpoint |
|---|---|
| Web kirish (U2-veb) | `POST /admin/auth/login/` `{username, password}` → JWT |
| Parol tiklash (U2a, superadmin) | `POST /admin/users/{id}/password/reset/` |

## 02 — Moderatsiya
| Amal | Kutilayotgan endpoint |
|---|---|
| Moderatsiya navbati (E4) | `GET /admin/moderation/announcements/?status=pending` |
| Qaror (tasdiqlash/rad/tuzatish) | `PATCH /admin/announcements/{id}/moderate/` `{decision, reason?}` |
| Kataloglar ro'yxati (E5) | `GET /admin/catalogs/{type}/` |
| Katalog CRUD | `POST/PUT/PATCH /admin/catalogs/{type}/{id}/` |

## 03 — Administratorlik
| Amal | Kutilayotgan endpoint |
|---|---|
| Foydalanuvchilar (A1) | `GET /admin/users/?role=&status=` · `GET /admin/users/{id}/` |
| Bloklash/rol/blacklist | `PATCH /admin/users/{id}/` `{action, reason}` |
| Hisobotlar (A2) | `GET /admin/reports/{type}/?period=&filters=` |
| Eksport | `GET /admin/reports/{type}/export/?format=pdf|xlsx|csv` |

## 04 — Billing nazorati
| Amal | Kutilayotgan endpoint |
|---|---|
| Tranzaksiyalar (A4) | `GET /admin/payments/?status=&provider=&period=` |
| Tafsilot / reconciliation | `GET /admin/payments/{id}/` · `POST /admin/payments/{id}/reconcile/` |
| Billing hisoboti | `GET /admin/reports/billing/` |

## 05 — Integratsiya boshqaruvi
| Amal | Kutilayotgan endpoint |
|---|---|
| Integratsiyalar holati (A3) | `GET /admin/integrations/` |
| Sozlash (endpoint/kalit/timeout) | `PATCH /admin/integrations/{id}/` (kalit shifrlangan) |
| Sinov so'rovi | `POST /admin/integrations/{id}/test/` |
| Yoqish/o'chirish | `PATCH /admin/integrations/{id}/toggle/` |

## 06 — Texnik qo'llab-quvvatlash + call-markaz
| Amal | Kutilayotgan endpoint |
|---|---|
| Murojaatlar (T2) | `GET /admin/tickets/?status=` · `PATCH /admin/tickets/{id}/` |
| Eskalatsiya | `POST /admin/tickets/{id}/escalate/` |
| Call-markaz ticket (T3) | `POST /admin/tickets/` `{user, category, subject, description}` |
| Foydalanuvchini topish (faqat o'qish) | `GET /admin/users/?search=` |

## R5 — Admin panel qo'shimchalari
| Amal | Kutilayotgan endpoint | Manba |
|---|---|---|
| Algoritm parametrlari (Top og'irliklari, SLA muddati, "narxi tushdi" %) | `GET/PATCH /admin/settings/algorithm/` | R5-AD-01 |
| SLA monitoring (muddati o'tgan so'rovlar) | `GET /admin/monitoring/sla/` | R5-AD-02 |

---
> Barcha web operatsiyalari JWT + RBAC tekshiruvidan o'tadi va audit jurnaliga yoziladi ([`_talablar.md`](_talablar.md)).
