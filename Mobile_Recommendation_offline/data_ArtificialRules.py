import pandas as pd
import numpy as np


def get_date(time):
    date, hour = time.split(" ")
    return date

def get_hour(time):
    date, hour = time.split(" ")
    return hour


# 商品全集
userAll = pd.read_csv('tianchi_fresh_comp_train_user.csv', usecols=['user_id', 'item_id', 'behavior_type', 'time'])
# print(userAll[0:4])
# print(userAll.info())
# print(userAll.duplicated().sum())

# 商品子集
itemSub = pd.read_csv('tianchi_fresh_comp_train_item.csv', usecols=['item_id'])
# print(itemSub[0:5])
# print(itemSub.item_id.value_counts().head())
# print(itemSub.duplicated().sum())

# 去除重复的行
itemSet = itemSub[['item_id']].drop_duplicates()

# 取user和item子集上的交集
userSub = pd.merge(userAll, itemSet, on='item_id', how='inner')

#将时间中的小时去除
userSub['time'] = userSub['time'].map(get_date)

#取出18号的数据
userSubTime=userSub[userSub['time']=='2014-12-18']

#取出加购物车和购买行为的数据
userSub_34=userSubTime[userSubTime['behavior_type'].isin([3,4])]

#
userSub_3=userSub_34[userSub_34['behavior_type'].isin([3])][['user_id','item_id','time']]
userSub_4=userSub_34[userSub_34['behavior_type'].isin([4])][['user_id','item_id','time']]

userSub_3.columns=['user_id','item_id','time3']
userSub_4.columns=['user_id','item_id','time4']

#取并集
result = pd.merge(userSub_3,userSub_4,on=['user_id','item_id'],how='outer')
#加购物车已经购买的
result_4=result.dropna()

result3=result[result['time4'].isnull()].drop(['time4'],axis=1)
result3=result3.dropna()
result3.drop_duplicates()

result3.to_csv('tianchi_mobile_recommendation_predict.csv',columns=['user_id','item_id'],index=False)
