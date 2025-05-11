# 关键指标




# 关键DAX

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