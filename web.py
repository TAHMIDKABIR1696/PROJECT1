import streamlit as st
import function


todos = function.open_todo()
def add_todo():
    todo = st.session_state["add"] + '\n'
    todos.append(todo)
    function.write_todo(todos)



st.title("MY TODO APP")
st.subheader("welcome....")
st.write("Let's increase your activity")


for index, todo in enumerate(todos):
    cb = st.checkbox(todo, key=todo)
    if cb:
        todos.pop(index)
        function.write_todo(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input("YOUR ACTIVITY:", placeholder="ADD TODOS",
              on_change=add_todo, key="add")
