import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))


import pandas as pd
import numpy as np

import pdb
pd.set_option('display.max_columns', 100)

from util.file_helper import FileReader


# ##################################
# shop 정리
# file_path = r'./../../data/csv/store/yogiyo_store(total).csv'
# df = pd.read_csv(file_path, sep=',', encoding='utf-8-sig')
#
#
#
# df = df[['id', 'name', 'address', 'categories', 'lat', 'lng', 'open_time_description',
#          'review_avg', 'review_count', 'logo_url']]
#
#
# df = df.rename({'id': 'shop_id', 'name': 'shop_name', 'address': 'shop_addr',
#                 'categories': 'cat', 'lat': 'shop_lat', 'lng': 'shop_lng',
#                 'open_time_description': 'open_time', 'review_avg': 'shop_rev_avg',
#                 'review_count': 'shop_rev_cnt', 'logo_url': 'shop_img'}, axis='columns')
#
# # print(df.columns)
# print(df.head())
#
# df.to_csv(f'./../../data/csv/store/shop.csv', sep=',', encoding='utf-8-sig', index=False)

# ###############################

# ##################################
# review 정리
file_path = r'./../../data/csv/important/review_df(37.520775, 127.022767).csv'
df = pd.read_csv(file_path, sep=',', encoding='utf-8-sig')

# 리뷰시간을 오더시간으로도 복제
col = df['time']
df['order_time'] = col


# 컬럼명 변경
df = df.rename({'orderid': 'or_id', 'comment': 'review_cmnt', 'rating_taste': 'taste_rate',
                'rating_quantity': 'quantity_rate', 'rating_delivery': 'delivery_rate',
                'time': 'review_time', 'owner_comment': 'owner_cmnt', 'id': 'shop_id'}, axis='columns')

# 컬럼 순서 조정
df = df[['or_id', 'order_time', 'review_cmnt', 'taste_rate', 'quantity_rate',
         'delivery_rate', 'review_time', 'owner_cmnt', 'userid', 'shop_id', 'food_id']]



# print(df.columns)
# print(df.head())
#
df.to_csv(f'./../../data/csv/reviewxxx.csv', sep=',', encoding='utf-8-sig', index=False)

# ###############################

# ##############################
# review 데이터에 평점 세부 분야 추가
# file_path = r'./../../data/csv/review.csv'
# df = pd.read_csv(file_path, sep=',', encoding='utf-8-sig')
#
# df = df[['customerid', 'rating_quantity', 'rating_taste', 'rating_delivery']]
#
# df = df.rename({'customerid': 'orderid'}, axis='columns')
# print(df.head())
#
# # pdb.set_trace()
#
# file_path = r'./../../data/csv/gangnam_seocho(add_owner_cmnt).csv'
# df2 = pd.read_csv(file_path, sep=',', encoding='utf-8-sig')
#
# merge_df = pd.merge(df, df2, on='orderid')
#
# merge_df.to_csv('review_df(add_owner_cmnt_rates).csv', sep=',', encoding='utf-8-sig', index=False)

# ##################################

# file_path = r'./../../data/csv/important/review_df(37.520775, 127.022767).csv'
# df2 = pd.read_csv(file_path, sep=',', encoding='utf-8-sig')
#
# merge_df = pd.merge(df, df2, on='orderid')
#
# merge_df.to_csv('review_dfx.csv', sep=',', encoding='utf-8-sig', index=False)















