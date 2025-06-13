# Reps Sales Performance Analysis

> Author: Nick & Derek
>
> Create Date: 2025-06-12
>
> Version: 0.1
>
> Content: Initial version with data cleansing and transformation

---

## Background & Tasks

## 颜色区分

#00EE00

#FF0000

***Analysis Exchange Rate with SGD & CNY against MYR***

- 至少两种以适当标签或表格形式呈现的描述性分析；

- 至少两种以适当图表或图表显示表示的图表分析；

- 至少两个可以进行交互的数据过滤菜单或选项，可以与上述描述性分析或图表分析之一或全部进行交互。

---

## Data Cleansing

1. A simple data file contains 2 exchanges rate:
   - `SGD` exchange rate to MYR
   - `CNY` exchange rate to MYR

2. `date` column formatted as `yyyy-mm-dd` to meet data modeling requirement.
---

![data cleansing & transformation](./01%20-%20data%20cleansing%20&%20transformation.png)

## Data Modeling

1. A calendar table is created for a many:1 relationship with `exchange_rate` table

```sql
calendar = 
var min_dt = MIN(exchange_rate[Date])
var max_dt = MAX(exchange_rate[Date])
return ADDCOLUMNS(
    CALENDAR(min_dt, max_dt),
    "dateid", FORMAT([Date], "yyyy-mm-dd"),
    "year", YEAR([Date]),
    "month", MONTH([Date]),
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

`dateid` is converted to `date` type, and will be used for the relationship in Power BI Model view.

![data modeling](./02%20-%20data%20modeling.png)

## DAX Design & Implementation

1. A measurement table is created to categorize different measures.

```sql
measurement = ROW("kpi_id", BLANK(), "kpi_name", BLANK())
```

2. Basic measurement

- SGD rate



## Dashboard Design & Implementation


## Q&A