# Diabetes Prediction System

This project is a Diabetes Prediction System that uses a Support Vector Machine (SVM) classifier to predict whether a person has diabetes based on certain medical input features. The model was trained using the Pima Indians Diabetes Database, which is a popular dataset for binary classification tasks. The system includes a graphical user interface (GUI) built using Tkinter, allowing users to input medical data and get real-time predictions.

## Table of Contents

- [Dataset](#dataset)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Model and Training](#model-and-training)
- [GUI](#gui)
- [License](#license)

## Dataset

The dataset used is the **Pima Indians Diabetes Database**, available on Kaggle. The dataset consists of 768 rows and 9 columns (8 features and 1 outcome).

- [Pima Indians Diabetes Dataset on Kaggle](https://www.kaggle.com/uciml/pima-indians-diabetes-database)

## Features

The system takes the following input features to predict the outcome:

1. **Pregnancies** - Number of times pregnant
2. **Glucose** - Plasma glucose concentration
3. **Blood Pressure** - Diastolic blood pressure (mm Hg)
4. **Skin Thickness** - Triceps skinfold thickness (mm)
5. **Insulin** - 2-Hour serum insulin (mu U/ml)
6. **BMI** - Body mass index (weight in kg/(height in m)^2)
7. **Diabetes Pedigree Function** - A function which scores likelihood of diabetes based on family history
8. **Age** - Age in years

The target variable is:

- **Outcome**: 0 (Not diabetic), 1 (Diabetic)

## Prerequisites

Make sure you have the following dependencies installed:

- Python 3.x
- NumPy
- Pandas
- scikit-learn
- Tkinter (comes with standard Python distribution)

You can install the required packages using:

```bash
pip install numpy pandas scikit-learn
