# AD-Tech Revenue Prediction

## Project Overview
This project focuses on analyzing the AD-Tech dataset derived from an advertising platform. The goal is to develop a predictive model that can predict total revenue from advertisements using both traditional Machine Learning (ML) techniques and Artificial Neural Network (ANN) models.

## Table of Contents
- [AD-Tech Revenue Prediction](#ad-tech-revenue-prediction)
  - [Project Overview](#project-overview)
  - [Table of Contents](#table-of-contents)
  - [Dataset](#dataset)
  - [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
  - [Model Development](#model-development)
    - [Feature Engineering and Encoders](#feature-engineering-and-encoders)
  - [API Implementation](#api-implementation)
    - [app.py](#apppy)
  - [Usage](#usage)
  - [Results](#results)
  - [Contributing](#contributing)
  - [License](#license)


## Dataset
The dataset, `AD-Tech.csv`, encapsulates daily metrics related to advertisements served across various websites, advertisers, and geographic locations, capturing details like impressions, viewability, and revenue generated.

## Exploratory Data Analysis (EDA)
The EDA includes examining distributions of key metrics, identifying patterns, and understanding the relationships between features. Feature Engineering is applied to enhance the model's performance.

## Model Development
Two models are developed in this project:

1. **Machine Learning Model**:
    - Linear Regression
    - Data preprocessing, model training, and evaluation are done using traditional ML techniques.

2. **Artificial Neural Network Model**:
    - A Sequential model with Dense layers.
    - Data normalization and model training using Keras and TensorFlow.

### Feature Engineering and Encoders
Feature engineering is a crucial step to improve the model's performance. The `model.py` file is created to handle all feature engineering tasks, including:
- Encoding categorical variables using label encoding and targed encoding.
- Drop useless columns.

The `model_encoders` directory contains specific scripts for label encoding and target encoding for each encoded column. These scripts are used within `model.py` to preprocess the data before feeding it into the models.

## API Implementation
An API is implemented using FastAPI to run the model and make predictions.

### app.py
The `app.py` file contains the FastAPI application with endpoints to interact with the model. It allows users to submit data and receive revenue predictions.

## Usage
To use the project:

1. Clone the repository.
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the FastAPI application:
    ```bash
    uvicorn app:app --reload
    ```
4. A model input is provided in the `input` directory

## Results
The performance of the models is evaluated using Mean Squared Error (MSE), Mean Absolute Error (MAE), and R-squared (R2) metrics.

## Contributing
Contributions are welcome. Please submit a pull request or open an issue for any changes or suggestions.

## License
This project is licensed under the MIT License.
