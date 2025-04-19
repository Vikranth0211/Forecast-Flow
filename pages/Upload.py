import streamlit as st
import pandas as pd
from utils.sample_data_generator import generate_sample_dataset

st.title("📤 Upload Sales Data")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.session_state['raw_data'] = df
    st.success("✅ Data uploaded successfully!")
    st.write(df.head())
else:
    st.info("Please upload a CSV file to proceed.")

# 🔘 Button to generate sample data
st.markdown("---")
st.subheader("🚀 Need a sample dataset?")
if st.button("Generate Sample Sales Data"):
    sample_df = generate_sample_dataset("sample_sales_data.csv")
    st.session_state['raw_data'] = sample_df
    st.success("Sample dataset generated successfully!")
    st.write(sample_df.head())
    st.download_button("📥 Download Sample CSV", data=sample_df.to_csv(index=False).encode(), file_name="sample_sales_data.csv", mime="text/csv")
