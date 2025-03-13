import streamlit as st
import pandas as pd
import numpy as np
import random
from sklearn.ensemble import RandomForestClassifier

# Title of the Streamlit app
st.title("🏏 Fantasy Cricket AI - Team Predictor")

# Load sample player data (Replace with actual dataset)
data = {
    "Player": ["Virat Kohli", "Rohit Sharma", "MS Dhoni", "Jasprit Bumrah", "Hardik Pandya", "KL Rahul"],
    "Batting Avg": [58, 45, 50, 20, 35, 42],
    "Bowling Avg": [0, 5, 0, 18, 25, 0],
    "Strike Rate": [135, 140, 130, 90, 150, 145],
    "Wickets": [0, 2, 0, 150, 75, 0],
}
df = pd.DataFrame(data)

st.subheader("📊 Player Stats")
st.dataframe(df)

# Select players to form a team
st.subheader("🏏 Select Your Fantasy Team")
selected_players = st.multiselect("Choose 11 Players:", df["Player"].tolist())

if len(selected_players) == 11:
    st.success("✅ You have selected 11 players!")
else:
    st.warning("⚠ Please select exactly 11 players!")

# AI Prediction Model (Dummy Model for Now)
st.subheader("🔮 AI Match Outcome Prediction")
if st.button("Predict Result"):
    if len(selected_players) != 11:
        st.error("❌ Please select exactly 11 players to proceed!")
    else:
        # Dummy AI Model
        random_outcome = random.choice(["Win", "Lose", "Draw"])
        st.write(f"**Prediction:** Your Fantasy Team is likely to **{random_outcome}** the match! 🏆")

st.markdown("---")
st.caption("Created by Fantasy Cricket AI - Powered by Streamlit 🚀")
