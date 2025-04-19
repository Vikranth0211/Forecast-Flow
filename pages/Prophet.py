import streamlit as st
from prophet import Prophet
import pandas as pd
import matplotlib.pyplot as plt

st.title("🕒 Time Series Forecasting with Prophet")

if 'raw_data' in st.session_state:
    df = st.session_state['raw_data']
    if 'Date' not in df.columns or 'Month3' not in df.columns:
        st.error("Dataset must contain 'Date' and 'Month3' columns for Prophet.")
    else:
        df_prophet = df[['Date', 'Month3']].rename(columns={"Date": "ds", "Month3": "y"})
        df_prophet['ds'] = pd.to_datetime(df_prophet['ds'])

        model = Prophet()
        model.fit(df_prophet)

        periods = st.slider("Months to forecast:", 1, 24, 6)
        future = model.make_future_dataframe(periods=periods, freq='M')
        forecast = model.predict(future)

        fig1 = model.plot(forecast)
        st.pyplot(fig1)
else:
    st.warning("Upload time-indexed data in 'Data Upload' page first.")