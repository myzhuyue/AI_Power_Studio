# Reps Sales Performance Analysis

> Author: Qin Yiyan & Derek
>
> Create Date: 2025-06-16
>
> Version: 0.1
>
> Content: Initial version with data cleansing and transformation

---

## Background & Tasks

***Shipping control:***

Database: Appendix1 
Calculation Field: sheet 9
Dimension: sheet “summary”(team, to region, product line, booking status, destination, plan month)
Summary & overview: power query

Monthly report: copy from sheet summary & overview（ignore part4)

***Goal:*** 
change tool from Power query to PBI 
improve visual display way

## Data Cleansing

Step 1, column type transformation:

- {"Team", type text}, 
- {"POL ", type text}, 
- {"To Region", type text}, 
- {"Product Type", type text}, 
- {"Plan Month", type text}, 
- {"Product Hierarchy", type text}, 
- {"Order Creator", type text}, 
- {"Order Create Date", type date}, 
- {"Sending Plant", type text}, 
- {"Hazard Class", type text}, 
- {"UN NO.", type text}, 
- {"Order Type", type text}, 
- {"Customer Name", type text}, 
- {"Freight Forwarder (who do booking)", type text}, 
- {"Order No.", type text}, 
- {"Material", type text}, 
- {"Order No. / Material", type text}, 
- {"Product and Package", type text}, 
- {"Order Quantity", Int64.Type}, 
- {"Unit", type text}, 
- {"Incoterms", type text}, 
- {"Destination", type text}, 
- {"Country / Region", type text}, 
- {"Required Delivery  Date (RDD)", type date}, 
- {"Goods Ready Date (MAD)", type date}, 
- {"Inspection Date", type date}, 
- {"Stock Status", type text}, 
- {"ETD from booking confirmation", type date}, 
- {"Sail time (ETA - ETD)", Int64.Type}, 
- {"ETA from booking confirmation", type date}, 
- {"ATD", type date}, 
- {"Loading Date (booking status = 4, 5, 6: actual; = 2, 3: plan)", type date}, 
- {"Booking Status", type text}, 
- {"Remark", type text}, 
- {"Container Type", type text}, 
- {"Container Quantity", Int64.Type}, 
- {"TEU", Int64.Type}, 
- {"Ocean Carrier", type text}, 
- {"Vessle / Voyage", type text}, 
- {"Bill of Lading", type text}, 
- {"Terminal (when in list)", type text}, 
- {"Tender carrier resource", type text}, 
- {"Rate Type", type text}, 
- {"Reason for spot quotation", type text}, 
- {"Total Local Freight POL Currency", Int64.Type}, 
- {"Total Ocean Freight in USD", Int64.Type}, 
- {"First date", type date}, 
- {"Delivery No.", type text}, 
- {"POD", type text}, 
- {"Reason for delay if have", type text}, 
- {"Tender Ocean Freight USD", Int64.Type}, 
- {"Spot Ocean Freight USD", Int64.Type}, 
- {"Business Line", type text}, 
- {"Product Line", type text}, 
- {"Planned Goods Issue Date", type date}, 
- {"Order Currency", type text}, 
- {"Total Order Amount", Int64.Type}, 
- {"Additional Ocean Cost  in USD", Int64.Type}, 
- {"Additional Local Cost POL Currency", type text}, 
- {"Addditonal Cost Reason", type text}

