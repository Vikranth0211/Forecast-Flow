#Month1 and Month2 Forecasting
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

st.title("🔮 Forecasting")

if 'raw_data' in st.session_state:
    df = st.session_state['raw_data']
    X = df[['Month1', 'Month2']]
    y = df['Month3']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

    model = LinearRegression()
    model.fit(X_train, y_train)

    st.session_state['model'] = model
    st.session_state['scaler'] = scaler

    st.subheader("Make Prediction")
    m1 = st.number_input("Month 1", min_value=0.0)
    m2 = st.number_input("Month 2", min_value=0.0)

    if st.button("Predict"):
        input_scaled = scaler.transform([[m1, m2]])
        result = model.predict(input_scaled)
        st.success(f"Predicted Month 3 Sales: {result[0]:.2f}")
else:
    st.warning("Upload data in 'Data Upload' page first.")
