import streamlit as st
import functions

print('Hello1')
todos = functions.get_todos()
def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    print('todo:',todo)
    todos.append(todo)
    functions.set_todos(todos)
    st.session_state['new_todo']=''

print('Hello2')


st.title("My ToDo App")
st.subheader("This is my todo app.")
st.write('This app is to increase your productivity.')

print('Hello3')

for index, todo in enumerate(todos):
    print('index-', index)
    checkbox = st.checkbox(label=f"{todo}", key=f"{todo}")
    if checkbox:
        print(checkbox)
        todos.pop(index)
        functions.set_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


print('Hello4')

st.text_input(label="Enter a todo", placeholder='Add a new todo..', on_change=add_todo, key='new_todo')

st.session_state

print('Hello5')