Step 2, AddColumn(#"Changed Type", "tender", each if [Rate Type] = "tender" then [TEU] else null)

Step 3, AddColumn(#"Added Conditional Column", "tender-ST", each if [Rate Type] = "tender-ST" then [TEU] else null)

Step 4, AddColumn(#"Added Conditional Column1", "spot", each if [Rate Type] = "spot" then [TEU] else null)

Step 5, AddColumn(#"Added Conditional Column2", "F term", each if [Rate Type] = "F term" then [TEU] else null)

Step 6, TransformColumnTypes(#"Added Conditional Column3",{{"tender", Int64.Type}, {"tender-ST", Int64.Type}, {"spot", Int64.Type}, {"F term", Int64.Type}, {"Order Create Date", type date}, {"Required Delivery  Date (RDD)", type date}, {"Goods Ready Date (MAD)", type date}, {"Inspection Date", type date}, {"ETD from booking confirmation", type date}, {"ETA from booking confirmation", type date}, {"ATD", type date}, {"Loading Date (booking status = 4, 5, 6: actual; = 2, 3: plan)", type date}})

Step 7, AddColumn(#"Changed Type1", "Order fulfilled", each if [Booking Status] = "6 Close" then [Order Quantity] else if [Booking Status] = "5 Departed" then [Order Quantity] else if [Booking Status] = "4 Loaded" then [Order Quantity] else null)

Step 8, TransformColumnTypes(#"Added Conditional Column4",{{"Order fulfilled", Int64.Type}})

Step 9, AddColumn(#"Changed Type2", "Order delete or Z2", each if [Booking Status] = "7 Delete" then [Order Quantity] else if [Booking Status] = "1 Order received" then [Order Quantity] else null)

Step 10, TransformColumnTypes(#"Added Conditional Column5",{{"Order delete or Z2", Int64.Type}})

## Data Modeling


## DAX Design & Implementation

***Basic Measures***

1. SUM of Order Quantity
2. SUM of TEU
3. COUNT of Order No.
4. SUM of Order Quantity(%)
5. SUM of Order Fulfilled
6. SUM of Order delted or Z2
7. SUM of order Fullfillment rate
8. SUM of Tender
9. SUM of Tender-ST
10. SUM of Spot
11. SUM of F-term
12. SUM of Tender Loading Rate
13. Tender utilization rate 1=Actual tender loaded TEU/Awarded allocation
14. Tender utilization rate 2=Actual tender loaded TEU/Reserved spaces
15. Tender loading rate=Actual tender loaded TEU/Actual demand
16. Whole APAC outbound volume-(2024-May VS 2025-May )
17. YoY decrease rate: -9%
18. MoM increase rate:23%


***Calculated Field***

Solve Order Field Formula
1. achievement rate =#NAME?/ (TEU-#NAME?)
2. Tender loading rate = (tender+'tender-ST' )/ (TEU-'F term' )
3. Spot 2 =#NAME?-#NAME?
4. Order fulfillment rate ='Order fulfilled' /('Order Quantity' -'Order delete or Z2' )

Actual tender loading rate per sourcing region
Tender loading rate ='Tender/total' / (TEU-'F term/TEU' )

Fulfillment rate=( Loaded+ Departed+ Close)/ Total order quantity

```sql

```

## Dashboard Design & Implementation

1. Part 1: 2023-2025 SHIPMENT ORDERS (RELEASED  FOR TRANSPORT PLANNING) overview
2. Part 2: Actual export operation overview of May 2025
3. Part 2: May’s orders fulfillment rate-(By product line loading)
4. Part 2: Tender loading rate  (data exclude "F" term orders)
5. Part 2: Tender loading rate  (data exclude "F" term orders)-Per receiving region
6. Part 2: Reason for spot
7. Part 3: Performance from key awarded carrier
8. Part 4: Awarded allocation VS Reserved space VS Actual tender loading
9. Part 5: Shpt trend and tender loading by biz
10. Part 5: Shpt trend and tender loading by biz(%)



## Q&A

初步需求分析：
// 需求：

1. 数据清洗转换10步骤；（含字段类型转换和新增字段等）；
2. 数据模型设计（如日期表，维度表，事实表等）；
3. 基础指标18个 + 4个衍生指标；
4. 可视化图表10+个（如柱状图，折线图，饼图等）；

已知问题：

- Calculated Field "achievement rate", "Spot 2" logic not clear
- DataFormat.Error: We couldn't convert to Number.  - Append1 - 1148行

> - Details:
> -     6104446537
> - 6104446566