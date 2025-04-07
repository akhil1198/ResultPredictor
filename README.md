# Student Math Score Predictor

End-to-end ML pipeline that predicts students' math scores using demographic and performance data. Features data preprocessing, model comparison, Flask web interface, and AWS deployment with CI/CD integration.


## 📋 Overview

This project implements a complete machine-learning pipeline to predict a student's math scores. It considers various factors such as gender, race/ethnicity, parental education level, lunch type, test preparation, and reading/writing scores to generate predictions.

The system is deployed as a web application where users can input their information and receive a predicted math score.

## 🏗️ Project Structure

The project follows a modular architecture:

```
.
├── artifact/                      # Directory for model artifacts
├── logs/                          # Application logs
├── notebook/                      # Jupyter notebooks for EDA and experimentation
├── src/                           # Source code
│   ├── components/                # Core ML pipeline components
│   │   ├── data_ingestion.py      # Data loading and splitting
│   │   ├── data_transformation.py # Feature preprocessing
│   │   └── model_trainer.py       # Model training and evaluation
│   ├── pipeline/                  # Inference pipeline
│   │   └── predict_pipeline.py    # Prediction functionality
│   ├── exception.py               # Custom exception handling
│   ├── logger.py                  # Logging configuration
│   └── utils.py                   # Utility functions
├── templates/                     # Web interface templates
│   ├── home.html                  # Main prediction form
│   └── index.html                 # Landing page
├── application.py                 # Flask application
├── requirements.txt               # Project dependencies
└── setup.py                       # Package installation
```

## ✨ Features

- **Data Preprocessing**: Automatic handling of categorical and numerical features
- **Multiple ML Models**: Evaluation of several regression algorithms
- **Hyperparameter Tuning**: Grid search for optimal model parameters
- **Custom Exception Handling**: Robust error management
- **Logging**: Comprehensive logging for debugging and monitoring
- **Web Interface**: User-friendly input form
- **CI/CD Integration**: Automated deployment pipeline
- **AWS Deployment**: Hosted on AWS Elastic Beanstalk

## 🚀 Deployment

The application is deployed on AWS Elastic Beanstalk and can be accessed at:
http://resultgenerator-env.eba-hbg2tp66.us-east-2.elasticbeanstalk.com/predictdata

## 🛠️ Technology Stack

- **Python**: Core programming language
- **scikit-learn**: ML model training and evaluation
- **pandas/numpy**: Data processing
- **Flask**: Web framework
- **AWS Elastic Beanstalk**: Cloud deployment
- **AWS CodePipeline**: CI/CD

## 📊 ML Models Evaluated

- Random Forest Regressor
- Decision Tree Regressor
- Gradient Boosting Regressor
- Linear Regression
- K-Neighbors Regressor
- AdaBoost Regressor

## 🔄 Data Flow

1. **Data Ingestion**: Raw data is loaded and split into training and testing sets
2. **Data Transformation**: Features are preprocessed (scaling, encoding)
3. **Model Training**: Multiple models are evaluated and the best is selected
4. **Prediction**: The trained model is used to make predictions on new data
5. **Web Interface**: Users interact with the model through a Flask application

