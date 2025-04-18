## Power Query

1. 数据源类型：Folder
2. 筛选行：Filter Rows，equals = .xlsx
3. 添加自选列：Custom Column, = Excel.Workbook([Content])
4. 筛选工作表：[Item] = "Capex tracker"



## 0 COA 是一个科目总表	

1. TB 文件夹里的是每个月科目余额表，这里取1月2月为例								
2. Transaction 文件夹里是每个月发生明细，这里也拿了1月和2月为例								
                                
要求：	2. Transaction  每月发生明细总额与1. TB  发生科目额对比分析，查看是否有差异							
                                
对比方法
1. TB 里面的 M 列 (Debit rept.period) 减去 O 列 (Credit report per.) 是发生额，应该等于Transaction 的M列  (Amount in local currency) 综合							
2. 敏感信息我都删除了，但是字段的title 我都保留，如果需要删除什么请与我确认。							
