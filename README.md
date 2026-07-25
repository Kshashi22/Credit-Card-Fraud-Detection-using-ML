# Credit Card Fraud Detection using Machine Learning

## Table of Contents

1. Project Overview
2. Problem Statement
3. Objectives
4. Dataset Information
5. Project Workflow
6. Data Preprocessing
7. Exploratory Data Analysis (EDA)
8. Feature Engineering
9. Model Development
10. Model Evaluation
11. Deployment
12. Project Structure
13. Results
14. Future Improvements
15. Conclusion

---

#  Project Overview

Credit card fraud has become one of the biggest challenges faced by financial institutions. Detecting fraudulent transactions accurately while minimizing false alarms is essential to reduce financial losses and maintain customer trust.

This project develops a machine learning-based fraud detection system that classifies transactions as **Fraudulent** or **Legitimate** using transaction behavior and customer activity patterns.

---

#  Problem Statement

Fraudulent transactions represent only a small percentage of all transactions, making the dataset highly imbalanced. Traditional rule-based systems often fail to detect evolving fraud patterns or generate excessive false positives.

The objective is to build an intelligent classification model capable of identifying fraudulent transactions with high recall while maintaining good precision.

---

#  Objectives

- Analyze transaction data to identify fraud patterns.
- Perform data cleaning and preprocessing.
- Engineer meaningful features to improve prediction.
- Train and compare multiple machine learning models.
- Evaluate models using fraud-specific metrics.
- Deploy the best-performing model for real-time predictions.

---

#  Dataset Information

The dataset contains anonymized credit card transaction records with various behavioral features.

### Features

| Column | Description |
|---------|-------------|
| distance_from_home | Distance between customer's home and transaction location |
| distance_from_last_transaction | Distance from previous transaction |
| ratio_to_median_purchase_price | Purchase amount compared to customer's median purchase |
| repeat_retailer | Transaction made at a previously visited retailer |
| used_chip | Whether EMV chip was used |
| used_pin_number | Whether PIN authentication was used |
| online_order | Whether transaction was online |
| fraud | Target variable (1 = Fraud, 0 = Legitimate) |

---

#  Project Workflow

```
Data Collection
        │
        ▼
Data Cleaning
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Feature Engineering
        │
        ▼
Data Scaling
        │
        ▼
Train-Test Split
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Model Deployment
```

---

#  Data Preprocessing

The preprocessing stage involved preparing the dataset for machine learning.

###  Missing Values

- Checked for missing values
- Verified data integrity before training

###  Duplicate Records

- Removed duplicate observations (if present)

###  Outlier Handling

Outliers were detected using box plots for:

- Distance from Home
- Distance from Last Transaction
- Purchase Price Ratio

Extreme values were capped using the **Interquartile Range (IQR)** technique to reduce their influence on the models.

---

#  Exploratory Data Analysis (EDA)

EDA was performed to understand transaction behavior and fraud patterns.

### Analysis Included

- Fraud vs Legitimate transaction distribution
- Correlation heatmap
- Feature distributions
- Box plots
- Purchase ratio analysis
- Distance analysis

### Key Insights

- Fraudulent transactions occur much less frequently than legitimate ones.
- Online transactions showed a higher probability of fraud.
- Large transaction distances were associated with suspicious activities.

---

# Feature Engineering

To improve predictive performance, additional features were created.

### Engineered Features

- Distance Ratio
- Transaction Risk Score
- Purchase Category
- Encoded Purchase Category

These engineered features captured customer purchasing behavior more effectively than raw features alone.

---

#  Model Development

The dataset was split into:

- **Training:** 80%
- **Testing:** 20%

Feature scaling was performed using **StandardScaler**.

### Models Implemented

- Logistic Regression
- Random Forest Classifier

---

#  Model Evaluation

Since fraud detection is an imbalanced classification problem, multiple evaluation metrics were considered.

### Metrics Used

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## Logistic Regression

### Performance

- Accuracy: **91.65%**

Confusion Matrix

```
[[166976 15581]
 [1124 16319]]
```

| Metric | Score |
|---------|------:|
| Precision | 0.51 |
| Recall | 0.94 |
| F1 Score | 0.66 |

---

## Random Forest

### Performance

- Accuracy: **94.27%**

Confusion Matrix

```
[[171253 11304]
 [153 17290]]
```

| Metric | Score |
|---------|------:|
| Precision | 0.60 |
| Recall | 0.99 |
| F1 Score | 0.75 |

---

#  Model Comparison

| Model | Accuracy | Precision | Recall | F1 Score |
|--------|----------|-----------|---------|----------|
| Logistic Regression | 91.65% | 0.51 | 0.94 | 0.66 |
| Random Forest | **94.27%** | **0.60** | **0.99** | **0.75** |

### Best Model

 **Random Forest** achieved the highest overall performance and was selected for deployment.

---

#  Deployment

The trained model was exported using **Joblib** and deployed as an interactive web application using **Streamlit**.

### Deployment Features

- Upload transaction details
- Predict Fraud / Legitimate
- Fast real-time inference
- User-friendly interface

---

#  Project Structure

```
Credit-Card-Fraud-Detection/

│── data/
│── notebooks/
│── models/
│── app/
│── src/
│── images/
│── requirements.txt
│── LICENSE
│── README.md
```

---

#  Results

- Achieved **94.27%** prediction accuracy using Random Forest.
- Successfully identified fraudulent transactions with **99% recall**.
- Reduced false negatives while maintaining strong classification performance.
- Built an end-to-end machine learning pipeline ready for deployment.

---

#  Future Improvements

- Implement XGBoost and LightGBM.
- Handle class imbalance using SMOTE.
- Integrate SHAP for Explainable AI.
- Deploy REST API using FastAPI.
- Containerize the application with Docker.
- Enable cloud deployment using AWS or Azure.
- Add real-time fraud monitoring dashboard.

---

#  Conclusion

This project demonstrates a complete machine learning workflow for credit card fraud detection—from data preprocessing and feature engineering to model training, evaluation, and deployment.

Among the evaluated models, **Random Forest** delivered the best performance, making it well-suited for detecting fraudulent transactions while minimizing false alarms.

Although this project is intended for educational and portfolio purposes, it showcases practical techniques commonly used in real-world fraud detection systems and provides a strong foundation for further enhancements such as explainable AI, ensemble learning, and real-time deployment.