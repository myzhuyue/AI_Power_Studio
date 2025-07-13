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

