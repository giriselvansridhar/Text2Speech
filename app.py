import streamlit as st
from gtts import gTTS
import re
import tempfile
import base64

st.set_page_config(page_title="🔊 Auto TTS with Highlight", layout="centered")

st.title("🗣️ Real-Time TTS with Highlights")
st.markdown("Text will be spoken and highlighted in real-time using Google TTS.")

text_input = st.text_area("📝 Write your text here:", height=300)

# Helper: Split into sentences
def split_sentences(text):
    return re.split(r'(?<=[.!?]) +', text)

# Helper: Play audio in browser automatically
def auto_play_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    md = f"""
    <audio autoplay="true" style="display:none;">
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(md, unsafe_allow_html=True)

# Read and highlight button
if st.button("🎬 Start Speaking with Highlights"):
    if not text_input.strip():
        st.warning("Please enter some text.")
    else:
        sentences = split_sentences(text_input)
        for i, sentence in enumerate(sentences):
            if sentence.strip():
                # Highlight current sentence
                st.markdown(f"<h4 style='color:#00f'>{sentence}</h4>", unsafe_allow_html=True)

                # Generate audio
                tts = gTTS(text=sentence, lang='en')
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
                    tts.save(tmp.name)
                    auto_play_audio(tmp.name)

                # Wait for the sentence to finish (estimated duration based on word count)
                duration = max(len(sentence.split()) / 2.5, 2)  # ~2.5 words/sec
                st.markdown("<hr>", unsafe_allow_html=True)
                st.sleep(duration)
