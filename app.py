import streamlit as st
from Encryption import encrypt_text, decrypt_text
from auth import hash_passkey, check_attempts, increment_attempts, reset_attempts
from storage import stored_data, add_entry, get_entry

st.set_page_config("🔐 Secure Data App")

def home():
    st.title("🔐 Secure Data System")
    choice = st.selectbox("Choose an option", ["Insert Data", "Retrieve Data", "Login Page"])
    if choice == "Insert Data":
        insert_data()
    elif choice == "Retrieve Data":
        retrieve_data()
    else:
        login()

def insert_data():
    st.subheader("📥 Store Data Securely")
    key = st.text_input("Enter a unique key")
    text = st.text_area("Enter text to encrypt")
    passkey = st.text_input("Enter a passkey", type="password")
    if st.button("Store"):
        hashed = hash_passkey(passkey)
        encrypted = encrypt_text(text)
        add_entry(key, encrypted, hashed)
        st.success("Data stored securely.")

def retrieve_data():
    st.subheader("🔍 Retrieve Data")
    key = st.text_input("Enter key")
    passkey = st.text_input("Enter your passkey", type="password")

    if check_attempts() >= 3:
        st.warning("Too many failed attempts. Reauthorization required.")
        st.switch_page("Login Page")
        return

    if st.button("Retrieve"):
        entry = get_entry(key)
        if entry and entry["passkey"] == hash_passkey(passkey):
            reset_attempts()
            decrypted = decrypt_text(entry["encrypted_text"])
            st.success(f"Decrypted Text: {decrypted}")
        else:
            increment_attempts()
            st.error(f"Incorrect passkey! Attempts left: {3 - check_attempts()}")

def login():
    st.subheader("🔐 Login Page")
    user = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if user == "admin" and password == "admin123":
            reset_attempts()
            st.success("Reauthorized. Go to Retrieve Data.")
        else:
            st.error("Invalid credentials.")

home()
