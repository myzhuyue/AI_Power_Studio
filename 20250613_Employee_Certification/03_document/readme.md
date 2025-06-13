# Reps Sales Performance Analysis

> Author: Hannaiio & Derek
>
> Create Date: 2025-06-13
>
> Version: 1.3
>
> Content: Initial version with data cleansing and transformation

---

## Background & Tasks

### Colors Design

#00EE00

#FF0000

## Data Cleansing

- v1.3 change request

1. 转换（A360A -> A360 Advanced, A360M -> A360 Master). 
2. Summary Card visual 字体加大加粗. 
3. Donut charts added Title.

## DAX Design & Implementation

1. A measurement table is created to categorize different measures.

```sql
measurement = ROW("kpi_id", BLANK(), "kpi_name", BLANK())
```

2. Basic measurement

- total_points

```sql
total_points = 
var a = CALCULATE(SUM(CertDifficulty[Points]), FILTER(Employee, Employee[Is Active] = "Yes"), FILTER('Version&CL', 'Version&CL'[if_met] = "met"))
return IF(ISBLANK(a), 0, a)
```

- valid_cert#

```sql
valid_cert# = 
var a = CALCULATE(COUNT(CertTracker[EID]), FILTER(CertTracker, CertTracker[CertValidation] = "Valid"), FILTER(Employee, Employee[Is Active] = "Yes"), FILTER('Version&CL', 'Version&CL'[if_met] = "met"))
return IF(ISBLANK(a), 0, a)
```

- employee_resign#
```sql
employee_resign# = 
var a = CALCULATE(COUNT(Employee[EID]), FILTER(Employee, Employee[Roll Off Reason] = "Resign"))
return IF(ISBLANK(a), 0, a)
```

## Dashboard Design & Implementation


## Q&A