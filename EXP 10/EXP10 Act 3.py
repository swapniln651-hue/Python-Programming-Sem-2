#Game: Create a Number Guessing Game (user guesses random number).
"""
Created on Mon Apr 27 15:54:05 2026

@author: swapnil
"""

import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game", page_icon="🎯")

st.title("🎯 Number Guessing Game")
st.write("I'm thinking of a number between **1 and 100**. Can you guess it?")

# 1. Initialize Game State
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# 2. Game Logic Function
def reset_game():
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# 3. User Interface
if not st.session_state.game_over:
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, key="guess_input")
    
    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        
        if guess < st.session_state.secret_number:
            st.warning(f"Too low! ⬆️ (Attempt: {st.session_state.attempts})")
        elif guess > st.session_state.secret_number:
            st.warning(f"Too high! ⬇️ (Attempt: {st.session_state.attempts})")
        else:
            st.success(f"🎉 Correct! The number was {st.session_state.secret_number}.")
            st.balloons()
            st.session_state.game_over = True
            st.rerun() # Refresh to show the Play Again button
else:
    st.write(f"### Game Over! You won in {st.session_state.attempts} attempts.")
    if st.button("Play Again"):
        reset_game()
        st.rerun()

# 4. Optional: Footer info
st.divider()
with st.expander("How this works"):
    st.write("""
    Because Streamlit scripts rerun on every interaction, we use `st.session_state` 
    to remember the 'Secret Number' and the number of 'Attempts' across those reruns.
    """)
