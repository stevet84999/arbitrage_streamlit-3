import streamlit as st
from arbitrage_engine import find_arbitrage_opportunities
from odds_api import fetch_odds
from config import SPORTS, BOOKMAKERS, REGIONS, MARKETS

st.set_page_config(page_title="Arbitrage Betting Dashboard", layout="wide")
st.title("Arbitrage Betting Dashboard")

try:
    odds_data = fetch_odds(SPORTS, BOOKMAKERS, REGIONS, MARKETS)
    arbs = find_arbitrage_opportunities(odds_data)

    if arbs:
        st.success(f"Found {len(arbs)} arbitrage opportunities")
        for arb in arbs:
            st.subheader(arb["event"])
            st.write("Best Odds:", arb["best_odds"])
            st.write("Profit Margin:", f"{arb['profit_percent']}%")
            st.markdown("---")
    else:
        st.info("No arbitrage opportunities found at the moment.")
except Exception as e:
    st.error(f"Error: {e}")
