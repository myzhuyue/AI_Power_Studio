## Power Query

1. 数据源类型：Folder
2. 筛选行：Filter Rows，equals = .xlsx
3. 添加自选列：Custom Column, = Excel.Workbook([Content])
4. 筛选工作表：[Item] = "Capex tracker"
