# Data Visualization

> Visualization is a way of thinking your business, turn the data insight into visuals.
> 




---

## 1. Common Visuals

### 1.1 Beautiful Bar Chart

> Bar charts are the standard for looking at a specific value across different categories.




---

## 2. Special Visuals


### 2.1 Pareto Analysis

> Pareto Analysis is a statistical technique that applies the Pareto Principle to data. This is more commonly known as the 80:20 Rule. 
> 
> The Pareto Principle is based on the presumption that a relatively small number of inputs (20%)  have most impact on the results/output (80%).  
> 
> The 80:20 rule can be applied to a wide variety of data in most businesses.  Examples include:
> - Which 20% of products make up 80% of sales
> - Which 20% of customers make up 80% of profit.

#### Why and When to Use
- Focus: Identify the “vital few” categories driving most outcomes.
- Use cases: defects/incidents, costs/revenue, service requests.

#### How to Perform
- Pick metric: Choose a single impact measure (count, cost, revenue).
- Aggregate: Summarize by category and sort descending by impact.
- Cumulative %: Compute cumulative share; mark smallest set reaching target (e.g., 80%).
- Act: Prioritize improvements on those categories and track change.

#### Power BI Implementation (Concept)
- Visual: Line and clustered column chart; bars = impact by category; line = cumulative %.
- Measures:
    - Total Impact: `SUM(Fact[Impact])`
    - Category Impact: `SUM(Fact[Impact])`
    - Cumulative %: rank categories by impact, sum up to current rank, divide by total.
- Tip: Use `ALLSELECTED()` in measures so slicers re-evaluate ranking and cumulative %.

---

> 帕累托分析是一种将帕累托原理应用于数据的统计技术，其更为人熟知的名称是80:20法则。  
> 帕累托原理基于这样一个假设：相对较少的投入（20%）会对结果/产出产生大部分影响（80%）。  
> 80:20法则可应用于大多数企业的各类数据，示例如下：  
> - 哪些20%的产品贡献了80%的销售额  
> - 哪些20%的客户创造了80%的利润

**DAX Measures** created as below:

1. ***Basic Sales***

```sql
basic_sales = 
var a = CALCULATE(sum(financials[Sales]))
return IF(ISBLANK(a), 0, a)
```

2. ***Cumulative Sales***
```sql
cumulative_sales_by_product = 
var a = [sales_value]
var b = SUMX(
    FILTER(SUMMARIZE(ALL(financials), financials[Product], "revenue", [sales_value]),
    [revenue] >= a
    )
    , [revenue]
)
return b
```
> Microsoft DAX Reference
> 
> [SUMX](https://learn.microsoft.com/en-us/dax/sumx-function-dax), Returns the sum of an expression evaluated for each row in a table.
```sql
-- syntax
SUMX(<table>, <expression>)
```

> [SUMMARIZE](https://learn.microsoft.com/en-us/dax/summarize-function-dax), Returns a summary table for the requested totals over a set of groups.
```sql
-- syntax
SUMMARIZE (<table>, <groupBy_columnName>[, <groupBy_columnName>]…[, <name>, <expression>]…)
```

3. ***Cumulative Percentage***
```sql
cumulative_percentage_by_product = 
var a = [cumulative_sales_by_product]
var b = CALCULATE([basic_sales], ALL(financials))
return DIVIDE(a, b)
```

**Visual Object**

In Power BI you can use a **Line and clustered column chart** chart:
- The column in the chart represents the **individual inputs**
- The line chart represents the **cumulative percentage** of the inputs as they build towards 80%.

![Line and clustered column chart](./Pareto%20Analysis.png)

You can also use table view to verify the basic data and cumulative data, remember to order the basic sales in descending order.

![Table chart](./Pareto%20Analysis%20-%20Table%20visual.png)