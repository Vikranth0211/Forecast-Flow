import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

st.title("🔮 Product-wise Forecasting with Model Selection")

if 'raw_data' in st.session_state:
    df = st.session_state['raw_data']
    if 'Product' not in df.columns:
        st.error("The dataset must include a 'Product' column.")
    else:
        product = st.selectbox("Select a product:", df['Product'].unique())
        product_df = df[df['Product'] == product]

        X = product_df[['Month1', 'Month2']]
        y = product_df['Month3']

        model_name = st.selectbox("Choose a model:", ["Linear Regression", "Random Forest", "XGBoost"])

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

        if model_name == "Linear Regression":
            model = LinearRegression()
        elif model_name == "Random Forest":
            model = RandomForestRegressor()
        else:
            model = XGBRegressor()

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        st.subheader("📈 Forecast Visualization")
        fig, ax = plt.subplots()
        ax.plot(y_test.values, label='Actual')
        ax.plot(y_pred, label='Predicted')
        ax.legend()
        st.pyplot(fig)

        st.subheader("📌 Predict for Custom Input")
        m1 = st.number_input("Month 1", value=0.0)
        m2 = st.number_input("Month 2", value=0.0)
        input_scaled = scaler.transform([[m1, m2]])
        if st.button("Forecast"):
            result = model.predict(input_scaled)
            st.success(f"Predicted Month 3 Sales: {result[0]:.2f}")
else:
    st.warning("Upload data in 'Data Upload' page first.")
