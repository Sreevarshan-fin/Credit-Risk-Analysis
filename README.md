# Credit Risk Analysis Project

## Objective
Develop an accurate, scalable, and interpretable machine learning model to predict customer loan defaults. The model aims to support financial institutions' decision-making by proactively identifying high-risk customers, thereby reducing Non-Performing Assets (NPA) and improving portfolio health.

## Score Range & Rating System
To evaluate customer credit risk, the model generates scores based on several features (e.g., loan-to-income ratio, delinquency ratio). Below is the rating system for these scores:

| **Score Range** | **Rating** |
|-----------------|------------|
| 300–500         | Poor       |
| 500–650         | Average    |
| 650–750         | Good       |
| 750–900         | Excellent  |

This rating system helps financial institutions categorize customers into different risk buckets and take appropriate action based on their creditworthiness.

## Situation
Financial institutions often face challenges in managing credit risk effectively. Traditional methods lacked sophistication in leveraging historical customer behavior, resulting in suboptimal loan disbursement decisions. To address this, datasets containing customer demographics, loan information, and bureau data were utilized to develop a comprehensive credit risk model with business-friendly interpretability.

## Task
- Consolidate and prepare disparate datasets (customers, loans, bureau) for machine learning.
- Engineer impactful features that capture customer financial behavior.
- Build, validate, and deploy predictive models capable of distinguishing between defaulters and non-defaulters.
- Address class imbalance without losing model generalization.
- Ensure the final solution provides explainable insights to non-technical stakeholders.

## Action

### Data Preprocessing
- Merged customer, loan, and bureau datasets using `cust_id`.
- Addressed missing values and outliers.
- Ensured consistency and validity through business rule validation.

### Exploratory Data Analysis (EDA)
- Visualized distributions and compared defaulters vs non-defaulters using KDE plots.
- Key findings:
  - Higher `loan_to_income` and `delinquency_ratio` strongly correlate with defaults.
  - Younger customers (18-35 years) had a higher probability of default.
  - Credit Utilization Ratio and Average DPD per Delinquency were significant risk indicators.

### Feature Engineering
- Created meaningful ratios like **Loan to Income (LTI) Ratio**, **Delinquency Ratio**, and **Average Days Past Due (DPD) per Delinquency**.
- Removed non-informative features and performed feature selection using **VIF** and **Information Value (IV)** analysis.

### Model Development
- **Baseline Models**: Logistic Regression, Random Forest, XGBoost Classifier.
- **Class Imbalance Handling**: SMOTE Tomek Links for synthetic balancing and noise reduction.
- **Hyperparameter Tuning**: RandomizedSearchCV and Optuna optimization for fine-tuning.

### Evaluation Metrics
- **Accuracy**
- **Precision, Recall, F1-Score** for both classes.
- **ROC AUC Score**
- **Confusion Matrix Analysis**

### Deployment Readiness
The final models were integrated with **Streamlit** for real-time predictions, with explainability visualizations to aid in decision-making.

## Key Insights
- Customers with **high loan_to_income ratios** are significantly riskier.
- **Younger customers (< 35 years)** showed a marginally higher default risk.
- **Credit utilization ratio** and **delinquency ratio** emerged as top predictors.
- Loan purposes such as **"Personal"** and **"Auto"** had higher default tendencies compared to **"Home"** loans.

## Conclusion
The **Credit Risk Analysis** project successfully developed a predictive system that can identify high-risk borrowers with significant accuracy, offering a business-friendly solution to improve risk management practices. The model has shown promising results and can be enhanced with continuous retraining and adaptation to new data.

---

## Repository Structure
```plaintext
Credit-Risk-Analysis/
│
├── data/                    # Raw and processed data files
│   ├── raw_data.csv
│   └── cleaned_data.csv
│
├── notebooks/                # Jupyter notebooks for exploration and model building
│   ├── 01_data_exploration.ipynb
│   └── 02_model_building.ipynb
│
├── src/                     # Python scripts for preprocessing, modeling, and deployment
│   ├── preprocessing.py
│   ├── model.py
│   └── app.py                # Streamlit app for deployment
│
├── requirements.txt         # List of dependencies
└── README.md                # This file
