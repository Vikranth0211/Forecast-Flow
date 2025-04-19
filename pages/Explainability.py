import streamlit as st
import shap
import numpy as np
import matplotlib.pyplot as plt

st.title("🧠 SHAP Explainability")

if 'raw_data' in st.session_state:
    df = st.session_state['raw_data']
    if 'Product' not in df.columns:
        st.error("The dataset must include a 'Product' column.")
    else:
        from sklearn.ensemble import RandomForestRegressor
        from sklearn.preprocessing import StandardScaler
        from sklearn.model_selection import train_test_split

        product = st.selectbox("Select a product:", df['Product'].unique())
        product_df = df[df['Product'] == product]
        X = product_df[['Month1', 'Month2']]
        y = product_df['Month3']

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

        model = RandomForestRegressor()
        model.fit(X_train, y_train)

        explainer = shap.Explainer(model.predict, X_test)
        shap_values = explainer(X_test)

#        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.subheader("Feature Importance (SHAP)")
        shap.summary_plot(shap_values, X_test, plot_type="bar", feature_names=["Month1", "Month2"])
        st.pyplot()
else:
    st.warning("Upload data in 'Data Upload' page first.")