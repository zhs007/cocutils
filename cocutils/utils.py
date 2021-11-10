# -*- coding:utf-8 -*-
import pandas as pd

def isBoolTrue(val):
    if isinstance(val, bool):
        return val
    
    if isinstance(val, str):
        if val.lower() == 'true':
            return True
    
    return False

def procDataFrame(df):
    df['level'] = 1
    curname = ''
    curlevel = 1

    for i, d in df.iterrows():
        if i == 0:
            continue
        
        if i == 1:
            for cc in df.columns.values:
                if pd.isna(df.at[i, cc]):
                    if df.at[0, cc] == 'String':
                        df.at[i, cc] = ''
                    elif df.at[0, cc] == 'boolean':
                        df.at[i, cc] = False
                    elif df.at[0, cc] == 'int':
                        df.at[i, cc] = 0              
                        
                if df.at[0, cc] == 'int':
                    if pd.isna(df.at[i, cc]):
                        df.at[i, cc] = 0
                    else:
                        df.at[i, cc] = int(df.at[i, cc])

                if df.at[0, cc] == 'boolean':
                    if pd.isna(df.at[i, cc]):
                        df.at[i, cc] = False
                    else:
                        df.at[i, cc] = isBoolTrue(df.at[i, cc])                        
        else:       
            for cc in df.columns.values:                    
                if pd.isna(df.at[i, cc]):
                    df.at[i, cc] = df.at[i - 1, cc]            
                    
                if df.at[0, cc] == 'int':
                    if pd.isna(df.at[i, cc]):
                        df.at[i, cc] = 0
                    else:
                        df.at[i, cc] = int(df.at[i, cc])

                if df.at[0, cc] == 'boolean':
                    if pd.isna(df.at[i, cc]):
                        df.at[i, cc] = False
                    else:
                        df.at[i, cc] = isBoolTrue(df.at[i, cc])                    
                    
                        
        if df.at[i, 'Name'] == curname:
            curlevel = curlevel + 1
            df.at[i, 'level'] = curlevel
        else:
            curname = df.at[i, 'Name']
            curlevel = 1

    return df.drop(0).reset_index(drop=True)

