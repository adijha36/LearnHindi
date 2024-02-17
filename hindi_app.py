import streamlit as st

page_bg_img = '''

<style>
.stApp {
  background-image: url("https://images.unsplash.com/photo-1657302156083-2e61fb23d161");
  background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Sample data: list of tuples with (question, answer)
flashcards = [
    {"question": "Hello", "answer": "Namaste", "difficulty": "Easy"},
    {"question": "How are you?", "answer": "Aap kaise ho?", "difficulty": "Easy"},
    {"question": "Thank you", "answer": "Dhanyawad", "difficulty": "Easy"},
    {"question": "Yes", "answer": "Haan", "difficulty": "Easy"},
    {"question": "No", "answer": "Nahi", "difficulty": "Easy"},
    {"question": "Goodbye", "answer": "Alvida", "difficulty": "Easy"},
    {"question": "Water", "answer": "Pani", "difficulty": "Easy"},
    {"question": "Food", "answer": "Khana", "difficulty": "Easy"},
    {"question": "How are you feeling?", "answer": "Aap kaisa mehsoos kar rahe hain?", "difficulty": "Medium"},
    {"question": "I'm doing well, thank you", "answer": "Main theek hoon, dhanyavad", "difficulty": "Medium"},
    {"question": "What are you doing today?", "answer": "Aap aaj kya kar rahe hain?", "difficulty": "Medium"},
    {"question": "I'm going to the market", "answer": "Main bazaar ja rahi hoon", "difficulty": "Medium"},
    {"question": "Where are you from?", "answer": "Aap kahan se hain?", "difficulty": "Medium"},
    {"question": "I'm from the United States", "answer": "Main United States se hoon", "difficulty": "Medium"},
    {"question": "What do you do for a living?", "answer": "Aap kya karte hain?", "difficulty": "Medium"},
    {"question": "I'm a teacher", "answer": "Main ek shikshak hoon", "difficulty": "Medium"},
    {"question": "Do you speak English?", "answer": "Kya aap Angrezi bolte hain?", "difficulty": "Medium"},
    {"question": "A little bit", "answer": "Thoda bahut", "difficulty": "Medium"},
    {"question": "What do you think of India?", "answer": "Aapko India ke baare mein kya lagta hai?", "difficulty": "Hard"},
    {"question": "It's a beautiful country with a rich history", "answer": "Yeh ek sundar desh hai jiska itihas bahut aamir hai", "difficulty": "Hard"},
    {"question": "What are your plans for the future?", "answer": "Aapke bhavishya ke liye kya yojana hai?", "difficulty": "Hard"},
    {"question": "I'm not sure yet", "answer": "Mujhe abhi tak pata nahi", "difficulty": "Hard"},
    {"question": "What is your biggest dream?", "answer": "Aapka sabse bada sapna kya hai?", "difficulty": "Hard"},
    {"question": "To travel the world", "answer": "Duniya ghoomna", "difficulty": "Hard"},
    {"question": "What is the meaning of life?", "answer": "Jeevan ka matlab kya hai?", "difficulty": "Hard"},
    {"question": "That's a difficult question to answer", "answer": "Yeh jawab dena mushkil hai", "difficulty": "Hard"},
    {"question": "What is your favorite thing about learning Hindi?", "answer": "Hindi seekhne ke baare mein aapka kya pasand hai?", "difficulty": "Hard"},
    {"question": "Can you help me?", "answer": "Kya aap meri madad kar sakte hain?", "difficulty": "Easy"},
    {"question": "What is your name?", "answer": "Aapka naam kya hai?", "difficulty": "Easy"},
    {"question": "I need a doctor", "answer": "Mujhe ek doctor ki zarurat hai", "difficulty": "Easy"},
    {"question": "I am lost", "answer": "Main kho gayi hoon", "difficulty": "Easy"},
    {"question": "I love you", "answer": "Main tumse pyar karti hoon", "difficulty": "Easy"},
    {"question": "I feel happy", "answer": "Mujhe khushi mehsoos ho rahi hai", "difficulty": "Medium"},
    {"question": "What is the time?", "answer": "Samay kya hua hai?", "difficulty": "Medium"},
    {"question": "Can you show me the way?", "answer": "Kya aap mujhe rasta dikha sakte hain?", "difficulty": "Medium"},
    {"question": "I would like to order food", "answer": "Mujhe khana order karna hai", "difficulty": "Medium"},
    {"question": "Where is the nearest ATM?", "answer": "Nikatam ATM kahan hai?", "difficulty": "Medium"},
    {"question": "How much does it cost?", "answer": "Iska kya daam hai?", "difficulty": "Hard"},
    {"question": "Can we have the bill, please?", "answer": "Kya hum bill le sakte hain, kripya?", "difficulty": "Hard"},
    {"question": "I need to change money", "answer": "Mujhe paise badalne hain", "difficulty": "Hard"},
    {"question": "Could you recommend a good restaurant?", "answer": "Kya aap ek achha restaurant suggest kar sakte hain?", "difficulty": "Hard"},
    {"question": "I am allergic to nuts", "answer": "Mujhe nuts se allergy hai", "difficulty": "Hard"},
    {"question": "Is there a hospital nearby?", "answer": "Kya yahan ke aas-paas ek hospital hai?", "difficulty": "Hard"},
    {"question": "I would like a map of the city", "answer": "Mujhe shahar ka naksha chahiye", "difficulty": "Hard"},
]


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
st.write(f":grey[**English: {filtered_flashcards[st.session_state.current_card]['question']}**]")

# Button to show the answer
if st.button("Show Answer"):
    st.write(f":grey[**Hindi: {filtered_flashcards[st.session_state.current_card]['answer']}**]")

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
