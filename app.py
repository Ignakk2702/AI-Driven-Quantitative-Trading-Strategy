import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Quant Lab", layout="wide")

st.title("🤖 AI Trading Strategy: Walk-Forward Results")

# Load the data you uploaded to GitHub
@st.cache_data
def load_data():
    df = pd.read_csv("backtest_results.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    # Calculate Cumulative Returns
    df['Strategy_Cum_Ret'] = (1 + df['Strategy_Ret']).cumprod()
    df['Market_Cum_Ret'] = (1 + df['Ret']).cumprod()
    return df

data = load_data()

# Sidebar Stats
st.sidebar.header("Strategy Overview")
st.sidebar.write(f"Total Days Traded: {len(data)}")

# Main Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Return", f"{(data['Strategy_Cum_Ret'].iloc[-1]-1):.2%}")
col2.metric("Sharpe Ratio", f"{(data['Strategy_Ret'].mean()/data['Strategy_Ret'].std()):.2f}")
col3.metric("Win Rate", f"{(data['Pred'] == (data['Ret'] > 0)).mean():.2%}")

# Plotting
st.subheader("Growth of $1: Strategy vs Market")
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(data['Date'], data['Strategy_Cum_Ret'], label="AI Strategy", color="#2ecc71")
ax.plot(data['Date'], data['Market_Cum_Ret'], label="Market (Buy & Hold)", color="#e74c3c", alpha=0.5)
ax.legend()
st.pyplot(fig)
