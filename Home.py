
import streamlit as st

st.set_page_config(page_title="Forecast Flow", page_icon="📊")

st.markdown("""
    <style>
    .stApp {
        background-image: url("https://www.google.com/url?sa=i&url=https%3A%2F%2Falfapeople.com%2Fus%2Fdynamics-365-sales-forecast%2F&psig=AOvVaw0LhGtwYgDzMFb0BQUwv7N3&ust=1745176689966000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCNCoj_fn5IwDFQAAAAAdAAAAABAE");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .block-container {
        background-color: rgba(255, 255, 255, 0.90);
        padding: 2rem;
        border-radius: 12px;
    }

    h1, h2, h3 {
        color: #003366;
    }

    .stButton > button {
        background-color: #003366;
        color: white;
        font-weight: bold;
        border-radius: 6px;
        padding: 0.5rem 1rem;
    }

    .stButton > button:hover {
        background-color: #001f3f;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Forecast Flow")
st.markdown("""
Welcome to the **Professional Sales Forecasting App**!

**Key features:**
- 🔍 Predict future sales for multiple products
- 🧠 Choose ML models: Linear, Random Forest, XGBoost
- 🧾 Download results as CSV or PDF
- 🔐 Secure login (optional)
- 📈 SHAP, Prophet & growth analytics

👉 Use the sidebar to explore!
""")
