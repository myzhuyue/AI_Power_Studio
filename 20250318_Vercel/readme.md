好的，为了更细致地分析人员流动率，我们可以在已有的表结构基础上增加员工的部门信息。假设 `employee_changes` 表新增了一个 `department` 字段用于记录员工所在部门，同时我们仍然保留 `employee_daily_snapshot` 表来记录每日员工数量。下面是基于 MySQL 编写的 SQL 代码，用于计算不同部门在月度、季度和年度的人员流动率：

```sql
-- 创建示例表 employee_changes，增加 department 字段
CREATE TABLE employee_changes (
    employee_id INT,
    event_date DATE,
    event_type VARCHAR(10),
    department VARCHAR(50)
);

-- 插入示例数据到 employee_changes
INSERT INTO employee_changes (employee_id, event_date, event_type, department)
VALUES
    (1, '2024-01-01', '入职', '销售部'),
    (2, '2024-01-15', '入职', '技术部'),
    (1, '2024-01-31', '离职', '销售部'),
    (3, '2024-02-01', '入职', '销售部'),
    (2, '2024-03-15', '离职', '技术部');

-- 创建示例表 employee_daily_snapshot
CREATE TABLE employee_daily_snapshot (
    snapshot_date DATE,
    employee_count INT,
    department VARCHAR(50)
);

-- 插入示例数据到 employee_daily_snapshot
INSERT INTO employee_daily_snapshot (snapshot_date, employee_count, department)
VALUES
    ('2024-01-01', 0, '销售部'),
    ('2024-01-15', 1, '销售部'),
    ('2024-01-31', 0, '销售部'),
    ('2024-02-01', 1, '销售部'),
    ('2024-02-28', 2, '销售部'),
    ('2024-03-15', 1, '销售部'),
    ('2024-03-31', 1, '销售部'),
    ('2024-01-01', 0, '技术部'),
    ('2024-01-15', 1, '技术部'),
    ('2024-01-31', 1, '技术部'),
    ('2024-02-28', 1, '技术部'),
    ('2024-03-15', 0, '技术部'),
    ('2024-03-31', 0, '技术部');

-- 计算月度部门人员流动率
SELECT 
    YEAR(s.snapshot_date) AS year,
    MONTH(s.snapshot_date) AS month,
    s.department,
    -- 计算当月部门离职人数
    SUM(CASE WHEN ec.event_type = '离职' AND YEAR(ec.event_date) = YEAR(s.snapshot_date) AND MONTH(ec.event_date) = MONTH(s.snapshot_date) AND ec.department = s.department THEN 1 ELSE 0 END) AS monthly_leaving_count,
    -- 计算当月部门平均员工人数
    AVG(s.employee_count) AS monthly_average_employees,
    -- 计算月度部门人员流动率
    SUM(CASE WHEN ec.event_type = '离职' AND YEAR(ec.event_date) = YEAR(s.snapshot_date) AND MONTH(ec.event_date) = MONTH(s.snapshot_date) AND ec.department = s.department THEN 1 ELSE 0 END) / 
    AVG(s.employee_count) * 100 AS monthly_turnover_rate
FROM 
    employee_daily_snapshot s
LEFT JOIN 
    employee_changes ec ON s.snapshot_date = ec.event_date AND s.department = ec.department
GROUP BY 
    YEAR(s.snapshot_date), MONTH(s.snapshot_date), s.department;

-- 计算季度部门人员流动率
SELECT 
    YEAR(s.snapshot_date) AS year,
    QUARTER(s.snapshot_date) AS quarter,
    s.department,
    -- 计算当季部门离职人数
    SUM(CASE WHEN ec.event_type = '离职' AND YEAR(ec.event_date) = YEAR(s.snapshot_date) AND QUARTER(ec.event_date) = QUARTER(s.snapshot_date) AND ec.department = s.department THEN 1 ELSE 0 END) AS quarterly_leaving_count,
    -- 计算当季部门平均员工人数
    AVG(s.employee_count) AS quarterly_average_employees,
    -- 计算季度部门人员流动率
    SUM(CASE WHEN ec.event_type = '离职' AND YEAR(ec.event_date) = YEAR(s.snapshot_date) AND QUARTER(ec.event_date) = QUARTER(s.snapshot_date) AND ec.department = s.department THEN 1 ELSE 0 END) / 
    AVG(s.employee_count) * 100 AS quarterly_turnover_rate
FROM 
    employee_daily_snapshot s
LEFT JOIN 
    employee_changes ec ON s.snapshot_date = ec.event_date AND s.department = ec.department
GROUP BY 
    YEAR(s.snapshot_date), QUARTER(s.snapshot_date), s.department;

-- 计算年度部门人员流动率
SELECT 
    YEAR(s.snapshot_date) AS year,
    s.department,
    -- 计算当年部门离职人数
    SUM(CASE WHEN ec.event_type = '离职' AND YEAR(ec.event_date) = YEAR(s.snapshot_date) AND ec.department = s.department THEN 1 ELSE 0 END) AS annual_leaving_count,
    -- 计算当年部门平均员工人数
    AVG(s.employee_count) AS annual_average_employees,
    -- 计算年度部门人员流动率
    SUM(CASE WHEN ec.event_type = '离职' AND YEAR(ec.event_date) = YEAR(s.snapshot_date) AND ec.department = s.department THEN 1 ELSE 0 END) / 
    AVG(s.employee_count) * 100 AS annual_turnover_rate
FROM 
    employee_daily_snapshot s
LEFT JOIN 
    employee_changes ec ON s.snapshot_date = ec.event_date AND s.department = ec.department
GROUP BY 
    YEAR(s.snapshot_date), s.department;
```

