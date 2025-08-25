# Sales Analysis_LV

> Author: Emma Wang & Derek
>
> Create Date: 2025-07-13
>
> Version: 0.1
>
> Content: Initial version with data cleansing and transformation

---

## Background & Tasks

***Goal:*** 
需求: MTD, YTD 的YOY， Chaumet 占其他品牌的占比，和整体占比的MTD， YTD， YOY（份额的增加和减少）

## Data Cleansing

In Power Editors:

1. Import all stored data from Excel file.
2. Removed non-sense columns.
3. Removed null value from Brand.
4. Replace null value with 0.0.
5. Merged all data files as one (fact_sales)

![Data Cleansing](./01%20-%20data%20cleansing.png)

## Data Modeling

1. Create new table:

```sql
dim_calendar = 
var min_dt = MIN(fact_sales[Date])
var max_dt = MAX(fact_sales[Date])
return ADDCOLUMNS(
    CALENDAR(min_dt, max_dt),
    "dateid", FORMAT([Date], "yyyy-mm-dd"),
    "year", YEAR([Date]),
    "month", FORMAT([Date],"mm"),
    "year_month", FORMAT([Date],"yyyy-mm"),
    "year_month_abbr", FORMAT([Date], "mmm-yy"),
    "month_eng", FORMAT([Date], "mmmm"),
    "quarter", "Q" & FORMAT([Date], "Q"),
    "day_of_week", FORMAT([Date], "dddd"),
    "week_number", WEEKNUM([Date]),
    "week_day", WEEKDAY([Date]),
    "is_weekend", IF(WEEKDAY([Date], 2) >= 6, 1, 0),
    "start_of_week", [Date] - WEEKDAY([Date], 1) + 1
    )
```
![Data Modeling](./02%20-%20data%20modeling.png)

## DAX Design & Implementation

***Basic Measures***
1. Basic sales
```sql
sales = 
var a = CALCULATE(sum(fact_sales[Sales]))
return IF(ISBLANK(a), 0, a)
```
2. Sales MTD
```sql
sales_mtd = 
var a = CALCULATE([sales], DATESMTD(dim_calendar[dateid]))
return IF(ISBLANK(a), 0, a)
```
3. Sales MTD YoY
```sql
sales_mtd_yoy% = 
var a = [sales_mtd] - [sales_mtd_ly]
var b = DIVIDE(a, [sales_mtd_ly])
return IF(ISBLANK(b), 0, b)
```
4. Sales YTD
```sql
sales_ytd = 
var a = CALCULATE([sales], DATESYTD(dim_calendar[dateid]))
return IF(ISBLANK(a), 0, a)
```
5. Sales YTD YoY
```sql
sales_ytd_yoy% = 
var a = [sales_ytd] - [sales_ytd_ly]
var b = DIVIDE(a, [sales_ytd_ly])
return IF(ISBLANK(b), 0, b)
```

***Calculated Field***

6. Sales MTD Chaumet
```sql
sales_mtd_chaumet = 
var a = CALCULATE([sales_mtd], ALL(fact_sales[Brand]), fact_sales[Brand] = "Chaumet")
return IF(ISBLANK(a), 0, a)
```
7. Sales MTD Chaumet YoY
```sql
sales_mtd_chaumet_yoy% = 
var a = [sales_mtd_chaumet] - [sales_mtd_chaumet_ly]
var b = DIVIDE(a, [sales_mtd_chaumet_ly])
return IF(ISBLANK(b), 0, b)
```
8. Sales MTD Chaumet%
```sql
sales_mtd_chaumet% = 
DIVIDE([sales_mtd_chaumet], [sales_mtd])
```
9.  Sales YTD Chaumet
```sql
sales_ytd_chaumet = 
var a = CALCULATE([sales_ytd], ALL(fact_sales[Brand]), fact_sales[Brand] = "Chaumet")
return IF(ISBLANK(a), 0, a)
```
10. Sales YTD Chaumet YoY
```sql
sales_ytd_chaumet_yoy% = 
var a = [sales_ytd_chaumet] - [sales_ytd_chaumet_ly]
var b = DIVIDE(a, [sales_ytd_chaumet_ly])
return IF(ISBLANK(b), 0, b)
```
11. Sales YTD Chaumet%
```sql
sales_ytd_chaumet% = 
DIVIDE([sales_ytd_chaumet], [sales_ytd])
```
12. Sales MTD Total
```sql
sales_mtd_total = 
var a = CALCULATE([sales_mtd], ALL(fact_sales[Brand]))
return IF(ISBLANK(a), 0, a)
```
13. Sales MTD Total%
```sql
sales_mtd_total% = 
DIVIDE([sales_mtd], [sales_mtd_total])
```
14. Sales YTD Total
```sql
sales_ytd_total = 
var a = CALCULATE([sales_ytd], ALL(fact_sales[Brand]))
return IF(ISBLANK(a), 0, a)
```
15. Sales YTD Total%
```sql
sales_ytd_total% = 
DIVIDE([sales_ytd], [sales_ytd_total])
```

## Dashboard Design & Implementation

1. Chaumet Analysis, including MTD, YTD, YoY and Chaumet vs other Brand.

![Dashboard](./04%20-%20dashboard.png)

## Q&A

TBD
