import streamlit as st
import random

# List of words to choose from
words = ['PYTHON', 'STREAMLIT', 'PROGRAMMING', 'COMPUTER', 'ALGORITHM', 'DATABASE', 'DEVELOPER']

def initialize_game():
    if 'word' not in st.session_state:
        st.session_state.word = random.choice(words)
        st.session_state.guessed_letters = set()
        st.session_state.tries = 6

def display_hangman(tries):
    stages = [  # Final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # Head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # Head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # Head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # Head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # Head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # Initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]

def main():
    st.title("Hangman Game")
    
    initialize_game()
    
    # Display the hangman
    st.text(display_hangman(st.session_state.tries))
    
    # Display the word with underscores for unguessed letters
    display_word = ''
    for letter in st.session_state.word:
        if letter in st.session_state.guessed_letters:
            display_word += letter + ' '
        else:
            display_word += '_ '
    st.subheader(display_word)
    
    # Display guessed letters
    st.write("Guessed letters:", ' '.join(sorted(st.session_state.guessed_letters)))
    
    # Input for letter guess
    guess = st.text_input("Guess a letter:", max_chars=1).upper()
    
    if st.button("Submit Guess"):
        if guess and guess.isalpha():
            if guess in st.session_state.guessed_letters:
                st.warning("You already guessed that letter!")
            else:
                st.session_state.guessed_letters.add(guess)
                if guess not in st.session_state.word:
                    st.session_state.tries -= 1
                    st.error("Wrong guess!")
                else:
                    st.success("Correct guess!")
        else:
            st.warning("Please enter a valid letter!")
    
    # Check win/lose conditions
    if all(letter in st.session_state.guessed_letters for letter in st.session_state.word):
        st.success("Congratulations! You won! 🎉")
        if st.button("Play Again"):
            st.session_state.clear()
            st.experimental_rerun()
    
    if st.session_state.tries <= 0:
        st.error(f"Game Over! The word was: {st.session_state.word}")
        if st.button("Play Again"):
            st.session_state.clear()
            st.experimental_rerun()

if __name__ == "__main__":
    main()
