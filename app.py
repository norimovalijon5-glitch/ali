import streamlit as st
import pandas as pd
from main import EnterpriseDecisionIntelligenceEngine

# Sahifa sozlamalari
st.set_page_config(page_title="Enterprise Decision Intelligence | CEO Dashboard", layout="wide")

# Xavfsizlik va kirish nazorati (Access Control)
st.sidebar.header("🔐 Security & Access Control")
user_role = st.sidebar.selectbox("Select User Role", ["Employee", "CEO / Executive Board"])

if user_role != "CEO / Executive Board":
    st.error("ACCESS DENIED: This analytical dashboard is restricted exclusively to the CEO and Executive Board members.")
    st.stop()

st.title("📊 Executive Decision Intelligence Dashboard")
st.markdown("### Real-time AI Analytics & 90% Accuracy Forecasting")

# AI dvigatelni ishga tushirish
ai_engine = EnterpriseDecisionIntelligenceEngine(company_name="Global Enterprise Holdings Corp")

# Excel faylni yuklash yoki avtomatik tahlil qilish
uploaded_file = st.sidebar.file_uploader("Upload Corporate Excel Data", type=["xlsx", "xls"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📁 Live Data Stream Preview")
        st.dataframe(df.tail(5))
        
    with col2:
        st.subheader("⚠️ Operational Risk Assessment")
        risk_report = ai_engine.detect_operational_anomalies(df)
        if risk_report["status"] == "Optimal":
            st.success(f"Status: {risk_report['status']}")
        else:
            st.warning(f"Status: {risk_report['status']}")
            for issue in risk_report["issues_found"]:
                st.error(issue)

    st.markdown("---")
    st.subheader("🔮 Predictive Analytics & Future Forecast (90% Confidence)")
    
    if 'Revenue' in df.columns:
        forecast = ai_engine.generate_high_accuracy_forecast(df['Revenue'].tolist())
        
        m1, m2, m3 = st.columns(3)
        m1.metric(label="Current Value", value=f"${forecast.get('current_value', 0):,}")
        m2.metric(label="Predicted Next Period", value=f"${forecast.get('predicted_next_period_value', 0):,}", delta=forecast.get('projected_growth_percentage'))
        m3.metric(label="Model Accuracy", value=forecast.get('model_confidence_accuracy'))
        
        st.line_chart(df['Revenue'])
    else:
        st.info("Please ensure your Excel file contains a 'Revenue' column for advanced forecasting.")
else:
    st.info("👈 Please upload your corporate Excel file from the sidebar to activate the AI analysis stream.")
