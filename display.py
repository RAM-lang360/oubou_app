import streamlit as st
def csv_import():
    # ヘッダーなしで読み込む → 自動的に列番号が 0, 1, 2, ... になる
    df = pd.read_csv('data.csv', header=None)

    # 各列（0列目と1列目）からNaNを除いてランダムに5つ抽出
    col0 = df[0].dropna()
    col1 = df[1].dropna()


    random_5_col0 = col0.sample(n=5, random_state=42).reset_index(drop=True)
    random_5_col1 = col1.sample(n=5, random_state=42).reset_index(drop=True)

    return random_5_col0, random_5_col1
# 最初の5つの文字列
left_strings,right_strings=csv_import()

# タイトル
st.title("10個の文字列から2つを選んでラベル用に")

# 文字列を札に書かれたように表示
st.write("以下の文字列から、ラベル用に2つを選んでください:")

# 左側の5つの文字列を表示
st.write("左側の文字列:")
col1, col2 = st.columns(2)

with col1:
    for s in left_strings:
        st.markdown(f"<div style='border: 2px solid white; padding: 10px; margin: 5px; display: inline-block; font-size: 20px; text-align: center;'>{s}</div>", unsafe_allow_html=True)

# 右側の5つの文字列を表示
with col2:
    for s in right_strings:
        st.markdown(f"<div style='border: 2px solid black; padding: 10px; margin: 5px; display: inline-block; font-size: 20px; text-align: center;'>{s}</div>", unsafe_allow_html=True)

# 文字列を選択するためのインタラクティブなラジオボタン
all_strings = left_strings + right_strings
selected = st.multiselect("ラベル用に選ぶ文字列", all_strings, default=[])

# 選択されたものを表示
if len(selected) == 2:
    st.write(f"選ばれたラベル: {selected[0]} と {selected[1]}")
else:
    st.write("2つの文字列を選んでください。")
