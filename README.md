# Stock Trend Prediction :chart:

## Table of Contents :bookmark_tabs:
1. [Project Description](#project-description)
2. [How to Install and Run the Project](#how-to-install-and-run-the-project)
3. [How to Use the Project](#how-to-use-the-project)
4. [Methodology](#methodology)
5. [Demo](#demo)
6. [Credits](#credits)

## Project Description :clipboard:
This project is a stock trend prediction tool implemented in Python using Long Short-Term Memory (LSTM) neural networks. The tool leverages historical stock price data to forecast future prices, aiding investors in making informed decisions. It gives users insights into stock trends, evaluation metrics, and visualizations to facilitate better understanding and analysis.

## How to Install and Run the Project :hammer_and_wrench:
To install and run the project locally, follow these steps:

1. **Clone the Repository:**
   - Open a terminal or command prompt.
   - Navigate to the directory where you want to clone the repository.
   - Run the following command to clone the repository:

     ```bash
     git clone https://github.com/a338wong/StockTrendPrediction.git
     ```

2. **Navigate to Project Directory:**
   - Change into the directory of the cloned repository:

     ```bash
     cd StockTrendPrediction
     ```

3. **Install Dependencies:**
   - Make sure you have Python installed on your machine. You can download it from [here](https://www.python.org/downloads/).
   - Install the required dependencies by running:

     ```bash
     pip install -r requirements.txt
     ```
   - This command will install all the necessary Python packages specified in the `requirements.txt` file.

4. **Run the Application:**
   - After installing the dependencies, you can run the application.
   - Execute the following command in your terminal:

     ```bash
     streamlit run app.py
     ```

5. **Access the Application:**
   - Once the application is running, it will provide a local URL (usually http://localhost:8501).
   - Open a web browser and navigate to the provided URL.
     
## How to Use the Project :open_book:
1. Upon running the application, you will be prompted to enter a stock ticker.
2. Enter the desired stock ticker and click on the "Predict Stock Price" button.
3. The application will fetch historical data, perform predictions, and display visualizations along with evaluation metrics.
4. Analyze the provided data, visualizations, and metrics to gain insights into the predicted stock trends.

## Methodology :bar_chart:
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
Visualizations are generated to compare the predicted stock prices with the actual prices using Plotly graph objects. Line charts are utilized to visualize the closing prices over time, as well as the predicted and actual prices.

#### 7. Interpretation and Analysis
- **Insights Generation**: The evaluation metrics and visualizations are analyzed to interpret the accuracy of the predictions and identify any trends or patterns in the data.
- **Decision Support**: The insights derived from the analysis can be used to support investment decision-making processes, providing investors with valuable information for portfolio management and risk assessment.

## Demo :cinema:
[Demo](https://github.com/a338wong/StockTrendPrediction/assets/153765340/a4a845fb-ae97-4cb8-8eaa-1f9a7adc85a3)

## Credits :trophy:
- **Alan Wong** - [GitHub Profile](https://github.com/a338wong) - [LinkedIn Profile](https://www.linkedin.com/in/alan-wong-309160212/)
- **GeeksforGeeks** - [Youtube](https://youtu.be/U_ZCiZ1TgOo?si=jg1cN20JLkQ-ZD2K)
  
--- 
