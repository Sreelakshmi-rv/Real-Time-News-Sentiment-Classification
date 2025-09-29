import streamlit as st
import pandas as pd
import glob
from textblob import TextBlob

st.set_page_config(page_title="Real-Time News Sentiment", layout="wide")
st.title("Real-Time News Sentiment Dashboard")
st.subheader("Positive / Negative Classification of News Headlines")

# Read all JSON files from the same folder as app.py
all_files = glob.glob("*.json")
headlines_list = []

for file in all_files:
    df = pd.read_json(file, lines=True)
    headlines_list.append(df)

if headlines_list:
    df_all = pd.concat(headlines_list, ignore_index=True)
    
    # Sentiment analysis
    def get_sentiment(text):
        return "Positive" if TextBlob(text).sentiment.polarity >= 0 else "Negative"
    
    df_all["Sentiment"] = df_all["headline"].apply(get_sentiment)
    
    # Display table
    st.dataframe(df_all)
    
    # Display bar chart
    sentiment_counts = df_all["Sentiment"].value_counts()
    st.bar_chart(sentiment_counts)
else:
    st.write("No headlines found. Make sure JSON files are in the same folder.")
