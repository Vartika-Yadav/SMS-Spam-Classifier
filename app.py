import streamlit as st
import joblib


# Page configuration
st.set_page_config(
    page_title="SMS Spam Classifier",
    page_icon="📩",
    layout="centered"
)


# Load trained pipeline
MODEL_PATH = "models/spam_classifier_pipeline.pkl"

model = joblib.load(MODEL_PATH)


# Header
st.title("📩 SMS Spam Classifier")

st.write(
    "Enter an SMS message below and the machine learning model "
    "will classify it as spam or ham."
)

st.divider()


# Message input
message = st.text_area(
    "Enter your message:",
    height=150,
    placeholder="Example: Congratulations! You won a free prize..."
)


# Prediction
if st.button("Classify Message", use_container_width=True):

    if message.strip() == "":
        st.warning("Please enter a message.")

    else:
        prediction = model.predict([message])[0]

        probability = model.predict_proba([message])[0]

        spam_probability = probability[1]
        ham_probability = probability[0]

        st.divider()

        if prediction == 1:
            st.error("🚨 SPAM MESSAGE")

            st.write(
                f"Spam probability: **{spam_probability:.2%}**"
            )

        else:
            st.success("✅ HAM / LEGITIMATE MESSAGE")

            st.write(
                f"Ham probability: **{ham_probability:.2%}**"
            )


# Model information
st.divider()

st.subheader("Model Information")

col1, col2 = st.columns(2)

with col1:
    st.write("**Feature Extraction**")
    st.write("TF-IDF")

with col2:
    st.write("**Classifier**")
    st.write("Logistic Regression")

st.caption(
    "SMS Spam Classification using NLP and Machine Learning"
)