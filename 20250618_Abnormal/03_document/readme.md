# Abnormal Analysis

> Author: Yue er & Derek
>
> Create Date: 2025-06-17
>
> Version: 0.1
>
> Content: Initial version with data cleansing and transformation

---

## Background & Tasks

***Goal:*** 
change tool from Power query to PBI 
improve visual display way

## Data Cleansing


## Data Modeling


## DAX Design & Implementation

***Basic Measures***



***Calculated Field***



```sql

```

## Dashboard Design & Implementation





## Q&A

- 日期维度目前只和“整合”表关联，无法与其他业务数据进行关联获取周的数据；
- 业务数据较多，应考虑合并业务数据，统一计算数量和金额；
- WoW（周比周）的DAX需要重新设计，基于统一的日期维度表上进行计算；
- 箭头、百分比（负数、正数显示不同颜色）基于上述内容进行优化即可。

