import pandas as pd
import numpy as np
from datetime import datetime
import io

# 生成更真实的测试数据
def generate_realistic_store_data():
    np.random.seed(42)
    
    # 创建时间范围：2024年1月到2025年12月
    dates = pd.date_range('2024-01-01', '2025-12-01', freq='MS')
    
    # 创建15个商店，使用更有意义的名称
    store_names = [
        '北京朝阳店', '上海静安店', '广州天河店', '深圳福田店', '成都锦江店',
        '杭州西湖店', '南京鼓楼店', '武汉江汉店', '西安雁塔店', '重庆渝中店',
        '苏州工业园区店', '天津和平店', '青岛市南店', '长沙芙蓉店', '郑州金水店'
    ]
    
    data = []
    
    for store in store_names:
        # 每个商店的初始特征
        base_area = np.random.randint(80, 300)  # 80-300平方米
        base_staff = np.random.randint(5, 20)   # 5-20名店员
        
        area = base_area
        staff = base_staff
        
        # 商店类型影响变化频率
        store_type = np.random.choice(['标准店', '旗舰店', '社区店'])
        
        for i, date in enumerate(dates):
            # 模拟业务变化（新店开业前几个月增长较快）
            if i < 6:  # 前6个月
                change_prob = 0.4
            else:
                change_prob = 0.2
            
            # 模拟面积变化
            if np.random.random() < change_prob:
                if store_type == '旗舰店':
                    area_change = np.random.choice([-20, -10, 15, 25, 30])
                elif store_type == '社区店':
                    area_change = np.random.choice([-5, -3, 3, 5, 8])
                else:  # 标准店
                    area_change = np.random.choice([-10, -5, 5, 10, 15])
                
                area = max(50, area + area_change)  # 最小面积50平方米
            
            # 模拟店员数量变化（更频繁）
            if np.random.random() < 0.35:
                if store_type == '旗舰店':
                    staff_change = np.random.choice([-3, -2, 2, 3, 4])
                else:
                    staff_change = np.random.choice([-2, -1, 1, 2, 3])
                
                staff = max(2, staff + staff_change)  # 最少2名店员
            
            # 季节性波动（节假日前后）
            month = date.month
            if month in [1, 2, 9, 10]:  # 春节、国庆等旺季
                seasonal_adjustment = np.random.randint(1, 3)
                current_staff = staff + seasonal_adjustment
            elif month in [6, 7, 8]:  # 淡季
                seasonal_adjustment = np.random.randint(-2, 0)
                current_staff = max(2, staff + seasonal_adjustment)
            else:
                current_staff = staff
            
            data.append({
                'YearMonth': date.strftime('%Y-%m'),
                'DateKey': int(date.strftime('%Y%m')),
                'StoreID': store,
                'StoreType': store_type,
                'StoreArea': area,
                'StaffCount': current_staff,
                'FullDate': date.replace(day=15)  # 月中作为参考日期
            })
    
    return pd.DataFrame(data)

# 生成数据
df = generate_realistic_store_data()

# 数据统计信息
print("=== 样例数据统计信息 ===")
print(f"数据时间范围：{df['YearMonth'].min()} 到 {df['YearMonth'].max()}")
print(f"商店数量：{df['StoreID'].nunique()} 家")
print(f"总数据量：{len(df):,} 行")
print(f"商店类型分布：")
print(df['StoreType'].value_counts())
print(f"\n商店面积统计：")
print(f"平均值：{df['StoreArea'].mean():.1f} 平方米")
print(f"最小值：{df['StoreArea'].min()} 平方米")
print(f"最大值：{df['StoreArea'].max()} 平方米")
print(f"\n店员数量统计：")
print(f"平均值：{df['StaffCount'].mean():.1f} 人")
print(f"最小值：{df['StaffCount'].min()} 人")
print(f"最大值：{df['StaffCount'].max()} 人")

# 显示前15行数据
print("\n=== 数据样例（前15行）===")
print(df.head(15).to_string(index=False))


# 创建数据下载链接
def create_download_links(df):
    # CSV格式
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False, encoding='utf-8-sig')
    csv_data = csv_buffer.getvalue()
    
    # Excel格式
    excel_buffer = io.BytesIO()
    with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='商店数据', index=False)
        # 添加数据说明工作表
        description = pd.DataFrame({
            '字段名': ['YearMonth', 'DateKey', 'StoreID', 'StoreType', 'StoreArea', 'StaffCount', 'FullDate'],
            '说明': [
                '年月（YYYY-MM格式）',
                '日期键（YYYYMM格式，用于关联日期表）',
                '商店名称',
                '商店类型（标准店/旗舰店/社区店）',
                '商店面积（平方米）',
                '店员数量（人）',
                '完整日期（用于排序和筛选）'
            ],
            '数据类型': ['文本', '整数', '文本', '文本', '整数', '整数', '日期']
        })
        description.to_excel(writer, sheet_name='数据字典', index=False)
    
    excel_data = excel_buffer.getvalue()
    
    return csv_data, excel_data

# 生成下载数据
csv_data, excel_data = create_download_links(df)

print("\n=== 数据文件已生成 ====")
print("您可以选择以下方式下载样例数据：")

# 在实际的Jupyter环境中，可以使用以下代码提供下载
# 这里提供保存到本地文件的方法
df.to_csv('store_data_sample.csv', index=False, encoding='utf-8-sig')
df.to_excel('store_data_sample.xlsx', index=False)

print("📥 数据文件已保存到本地：")
print("1. store_data_sample.csv (CSV格式)")
print("2. store_data_sample.xlsx (Excel格式)")

# 显示一些数据分析示例
print("\n=== 数据分析示例 ===")
latest_date = df['DateKey'].max()
latest_data = df[df['DateKey'] == latest_date]

print(f"最新时点（{latest_date}）数据统计：")
print(f"总商店面积：{latest_data['StoreArea'].sum():,} 平方米")
print(f"总店员数量：{latest_data['StaffCount'].sum():,} 人")
print(f"平均单店面积：{latest_data['StoreArea'].mean():.1f} 平方米")
print(f"平均单店店员：{latest_data['StaffCount'].mean():.1f} 人")

# 按商店类型统计
print(f"\n按商店类型统计（最新时点）：")
type_stats = latest_data.groupby('StoreType').agg({
    'StoreArea': ['count', 'mean', 'sum'],
    'StaffCount': ['mean', 'sum']
}).round(1)
print(type_stats)