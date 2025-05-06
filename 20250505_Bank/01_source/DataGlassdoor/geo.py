import pandas as pd
import os
from geonamescache import GeonamesCache


current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir, 'data.csv')

# 读取原始数据
df = pd.read_csv(csv_file_path)

# 初始化GeonamesCache
gc = GeonamesCache()
cities = gc.get_cities()
countries = gc.get_countries()

# 定义函数获取国家信息
def get_country_info(city):
    for city_info in cities.values():
        if city_info.get('name') == city:
            country_code = city_info.get('countrycode')
            if country_code:
                country_name = countries.get(country_code).get('name')
                return country_name, country_code
    return None, None

# 为每个城市补充国家信息
country_names = []
country_iso_codes = []
for index, row in df.iterrows():
    city = row['city']
    country_name, country_iso_code = get_country_info(city)
    country_names.append(country_name)
    country_iso_codes.append(country_iso_code)

# 将补充的信息添加到DataFrame
df['country_name'] = country_names
df['country_iso_code'] = country_iso_codes

# 保存结果
df.to_csv('data_with_country_info.csv', index=False)