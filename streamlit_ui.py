import streamlit as st
import requests

st.set_page_config(page_title="Autocomplete Search Engine")
st.title("🔍 Autocomplete Search Engine")

# Create input field and update on change
if "prefix" not in st.session_state:
    st.session_state.prefix = ""

def update_prefix():
    st.session_state.prefix = st.session_state.input

st.text_input("Start typing...", key="input", on_change=update_prefix)

prefix = st.session_state.prefix

if prefix:
    try:
        res = requests.get(f"http://localhost:5000/autocomplete?prefix={prefix}")
        suggestions = res.json()
        st.code(f"Status: {res.status_code}")
        if suggestions:
            st.write("Suggestions:")
            for s in suggestions:
                st.markdown(f"- {s}")
        else:
            st.warning("No matches found.")
    except Exception as e:
        st.error(f"Flask not running or error: {e}")
