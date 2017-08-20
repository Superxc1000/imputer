def gregwreg(col1, df):
    if str(df[col1].dtype) not in ('float32', 'float64'):
        print "Wrong Type"
        return
    import pandas as pd
    from xgboost import XGBRegressor
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