# streamlit-youtube-monetization
📊 YouTube Content Monetization Modeler
📌 Project Overview

The YouTube Content Monetization Modeler is a machine learning project designed to predict YouTube advertisement revenue based on video performance metrics such as views, likes, comments, watch time, and audience location.

This project demonstrates how data analytics and predictive modeling can help content creators and media companies estimate revenue and optimize their content strategy.

The project includes data preprocessing, exploratory data analysis, feature engineering, machine learning model development, and deployment using Streamlit.

🎯 Problem Statement

YouTube creators and digital media companies depend heavily on advertising revenue. However, predicting how much revenue a video will generate can be challenging because it depends on multiple factors such as:

Video engagement

Watch time

Viewer location

Device usage

Audience interaction

The objective of this project is to build a predictive model that estimates YouTube ad revenue using video performance metrics.

📂 Dataset

Dataset Size: ~122,000 rows

Data Type: Synthetic YouTube performance data
Data Cleaning

Several preprocessing steps were performed to ensure data quality:

Handled missing values (~5%) using:

Median imputation for numerical features

Most frequent value for categorical features

Removed duplicate records (~2%)

Performed outlier detection and capping to reduce the impact of extreme values

📊 Exploratory Data Analysis (EDA)

Key insights discovered during analysis:

Watch Time has a strong correlation with ad revenue

Countries such as US and UK tend to generate higher revenue

TV and Desktop devices show longer watch times

Engagement metrics such as likes and comments influence revenue prediction

Visualization techniques used:

Correlation heatmaps

Distribution plots

Boxplots

Scatter plots

⚙️ Feature Engineering

To improve model performance, several new features were created:

Engagement Rate

(Likes + Comments) / Views

Retention Rate

Watch Time / (Views × Video Length)

Performance Score

Weighted combination of Views, Likes, and Comments

Total Attention

Views × Watch Time

These engineered features help capture user engagement and viewer behavior more effectively.

🤖 Machine Learning Models

Multiple machine learning models were trained and compared:

Linear Regression

Random Forest Regressor

XGBoost Regressor

AdaBoost Regressor

Histogram Gradient Boosting Regressor

Selected Model

Linear Regression

Although Random Forest slightly outperformed it, Linear Regression was selected because it provides better interpretability while maintaining high accuracy.

📈 Model Performance
Metric	Value
R² Score	0.949
MAE	$4.90
RMSE	$13.85

The model explains approximately 95% of the variance in YouTube ad revenue.

🖥 Streamlit Web Application

A Streamlit application was developed to make the model interactive.

Users can input video metrics such as:

Views

Likes

Comments

Watch Time

Country

Device

The app then processes the inputs using the preprocessor pipeline and generates real-time revenue predictions.

🛠 Tech Stack

Programming & Libraries

Python

Pandas

NumPy

Scikit-learn

Matplotlib

Seaborn

Deployment

Streamlit

Tools Used

VS Code

Jupyter Notebook

GitHub
