# Dimension

1. University
   - from data source, we can generate the university dimension from student table, which include "Russell Group" infomation, and after further validation from both "Staff" and "Finance" table, all the UKPRN is included in "Student" table.

2. Calendar
   - A calendar or date table is needed to do the trend analysis. It can be retrived from "Finance", "Staff" and "Student" table with "StartDate" field.


``` sql
var min_dt = MINX(UNION(VALUES(stu[StartDate]), VALUES(sta[StartDate]), VALUES(fin[StartDate])), [StartDate])
var max_dt = MAXX(UNION(VALUES(stu[StartDate]), VALUES(sta[StartDate]), VALUES(fin[StartDate])), [StartDate])
```

# DAX measures

## Follow with Doc

``` sql
stu_num_uom = 
var a = CALCULATE(SUM('HESA Student'[Number]), FILTER(University, University[UKPRN] = "10007798"), FILTER('HESA Student', 'HESA Student'[Academic Year] = "2023/24")) // UKPRN of Manchester
return IF(ISBLANK(a), 0, a)
```










## Basic Metrics (University of Manchester)
1.	Resource Efficiency Metrics:

``` sql
- Student-to-Staff Ratio = [Total Student Numbers] / [Total Staff Numbers]
- Income per Student = [Sum of Income(£000s)] / [Total Student Numbers]
- Income per Staff Member = [Sum of Income(£000s)] / [Total Staff Numbers]
```

2.	Student Composition Metrics:

``` sql
- First Degree % = [First degree] / [Total Student Numbers]
- Postgraduate Taught % = [Postgraduate taught] / [Total Student Numbers]
- Postgraduate Research % = [Postgraduate research] / [Total Student Numbers]
- Full-time Student % = [Full-time Students] / [Total Student Numbers]
```

3.	Income Source Analysis:

``` sql
- Research Councils Income % = [Research Councils] / [Sum of Income(£000s)]
- UK-based Charities Income % = [UK-based charities] / [Sum of Income(£000s)]
- Industry Income % = [Industry] / [Sum of Income(£000s)]
```

## Russell Group Comparison Measures

1.	Russell Group Position Metrics:

- Rank within Russell Group for Student Numbers
- Rank within Russell Group for Staff Numbers
- Rank within Russell Group for Total Income
- Rank within Russell Group for Research Council Income

2.	Russell Group Comparison Ratios:

``` sql
- Student Numbers vs Russell Group Average = [UoM Total Student Numbers] / AVERAGEX(FILTER(ALL(Universities), [Russell Group Member]=TRUE), [Total Student Numbers])
- Income vs Russell Group Average = [UoM Sum of Income(£000s)] / AVERAGEX(FILTER(ALL(Universities), [Russell Group Member]=TRUE), [Sum of Income(£000s)])
- Research Income % vs Russell Group Average
```

3.	Russell Group Market Share Measures:

``` sql
- UoM % of Russell Group Students = [UoM Total Student Numbers] / SUMX(FILTER(ALL(Universities), [Russell Group Member]=TRUE), [Total Student Numbers])
- UoM % of Russell Group Income = [UoM Sum of Income(£000s)] / SUMX(FILTER(ALL(Universities), [Russell Group Member]=TRUE), [Sum of Income(£000s)])
- UoM % of Russell Group Research Income
```

4.	Russell Group vs Non-Russell Group Comparisons:

- Russell Group vs Non-Russell Group Average Student Numbers
- Russell Group vs Non-Russell Group Average Staff Numbers
- Russell Group vs Non-Russell Group Average Income
- Russell Group vs Non-Russell Group Research Income %

## Advanced Analytical Measures

1.	Specialization Metrics:

``` sql
- Research Intensity vs Russell Group Average = [Postgraduate research]/[Total Student Numbers] / AVERAGEX(FILTER(ALL(Universities), [Russell Group Member]=TRUE), [Postgraduate research]/[Total Student Numbers])
- Industry Engagement vs Russell Group Average = [Industry]/[Sum of Income(£000s)] / AVERAGEX(FILTER(ALL(Universities), [Russell Group Member]=TRUE), [Industry]/[Sum of Income(£000s)])
```

2.	Efficiency Comparisons:

- Student-Staff Ratio vs Russell Group Average
- Income per Student vs Russell Group Average
- Research Income per Staff vs Russell Group Average

3.	Percentile Measures:

- Student Numbers Percentile within Russell Group
- Income Percentile within Russell Group
- Research Income Percentile within Russell Group



# UIUX

- 曼彻斯特大学官方的颜色是：紫色#660099，黄色#FFCC33，灰色#999999。我们以紫色和黄色为准就好。