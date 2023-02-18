import streamlit as st
import yfinance as yf
import datetime



st.write ("""
          # Welcome to our Stock Analysis App
          
          """)

ticker_symbol = st.text_input('Enter Stock Symbol', 'AAPL', key='placeholder')

ticker_data = yf.Ticker(ticker_symbol)
col1, col2= st.columns(2)

with col1:
    start_date = st.date_input(
        "Enter Start Date",
        datetime.date(2019, 1, 1))
with col2:
    end_date = st.date_input(
        "Enter End Date",
        datetime.date(2023, 2, 17))

tickers_df=ticker_data.history(period="1d",
                               start=f"{start_date}",
                               end=f"{end_date}")


st.write(f"""
         ### Showing Data for {ticker_symbol} stock""")

st.dataframe(tickers_df)

st.write(f"""
         ### Daily Closing price of {ticker_symbol} """)
st.line_chart(tickers_df['Close'])

st.write(f"""
         ### Daily volume of {ticker_symbol} """)
st.line_chart(tickers_df['Volume'])


col1, col2= st.columns(2)

with col1:
    st.write(f"""
             ### Daily Closing price of {ticker_symbol} """)
    st.line_chart(tickers_df['Close'])

with col2:
    st.write(f"""
             ### Daily volume of {ticker_symbol} """)
    st.line_chart(tickers_df['Volume'])