### 代码解释：
1. **创建和插入数据**：
    - 创建了 `employee_changes` 表并增加了 `department` 字段，插入了包含部门信息的员工入职和离职记录。
    - 创建了 `employee_daily_snapshot` 表，也增加了 `department` 字段，插入了各部门每日的员工数量数据。
2. **计算月度部门人员流动率**：
    - 使用 `LEFT JOIN` 将 `employee_daily_snapshot` 表和 `employee_changes` 表根据日期和部门进行连接。
    - 通过 `SUM` 和 `CASE WHEN` 语句计算当月特定部门的离职人数。
    - 使用 `AVG` 函数计算当月该部门的平均员工人数。
    - 最后计算出月度部门人员流动率。
3. **计算季度部门人员流动率**：与计算月度部门人员流动率类似，只是分组依据变为年份、季度和部门。
4. **计算年度部门人员流动率**：同样通过连接两个表，根据年份和部门分组，计算当年特定部门的离职人数、平均员工人数，进而得出年度部门人员流动率。

这样，我们就可以分析不同部门在不同时间周期的人员流动情况了。 

### MTD, QTD, YTD Turnover Rate

假设你有一个名为 `employee_changes` 的表，其结构如下：
- `employee_id`：员工ID
- `department`：员工所在部门
- `change_date`：人员变动日期
- `change_type`：人员变动类型（如入职、离职）

以下是一个示例 SQL 查询，用于计算每个部门的月到日期（MTD）、季到日期（QTD）和年到日期（YTD）的人员流动率。为了计算人员流动率，我们假设人员流动率是指入职和离职人数之和与该部门总员工数的比例。

