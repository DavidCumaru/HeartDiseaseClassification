# Heart Disease

![Descrição da imagem](img/Heart_Disease.jpg)

## Context

Cardiovascular diseases (CVDs) are the leading cause of death worldwide, claiming approximately 17.9 million lives annually and accounting for 31% of all global deaths. Four out of five CVD-related deaths result from heart attacks and strokes, with one-third of these deaths occurring prematurely in individuals under 70 years of age. Heart failure, a common outcome of CVDs, underscores the critical need for early detection and treatment. This dataset comprises 11 key features that can be utilized to predict the likelihood of heart disease.

Individuals with cardiovascular diseases or those at high cardiovascular risk—due to factors such as hypertension, diabetes, hyperlipidemia, or pre-existing conditions—require early intervention. Machine learning models can play a crucial role in identifying at-risk individuals and supporting preventive healthcare strategies.

## About the Project

### Objective

This project aims to develop a predictive system for cardiovascular diseases using a dataset of patient attributes. By analyzing these attributes, the model can assess a patient's risk of heart-related issues, aiding in early intervention and targeted care.

### Dataset Features

- Age: Age of the patient (years).

- Sex: Sex of the patient (M: Male, F: Female).

- ChestPainType: Type of chest pain:

  - TA: Typical Angina

  - ATA: Atypical Angina

  - NAP: Non-Anginal Pain

- ASY: Asymptomatic

- RestingBP: Resting blood pressure (mm Hg).

- Cholesterol: Serum cholesterol level (mg/dl).

- FastingBS: Fasting blood sugar (1 if > 120 mg/dl, 0 otherwise).

- RestingECG: Resting electrocardiogram results:

  - Normal: Normal

  - ST: ST-T wave abnormality (e.g., T wave inversions, ST elevation or depression > 0.05 mV)

  - LVH: Probable/definite left ventricular hypertrophy by Estes' criteria

- MaxHR: Maximum heart rate achieved (numeric value between 60 and 202).

- ExerciseAngina: Exercise-induced angina (Y: Yes, N: No).

- Oldpeak: Depression in ST segment induced by exercise relative to rest (numeric value).

- ST_Slope: Slope of the peak exercise ST segment:

  - Up: Upsloping

  - Flat: Flat

  - Down: Downsloping

- HeartDisease: Output class:

  - 1: Presence of heart disease

  - 0: Normal

## Approach

### 1. Exploratory Data Analysis (EDA)

<b>Objective:</b> Understand the data distribution, identify patterns and trends, and detect anomalies or missing values.

<b>Key Insights:</b> Using statistical summaries and visualizations, we examined the relationship between various features and the likelihood of heart disease.

### 2. Data Preprocessing

- <b>Cleaning:</b> Addressed missing or inconsistent values (e.g., replaced zeros in resting blood pressure and cholesterol with median values).

- <b>Encoding:</b> Transformed categorical variables into numerical formats for compatibility with machine learning models.

- <b>Scaling:</b> Normalized numerical features to ensure consistent input ranges for machine learning algorithms.

### 3. Machine Learning

- <b>Model Selection:</b> Experimented with various machine learning algorithms, including logistic regression, support vector machines (SVM), and random forests.

- <b>Hyperparameter Tuning:</b> Used GridSearchCV to optimize model performance.

- <b>Evaluation:</b> Assessed models using metrics such as accuracy, precision, recall, F1-score, ROC-AUC, and confusion matrices.

## Results and Implications

- <b>Model Performance:</b> The best-performing model achieved high predictive accuracy, demonstrating its reliability in identifying at-risk patients.

- <b>Key Predictors:</b> Variables such as Age, ChestPainType, MaxHR, and Cholesterol were strongly correlated with heart disease risk.

- <b>Healthcare Impact:</b> Early detection of heart disease risk can lead to timely intervention, potentially reducing morbidity and mortality rates. The model provides a scalable solution for healthcare providers to assess risk factors efficiently.
