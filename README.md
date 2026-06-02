# fastapi-soldiers-management

### Required Endpoints

| Method     | Path             | Action (פעולה)     | Response Code (קוד תשובה) |
| :--------- | :--------------- | :----------------- | :------------------------ |
| **GET**    | `/soldiers`      | קבלת כל החיילים    | 200                       |
| **GET**    | `/soldiers/{id}` | קבלת חייל לפי מזהה | 404 / 200                 |
| **POST**   | `/soldiers`      | הוספת חייל חדש     | 201                       |
| **PUT**    | `/soldiers/{id}` | עדכון חייל קיים    | 404 / 200                 |
| **DELETE** | `/soldiers/{id}` | מחיקת חייל         | 404 / 200                 |
