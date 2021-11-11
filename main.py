# -*- coding:utf-8 -*-
from utils import loadVersion
from cocutils import procDataFrame, findAllFile, sc2png
import pandas as pd
import xlsxviewer

print('cocutils version is {}'.format(loadVersion()))

df = pd.read_csv('./coccsv/logic/characters.csv')
df1 = procDataFrame(df)
df1.to_excel('./output/characters.xlsx')
xlsxviewer.genDataFrameScattersWithColumn(df1, 'Name', ['HP'], ['level'], ['Hitpoints'], './output/characters_HP.html', 'lines', False)
xlsxviewer.genDataFrameScattersWithColumn(df1, 'Name', ['DPS'], ['level'], ['DPS'], './output/characters_DPS.html', 'lines', False)

df = pd.read_csv('./coccsv/logic/buildings.csv')
df1 = procDataFrame(df)
df1.to_excel('./output/buildings.xlsx')
xlsxviewer.genDataFrameScattersWithColumn(df1, 'Name', ['HP'], ['level'], ['Hitpoints'], './output/buildings_HP.html', 'lines', False)
xlsxviewer.genDataFrameScattersWithColumn(df1, 'Name', ['DPS'], ['level'], ['DPS'], './output/buildings_DPS.html', 'lines', False)

df = pd.read_csv('./coccsv/logic/heroes.csv')
df1 = procDataFrame(df)
df1.to_excel('./output/heroes.xlsx')
xlsxviewer.genDataFrameScattersWithColumn(df1, 'Name', ['HP'], ['level'], ['Hitpoints'], './output/heroes_HP.html', 'lines', False)
xlsxviewer.genDataFrameScattersWithColumn(df1, 'Name', ['DPS'], ['level'], ['DPS'], './output/heroes_DPS.html', 'lines', False)

for fn in findAllFile('./cocsc/', '_tex.sc'):
    print(fn)
    sc2png(fn, './output')