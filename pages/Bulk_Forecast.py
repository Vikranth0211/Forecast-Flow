import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

st.title("📦 Bulk Product Forecast")

uploaded = st.file_uploader("Upload CSV with 'Month1', 'Month2' columns for bulk forecast", type=['csv'])

if uploaded:
    data = pd.read_csv(uploaded)
    if not {'Month1', 'Month2'}.issubset(data.columns):
        st.error("Uploaded file must have 'Month1' and 'Month2' columns.")
    else:
        model = LinearRegression()
        dummy = pd.DataFrame({
            'Month1': np.random.randint(1000, 5000, 20),
            'Month2': np.random.randint(1000, 5000, 20)
        })
        dummy['Month3'] = dummy['Month1'] * 0.5 + dummy['Month2'] * 0.5
        X_train = dummy[['Month1', 'Month2']]
        y_train = dummy['Month3']

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_train)
        model.fit(X_scaled, y_train)

        input_scaled = scaler.transform(data[['Month1', 'Month2']])
        data['Predicted_Month3'] = model.predict(input_scaled)

        st.write("📄 Bulk Forecast Results:")
        st.write(data)

        st.download_button("Download Forecast CSV", data.to_csv(index=False).encode(), "bulk_forecast.csv", "text/csv")
else:
    st.info("Upload a dataset to forecast.")