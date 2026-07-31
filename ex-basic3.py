import streamlit as st

st.title("今日の料理")
st.header("カレーライス")
st.image("https://housefoods.jp/_sys/catimages/recipe/hfrecipe/items/00025463/0.1200-.jpeg")
st.subheader("材料")
md ="""
#材料
- 肉：300g
- ジャガイモ：2個
- 人参：小1本

###作り方
1. 材料を切る
2. 肉を痛める
3. 煮込んでルーをいれる
"""

st.markdown(md)

