# Stock Trend Prediction :chart:

## Table of Contents
1. [Project Description](#project-description)
2. [How to Install and Run the Project](#how-to-install-and-run-the-project)
3. [How to Use the Project](#how-to-use-the-project)
4. [Methodology](#methodology)
5. [Demo](#demo)
6. [Credits](#credits)

## Project Description
This project is a stock trend prediction tool implemented in Python using Long Short-Term Memory (LSTM) neural networks. The tool leverages historical stock price data to forecast future prices, aiding investors in making informed decisions. It gives users insights into stock trends, evaluation metrics, and visualizations to facilitate better understanding and analysis.

## How to Install and Run the Project
To install and run the project locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Ensure you have Python installed on your machine.
4. Run the application by executing `streamlit run app.py` in your terminal.

## How to Use the Project
1. Upon running the application, you will be prompted to enter a stock ticker.
2. Enter the desired stock ticker and click on the "Predict Stock Price" button.
3. The application will fetch historical data, perform predictions, and display visualizations along with evaluation metrics.
4. Analyze the provided data, visualizations, and metrics to gain insights into the predicted stock trends.

## Methodology
#### 1. Data Collection
- **Source**: The Yahoo Finance API (`yfinance`) collects historical stock price data for the specified stock ticker.
- **Time Period**: Data is collected from January 1, 2010, to January 1, 2024, to capture long-term trends and fluctuations in the stock market.
- **Data Attributes**: The collected data includes attributes such as Open, High, Low, Close, Volume, and Adjusted Close prices for each trading day.

#### 2. Data Preprocessing
- **Cleaning**: The collected data is checked for missing values, outliers, and inconsistencies. Any irregularities are handled appropriately to ensure data integrity.
- **Normalization**: Data normalization is performed using Min-Max scaling with a feature range between 0 and 1 to ensure uniformity and stabilize the training process.
- **Train-Test Split**: The data is split into training and testing sets, with 70% of the data used for training and the remaining 30% for testing.

#### 3. Model Architecture
- **Long Short-Term Memory (LSTM)**: The LSTM neural network architecture is chosen for its ability to capture long-term dependencies and patterns in sequential data. LSTMs are well-suited for time series forecasting tasks like stock price prediction.
- **Model Loading**: The pre-trained LSTM model is loaded using the `load_model` function from the Keras library.

#### 4. Model Training
- **Input Sequences**: The training data is organized into input sequences of 100 consecutive data points to capture temporal patterns. Each input sequence corresponds to a window of historical stock prices.
- **Batch Training**: The model is trained using mini-batch gradient descent with a specified batch size. Batch training enhances the efficiency of training and allows for parallel processing of multiple data samples.

#### 5. Model Evaluation
Several evaluation metrics are calculated to assess the performance of the LSTM model:
  - **Mean Squared Error (MSE)**: Measures the average squared difference between the predicted and actual stock prices. A lower MSE indicates better accuracy.
  - **Mean Absolute Error (MAE)**: Measures the average absolute difference between the predicted and actual stock prices. It provides a more interpretable measure of prediction error compared to MSE.
  - **Root Mean Squared Error (RMSE)**: Represents the square root of the MSE, providing a measure of the standard deviation of prediction errors. RMSE is sensitive to large errors and penalizes them more heavily.
  - **Mean Absolute Percentage Error (MAPE)**: Computes the mean percentage difference between the predicted and actual stock prices. MAPE is expressed as a percentage and provides a relative measure of accuracy.
  - **Coefficient of Determination (R-squared)**: Indicates the proportion of the variance in the dependent variable (stock prices) that is predictable from the independent variable (predicted prices). A higher R-squared value indicates a better model fit.
  - **Adjusted R-squared**: Adjusts the R-squared value to account for the number of predictors in the model. It penalizes excessive complexity and provides a more reliable measure of model fit for multiple predictors.
 
#### 6. Visualization
- **Visualization**: Visualizations are generated to compare the predicted stock prices with the actual prices using Plotly graph objects. Line charts are utilized to visualize the closing prices over time, as well as the predicted and actual prices.

#### 7. Interpretation and Analysis
- **Insights Generation**: The evaluation metrics and visualizations are analyzed to interpret the accuracy of the predictions and identify any trends or patterns in the data.
- **Decision Support**: The insights derived from the analysis can be used to support investment decision-making processes, providing investors with valuable information for portfolio management and risk assessment.

## Demo 
[Demo](https://github.com/a338wong/StockTrendPrediction/assets/153765340/a4a845fb-ae97-4cb8-8eaa-1f9a7adc85a3)

## Credits
- **[Alan Wong]** - [GitHub Profile](https://github.com/a338wong) - [LinkedIn Profile](www.linkedin.com/in/a338wong)
- **[GeeksforGeeks]** - [Youtube](https://www.youtube.com/watch?v=s3CnE2tqQdo&list=PLqM7alHXFySExPLJSzpKfKe6JO44Qm0qj&index=11)
  
--- 
