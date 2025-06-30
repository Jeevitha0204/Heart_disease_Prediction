# Heart_disease_Prediction
ML app to predict heart disease 
# Heart Disease Prediction Web App

This project is a machine learning-based web application that predicts the likelihood of heart disease in patients based on clinical parameters. The model was trained using a public dataset and deployed using **Streamlit**, allowing real-time predictions directly from a user-friendly interface.

# Project Highlights

-  Machine learning model trained on cardiovascular health data
-  Performed Exploratory Data Analysis (EDA) and data preprocessing
-  Compared multiple classification models using Scikit-learn
-  Selected the best-performing model for deployment
-  Developed an interactive web app using **Streamlit**


# Features

- Upload or manually input patient data (e.g., age, cholesterol, blood pressure, etc.)
- View real-time heart disease risk prediction (Yes/No)
- Backend powered by trained ML model
- Simple and intuitive interface for non-technical users


# Tools and Technologies

- **Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn  
- **Model:** Logistic Regression (or Random Forest, Decision Tree — depending on your final model)  
- **Frontend:** Streamlit  
- **Deployment:** Streamlit Sharing (or Hugging Face Spaces)


# Installation & Setup

```bash
# Clone the repository
git clone https://github.com/Jeevitha0204/Heart_disease_Prediction.git
cd Heart_disease_Prediction

# Install required packages
pip install -r requirements.txt

# Run the app locally
streamlit run app.py

# Dataset Used
Source: UCI Heart Disease Dataset
Features: Age, Sex, Chest Pain Type, Cholesterol, Blood Pressure, etc.
Target: Presence of heart disease (0 = No, 1 = Yes)

# Machine Learning Workflow
Data Cleaning & Preprocessing

Handled missing values, categorical encoding, and scaling
EDA
Correlation matrix, distribution plots, outlier detection

Model Building
Compared Logistic Regression, Random Forest, SVM
Evaluated with Accuracy, Precision, Recall, F1-Score

Deployment
Final model saved as heart_model.pkl
Integrated with Streamlit for web deployment









