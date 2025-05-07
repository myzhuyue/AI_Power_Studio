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


# Issue Solving

``` sql
income_uom_rg_ind_eng_switch = 
SWITCH(
    SELECTEDVALUE(University[uom_rg]),
    "University of Manchester", [income_uom_ind_ratio%],
    [income_rus_ind_ratio%]
)

dim_industry_engagement = 
UNION(
    ROW("Category", "University of Manchester", "Industry Engagement", [income_uom_ind_ratio%]),
    ROW("Category", "Russell Group", "Industry Engagement", [income_rus_ind_ratio%])
)


income_uom_rg_res_switch = 
SWITCH(
    SELECTEDVALUE(University[uom_rg]),
    "University of Manchester", [income_uom_res],
    [income_avg_rus_res]
)

dim_research_council_income = 
UNION(
    ROW("Category", "University of Manchester", "Research Income", [income_uom_res]),
    ROW("Category", "Russell Group", "Research Income", [income_avg_rus_res])
)
```

文件中包含一个工作表“data”，其中包含4个字段学位：“level of study”, 性质："mode of study", 曼彻斯特大学学生人数："uom staff number", 罗素集团学生人数："rus staff number".

要求通过Power BI DAX进行下面计算：

1. 计算“曼彻斯特大学”， “罗素集团”，在学位，性质两个维度下，各个维度成员下的学生人数的数量，比例；
2. 将"level of study"维度下的“first degree”、"postgraduate taught"、"postgraduate research"三个维度成员，与“mode of study”维度下的“full”维度成员合并在一个新的维度中，展示各自的原始学生人数比例。


``` sql
dim_level_mode = 
UNION(
    SELECTCOLUMNS(
        FILTER('HESA Student', 'HESA Student'[Level of study] IN {"First Degree", "Postgraduate (taught)", "Postgraduate (research)"}),
        "level mode dimension", 'HESA Student'[Level of study],
        "uom student number", [stu_num_uom],
        "rus student number", [stu_num_rus]
    ),
    SELECTCOLUMNS(
        FILTER('HESA Student', 'HESA Student'[Mode of study] = "Full-time"),
        "level mode dimension", 'HESA Student'[Mode of study],
        "uom student number", [stu_num_uom],
        "rus student number", [stu_num_rus]
    )
)
```

``` sql
stu_rus_all = 
CALCULATE(SUM('HESA Student'[Number]), FILTER(University, University[Russell Group] = "Member"), FILTER('HESA Student', 'HESA Student'[Academic Year] = "2023/24"))

stu_rus_all_1 = 
CALCULATE(SUM(dim_level_mode[rus student number]))

stu_rus_all_ratio = 
DIVIDE([stu_rus_all_1], [stu_rus_all])


stu_uom_all = 
CALCULATE(SUM('HESA Student'[Number]), FILTER(University, University[UKPRN] = "10007798"), FILTER('HESA Student', 'HESA Student'[Academic Year] = "2023/24"))

stu_uom_all_1 = 
CALCULATE(SUM(dim_level_mode[uom student number]))

stu_uom_all_ratio = 
DIVIDE([stu_uom_all_1], [stu_uom_all])
```