# 🎭 IBM Watson Emotion Detection App

A simple web app that uses **IBM Watson Natural Language Understanding (NLU)**  
to analyze emotions in text (joy, sadness, anger, fear, disgust).  

## 🚀 Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🌐 Deploy on Streamlit Cloud
1. Fork this repo.
2. Go to [Streamlit Cloud](https://share.streamlit.io).
3. Select this repo and deploy.
4. Add your **IBM credentials** in Streamlit **Secrets Manager**:

```toml
[IBM]
API_KEY = "your-ibm-api-key"
URL = "your-ibm-service-url"
```

🎉 Done! Your app will be live.
