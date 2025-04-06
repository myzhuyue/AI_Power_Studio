import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取数据
video_df = pd.read_excel('/01_source/Case Study.xlsx', sheet_name='Video data', engine='openpyxl')
live_df = pd.read_excel('/01_source/Case Study.xlsx', sheet_name='Live data', engine='openpyxl')
incentive_df = pd.read_excel('/01_source/Case Study.xlsx', sheet_name='Incentive mission data', engine='openpyxl')

# 合并数据
video_merged = pd.merge(video_df, incentive_df, on='Seller_code', how='left')
live_merged = pd.merge(live_df, incentive_df, on='Seller_code', how='left')

# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300

# 1. 渠道与活动目的交叉分析（分组柱状图）
# 计算各活动目的在不同渠道的GMV均值
channel_purpose_gmv = pd.concat([
    video_merged.groupby('Mission_purpose')['Video GMV'].mean().reset_index(name='GMV').assign(Channel='Video'),
    live_merged.groupby('Mission_purpose')['Lives GMV'].mean().reset_index(name='GMV').assign(Channel='Live')
])

# 绘制分组柱状图
plt.figure(figsize=(10, 6))
sns.barplot(x='Mission_purpose', y='GMV', hue='Channel', data=channel_purpose_gmv)
plt.title('Average GMV by Mission Purpose and Channel')
plt.xlabel('Mission Purpose')
plt.ylabel('Average GMV')
plt.legend(title='Channel')
plt.show()

# 2. 商家GMV分布与TOP案例（气泡图）
# 合并视频和直播数据
merged_data = pd.merge(video_df[['Seller_code', 'Duration_video (seconds)', 'Video GMV']],
                       live_df[['Seller_code', 'Duration_lives (minutes)', 'Lives GMV']],
                       on='Seller_code', how='outer')

# 绘制气泡图
plt.figure(figsize=(10, 6))
plt.scatter(merged_data['Duration_video (seconds)'], merged_data['Duration_lives (minutes)'],
            s=merged_data['Lives GMV'] + merged_data['Video GMV'], alpha=0.5)
plt.title('Merchant GMV Distribution (Bubble Size Represents GMV)')
plt.xlabel('Video Duration (seconds)')
plt.ylabel('Live Duration (minutes)')
plt.show()

# 3. 活动状态与GMV关联（折线图 + 面积图）
# 假设数据有时间维度，这里简单按日期排序，实际使用中需要根据真实数据处理
video_merged['Date'] = pd.to_datetime(video_merged['Date'])
live_merged['Date'] = pd.to_datetime(live_merged['Date'])

# 按日期和活动状态分组计算GMV总和
video_status_gmv = video_merged.groupby(['Date', 'Mission_status'])['Video GMV'].sum().unstack()
live_status_gmv = live_merged.groupby(['Date', 'Mission_status'])['Lives GMV'].sum().unstack()

# 绘制折线图 + 面积图
fig, axes = plt.subplots(2, 1, figsize=(10, 12))
video_status_gmv.plot.area(ax=axes[0])
axes[0].set_title('Relationship between Video Channel Mission Status and GMV')
axes[0].set_xlabel('Date')
axes[0].set_ylabel('Total GMV')

live_status_gmv.plot.area(ax=axes[1])
axes[1].set_title('Relationship between Live Channel Mission Status and GMV')
axes[1].set_xlabel('Date')
axes[1].set_ylabel('Total GMV')

plt.tight_layout()
plt.show()