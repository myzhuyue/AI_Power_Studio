> Author: [DSPowerStudio](dspowerstudio@outlook.com)
>
> Create Date: 2025-05-19
>
> Last Update Date: 2025-05-19
>
> Version: v0.2
>
> Content: Initial version for draft analysis

---

# Table of Content

- [Table of Content](#table-of-content)
- [质量数据分析](#质量数据分析)
  - [1. 源数据分析](#1-源数据分析)
    - [数据字典](#数据字典)
  - [2. 数据清洗](#2-数据清洗)
  - [3. 数据建模](#3-数据建模)
  - [4. DAX指标](#4-dax指标)
  - [5. 数据可视化](#5-数据可视化)
    - [维度](#维度)
    - [事实数据](#事实数据)
    - [详细图表](#详细图表)
  - [问题清单](#问题清单)
    - [已知问题](#已知问题)
    - [待确认问题](#待确认问题)
    - [待补充数据](#待补充数据)

# 质量数据分析

---

## 1. 源数据分析

### 数据字典

|字段名称|类型|Sample Date|
|-------------|---------|---------|
送检序号|string|20250102001
送检日期|date|2025/01/02
送检时间|time|8：00
订单号|string|PO172418
材料名称|string|冲片
材料编号|string|2517683-002
供应商|string|同创
数量|decimal|25000.00 
单位|string|EA
质保单（材质证明）|string|Y
检验报告|string|Y
样机通知号|string|
送检人|string|王红利
AQL|decimal|0.25
检查水平|decimal|2
抽样方案|string|正常
样本量|decimal|5
检测结果|string|合格
不合格品数量|decimal|
不合格问题|string|
检验员|string|岳志洲
完成日期|date|2/1/2025
完成时间|time|18:30
送检与完成时间差|decimal|

---

## 2. 数据清洗

1. 合并文件中不同工作表的数据；
2. 按数据字典统一数据结构和类型；
3. 替换异常数据，如空值处理，时间日期类型不一致等问题；
4. 数值类型数据的异常值处理；
5. 增加自定义指标（如检验完成时间，急件完成度category）
---

## 3. 数据建模

**TBD**

---

## 4. DAX指标

**TBD**

---

## 5. 数据可视化

### 维度

1. 供应商
2. 日期时间维度（年份、月份）
3. 来料类别
4. 样机通知号

### 事实数据

1. 检验总数量
2. 不良品数量
3. 批次缺陷率
4. 受检率
5. 8D关闭率

> 考虑到自定义切片器的影响，上述指标会扩展到5 * 4 * 2 = 40个左右

### 详细图表

1. 5 Card visual
2. Bar Charts
3. 自定义切片器（周、月、季度、年）
4. Line chart * 4
5. Pie chart
6. 自定义卡片 * 2 （15% weekday，85% workday）
7. Scatter Chart：检验完成时间记录
8. Bar Chart with custom category (Morning, Noon, Afternoon, Eventing)


## 问题清单

### 已知问题

- 1 ～ 5 月数据结构与6月，12月数据结构不一致

### 待确认问题

- 【Done】来料类别通过哪个字段筛选？
  - 通过“材料名称”筛选

- 【Done】批次缺陷率
```sql
[批次缺陷率] = 
var a = SUM([不合格数量])
var b = SUM(数量)
return DIVIDE(a, b)
```

- 受检率
```sql
TBD
```

- 8D关闭率
```sql
TBD
```

### 待补充数据

- 供应商主数据（报告上需要通过“供应商”进行筛选）
- 材料主数据（报告上需要通过“来料类别”进行筛选）