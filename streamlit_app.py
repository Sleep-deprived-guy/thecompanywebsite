import streamlit as st
import time
import code1
import streamlit as st
import time
import code1
import code2
import code3

st.title("THE COMPANY website V1.0")
st.write("V1.0 Changelog: Created website")

def run_task2():
    st.session_state.result2 = None
    with st.spinner("Rolling D20..."):
        res = code2.run_task2()
    st.session_state.result2 = res

def run_task():
    st.session_state.result = None
    with st.spinner("Running task..."):
        res = code1.run_task()
    st.session_state.result = res

def run_task3():
    st.session_state.result3 = None
    with st.spinner("Rolling D100..."):
        res = code3.run_task3()
    st.session_state.result3 = res


if "result" not in st.session_state:
    st.session_state.result = None

# Button that runs Python code when pressed
st.button("Generate NPC", on_click=run_task)

if st.session_state.result is not None:
    st.success("NPC completed")
    st.write(st.session_state.result)

st.button("Roll D20", on_click=run_task2)
if st.session_state.result2 is not None:
    st.success("Rolled")
    st.write(st.session_state.result2)

st.button("Roll D100", on_click=run_task3)
if st.session_state.result3 is not None:
    st.success("Rolled")
    st.write(st.session_state.result3)
