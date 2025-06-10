import streamlit as st
import string
import random

#initial state variables
if 'length' not in st.session_state:
    st.session_state.length = 12
if 'letters' not in st.session_state:
    st.session_state.letters = False
if 'digits' not in st.session_state:
    st.session_state.digits = False
if 'punctuation' not in st.session_state:
    st.session_state.punctuation = False

#modified the generate_password function to use passed arguments instead of globals
def generate_password(length, letters, digits, punctuation):
    charsList = ""
    password = []

    if letters:
        charsList += string.ascii_letters
        password.append(random.choice(string.ascii_letters))
    if digits:
        charsList += string.digits
        password.append(random.choice(string.digits))
    if punctuation:
        charsList += string.punctuation
        password.append(random.choice(string.punctuation))

    if not charsList:
        return "❌ Please select at least one character type."

    while len(password) < length:
        password.append(random.choice(charsList))

    random.shuffle(password)
    return "".join(password)


#UI
st.set_page_config(page_title="Star Wars Password Generator", page_icon="🔐")

st.title("🔐 Star Wars Password Generator")
st.markdown("""
Welcome, **Padawan**!  
Trained by the Resistance IT masters, this generator is here to forge the galaxy’s strongest passwords.  
May your credentials never fall into Sith hands.
""")

#user input
st.session_state.length = st.slider("Password Length", 4, 50, st.session_state.length)
st.session_state.letters = st.checkbox("Include Letters (A-Z, a-z)", value=True)
st.session_state.digits = st.checkbox("Include Digits (0-9)")
st.session_state.punctuation = st.checkbox("Include Punctuation (!@#$...)")

#generate
if st.button("Generate Password"):
    result = generate_password(
        st.session_state.length,
        st.session_state.letters,
        st.session_state.digits,
        st.session_state.punctuation
    )
    st.success(f"Your generated password is:\n\n`{result}`")

st.markdown("---")
st.caption("Crafted by JediTech™ | May the Force be with your credentials.")