```sql
-- 假设今天的日期
WITH current_date_cte AS (
    SELECT '2025-03-18'::date AS current_date
),
-- 计算每个部门的月到日期（MTD）入职和离职人数
mtd_changes AS (
    SELECT 
        department,
        SUM(CASE WHEN change_type = '入职' THEN 1 ELSE 0 END) AS mtd_hires,
        SUM(CASE WHEN change_type = '离职' THEN 1 ELSE 0 END) AS mtd_fires
    FROM 
        employee_changes
    CROSS JOIN 
        current_date_cte
    WHERE 
        EXTRACT(YEAR FROM change_date) = EXTRACT(YEAR FROM current_date)
        AND EXTRACT(MONTH FROM change_date) = EXTRACT(MONTH FROM current_date)
    GROUP BY 
        department
),
-- 计算每个部门的季到日期（QTD）入职和离职人数
qtd_changes AS (
    SELECT 
        department,
        SUM(CASE WHEN change_type = '入职' THEN 1 ELSE 0 END) AS qtd_hires,
        SUM(CASE WHEN change_type = '离职' THEN 1 ELSE 0 END) AS qtd_fires
    FROM 
        employee_changes
    CROSS JOIN 
        current_date_cte
    WHERE 
        EXTRACT(YEAR FROM change_date) = EXTRACT(YEAR FROM current_date)
        AND EXTRACT(QUARTER FROM change_date) = EXTRACT(QUARTER FROM current_date)
    GROUP BY 
        department
),
-- 计算每个部门的年到日期（YTD）入职和离职人数
ytd_changes AS (
    SELECT 
        department,
        SUM(CASE WHEN change_type = '入职' THEN 1 ELSE 0 END) AS ytd_hires,
        SUM(CASE WHEN change_type = '离职' THEN 1 ELSE 0 END) AS ytd_fires
    FROM 
        employee_changes
    CROSS JOIN 
        current_date_cte
    WHERE 
        EXTRACT(YEAR FROM change_date) = EXTRACT(YEAR FROM current_date)
    GROUP BY 
        department
),
-- 计算每个部门的总员工数
total_employees AS (
    SELECT 
        department,
        COUNT(DISTINCT employee_id) AS total_emp
    FROM 
        employee_changes
    GROUP BY 
        department
)
-- 最终结果，计算各部门的 MTD、QTD、YTD 人员流动率
SELECT 
    t.department,
    COALESCE((m.mtd_hires + m.mtd_fires)::numeric / t.total_emp, 0) AS mtd_turnover_rate,
    COALESCE((q.qtd_hires + q.qtd_fires)::numeric / t.total_emp, 0) AS qtd_turnover_rate,
    COALESCE((y.ytd_hires + y.ytd_fires)::numeric / t.total_emp, 0) AS ytd_turnover_rate
FROM 
    total_employees t
LEFT JOIN 
    mtd_changes m ON t.department = m.department
LEFT JOIN 
    qtd_changes q ON t.department = q.department
LEFT JOIN 
    ytd_changes y ON t.department = y.department
ORDER BY 
    t.department;
```

### 代码解释
1. **`current_date_cte`**：定义当前日期，方便后续计算。
2. **`mtd_changes`**：计算每个部门在本月内的入职和离职人数。
3. **`qtd_changes`**：计算每个部门在本季度内的入职和离职人数。
4. **`ytd_changes`**：计算每个部门在本年度内的入职和离职人数。
5. **`total_employees`**：计算每个部门的总员工数。
6. **最终查询**：将上述结果进行合并，计算每个部门的 MTD、QTD、YTD 人员流动率，并按部门排序。

### 注意事项
- 上述代码中的日期比较是基于 PostgreSQL 数据库的函数，不同的数据库系统可能会有不同的日期函数，需要根据实际情况进行调整。
- 代码中使用了 `COALESCE` 函数来处理可能的除零错误，确保结果的准确性。

### Apache Superset SQLlab

要使用 Apache Superset 实现 MTD（月到日期）、QTD（季到日期）、YTD（年到日期）的人员流动率的可视化，你可以按以下步骤操作：

### 1. 准备数据
确保你的数据库中有包含员工变动信息的表，例如表结构如下：
- `employee_id`：员工 ID
- `department`：员工所在部门
- `change_date`：人员变动日期
- `change_type`：人员变动类型（如入职、离职）

### 2. 连接数据源到 Apache Superset
在 Apache Superset 中配置数据库连接，使其能够访问上述包含员工变动信息的表。操作步骤如下：
- 登录 Apache Superset 界面。
- 点击界面左上角的 “Sources”，选择 “Databases”。
- 点击 “+ DATABASE”，填写数据库连接信息（如数据库类型、主机、端口、用户名、密码等），然后测试连接并保存。

### 3. 创建数据集
在连接好数据源后，需要创建一个数据集用于后续的可视化操作：
- 点击 “Sources”，选择 “Datasets”。
- 点击 “+ DATASET”，选择之前连接的数据库和员工变动信息表。
- 对表的字段进行检查和设置，确保日期字段的数据类型正确，然后保存数据集。

