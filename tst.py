import streamlit as st
import pandas as pd
import random as rd
def csv_import():
    # ヘッダーなしで読み込む → 自動的に列番号が 0, 1, 2, ... になる
    df = pd.read_csv('data.csv', header=None)

    print(type(list(df)))
    # random_5_col0 = rd.sample(df[0],5)
    # random_5_col1 = rd.sample(df[1],5)

    # return random_5_col0, random_5_col1
# 最初の5つの文字列
csv_import()