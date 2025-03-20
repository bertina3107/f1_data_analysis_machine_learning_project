# Formula One Data Analysis and Prediction
https://cwbf1dataanalysisproject.streamlit.app/

<img width="1440" alt="Screen Shot 2025-03-20 at 11 27 08 AM" src="https://github.com/user-attachments/assets/85c3f289-8863-4254-af58-86512c8f9bd1" />

## Overview

This project analyzes historical Formula 1 race data from the Ergast API to identify trends and provide detailed race overviews. The first step involved preprocessing and cleaning the data, handling missing values, and standardizing formats to ensure accuracy. Using Python libraries like Pandas and Matplotlib, the data was then analyzed to uncover general trends across seasons and insights into specific races. Finally, a Random Forest Classifier was implemented to predict race winners based on factors such as starting grid position, team performance, and driver history.

## Features

1. Fetches real-time and historical F1 race data from the Ergast API for analysis and prediction.
2. Preprocesses and cleans the data, handling missing values and standardizing formats for consistency.
3. Analyzes historical race data to identify general trends, performance patterns, and race-specific insights using Python libraries like Pandas and Matplotlib.
4. Performs feature engineering, creating relevant attributes such as grid position, constructor wins, and driver wins to enhance model accuracy.
5. Trains a Random Forest Classifier to predict race winners based on engineered features.
6. Evaluates model performance using accuracy, classification reports, and feature importance to assess prediction reliability.
7. Provides race-by-race predictions for specific F1 seasons and visualizes actual vs. predicted winners using heatmaps.

## Data Sources

Ergast API (http://ergast.com/mrd/)
Data includes driver information, constructor details, grid positions, finishing positions, and race results from 2015 to 2023
Kaggle Dataset (https://www.kaggle.com/datasets/lakshayjain611/f1-races-results-dataset-1950-to-2024/data)