### 4. 编写 SQL 查询
使用 Apache Superset 的 SQL Lab 编写 SQL 查询来计算 MTD、QTD、YTD 的人员流动率。以下是一个示例 SQL 查询：

```sql
-- 假设今天的日期
WITH current_date_cte AS (
    SELECT CURRENT_DATE AS current_date
),
-- 计算每个部门的月到日期（MTD）入职和离职人数
mtd_changes AS (
    SELECT 
        department,
        SUM(CASE WHEN change_type = '入职' THEN 1 ELSE 0 END) AS mtd_hires,
        SUM(CASE WHEN change_type = '离职' THEN 1 ELSE 0 END) AS mtd_fires
    FROM 
        your_table_name
    CROSS JOIN 
        current_date_cte
    WHERE 
        EXTRACT(YEAR FROM change_date) = EXTRACT(YEAR FROM current_date)
        AND EXTRACT(MONTH FROM change_date) = EXTRACT(MONTH FROM current_date)
    GROUP BY 
        department
),
-- 计算每个部门的季到日期（QTD）入职和离职人数
qtd_changes AS (
    SELECT 
        department,
        SUM(CASE WHEN change_type = '入职' THEN 1 ELSE 0 END) AS qtd_hires,
        SUM(CASE WHEN change_type = '离职' THEN 1 ELSE 0 END) AS qtd_fires
    FROM 
        your_table_name
    CROSS JOIN 
        current_date_cte
    WHERE 
        EXTRACT(YEAR FROM change_date) = EXTRACT(YEAR FROM current_date)
        AND EXTRACT(QUARTER FROM change_date) = EXTRACT(QUARTER FROM current_date)
    GROUP BY 
        department
),
-- 计算每个部门的年到日期（YTD）入职和离职人数
ytd_changes AS (
    SELECT 
        department,
        SUM(CASE WHEN change_type = '入职' THEN 1 ELSE 0 END) AS ytd_hires,
        SUM(CASE WHEN change_type = '离职' THEN 1 ELSE 0 END) AS ytd_fires
    FROM 
        your_table_name
    CROSS JOIN 
        current_date_cte
    WHERE 
        EXTRACT(YEAR FROM change_date) = EXTRACT(YEAR FROM current_date)
    GROUP BY 
        department
),
-- 计算每个部门的总员工数
total_employees AS (
    SELECT 
        department,
        COUNT(DISTINCT employee_id) AS total_emp
    FROM 
        your_table_name
    GROUP BY 
        department
)
-- 最终结果，计算各部门的 MTD、QTD、YTD 人员流动率
SELECT 
    t.department,
    COALESCE((m.mtd_hires + m.mtd_fires)::numeric / t.total_emp, 0) AS mtd_turnover_rate,
    COALESCE((q.qtd_hires + q.qtd_fires)::numeric / t.total_emp, 0) AS qtd_turnover_rate,
    COALESCE((y.ytd_hires + y.ytd_fires)::numeric / t.total_emp, 0) AS ytd_turnover_rate
FROM 
    total_employees t
LEFT JOIN 
    mtd_changes m ON t.department = m.department
LEFT JOIN 
    qtd_changes q ON t.department = q.department
LEFT JOIN 
    ytd_changes y ON t.department = y.department
ORDER BY 
    t.department;
```

在上述查询中，请将 `your_table_name` 替换为实际的表名。将此查询在 SQL Lab 中执行并保存查询结果为一个新的数据集。

### 5. 创建可视化图表
使用保存的查询结果数据集创建可视化图表，步骤如下：
- 点击 “Charts”，选择 “+ CHART”。
- 选择之前保存的查询结果数据集。
- 选择合适的可视化类型，如表格、柱状图等。
- 在 “Metrics” 中选择 `mtd_turnover_rate`、`qtd_turnover_rate`、`ytd_turnover_rate` 作为要展示的指标。
- 在 “Group by” 中选择 `department` 进行分组。
- 根据需要调整图表的样式、颜色、标签等设置。
- 完成设置后，点击 “Save” 保存图表。

