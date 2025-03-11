# f1_data_analysis_machine_learning_project
https://cwbf1dataanalysisproject.streamlit.app/

Overview

This project aims to predict the winner of Formula 1 races using historical race data from the Ergast API. The model leverages machine learning techniques, specifically a Random Forest Classifier, to analyze various race factors such as starting grid position, team performance, and driver history.

Features

Fetches real-time and historical F1 race data from the Ergast API

Performs feature engineering by creating relevant attributes like grid position, constructor wins, and driver wins

Trains a Random Forest Classifier to predict race winners

Evaluates model performance using accuracy, classification reports, and feature importance

Provides race-by-race predictions for specific F1 seasons

Compares actual vs. predicted winners using heatmaps

Data Sources

Ergast API (http://ergast.com/mrd/)

Data includes driver information, constructor details, grid positions, finishing positions, and race results from 2023 and 2024

