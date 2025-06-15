# 20250525开发纪要

## 已知问题

1. contact 表中，"industry", "Salesperson", "Trading Partner ID"均为空，后期会影响分析维度；
2. product 表中，缺少product id，无法通过name字段作为主键，有重复记录。目前只能通过sku与sales oorder line表中的 “Product”字段进行匹配。
3. salesorder 表中缺少sales order number，目前使用"Order Reference"字段代替；
4. salesorderline表中，缺少sales order line number, 多个字段如“CF RMA Unit Serial Number”，“CF Serial Number[1-10]”， “CF-ShipExpress SO Return Tracking”为空，表中product名称与product表的name信息无法匹配；

## 模型设计

![sales model](./03_document/model_2025-05-25%20174243.png)


## 报告设计

![报告设计](./03_document/report_2025-05-25%20175834.png)

# 需求说明文档

## 1. 背景简介

> 一家贸易公司，公司的主营业务就是从总部采购货物，向当地的经销商批发出售和电商零售出售。
> 
> SKU大概90个，零部件大概200 - 300个，每年大概销售300万人民币，货物单价大概1000人民币左右
> 
> 有一个自营仓库，一个第三方仓库。
> 
> 采用的系统叫ODOO。

---

## 2. 数据面板需求：

### 2.1 主页

显示关键绩效指标（KPI）、当月的收入，毛利、KPI完成比例、销售摘要、fulfillment摘要和库存摘要。

### 2.2 销售页面

关键截至目前的总销售额、同比比较，以及按账户、产品和地区的销售分析。

**维度**: 账户，产品，地理位置、日期维度（需要同比）

**度量**: 总销售额

> DAX如下所示

``` sql
sales = CALCULATE(SUM(table1[sales]))
```

***问题***: 

1. 是否统计销售量（区别与销售额）
2. 上述三个维度是否满足需求（账户、产品、地理位置）

### 2.3 Fulfillment页面

包括每月总订单数、每月总配送数、完成率（%）、订单周期时间、订单准确率（%）和发货准确率（%）。

### 2.4 库存页面

展示库存总价值、总数量、低库存预警、库存过剩的SKU、库存周转率、平均库存天数以及仓库容量利用率。


### 2.5 退货页面

展现截止目前退货金额，按退货原因进行分析。（第二步在做）