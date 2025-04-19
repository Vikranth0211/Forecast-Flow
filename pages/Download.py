
import streamlit as st
import pandas as pd

st.title("📥 Download Forecast Output")

if all(k in st.session_state for k in ['raw_data', 'model', 'scaler']):
    df = st.session_state['raw_data'].copy()
    X = df[['Month1', 'Month2']]
    X_scaled = st.session_state['scaler'].transform(X)
    df['Predicted_Month3'] = st.session_state['model'].predict(X_scaled)

    st.write(df.head())

    st.download_button(
        "Download Predictions",
        data=df.to_csv(index=False).encode(),
        file_name="sales_predictions.csv",
        mime="text/csv"
    )
else:
    st.warning("Train a model first in 'Forecasting' page.")
