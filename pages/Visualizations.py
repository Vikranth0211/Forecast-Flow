
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📈 Data Visualization")

if 'raw_data' in st.session_state:
    df = st.session_state['raw_data']

    st.subheader("📉 Monthly Sales Trends")
    st.line_chart(df[['Month1', 'Month2', 'Month3']])

    st.subheader("📊 Average Sales by Promotion")
    avg_by_promo = df.groupby('Promo')['Month3'].mean().reset_index()
    st.bar_chart(avg_by_promo.set_index('Promo'))

    st.subheader("📊 Average Sales by Holiday")
    avg_by_holiday = df.groupby('Holiday')['Month3'].mean().reset_index()
    st.bar_chart(avg_by_holiday.set_index('Holiday'))

else:
    st.warning("Please upload data on the 'Data Upload' page first.")
