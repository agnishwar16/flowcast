<div align="center">

# 🚖 FlowCast
### AI-Powered NYC Taxi Demand Prediction

An end-to-end Machine Learning project that predicts hourly taxi demand using historical NYC Yellow Taxi data through advanced feature engineering and regression models.

---

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![XGBoost](https://img.shields.io/badge/XGBoost-Regressor-green?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple?style=for-the-badge&logo=pandas)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

</div>

---

# 📖 Overview

FlowCast is an end-to-end Machine Learning project that predicts hourly taxi demand across New York City using historical Yellow Taxi trip records.

The project demonstrates the complete Machine Learning lifecycle—from raw data preprocessing and exploratory analysis to feature engineering, model training, evaluation, and deployment.

The final model enables demand prediction for any pickup location and time based on historical demand patterns.

---

# ✨ Features

- 📂 Data Cleaning & Preprocessing
- 📊 Exploratory Data Analysis (EDA)
- ⏰ Hourly Demand Aggregation
- 🧠 Time-Series Feature Engineering
- 🤖 Multiple Regression Models
- 📈 Model Performance Comparison
- ⭐ Feature Importance Analysis
- 💾 Model Serialization using Joblib
- 🔮 Demand Prediction
- 🚀 Ready for Streamlit Deployment

---

# 🛠 Tech Stack

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- XGBoost

### Data Analysis

- Pandas
- NumPy

### Visualization

- Matplotlib

### Model Persistence

- Joblib

### Development Environment

- Jupyter Notebook
- Git
- GitHub

---

# 📂 Project Structure

```text
FLOWCAST/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── images/
│
├── models/
│   └── best_model.pkl
│
├── notebooks/
│   ├── 01_data_loading.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_demand_aggregation.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_model_training.ipynb
│   └── 06_model_deployment.ipynb
│
├── reports/
│   ├── feature_importance.csv
│   ├── model_results.csv
│   └── sample_prediction.csv
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🔄 Machine Learning Pipeline

```text
               Raw Taxi Trip Data
                      │
                      ▼
          Data Cleaning & Preprocessing
                      │
                      ▼
      Exploratory Data Analysis (EDA)
                      │
                      ▼
       Hourly Demand Aggregation
                      │
                      ▼
         Feature Engineering
                      │
                      ▼
        Model Training & Evaluation
                      │
                      ▼
       Best Model Selection
                      │
                      ▼
      Machine Learning Deployment
                      │
                      ▼
          Taxi Demand Prediction
```

---

# 🧠 Feature Engineering

## Time Features

- Hour
- Day of Week
- Month
- Weekend Indicator
- Peak Hour Indicator

## Historical Demand Features

- Lag 1
- Lag 24
- Rolling Mean (3)
- Rolling Mean (24)
- Rolling Standard Deviation (24)

These features enable the model to learn temporal demand trends and improve prediction accuracy.

---

# 🤖 Models Evaluated

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

---

# 📊 Model Performance

| Model | R² Score | MAE | RMSE |
|-------|---------:|----:|------:|
| Linear Regression | 0.9516 | 9.13 | 17.95 |
| **Random Forest** ⭐ | **0.9730** | **6.03** | **13.40** |
| XGBoost | 0.9632 | 6.61 | 15.65 |

The **Random Forest Regressor** achieved the highest predictive performance and was selected as the final production model.

---

# 📈 Feature Importance

The trained Random Forest model identifies which engineered features contribute most to prediction accuracy.

The most influential features include:

- Rolling Mean (3)
- Lag 1
- Lag 24
- Rolling Mean (24)

A complete feature importance report is available inside the **reports/** directory.

---

# 🔮 Sample Prediction

### Input

| Feature | Value |
|----------|------:|
| Pickup Location | 161 |
| Hour | 10 |
| Day of Week | 2 |
| Month | 3 |
| Weekend | 0 |
| Peak Hour | 1 |
| Lag 1 | 42 |
| Lag 24 | 36 |

### Output

```text
Predicted Taxi Demand

39.40
```

---

# 📦 Project Outputs

The project generates:

- ✅ Cleaned Dataset
- ✅ Hourly Demand Dataset
- ✅ Feature Engineered Dataset
- ✅ Trained Random Forest Model
- ✅ Model Evaluation Report
- ✅ Feature Importance Report
- ✅ Sample Prediction Report

---

# 🚀 Future Roadmap

- [x] Data Cleaning
- [x] Exploratory Data Analysis
- [x] Feature Engineering
- [x] Model Training
- [x] Model Evaluation
- [x] Model Deployment
- [ ] Interactive Streamlit Dashboard
- [ ] Cloud Deployment
- [ ] FastAPI Backend
- [ ] Real-Time Predictions

---

# 📚 Learning Outcomes

This project demonstrates practical experience with:

- End-to-End Machine Learning
- Data Preprocessing
- Exploratory Data Analysis
- Time-Series Feature Engineering
- Regression Algorithms
- Feature Importance Analysis
- Model Evaluation
- Model Serialization
- Machine Learning Deployment
- Version Control using Git & GitHub

---

# 👨‍💻 Author

**Your Name**

B.Tech Computer Science Engineering (Artificial Intelligence)

Machine Learning • Artificial Intelligence • Data Science

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

</div>