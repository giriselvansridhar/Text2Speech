import streamlit as st
from gtts import gTTS
import os
import re
import tempfile

st.set_page_config(page_title="Text-to-Speech Editor", layout="centered")

st.title("🗣️ Text-to-Speech Editor (Streamlit Cloud Compatible)")
st.markdown("Type your text below. Each sentence will be read out as audio using Google TTS.")

text_input = st.text_area("📝 Write your text here:", height=300)

# Sentence splitting
def split_sentences(text):
    return re.split(r'(?<=[.!?]) +', text)

# Button to read text
if st.button("🔊 Read Sentences"):
    if text_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        sentences = split_sentences(text_input)
        for idx, sentence in enumerate(sentences):
            if sentence.strip():
                st.write(f"📢 Speaking: `{sentence}`")
                tts = gTTS(text=sentence, lang='en')
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
                    tts.save(tmp.name)
                    st.audio(tmp.name, format="audio/mp3")

# Optional: Auto-read on update
st.markdown("---")
auto = st.checkbox("🔁 Auto-read on update", value=False)

if auto and text_input.strip():
    sentences = split_sentences(text_input)
    for sentence in sentences:
        if sentence.strip():
            st.write(f"📢 Auto-speaking: `{sentence}`")
            tts = gTTS(text=sentence, lang='en')
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
                tts.save(tmp.name)
                st.audio(tmp.name, format="audio/mp3")
