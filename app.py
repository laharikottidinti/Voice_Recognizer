import streamlit as st
import boto3
from voicerecognizer import voiceToText

st.title('Sentimental Analysis')

if st.button("Predict"):
    try:
        with st.spinner('Recording and analyzing...'):
            st.markdown('Recording started : ')
            text = voiceToText()

        st.success("Recording and analysis complete!")
        st.markdown("You spoke: " + str(text))
        
        client = boto3.client('comprehend')
        response = client.detect_sentiment(Text=text, LanguageCode='en')

        if response["Sentiment"] == "POSITIVE":
            st.success("Positive Statement")
        elif response["Sentiment"] == "NEGATIVE":
            st.error("Negative Statement")
        elif response["Sentiment"] == "NEUTRAL":
            st.warning("Neutral Statement")
        elif response["Sentiment"] == "MIXED":
            st.write("Mixed Statement")
        else:
            st.write("Invalid Text")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
