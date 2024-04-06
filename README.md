# django 를 이용한 카페 키오스크 프로그램만들기.

### DB(menu,customer,order,kategorie,Logs)
---
- **customer/order**:(1:N)
- **order/menu**:(N:M)
- **menu/kategorie**:(N:1)
- **Logs**:별도 시스템에서 발생하는 다양한 이벤트를 기록
### 관계도
---
![alt text](image.png)

## Table
### Customer
---
- Customer ID           /PK
- Name                  /str
- PhoneNumber           /str

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
- Name                  /str
- Price                 /int

### OrderMenu(연결 테이블)
---
- OrderMenu ID          /PK
- Order ID <-Order      /FK
- Menu ID <-Menu        /FK
- Order_Quantity        /int
- ItemsPrice            /int

### Category
---
- Category ID           /PK
- Name                  /str

### Logs
---
- Log ID                /PK
- Type                  /str
- Timestamp             /dateTime

## 2024 04 03
-
## 2024 04 06
### 고쳐야할것
---
1 menu Quantity 값이 0일때 더이상 선택을 할 수없게 바꾸기
2 결제 버튼 만들고 누르면 order.html 로 넘어가게/order.html 페이지 구성하기
3 페이지 꾸미기 