# Meeting Memo

> Author: Derek
> 
> Date: 2025-05-14

---

## Data Exploration

**Staffing Manpower**

Structures

- In the door (Total hired)
- On the floor（actual working）

Total Balance_to_Go - Data will be decrease, like burning-down chart.

## Visual

1. Trending of Actual / NCO Created
2. Balance to Go, Line Chart (Production Rate%)

## KPIs

1. Production rate% = SUM( Actual + NCO Closed) / Staff on Floor

2. Actual vs ***Plan*** (Per Aircraft or Barge) = 

3. NCO Closed vs ***Planned to-be Closed*** = 

## Follow up actions:

1. Historical Data:
- Actuals
- NCOs Closed	
- NCOs Created

2. Score Card:
- Historical Data with Excel file format & Sheet name "Table 1"

3. Target Data for actual and NCO Closed

4. Staff on Floor - Add Aircraft info

## 关键DAX

> DAX (Data Analysis Expression)

``` sql
balance_wtd = 
var currentdate = MAX('Calendar'[Date])
var startofweek = currentdate - WEEKDAY(currentdate, 1) + 1
RETURN
CALCULATE([balance],
DATESBETWEEN(
    'Calendar'[Date],
    startofweek,
    currentdate
)
)
```


``` sql
balance_wtd_lw = 
var currentdate = MAX('Calendar'[Date])
var startofthisweek = currentdate - WEEKDAY(currentdate, 1) + 1
var startoflastweek = startofthisweek - 7
var endoflastweek = startofthisweek - 1
RETURN
CALCULATE([balance],
DATESBETWEEN(
    'Calendar'[Date],
    startoflastweek,
    endoflastweek
)
)
```