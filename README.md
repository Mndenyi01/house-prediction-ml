A basic skill representation.

Project Architecture and structure initialisation.

🏠 House Price Prediction – Project
--------------------------------------------------
1. 📌 Project Overview

This project is an end-to-end machine learning regression pipeline designed to predict house prices using structured housing data. It covers the full ML lifecycle — from data cleaning and exploratory analysis to model training, evaluation, regularization, and deployment through an interactive Streamlit dashboard.<br>
The Dataset was downloaded from Kaggle, link below:-

https://www.kaggle.com/datasets/rishitaverma02/house-prices-advanced-regression-techniques
<br> - Rishita Verma <br>(I hope it's correct)

The goal of the project is not only predictive performance, but also interpretability, stability, and real-world usability.

2. 🎯 Objectives:-

- Clean and preprocess raw housing data
- Perform exploratory data analysis (EDA) to uncover key price drivers
- Build and compare regression models
- Handle multicollinearity using regularization
- Deploy a trained model using Streamlit
- Communicate insights clearly for non-technical stakeholders

3. 📊 Data Processing & EDA

- Dropped features with excessive missing values
- Imputed remaining missing data appropriately
- Performed univariate and multivariate analysis
- Identified strong predictors such as:
    - Overall quality
    - Living area
    - Garage capacity
    -Basement size
- Applied log transformation to the target variable (SalePrice) to reduce skewness

4. 🤖 Modeling Approach

Three regression models were trained and evaluated:

|Model	            |R²     |RMSE   |
|:------------------|:-----:|------:|
|Linear Regression	|~0.77	|~0.21  |
|Ridge Regression	|~0.79	|~0.20  |
|Lasso Regression	|~0.84	|~0.17  |

Model Selection

- Ridge Regression was selected for deployment due to:
    - Better handling of multicollinearity
    - Improved stability over standard linear regression
    - Retention of all features for safer real-world use

- Lasso Regression was used for feature selection and interpretability analysis

5. 📈 Evaluation & Insights
- Ridge regression showed improved generalization over baseline linear regression
- Lasso reduced feature count significantly, indicating feature redundancy
- Residual analysis showed reasonable error distribution with higher uncertainty at extreme prices
- Roof material, overall quality, and living area were among the strongest price drivers

6. 🚀 Deployment (Streamlit App)

An interactive Streamlit dashboard was built to:

- Accept key house features as user input
- Apply preprocessing and scaling
- Predict house prices using the trained Ridge model
- Display predictions in real price units (inverse log transformation applied)

To run the app locally(in the root folder):

> streamlit run dashboard/app.py

7. ⚠️ Limitations & Future Improvements
- Linear models cannot fully capture non-linear relationships
- No cross-validation or hyperparameter tuning yet
- Limited user inputs for simplicity
- Future improvements could include:
    -Tree-based models (Random Forest, XGBoost)
    -Cross-validated regularization
    -Richer dashboard visualizations

8. 🧠 Key Skills Demonstrated

- Data cleaning & preprocessing
- Exploratory data analysis (EDA)
- Feature engineering & encoding
- Regression modeling & regularization
- Model evaluation & diagnostics
- Feature importance interpretation
- Model deployment with Streamlit
- Debugging and production awareness
- Technical communication & storytelling

9. 📌 Conclusion

This project demonstrates a practical, end-to-end machine learning workflow with an emphasis on clarity, correctness, and deployment readiness. It reflects how real-world ML systems are built, evaluated, and communicated.

👤 Author
----------

Anthony Mndenyi<br>
- Second Year Student | Multimedia University Of Kenya
- Aspiring Data Scientist / Machine Learning Engineer
