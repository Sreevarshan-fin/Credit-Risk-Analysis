
# Credit Risk Modelling – Lauki Finance 

This project builds an interpretable credit risk model for an NBFC using historical loan data to estimate probability of default and support scalable, data-driven credit decisions.

**[![Open in Streamlit](https://img.shields.io/badge/Launch%20App-Streamlit-%23FF4B4B?logo=streamlit&logoColor=white&style=for-the-badge&labelColor=FF4B4B)](https://credit-risk-analysis-jj3vtj43niyqoxbokhujxx.streamlit.app/)**  

## The Story Behind the Project

Lauki Finance is an NBFC that focuses on lending to customers who are often excluded by traditional banks. While this helps expand financial access, it also exposes the business to higher credit risk. At the time of this project, credit evaluation at Lauki Finance relied heavily on manual judgment. As loan applications increased, this approach became slow, inconsistent, and difficult to scale, leading to delays in decisions and increased exposure to defaults.

The goal of this project was to address this challenge by building a **data-driven, interpretable credit risk model** that could help the Risk Unit consistently measure borrower risk and support better credit decisions.

---

## What the Project Aimed to Solve

The core problem was not just predicting defaults, but **measuring risk in a way that the business could trust and use**. The risk team needed a model that could:

* Rank customers by default risk
* Work reliably on future data
* Be explainable enough for audits and business discussions
* Support decision-making without fully automating approvals

This project focuses on **credit risk measurement**, not black-box automation.

---

## How the Problem Was Approached

To solve this, historical loan data from Lauki Finance was used, covering customer details, loan characteristics, and credit bureau information. The project followed a structured, industry-aligned credit risk modeling workflow, starting from data preparation and ending with time-based validation.

Rather than relying on a single algorithm, multiple models were explored to compare performance and stability. The emphasis throughout was on **risk ranking quality**, not just prediction accuracy.

---

## Data and Validation Strategy

The dataset included two years of historical loan data:

* February 2022 to February 2024 for training and validation
* March 2024 to May 2024 as an out-of-time test set

Using an out-of-time dataset ensured the model was evaluated on future, unseen data, which is critical in real-world credit risk modeling. This helped confirm that the model could generalize beyond the period it was trained on.

---

## Features Used in the Model

The data was grouped into three major feature categories:

* Customer features capturing borrower profile attributes
* Loan features describing loan structure and purpose
* Bureau features reflecting historical credit behavior and repayment patterns

Together, these features allowed the model to capture both **who the borrower is** and **how they have behaved financially in the past**.

---

## Target Definition

The modeling task was framed as a binary classification problem, where the target variable represented whether a borrower defaulted or not. This aligns with standard probability-of-default modeling used across banks and NBFCs.

---

## Preparing the Data for Modeling

Before training the models, several preprocessing steps were applied to ensure data quality and stability. Invalid values in loan purpose were handled, predictive features were selected using Information Value and domain knowledge, multicollinearity was checked using VIF, and numeric variables were scaled using Min–Max scaling. These steps ensured that the model inputs were both statistically sound and business-relevant.

---

## Model Development and Tuning

Multiple algorithms were trained and compared, including Logistic Regression, Random Forest, and XGBoost. This allowed a balance between interpretability and predictive power. To improve performance and avoid overfitting, hyperparameter tuning was carried out using RandomizedSearchCV and Optuna.

---

## How Model Performance Was Evaluated

Model evaluation focused on metrics that matter in credit risk:

* AUC and Gini to measure ranking power
* KS statistic to assess separation between defaulters and non-defaulters
* Classification reports to understand prediction behavior

Special attention was given to performance consistency across training, test, and out-of-time datasets.

---

## Business Perspective on the Model Output

Instead of directly approving or rejecting loans, the final model produces **interpretable risk scores**. These scores can be translated into business rules and integrated with a Business Rule Engine. This allows Lauki Finance to automate parts of the decision process while still retaining analyst oversight and regulatory transparency.

---

## Final Outcome 
The result of Phase 1 is a validated, industry-aligned credit risk model that:

* Accurately ranks customers by default risk
* Meets defined performance benchmarks
* Performs consistently on future data
* Produces explainable outputs suitable for risk teams
* Can be extended into downstream decision or rule-based systems

---

## Overall Goal

The broader goal of this project is to provide Lauki Finance with a **practical and scalable credit risk modeling foundation**. By combining strong statistical performance with interpretability, the model helps reduce bad loans, improve decision turnaround time, and support data-driven lending operations as the business grows.

---





