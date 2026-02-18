import streamlit as st
import time
import code1
import streamlit as st
import time
import code1

st.title("THE COMPANY website V1.0")
st.write("V1.0 Changelog: Created website")


def run_task():
    st.session_state.result = None
    with st.spinner("Running task..."):
        res = code1.run_task()
    st.session_state.result = res


if "result" not in st.session_state:
    st.session_state.result = None

# Button that runs Python code when pressed
st.button("Generate NPC", on_click=run_task)

if st.session_state.result is not None:
    st.success("NPC complete")
    st.write(st.session_state.result)
