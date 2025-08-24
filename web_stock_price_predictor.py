import streamlit as st
import pandas as pd
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt
import yfinance as yf


st.title ("Stock Price Predictor App By Suvojit")

stock = st.text_input("Enter the stock ID","GOOG")

from datetime import datetime
end = datetime.now()
start = datetime(end.year-20,end.month,end.day)

google_data = yf.download(stock, start, end)

model = load_model("Latest_stock_price_model.keras")
st.subheader("Stock Data")
st.write(google_data)

spliting_len = int(len(Google_data)*0.7)
x_test = pd.DataFrame(google_data.Close[spliting_len:])

def plot_graph(figsize, values, full_data):
    fig = plt.figure(figsize=figsize)
    plt.plot(values,'Orange')
    plt.plot(full_data.close, 'b')
    return fig







