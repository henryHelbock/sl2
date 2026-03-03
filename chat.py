import streamlit as st
from google import genai

# --- Hardcoded API key ---
API_KEY = "AIzaSyCfPXue_4tcr6hjPR15CYW0JunmKEaovHc"

# --- Create Gemini client (Gemini Developer API / AI Studio key) ---
client = genai.Client(api_key=API_KEY)

MODEL_ID = "gemini-3-flash-preview"

st.set_page_config(page_title="Gemini + Streamlit", layout="centered")
st.title("🤖 Gemini Chat (AI Studio API key)")

# --- Session state for chat history ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render chat history
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# Chat input
prompt = st.chat_input("Ask something…")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            try:
                response = client.models.generate_content(
                    model=MODEL_ID,
                    contents=prompt,
                )
                answer = response.text
            except Exception as e:
                answer = f"Error calling Gemini API: {e}"

            st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
