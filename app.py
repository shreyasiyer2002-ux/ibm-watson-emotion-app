import streamlit as st
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions

# Load credentials from Streamlit secrets
api_key = st.secrets["IBM"]["API_KEY"]
url = st.secrets["IBM"]["URL"]

# IBM Watson setup
authenticator = IAMAuthenticator(api_key)
nlu = NaturalLanguageUnderstandingV1(
    version='2021-08-01',
    authenticator=authenticator
)
nlu.set_service_url(url)

def analyze_emotion(text):
    """Analyze emotions in the given text using IBM Watson NLU."""
    response = nlu.analyze(
        text=text,
        features=Features(emotion=EmotionOptions())
    ).get_result()
    return response["emotion"]["document"]["emotion"]

# 🌐 Streamlit UI
st.set_page_config(page_title="IBM Watson Emotion Detector", page_icon="🎭")

st.title("🎭 IBM Watson Emotion Detection")
st.write("Enter some text and let IBM Watson detect emotions (joy, sadness, anger, fear, disgust).")

user_input = st.text_area("✍️ Enter text here:", "")

if st.button("🔍 Analyze Emotion"):
    if user_input.strip():
        emotions = analyze_emotion(user_input)

        st.subheader("Detected Emotions:")
        for emotion, score in emotions.items():
            st.write(f"**{emotion.capitalize()}**: {score:.4f}")

        st.subheader("📊 Emotion Scores")
        st.bar_chart(emotions)
    else:
        st.warning("⚠️ Please enter some text before analyzing.")
