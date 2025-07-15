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
Calendar = 
VAR min_dt = MIN('fact'[月份])
VAR max_dt = MAX('fact'[月份])
RETURN
ADDCOLUMNS(
    CALENDAR(min_dt, max_dt),
    "dateid", FORMAT([Date], "yyyy-MM-dd"),
    "year", YEAR([Date]),
    "month", FORMAT([Date],"MM"),
    "year_month", FORMAT([Date],"yyyy-MM"),
    "year_month_abbr", FORMAT([Date], "mmm-yy"),
    "month_eng", FORMAT([Date], "mmmm"),
    "quarter", "Q" & FORMAT([Date], "Q"),
    "day_of_week", FORMAT([Date], "dddd"),
    "week_number", WEEKNUM([Date]),
    "week_day", WEEKDAY([Date]),
    "is_weekend", IF(WEEKDAY([Date], 2) >= 6, 1, 0),
    "start_of_week", [Date] - WEEKDAY([Date], 2) + 1,
    "fiscal_year", IF(MONTH([Date]) >= 4, YEAR([Date]), YEAR([Date]) - 1),
    "is_holiday", 
        SWITCH(TRUE(),
            [Date] = DATE(YEAR([Date]),1,1), 1,
            [Date] >= DATE(YEAR([Date]),1,28) && [Date] <= DATE(YEAR([Date]),2,4), 1,
            [Date] = DATE(YEAR([Date]),4,4), 1,
            [Date] >= DATE(YEAR([Date]),5,1) && [Date] <= DATE(YEAR([Date]),5,5), 1,
            [Date] >= DATE(YEAR([Date]),5,31) && [Date] <= DATE(YEAR([Date]),6,2), 1,
            [Date] = DATE(YEAR([Date]),10,6), 1,
            [Date] >= DATE(YEAR([Date]),10,1) && [Date] <= DATE(YEAR([Date]),10,8), 1,
            0
        ),
    "holiday_name",
        SWITCH(TRUE(),
            [Date] = DATE(YEAR([Date]),1,1), "New Year's Day",
            [Date] >= DATE(YEAR([Date]),1,28) && [Date] <= DATE(YEAR([Date]),2,4), "Spring Festival",
            [Date] = DATE(YEAR([Date]),4,4), "Qingming Festival",
            [Date] >= DATE(YEAR([Date]),5,1) && [Date] <= DATE(YEAR([Date]),5,5), "Labor Day",
            [Date] >= DATE(YEAR([Date]),5,31) && [Date] <= DATE(YEAR([Date]),6,2), "Dragon Boat Festival",
            [Date] = DATE(YEAR([Date]),10,6), "Mid-Autumn Festival",
            [Date] >= DATE(YEAR([Date]),10,1) && [Date] <= DATE(YEAR([Date]),10,8), "National Day",
            BLANK()
        )
)
```


```sql
Calendar = 
VAR min_dt = MIN('fact'[月份])
VAR max_dt = MAX('fact'[月份])
RETURN
ADDCOLUMNS(
    CALENDAR(min_dt, max_dt),
    "dateid", FORMAT([Date], "yyyy-MM-dd"),
    "year", YEAR([Date]),
    "month", FORMAT([Date],"MM"),
    "year_month", FORMAT([Date],"yyyy-MM"),
    "year_month_abbr", FORMAT([Date], "mmm-yy"),
    "month_eng", FORMAT([Date], "mmmm"),
    "quarter", "Q" & FORMAT([Date], "Q"),
    "day_of_week", FORMAT([Date], "dddd"),
    "week_number", WEEKNUM([Date]),
    "week_day", WEEKDAY([Date]),
    "is_weekend", IF(WEEKDAY([Date], 2) >= 6, 1, 0),
    "start_of_week", [Date] - WEEKDAY([Date], 2) + 1,
    "fiscal_year", IF(MONTH([Date]) >= 4, YEAR([Date]), YEAR([Date]) - 1),
    "is_holiday", 
        SWITCH(TRUE(),
            // New Year's Day
            FORMAT([Date], "MM-dd") = "01-01", 1,
            // Qingming (approx Apr 4 or 5)
            FORMAT([Date], "MM-dd") = "04-04" || FORMAT([Date], "MM-dd") = "04-05", 1,
            // Labor Day
            FORMAT([Date], "MM-dd") = "05-01", 1,
            // National Day
            FORMAT([Date], "MM-dd") >= "10-01" && FORMAT([Date], "MM-dd") <= "10-07", 1,
            // Estimated Spring Festival (Lunar New Year)
            [Date] IN {
                DATE(2026,2,17), DATE(2027,2,6), DATE(2028,1,26),
                DATE(2029,2,13), DATE(2030,2,3), DATE(2031,1,23),
                DATE(2032,2,11), DATE(2033,1,31), DATE(2034,2,19)
            }, 1,
            // Estimated Dragon Boat Festival
            [Date] IN {
                DATE(2026,6,19), DATE(2027,6,9), DATE(2028,5,28),
                DATE(2029,6,16), DATE(2030,6,5), DATE(2031,5,25),
                DATE(2032,6,12), DATE(2033,6,1), DATE(2034,6,20)
            }, 1,
            // Estimated Mid-Autumn Festival
            [Date] IN {
                DATE(2026,9,27), DATE(2027,9,16), DATE(2028,10,4),
                DATE(2029,9,22), DATE(2030,9,12), DATE(2031,10,1),
                DATE(2032,9,19), DATE(2033,9,8), DATE(2034,9,26)
            }, 1,
            0
        ),
    "holiday_name",
        SWITCH(TRUE(),
            FORMAT([Date], "MM-dd") = "01-01", "New Year's Day",
            FORMAT([Date], "MM-dd") = "04-04" || FORMAT([Date], "MM-dd") = "04-05", "Qingming Festival",
            FORMAT([Date], "MM-dd") = "05-01", "Labor Day",
            FORMAT([Date], "MM-dd") >= "10-01" && FORMAT([Date], "MM-dd") <= "10-07", "National Day",
            [Date] IN {
                DATE(2026,2,17), DATE(2027,2,6), DATE(2028,1,26),
                DATE(2029,2,13), DATE(2030,2,3), DATE(2031,1,23),
                DATE(2032,2,11), DATE(2033,1,31), DATE(2034,2,19)
            }, "Spring Festival",
            [Date] IN {
                DATE(2026,6,19), DATE(2027,6,9), DATE(2028,5,28),
                DATE(2029,6,16), DATE(2030,6,5), DATE(2031,5,25),
                DATE(2032,6,12), DATE(2033,6,1), DATE(2034,6,20)
            }, "Dragon Boat Festival",
            [Date] IN {
                DATE(2026,9,27), DATE(2027,9,16), DATE(2028,10,4),
                DATE(2029,9,22), DATE(2030,9,12), DATE(2031,10,1),
                DATE(2032,9,19), DATE(2033,9,8), DATE(2034,9,26)
            }, "Mid-Autumn Festival",
            BLANK()
        )
)

```


```sql
measurement = ROW("kpi_id", BLANK(), "kpi_name", BLANK())
```