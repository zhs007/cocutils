# -*- coding:utf-8 -*-
from utils import loadVersion
from cocutils import procDataFrame
import pandas as pd

print('cocutils version is {}'.format(loadVersion()))

df = pd.read_csv('./coccsv/logic/characters.csv')
df1 = procDataFrame(df)
df1.to_excel('./output/characters.xlsx')

df = pd.read_csv('./coccsv/logic/buildings.csv')
df1 = procDataFrame(df)
df1.to_excel('./output/buildings.xlsx')

df = pd.read_csv('./coccsv/logic/heroes.csv')
df1 = procDataFrame(df)
df1.to_excel('./output/heroes.xlsx')