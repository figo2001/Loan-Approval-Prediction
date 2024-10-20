# Loan Approval Prediction

This project predicts the approval of loans based on a dataset of historical loan data. The goal is to automate the loan application review process by using machine learning to classify whether an applicant's loan will be approved or rejected.

## Overview

Loan approval prediction is a classification problem where we aim to predict whether a loan application will be approved based on features such as applicant income, loan amount, credit history, etc.

This project includes:
- Data preprocessing
- Model training and evaluation
- Web-based prediction system (frontend + backend)

## Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: Python (Flask)
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn

## Project Structure

```bash
Loan-Approval-Prediction/
│
├── app.py                    # Backend Python script (Flask)
├── static/                   # Static files (CSS, images, etc.)
│   └── style.css             # Styling for the web app
├── templates/                # HTML templates
│   └── index.html            # Main web page
├── models/                   # Saved machine learning models
│   └── loan_model.pkl        # Pre-trained model for loan prediction
├── dataset/                  # Dataset used for training and testing
│   └── loan_data.csv         # Historical loan data
├── README.md                 # Project documentation
└── requirements.txt          # Dependencies
```

## Features

- **Loan Approval Prediction**: Classify whether a loan will be approved or not based on input features.
- **Web Interface**: Simple web form for users to input data and get loan approval results.
- **Model Training**: Code for training, evaluating, and saving machine learning models.
- **Data Visualization**: Visual insights into dataset features.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/Loan-Approval-Prediction.git
    cd Loan-Approval-Prediction
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate    # On Linux/Mac
    venv\Scripts\activate       # On Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the web application:
    ```bash
    python app.py
    ```
    
## Usage

1. Open the web application in your browser.
2. Fill in the loan applicant details in the form.
3. Click the "Predict" button to get the loan approval status.

## Model Training

To train the loan approval model, follow these steps:

1. Load and preprocess the dataset using the provided Jupyter notebooks or scripts.
2. Train a classification model using algorithms like Logistic Regression, Random Forest,Catboost etc.
3. Evaluate the model on test data.
4. Save the trained model in the `models/` directory for later use.

## Screenshots
![Screenshot 2024-10-21 at 03-12-55 Document](https://github.com/user-attachments/assets/ca7241e3-251b-44fc-b5e6-13dba5a82948)