### 6. 创建仪表盘
将创建好的可视化图表添加到仪表盘，方便集中展示和查看：
- 点击 “Dashboards”，选择 “+ DASHBOARD”。
- 为仪表盘命名并创建。
- 在仪表盘编辑界面，点击 “+ ADD CHARTS”，选择之前创建的可视化图表添加到仪表盘。
- 调整图表的位置和大小，使仪表盘布局合理。
- 保存仪表盘，即可随时查看 MTD、QTD、YTD 的人员流动率情况。 




以下是针对你的要求，使用 Common Table Expression (CTE) 重新编写的计算 MTD、QTD 和 YTD 员工流失率的 SQL 代码，充分考虑了按天存储数据以及 `employee_ID` 去重的问题：

### 计算 MTD 员工流失率
```sql
-- 先获取所有 distinct 的 snapshot_date 中的最大月份的最大日期作为 MTD 的截止日期
WITH MTDMaxDate AS (
    SELECT MAX(snapshot_date) AS mtd_max_date
    FROM (
        SELECT DISTINCT snapshot_date
        FROM employee
    ) AS subquery
    WHERE DATE_TRUNC('month', snapshot_date) = DATE_TRUNC('month', (SELECT MAX(snapshot_date) FROM (SELECT DISTINCT snapshot_date FROM employee) AS inner_subquery))
),
-- 计算当月至今的相关数据
MTDData AS (
    SELECT 
        TO_VARCHAR(DATE_TRUNC('month', mmd.mtd_max_date), 'YYYY-MM') AS mtd_period,
        COUNT(DISTINCT CASE WHEN e.status = 'resign' AND e.snapshot_date <= mmd.mtd_max_date AND DATE_TRUNC('month', e.snapshot_date) = DATE_TRUNC('month', mmd.mtd_max_date) THEN e.employee_id END) AS num_resigned_mtd,
        COUNT(DISTINCT CASE WHEN e.status = 'in service' AND e.snapshot_date <= mmd.mtd_max_date AND DATE_TRUNC('month', e.snapshot_date) = DATE_TRUNC('month', mmd.mtd_max_date) THEN e.employee_id END) AS num_in_service_mtd
    FROM 
        employee e,
        MTDMaxDate mmd
)
-- 计算 MTD 平均员工数量和员工流失率
SELECT 
    mtd_period,
    num_resigned_mtd,
    num_in_service_mtd,
    ((num_resigned_mtd + num_in_service_mtd) / 2) AS average_employees_mtd,
    ROUND(100.0 * num_resigned_mtd / ((num_resigned_mtd + num_in_service_mtd) / 2), 2) AS turnover_rate_mtd
FROM 
    MTDData;
```

### 计算 QTD 员工流失率
```sql
-- 先获取所有 distinct 的 snapshot_date 中的最大季度的最大日期作为 QTD 的截止日期
WITH QTDMaxDate AS (
    SELECT MAX(snapshot_date) AS qtd_max_date
    FROM (
        SELECT DISTINCT snapshot_date
        FROM employee
    ) AS subquery
    WHERE DATE_TRUNC('quarter', snapshot_date) = DATE_TRUNC('quarter', (SELECT MAX(snapshot_date) FROM (SELECT DISTINCT snapshot_date FROM employee) AS inner_subquery))
),
-- 计算本季度至今的相关数据
QTDData AS (
    SELECT 
        TO_VARCHAR(DATE_TRUNC('quarter', qmd.qtd_max_date), 'YYYY-Q') AS qtd_period,
        COUNT(DISTINCT CASE WHEN e.status = 'resign' AND e.snapshot_date <= qmd.qtd_max_date AND DATE_TRUNC('quarter', e.snapshot_date) = DATE_TRUNC('quarter', qmd.qtd_max_date) THEN e.employee_id END) AS num_resigned_qtd,
        COUNT(DISTINCT CASE WHEN e.status = 'in service' AND e.snapshot_date <= qmd.qtd_max_date AND DATE_TRUNC('quarter', e.snapshot_date) = DATE_TRUNC('quarter', qmd.qtd_max_date) THEN e.employee_id END) AS num_in_service_qtd
    FROM 
        employee e,
        QTDMaxDate qmd
)
-- 计算 QTD 平均员工数量和员工流失率
SELECT 
    qtd_period,
    num_resigned_qtd,
    num_in_service_qtd,
    ((num_resigned_qtd + num_in_service_qtd) / 2) AS average_employees_qtd,
    ROUND(100.0 * num_resigned_qtd / ((num_resigned_qtd + num_in_service_qtd) / 2), 2) AS turnover_rate_qtd
FROM 
    QTDData;
```

