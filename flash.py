import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect('flashcards.db', check_same_thread=False)
c = conn.cursor()

st.sidebar.header("Add a Flashcard")
question = st.sidebar.text_input("Question")
answer = st.sidebar.text_input("Answer")
category = st.sidebar.text_input("Category (optional)")

if st.sidebar.button("Add Flashcard"):
    if question and answer:
        c.execute("INSERT INTO flashcards (question, answer, category) VALUES (?, ?, ?)",
                  (question, answer, category))
        conn.commit()
        st.sidebar.success("Flashcard added!")
    else:
        st.sidebar.error("Question and Answer cannot be empty!")

df = pd.read_sql_query("SELECT * FROM flashcards", conn)
st.title("Mini Flashcard Learning App")

if "current_card" not in st.session_state:
    st.session_state.current_card = None

if not df.empty:
    if st.button("Show Random Flashcard"):
        st.session_state.current_card = df.sample(1).iloc[0]

    if st.session_state.current_card is not None:
        st.subheader("Question:")
        st.write(st.session_state.current_card['question'])

        if st.checkbox("Show Answer"):
            st.subheader("Answer:")
            st.write(st.session_state.current_card['answer'])
else:
    st.info("No flashcards yet. Add some in the sidebar!")

with st.expander("All Flashcards"):
    st.dataframe(df)
