#





##



```sql
Calendar = 
var min_dt = MIN('fact'[月份])
var max_dt = MAX('fact'[月份])
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


```sql
measurement = ROW("kpi_id", BLANK(), "kpi_name", BLANK())
```