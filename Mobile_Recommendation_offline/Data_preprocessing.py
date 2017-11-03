import numpy as np
import pandas as pd

if __name__ == '__main__':
    userTable=pd.read_csv('../DataSet/tianchi_fresh_comp_train_user.csv',\
    usecols = ['user_id','item_id','behavior_type','time'])
    itemTable=pd.read_csv('../DataSet/tianchi_fresh_comp_train_item.csv')
    userTable=userTable[userTable.item_id.isin(list(itemTable.item_id))]
    userTable['days']=userTable['time'].map(lambda x:x.split(' ')[0])
    userTable['hour']=userTable['time'].map(lambda x:x.split(' ')[1])
    userTable=userTable[userTable['days'] != '2014-12-11']
    userTable=userTable[userTable['days'] != '2014-12-12']
    userTable.to_csv('../DataSet/subData.csv',index=None)
