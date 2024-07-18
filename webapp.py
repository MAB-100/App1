import streamlit as st
import functions


todos = functions.get_todos()


st.title("TODOs App")
st.subheader("Welcome to the TODOs App")
st.write("This is a simple TODOs App built using Python and Streamlit")

for todo in todos:
    st.checkbox(todo)


st.text_input("", placeholder="Enter a todo....")
