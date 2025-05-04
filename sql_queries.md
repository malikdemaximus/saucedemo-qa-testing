## 📌 Примеры SQL для тестирования  
```sql
-- Проверка пользователей в базе  
SELECT * FROM users WHERE login = 'standard_user';  

-- Поиск заказов за сегодня  
SELECT * FROM orders WHERE date = CURRENT_DATE;  
```  
