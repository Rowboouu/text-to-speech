import os
from gtts import gTTS
import streamlit as st

# Streamlit UI
st.title("Text-to-Speech App")
st.write("Enter text below, and I'll convert it to speech!")

# Input text from the user
text_input = st.text_area("Enter your text:", "")

# Dropdown to select language and accent
language = st.selectbox("Select Language:", ["English", "French", "Spanish"])
accent = st.selectbox("Select Accent (for English):", ["Default", "British", "Indian"])

# Map language and accent
lang_map = {"English": "en", "French": "fr", "Spanish": "es"}
tld_map = {"Default": "com", "British": "co.uk", "Indian": "co.in"}

# Generate speech on button click
if st.button("Convert to Speech"):
    if text_input.strip():
        lang = lang_map[language]
        tld = tld_map[accent] if language == "English" else "com"
        
        # Convert text to speech
        tts = gTTS(text=text_input, lang=lang, tld=tld)
        audio_file = "output.mp3"
        tts.save(audio_file)

        # Play or download the audio file
        st.audio(audio_file, format="audio/mp3")
        st.success("Speech generated successfully!")
    else:
        st.error("Please enter some text.")

