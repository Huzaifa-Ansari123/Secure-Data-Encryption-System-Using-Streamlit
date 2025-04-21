import hashlib
import streamlit as st

def hash_passkey(passkey: str) -> str:
    return hashlib.sha256(passkey.encode()).hexdigest()

def check_attempts():
    if "attempts" not in st.session_state:
        st.session_state.attempts = 0
    return st.session_state.attempts

def increment_attempts():
    st.session_state.attempts += 1

def reset_attempts():
    st.session_state.attempts = 0
