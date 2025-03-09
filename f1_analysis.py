import streamlit as st
import fastf1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit UI
st.title("🏎️ Formula 1 Data Analysis Dashboard")
st.sidebar.header("Select Race Details")

# User inputs
year = st.sidebar.selectbox("Select Year", [2023, 2022, 2021])
race_name = st.sidebar.text_input("Enter Race Name (e.g., Abu Dhabi)")
session_type = st.sidebar.selectbox("Session Type", ["R", "Q", "FP2"])
driver_filter = st.sidebar.multiselect("Select Drivers for Comparison", driver_laps, default=driver_laps[:2])

# Load race data
if st.sidebar.button("Load Data"):
    try:
        session = fastf1.get_session(year, race_name, session_type)
        session.load()
        st.success(f"Data Loaded for {race_name} {year} ({session_type})")

         # Extract Lap Data
        st.subheader("Lap Time Analysis")
        driver_laps = session.laps["Driver"].unique()
        driver_filter = st.sidebar.multiselect("Select Drivers for Comparison", driver_laps, default=driver_laps[:2])
        filtered_laps = session.laps[session.laps["Driver"].isin(driver_filter)]
        filtered_laps["LapTime"] = filtered_laps["LapTime"].dt.total_seconds()
    
        # Plot Lap Times
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.lineplot(data=filtered_laps, x="LapNumber", y="LapTime", hue="Driver", ax=ax)
        plt.xlabel("Lap Number")
        plt.ylabel("Lap Time (seconds)")
        plt.title("Lap Time Comparison")
        st.pyplot(fig)
    
        # Pit Stop Analysis
        st.subheader("Pit Stop Strategy")
        pit_stops = session.laps[["Driver", "LapNumber", "Compound"]].drop_duplicates()
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.scatterplot(data=pit_stops, x="LapNumber", y="Driver", hue="Compound", s=100, ax=ax)
        plt.xlabel("Lap Number")
        plt.ylabel("Driver")
        plt.title("Pit Stop Strategy")
        plt.legend(title="Tire Compound")
        st.pyplot(fig)
    
        # Sector Times Analysis
        st.subheader("Sector Times Analysis")
        sector_times = session.laps[session.laps["Driver"].isin(driver_filter)][["Driver", "LapNumber", "Sector1Time", "Sector2Time", "Sector3Time"]].dropna()
        sector_times = sector_times.melt(id_vars=["Driver", "LapNumber"], var_name="Sector", value_name="Time")
        sector_times["Time"] = sector_times["Time"].dt.total_seconds()
    
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.lineplot(data=sector_times, x="LapNumber", y="Time", hue="Sector", style="Driver", ax=ax)
        plt.xlabel("Lap Number")
        plt.ylabel("Sector Time (seconds)")
        plt.title("Sector Times Comparison")
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Error loading data: {e}")
