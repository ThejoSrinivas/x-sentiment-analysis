import streamlit as st
from preprocess import clean_text
from main import predict_sentiment

st.title("X Sentiment Analysis")
user_input = st.text_area("Enter an X post:", "Type here...")
if st.button("Analyze"):
    if user_input:
        result = predict_sentiment(user_input)
        st.write(f"Sentiment: **{result}**")
    else:
        st.write("Please enter some text.")
      