### 计算 YTD 员工流失率
```sql
-- 先获取所有 distinct 的 snapshot_date 中的最大年份的最大日期作为 YTD 的截止日期
WITH YTDMaxDate AS (
    SELECT MAX(snapshot_date) AS ytd_max_date
    FROM (
        SELECT DISTINCT snapshot_date
        FROM employee
    ) AS subquery
    WHERE DATE_TRUNC('year', snapshot_date) = DATE_TRUNC('year', (SELECT MAX(snapshot_date) FROM (SELECT DISTINCT snapshot_date FROM employee) AS inner_subquery))
),
-- 计算本年度至今的相关数据
YTDData AS (
    SELECT 
        TO_VARCHAR(DATE_TRUNC('year', ymd.ytd_max_date), 'YYYY') AS ytd_period,
        COUNT(DISTINCT CASE WHEN e.status = 'resign' AND e.snapshot_date <= ymd.ytd_max_date AND DATE_TRUNC('year', e.snapshot_date) = DATE_TRUNC('year', ymd.ytd_max_date) THEN e.employee_id END) AS num_resigned_ytd,
        COUNT(DISTINCT CASE WHEN e.status = 'in service' AND e.snapshot_date <= ymd.ytd_max_date AND DATE_TRUNC('year', e.snapshot_date) = DATE_TRUNC('year', ymd.ytd_max_date) THEN e.employee_id END) AS num_in_service_ytd
    FROM 
        employee e,
        YTDMaxDate ymd
)
-- 计算 YTD 平均员工数量和员工流失率
SELECT 
    ytd_period,
    num_resigned_ytd,
    num_in_service_ytd,
    ((num_resigned_ytd + num_in_service_ytd) / 2) AS average_employees_ytd,
    ROUND(100.0 * num_resigned_ytd / ((num_resigned_ytd + num_in_service_ytd) / 2), 2) AS turnover_rate_ytd
FROM 
    YTDData;
```

### 代码解释

#### MTD 计算部分
1. **MTDMaxDate CTE**：
首先通过子查询获取 `employee` 表中所有不同的 `snapshot_date`。然后在外部查询中，筛选出这些日期中最大月份的日期，并从中选取最大的日期作为 MTD 计算的截止日期 `mtd_max_date`。这样可以确保是基于该月最后一天的数据来计算 MTD 员工流失率。
2. **MTDData CTE**：
基于前面得到的 MTD 截止日期，按照日期条件筛选出当月至今的数据。使用 `COUNT(DISTINCT...)` 函数分别统计离职员工和在职员工的唯一 `employee_id` 数量，并按照月份进行格式化显示时间段。
3. **最终计算和输出**：
根据 MTDData 中统计的离职和在职员工数量，计算平均员工数量，再按照员工流失率的计算公式得出 MTD 员工流失率，并保留两位小数输出。

#### QTD 和 YTD 计算部分
逻辑与 MTD 计算部分类似，只是时间粒度从月份分别变为季度和年份。在 `QTDMaxDate` CTE 中获取最大季度的最大日期作为 QTD 计算的截止日期；在 `YTDMaxDate` CTE 中获取最大年份的最大日期作为 YTD 计算的截止日期。后续基于这些截止日期分别进行相关数据的统计和员工流失率的计算。

你可以在 Superset 的 SQL Lab 中依次复制粘贴上述代码并执行，以分别获取 MTD、QTD 和 YTD 的员工流失率计算结果。 