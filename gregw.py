import pandas as pd
import numpy as np
from xgboost import XGBRegressor, XGBClassifier

def impute_reg(col1, df):
    if str(df[col1].dtype) not in ('float32', 'float64'):
        print "Wrong Type"
        return
    target = df[col1]
    column_names = list(df.columns)
    column_names.remove(col1)
    nex = pd.get_dummies(df[column_names], drop_first = True)
    nex = pd.concat([target, nex], axis = 1)
    train = nex[pd.isnull(nex[col1]) == False]
    pred = nex[pd.isnull(nex[col1]) == True]
    if len(pred) == 0:
        print "No Missing / NaN Data"
        return
    y = train[col1]
    train.drop(col1, axis = 1, inplace = True)
    pred.drop(col1, axis = 1, inplace = True)
    XGB = XGBRegressor()
    XGB.fit(train, y)
    for x in list(pred.index):
        value = XGB.predict(pred.loc[[x]])
        df.loc[x, col1] = value[0]
    return df

def impute_cal(col1, df):
    if df[col1].dtype != 'object':
        print "Wrong Type"
        return
    target = df[col1]
    column_names = list(df.columns)
    column_names.remove(col1)
    nex = pd.get_dummies(df, drop_first = True)
    nex = pd.concat([target, nex], axis = 1)
    train = nex[pd.isnull(nex[col1]) == False]
    pred = nex[pd.isnull(nex[col1]) == True]
    if len(pred) == 0:
        print pred
        print "No Missing / NaN Data"
        return
    y = train[col1]
    pred.drop(col1, axis = 1, inplace = True)
    train.drop(col1, axis = 1, inplace = True)    
    XGB = XGBClassifier()
    XGB.fit(train, y)
    for x in list(pred.index):
        value = XGB.predict(pred.loc[[x]])
        df.loc[x, col1] = value[0]
    return df

def dataset():
    data = pd.DataFrame({
        'rain': [0, 0, 1, 1, 1, -1, 0, -1],
        'sprinkler': [0, 1, 1, 0, 1, 0, 1, -1],
        'wet_sidewalk': [0, 1, 1, 1, 1, 1, -1, 0],
        'some_num': [1.1, np.NaN, 0.2, -0.4, 0.1, 0.2, 0.0, 3.9],
        'some_str': ['B', 'A', 'A', 'A', 'A', 'A', 'A', np.NaN]
    })
    return data