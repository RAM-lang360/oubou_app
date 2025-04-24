import streamlit as st
import pandas as pd
import random as rd

def csv_import():
    df = pd.read_csv('data.csv', header=None)
    random_5_col0 = rd.sample(list(df[0]), 5)
    random_5_col1 = rd.sample(list(df[1]), 5)
    return random_5_col0, random_5_col1

# 初期化：セッションステートに文字列を保持
if "left_strings" not in st.session_state or "right_strings" not in st.session_state:
    left_strings, right_strings = csv_import()
    st.session_state.left_strings = left_strings
    st.session_state.right_strings = right_strings

# タイトル
st.title("10個の文字列から2つを選んでラベル用に")

st.write("以下の文字列から、ラベル用に2つを選んでください:")

# 表示
col1, col2 = st.columns(2)
with col1:
    st.write("左側の文字列:")
    for s in st.session_state.left_strings:
        st.markdown(
            f"<div style='border: 2px solid white; padding: 10px; margin: 5px; display: inline-block; font-size: 20px; text-align: center;'>{s}</div>",
            unsafe_allow_html=True)

with col2:
    st.write("右側の文字列:")
    for s in st.session_state.right_strings:
        st.markdown(
            f"<div style='border: 2px solid white; padding: 10px; margin: 5px; display: inline-block; font-size: 20px; text-align: center;'>{s}</div>",
            unsafe_allow_html=True)

# ユーザーの選択
selected0 = st.selectbox("上文字", st.session_state.left_strings)
selected1 = st.selectbox("下文字", st.session_state.right_strings)

# 確定ボタン
# 確定ボタン
if st.button("確定"):
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    # 結合した文字列を表示
    combined_label = " ".join(selected0 + selected1)
    st.markdown(
        f"""
        <div style='
            border: 4px solid #4CAF50;
            border-radius: 12px;
            padding: 30px;
            margin: 30px auto;
            width: fit-content;
            font-size: 36px;
            text-align: center;
            background-color: #f0f0f0;
            color: #333;
            box-shadow: 4px 4px 10px rgba(0,0,0,0.1);
        '>{combined_label}</div>
        """,
        unsafe_allow_html=True
    )
else:
    st.write("2つの文字列を選んでください。")

