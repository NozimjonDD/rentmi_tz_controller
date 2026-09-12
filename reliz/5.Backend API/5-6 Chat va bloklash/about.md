# 5-6 Chat va bloklash

**Manba:** [Release 4 14.06.2026 (Confluence)](https://rentmi.atlassian.net/wiki/spaces/~71202079d067c95f7a441fb0ca94a54260ce25/pages/29425665)

- Chat messaging: POST /chats/{id}/messages — asinxron xabar yuborish `R4`
- Chat xabarlar tarixi: GET /chats/{id}/messages — pagination bilan `R4`
- Rasm yuklash (chat): S3 orqali, URL qaytariladi `R4`
- Xabar o'chirish: DELETE /chats/{id}/messages/{msg_id} `R4`
- Block funksionali: POST /users/{id}/block — sabab va to'liq bloklash mantig'i `R4`
