import streamlit as st
import pandas as pd

# app.py (홈 페이지)
# st.title(" 심부전 분석")
# st.write("👈 메뉴를 선택하세요")

def home():      
    st.title("🏠 홈")
def data():
    st.title("📊 데이터")
    
pg = st.navigation([  
    st.Page(home, title="홈",
        icon="🏠", default=True),
    st.Page(data, title="데이터",
        icon="📊"),
])
pg.run() 