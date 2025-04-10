import streamlit as st
import pyttsx3
import re
import time

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # Speaking speed

st.set_page_config(page_title="Text-to-Speech Editor", layout="centered")

st.title("🗣️ Text-to-Speech Editor")
st.markdown("Type your text below. Each sentence will be read out automatically.")

# Text area input
text_input = st.text_area("📝 Write your text here:", height=300)

# Button to trigger TTS
if st.button("🔊 Read Sentences"):
    if text_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        sentences = re.split(r'(?<=[.!?]) +', text_input)
        for sentence in sentences:
            st.write(f"📢 Speaking: `{sentence}`")
            engine.say(sentence)
            engine.runAndWait()
            time.sleep(0.5)  # Slight pause between sentences

# Optional: Auto-read on update
st.markdown("---")
auto = st.checkbox("🔁 Auto-read on update", value=False)

if auto and text_input.strip():
    sentences = re.split(r'(?<=[.!?]) +', text_input)
    for sentence in sentences:
        st.write(f"📢 Auto-speaking: `{sentence}`")
        engine.say(sentence)
        engine.runAndWait()
        time.sleep(0.5)
