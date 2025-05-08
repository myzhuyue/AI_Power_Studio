import pandas as pd
import os
from openpyxl import load_workbook

# 定义文件路径
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir,  'review.xlsx')

# 读取文件
excel_file = pd.ExcelFile(file_path)

# 获取所有表名
sheet_names = excel_file.sheet_names
sheet_names

# 遍历不同工作表表
# for sheet_name in sheet_names:
#     # 获取当前工作表的数据
#     df = excel_file.parse(sheet_name)

#     # 查看数据的基本信息
#     print(f'sheet表名为{sheet_name}的基本信息：')
#     df.info()

#     # 查看数据集行数和列数
#     rows, columns = df.shape

#     if rows < 100 and columns < 20:
#         # 短表数据（行数少于100且列数少于20）查看全量数据信息
#         print(f'sheet表名为{sheet_name}的全部内容信息：')
#         print(df.to_csv(sep='\t', na_rep='nan'))
#     else:
#         # 长表数据查看数据前几行信息
#         print(f'sheet表名为{sheet_name}的前几行内容信息：')
#         print(df.head().to_csv(sep='\t', na_rep='nan'))

# 读取数据
df_review_header = excel_file.parse('review_header')
df_category = excel_file.parse('category')

# 填充 pros 和 cons 字段的缺失值为空字符串
df_review_header['pros'] = df_review_header['pros'].fillna('')
df_review_header['cons'] = df_review_header['cons'].fillna('')

# 加载 Excel 文件
wb = load_workbook(file_path)

# 获取工作表
ws = wb['review_line']

# 插入表头
ws.append(['reviewID', 'Pros or Cons', 'Main Category', 'Sub-category'])

# 遍历 review_header 表的每一行
for index, row in df_review_header.iterrows():
    review_id = row['reviewID']
    pros = row['pros']
    cons = row['cons']

    # 遍历 category 表的每一行
    for cat_index, cat_row in df_category.iterrows():
        main_category = cat_row['Main Category']
        sub_category = cat_row['Sub-category']
        keywords = cat_row['Keyword'].split(', ')

        # 检查 pros 是否包含关键字
        for keyword in keywords:
            if keyword.strip().lower() in pros.lower():
                ws.append([review_id, 'Pros', main_category, sub_category])

        # 检查 cons 是否包含关键字
        for keyword in keywords:
            if keyword.strip().lower() in cons.lower():
                ws.append([review_id, 'Cons', main_category, sub_category])

# 保存修改后的 Excel 文件
wb.save('./AI_Power_Studio/20250505_Bank/01_source/DataGlassdoor/review_updated.xlsx')