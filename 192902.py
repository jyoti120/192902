import streamlit as st
import pandas as pd

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="1929 Crash – Investing Activities",
    layout="centered"
)

st.title("📉 1929 Crash & Great Depression")
st.subheader("Key Investing Activities & Market Impact")

# -----------------------------
# Data
# -----------------------------
data = {
    "Investing Activity": [
        "Margin Buying (Speculative Leverage)",
        "Panic Selling & Mass Liquidation",
        "Flight to Safety (Government Bonds)",
        "Short Selling (Bearish Bets)",
        "Government Investment (New Deal)"
    ],
    "Impact Intensity (1–5)": [5, 5, 3, 4, 4]
}

df = pd.DataFrame(data)
df = df.set_index("Investing Activity")

# -----------------------------
# Show Data
# -----------------------------
st.markdown("### 📊 Impact Comparison Chart")
st.bar_chart(df)

# -----------------------------
# Explanation
# -----------------------------
st.markdown("""
### 🔍 Interpretation
- **Margin buying** and **panic selling** caused extreme market collapse  
- **Government bonds** acted as a safe haven  
- **Short sellers** profited during the downturn  
- **New Deal investments** helped revive demand and employment  
""")
