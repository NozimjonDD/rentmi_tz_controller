4.1.6.2. Ma'lumotlarni ruxsatsiz kirishdan himoya qilishga talablar

Tizim quyidagi himoya mexanizmlarini qo'llashi lozim:

- foydalanuvchi parollari va PIN-kodlari bir tomonlama xeshlash (bcrypt, Argon2 kabi algoritmlar) orqali saqlanishi;
- shaxsiy ma'lumotlar (pasport ma'lumotlari, aloqa ma'lumotlari) ma'lumotlar bazasida shifrlangan holda saqlanishi;
- tizim va foydalanuvchi o'rtasidagi barcha aloqa HTTPS (TLS 1.2 va undan yuqori versiyalari) protokoli orqali himoyalanishi;
- API darajasidagi so'rovlar autentifikatsiya tokenlari (JWT, OAuth 2.0 yoki shunga o'xshash mexanizmlar) orqali himoyalanishi;
- noto'g'ri autentifikatsiya urinishlari soni belgilangan miqdordan oshganda(ketma-ket 3 marta) hisob 10 daqiqaga vaqtinchalik bloklanishi;
- tizim SQL injeksiyalari, XSS, CSRF va boshqa OWASP Top 10 hujumlariga qarshi himoya mexanizmlari bilan jihozlanishi;
- foydalanuvchining shaxsiy ma'lumotlariga kirish bo'yicha barcha operatsiyalar audit jurnalida qayd etilishi.
