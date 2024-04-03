# django 를 이용한 카페 키오스크 프로그램만들기.

### DB(menu,customer,order,kategorie,Logs)
---
- **customer/order**:(1:N)
- **order/menu**:(N:M)
- **menu/kategorie**:(N:1)
- **Logs**:별도 시스템에서 발생하는 다양한 이벤트를 기록
### 관계도
---

## Table
### Customer
---
- Customer ID           /PK
- Name                  /char
- PhoneNumber           /int

### Order
---
- Order ID              /PK
- Customer ID <-Customer/FK
- OrderDate             /dateTime
- TotalPrice            /int

### Menu
---
- Menu ID               /PK
- Category ID <-Category/FK
- Quantity              /int
- Name                  /char
- Price                 /int

### OrderMenu(연결 테이블)
---
- OrderMenu ID          /PK
- Order ID <-Order      /FK
- Menu ID <-Menu        /FK
- Quantity              /int
- ItemsPrice            /int

### Category
---
- Category ID           /PK
- Name                  /char

### Logs
---
- Log ID                /PK
- Type                  /str
- Timestamp             /dateTime

## 2024 04 03
-