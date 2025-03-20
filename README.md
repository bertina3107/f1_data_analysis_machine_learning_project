# Formula One Data Analysis and Prediction
https://cwbf1dataanalysisproject.streamlit.app/

<img width="1440" alt="Screen Shot 2025-03-20 at 11 27 08 AM" src="https://github.com/user-attachments/assets/85c3f289-8863-4254-af58-86512c8f9bd1" />

## Overview

This project aims to predict the winner of Formula 1 races using historical race data from the Ergast API. The model leverages machine learning techniques, specifically a Random Forest Classifier, to analyze various race factors such as starting grid position, team performance, and driver history.

## Features

1. Fetches real-time and historical F1 race data from the Ergast API

2. Performs feature engineering by creating relevant attributes like grid position, constructor wins, and driver wins

3. Trains a Random Forest Classifier to predict race winners

4. Evaluates model performance using accuracy, classification reports, and feature importance

5. Provides race-by-race predictions for specific F1 seasons

6. Compares actual vs. predicted winners using heatmaps

## Data Sources

Ergast API (http://ergast.com/mrd/)

Data includes driver information, constructor details, grid positions, finishing positions, and race results from 2015 to 2023

