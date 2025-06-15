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

## Data Cleansing

## Data Modeling


## DAX Design & Implementation


```sql
下半年销售额 = CALCULATE(SUM('下半年销售明细'[订单金额/元]))


订单金额排名按商品 = rank(
    ALLSELECTED('商品信息'[商品名称]),
    ORDERBY('下半年销售明细'[下半年销售额],desc,'商品信息'[商品名称])
    )


虚拟订单额 = MAXX(
    ALLSELECTED('商品信息'[商品名称]),
    [下半年销售额]
) / 10
```

## Dashboard Design & Implementation


## Q&A