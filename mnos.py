import streamlit as st

st.title("Simple Streamlit App")
st.write("Welcome to our simple app!")

# Add a text input box and a button
name = st.text_input("What is your name?")
if st.button("Click here"):
    st.write(f"Hello, {name}!")