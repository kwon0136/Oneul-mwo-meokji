import streamlit as st
import pandas as pd
import random

st.title("🍱 오늘 점심 뭐 먹지")

# CSV에서 메뉴 불러오기
@st.cache_data
def load_menus():
    df = pd.read_csv("menus.csv")
    return df

df = load_menus()

# 거리 선택
distance_list = df['거리'].unique().tolist()
distance = st.selectbox("오늘의 이동거리를 정해주세요", distance_list)

# 추천 버튼
if st.button("추천 받기"):
    filtered = df[df['거리'] == distance]
    menu = random.choice(filtered['메뉴'].tolist())
    st.success(f"👉 '{menu}' 당첨!")
