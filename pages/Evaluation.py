# Create Evaluation.py with metrics for selected product model

import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np
import pandas as pd

st.title("📊 Product-wise Model Evaluation")

if 'raw_data' in st.session_state:
    df = st.session_state['raw_data']

    if 'Product' not in df.columns or 'Month1' not in df.columns or 'Month2' not in df.columns or 'Month3' not in df.columns:
        st.error("❌ Dataset must include 'Product', 'Month1', 'Month2', and 'Month3' columns.")
    else:
        selected_product = st.selectbox("Select a Product for Evaluation:", df['Product'].unique())
        product_df = df[df['Product'] == selected_product]

        st.write(f"📋 Evaluation Data for **{selected_product}**")
        st.dataframe(product_df)

        # Prepare model
        X = product_df[['Month1', 'Month2']]
        y = product_df['Month3']
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Evaluation metrics
        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        rmse = mean_squared_error(y_test, y_pred, squared=False)

        st.subheader("📈 Evaluation Metrics")
        st.metric("R² Score", f"{r2:.2f}")
        st.metric("Mean Absolute Error (MAE)", f"{mae:.2f}")
        st.metric("Root Mean Squared Error (RMSE)", f"{rmse:.2f}")
else:
    st.warning("Please upload data on the 'Data Upload' page first.")

