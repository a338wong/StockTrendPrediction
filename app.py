import numpy as np
import pandas as pd
import yfinance as yf
from keras.models import load_model
import streamlit as st
import plotly.graph_objects as go
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Function to load the model
@st.cache_data
def load_nn_model():
    return load_model('keras_model.h5')

# Function to preprocess data and make predictions
@st.cache_data(show_spinner="Predicting... Please wait.")

def predict_stock_price(_model, user_input):
    start = '2010-01-01'
    end = '2024-01-01'
    df = yf.download(user_input, start=start, end=end)

    if df.empty:
        st.error("No Data Found")
        return

    st.subheader(f'Data from {start.split("-")[0]} - {end.split("-")[0]}')
    st.write(df.describe())

    # Splitting Data into Training and Testing
    data_training = pd.DataFrame(df['Close'][0:int(len(df) * 0.70)])
    data_testing = pd.DataFrame(df['Close'][int(len(df) * 0.70):int(len(df))])

    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0, 1))
    data_training_array = scaler.fit_transform(data_training)

    # Load Model
    model = load_nn_model()

    # Testing
    past_100_days = data_training.tail(100)
    final_df = pd.DataFrame({'Close': past_100_days['Close'].tolist() + data_testing['Close'].tolist()})
    input_data = scaler.fit_transform(final_df)

    x_test = []
    y_test = []

    for i in range(100, input_data.shape[0]):
        x_test.append(input_data[i - 100: i])
        y_test.append(input_data[i, 0])

    x_test, y_test = np.array(x_test), np.array(y_test)
    y_predicted = model.predict(x_test)
    scaler = scaler.scale_

    scale_factor = 1 / scaler[0]
    y_predicted = y_predicted * scale_factor
    y_test = y_test * scale_factor

    # Visualization
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Closing Price'))
    fig1.update_layout(title='Closing Price vs Time',
                       xaxis_title='Time',
                       yaxis_title='Closing Price')

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Closing Price'))
    fig2.add_trace(go.Scatter(x=df.index, y=df['Close'].rolling(100).mean(), mode='lines', name='100MA'))
    fig2.update_layout(title='Closing Price vs Time with 100MA',
                       xaxis_title='Time',
                       yaxis_title='Price')

    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Closing Price'))
    fig3.add_trace(go.Scatter(x=df.index, y=df['Close'].rolling(100).mean(), mode='lines', name='100MA'))
    fig3.add_trace(go.Scatter(x=df.index, y=df['Close'].rolling(200).mean(), mode='lines', name='200MA'))
    fig3.update_layout(title='Closing Price vs Time with 100MA & 200MA',
                       xaxis_title='Time',
                       yaxis_title='Price')

    fig4 = go.Figure()
    fig4.add_trace(go.Scatter(x=np.arange(len(y_test)), y=y_test, mode='lines', name='Original Price'))
    fig4.add_trace(go.Scatter(x=np.arange(len(y_predicted)), y=y_predicted.flatten(), mode='lines', name='Predicted Price', line=dict(color='red')))
    fig4.update_layout(title='Original Price vs Predicted Price',
                       xaxis_title='Time (Days)',
                       yaxis_title='Price (USD)')

    st.plotly_chart(fig1)
    st.plotly_chart(fig2)
    st.plotly_chart(fig3)
    st.plotly_chart(fig4)

    # Evaluation Metrics

    mse = mean_squared_error(y_test, y_predicted)
    mae = mean_absolute_error(y_test, y_predicted)
    rmse = np.sqrt(mse)
    mape = np.mean(np.abs((y_test - y_predicted) / y_test)) * 100
    ss_residual = np.sum((y_test - y_predicted) ** 2)
    ss_total = np.sum((y_test - np.mean(y_test)) ** 2)
    r_squared = 1 - (ss_residual / ss_total)
    n = len(y_test)
    p = x_test.shape[1]
    adjusted_r_squared = 1 - ((1 - r_squared) * (n - 1) / (n - p - 1))

    with st.expander("Evaluation Metrics"):
        if mse is not None:
            st.write("Mean Squared Error (MSE):", f"{mse:.2f}")
            st.write("Mean Absolute Error (MAE):", f"{mae:.2f}")
            st.write("Root Mean Squared Error (RMSE):", f"{rmse:.2f}")
            st.write("Mean Absolute Percentage Error (MAPE):", f"{mape:.2f}%")
            st.write("Coefficient of Determination (R-squared):", f"{r_squared:.2f}")
            st.write("Adjusted R-squared:", f"{adjusted_r_squared:.2f}")
        else:
            st.write("Please make a prediction first.")

# Streamlit UI
st.title("Stock Trend Prediction")
user_input = st.text_input('Enter Stock Ticker', '')

if st.button('Predict Stock Price'):
    predict_stock_price(load_nn_model(), user_input)

# Add a footer
st.markdown(
    """
    --- 
    *Disclaimer: This app provides stock price predictions for educational purposes. 
    Always do your own research before making any investment decisions.*
    """
)
