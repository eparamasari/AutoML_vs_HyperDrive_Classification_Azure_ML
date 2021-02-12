# Heart Failure Prediction: A Classification Model in Azure ML

This project is the Capstone Project for Udacity's Machine Learning Engineer for Microsoft Azure Nanodegree
In this project, a binary classification model was trained to predict the event of heart failure. Two methods of training were done, Azure Automated ML and Hyperdrive run.

## Project Set Up and Installation

This project uses:

- Jupyter Notebook 6
- Python 3.7
- Azure ML

## Dataset

### Overview

This is a binary classification task that will predict death by heart failure. The dataset was acquired from Kaggle at <https://www.kaggle.com/andrewmvd/heart-failure-clinical-data>. The dataset has thirteen columns and can be used to predict whether the event of death occur or not.

### Task

A binary classification task was performed using twelve features to predict the occurrence of death.

These are the thirteen columns in the dataset, with twelve independent features and the last column as label:

- age (int): self explanatory
- anaemia (bool): whether there has been a decrease of red blood cells or hemoglobin
- creatinine_phosphokinase (int): level of the CPK enzyme in the blood in mcg/L
- diabetes (bool): whether the patient has diabetes
- ejection_fraction (int): percentage of blood leaving the heart at each contraction
- high_blood_pressure (bool): whether the patient has hypertension
- platelets (int): platelets in the blood in kiloplatelets/mL
- serum_creatinine (float): level of serum creatinine in the blood in mg/dL
- serum_sodium (int): level of serum sodium in the blood in mEq/L
- sex (int): female or male (binary)
- DEATH_EVENT (bool): whether the patient passed away

### Access

The data was available publicly in a github repo and accessed at <https://raw.githubusercontent.com/eparamasari/ML_Engineer_ND_Capstone/main/data/heart_failure_clinical_records_dataset.csv> before being changed into a tabular dataset.

## Automated ML

*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### AutoML Results

*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

The best model was found to be ... with and accuracy of

For further improvement, one can try and change the hyperparameters

*TODO* Remember to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning

*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search

Logistic Regression was chosen in this run, since it is one of the best algorithm for a binary classification task.

### HyperDrive Run Results

*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

To improve the results, one can try to use other types of classification models, such as Decision Tree or Random Forest Classifier, in the HyperDrive Run, to see if it would be better than than the Automated ML

*TODO* Remember to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment

*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording

*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:

- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response
