import streamlit as st
from gtts import gTTS
import glob
import time
import os
from util.flashcards import get_flashcards

page_bg_img = '''

<style>
.stApp {
  background-image: url("https://images.unsplash.com/photo-1624139283061-adee53a59791");
  background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Sample data: list of tuples with (question, answer)

flashcards = get_flashcards()

def text_to_speech(text):
    tts = gTTS(text, lang= "hi")
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name

# Allow the user to select a difficulty level
difficulty_level = st.selectbox(
    ":grey[**Select the difficulty level:**]",
    options=["Easy", "Medium", "Hard"],
    index=0  # Default to the first option, "Easy"
)

filtered_flashcards = [card for card in flashcards if card["difficulty"] == difficulty_level]

# Session state to keep track of current flashcard
if 'current_card' not in st.session_state:
    st.session_state.current_card = 0  # Start with the first card

    
# Display the current question
st.write(f":blue[**English:**] {filtered_flashcards[st.session_state.current_card]['question']}")

# Button to show the answer
if st.button("Show Answer"):
    st.write(f" :green[**Hindi:**] {filtered_flashcards[st.session_state.current_card]['answer']}")

if st.button("Hear"):
    result = text_to_speech(filtered_flashcards[st.session_state.current_card]['answer'])
    audio_file = open(f"temp/{result}.mp3", "rb")
    audio_bytes = audio_file.read()
    st.markdown(f"## Your audio:")
    st.audio(audio_bytes, format="audio/mp3", start_time=0)


def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)

# Navigation buttons
col1, col2 = st.columns(2)


with col1:
    # Button to go to the previous card
    if st.button("Previous"):
        if st.session_state.current_card > 0:
            st.session_state.current_card -= 1
        st.experimental_rerun()

with col2:
    # Button to go to the next card
    if st.button("Next"):
        if st.session_state.current_card < len(filtered_flashcards) - 1:
            st.session_state.current_card += 1
        st.experimental_rerun()
