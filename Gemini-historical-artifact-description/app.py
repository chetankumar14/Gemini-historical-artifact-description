import streamlit as st
import google.generativeai as genai

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Gemini Historical Artifact Generator",
    page_icon="🏛",
    layout="centered"
)

st.title("🏛 Historical Artifact Description Generator")
st.markdown("Generate structured historical descriptions using Google Gemini.")

st.markdown("---")

# ---------------------------
# User Inputs
# ---------------------------
artifact_name = st.text_input("Artifact Name / Historical Period")

word_count = st.slider(
    "Select Word Count",
    min_value=50,
    max_value=2000,
    step=100,
    value=800
)

api_key = st.text_input(
    "Enter Google API Key",
    type="password"
)

generate_button = st.button("Generate Description")

st.markdown("---")

# ---------------------------
# Dynamic Generation
# ---------------------------
if generate_button:

    if not artifact_name:
        st.warning("Please enter an artifact name.")
        st.stop()

    if not api_key:
        st.warning("Please enter your Google API key.")
        st.stop()

    try:
        # 🔹 Configure Gemini dynamically using user key
        genai.configure(api_key=api_key)

        # 🔹 Initialize model AFTER key is entered
        model = genai.GenerativeModel("gemini-2.5-flash")

        prompt = f"""
        You are a professional historian and museum curator.

        Write a well-structured historical description of approximately {word_count} words about "{artifact_name}".

        Structure the response into:
        1. Introduction
        2. Historical Context
        3. Artistic / Structural Features
        4. Cultural Significance
        5. Legacy and Modern Relevance

        Maintain a formal academic tone.
        """

        with st.spinner("Connecting to Google Gemini and generating content..."):
            response = model.generate_content(prompt)

        st.success("Connected Successfully! Content Generated.")
        st.markdown(response.text)

    except Exception as e:
        st.error("Failed to connect to Google Gemini.")
        st.error(str(e))
