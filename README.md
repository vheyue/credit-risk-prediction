# Credit Risk Prediction

## Project Overview

This project explores credit risk classification using machine learning. The goal is to identify customers with potentially higher credit risk and evaluate how classification thresholds affect model performance and hypothetical business costs.

## Dataset

- **Source:** UCI Machine Learning Repository — Statlog (German Credit Data)
- **Observations:** 1,000
- **Predictive features:** 20
- **Target:** Credit risk class (1 = good risk, 2 = bad risk)
- **Class distribution:** 70% good risk, 30% bad risk

## Technologies

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Google Colab

## Methodology

1. Data loading and exploratory data analysis.
2. Descriptive statistics and visualizations.
3. Stratified train/test split (80/20).
4. Categorical encoding andnumerical scaling using a preprocessing pipeline.
5. Logistic Regression classification.
6. Model evaluation using accuracy, precision, recall, F1-score, and a confusion matrix.
7. Exploratory comparison of classification thresholds and hypothetical misclassification costs.

## Results

| Metric | Threshold 0.50 | Threshold 0.30 |
|---|---:|---:|
| Accuracy | 78.00% | 75.50% |
| Precision (bad risk) | 66.67% | 56.32% |
| Recall (bad risk) | 53.33% | 81.67% |
| F1-score (bad risk) | 59.26% | 66.67% |
| Hypothetical misclassification cost | €148,000 | €74,000 |

Reducing the classfication threshold from 0.50 to 0.30 increased the recall for bad-risk customers, although it also increased false positives.

Under the illustrative cost assumptions, the estimated misclassification cost decreased by 50%.

**Important:** The threshold comparison was performed on the test set as an educational experiment. A production-ready workflow would select the threshold using validation data and evaluate the final approach on an untouched test set.

## Key Learnings

- Classification accuracy alone may not reflect business objectives.
- Recall is particularly relevant when missing high-risk customers is costly.
- Classification thresholds influence the balance between false positives and false negatives.
- Preprocessing pipelines help prevent data leakage.

## Next Steps

- Implement cross-validation.
- Select classification thresholds using validation data.
- Compare Logistic Regression with additional classification algorithms.
- Explore feature importance and mdel interpretability.

## Project Status

Work in progress — initial exploratory analysis and Logistic Regression baseline completed.
