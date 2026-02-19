import streamlit as st
import time
import code1
import streamlit as st
import time
import code1
import code2
import code3

st.title("THE COMPANY website V1.0")

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
if "result2" not in st.session_state:
    st.session_state.result2 = None
if "result3" not in st.session_state:
    st.session_state.result3 = None
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

st.text_input("custom dice", key="dice_input")
if st.session_state.dice_input:
    st.button("Roll Custom Dice", on_click=st.write("press to roll again:"))
    try:
        sides = int(st.session_state.dice_input)
        if sides > 0:
            result = code3.roll_custom_dice(sides)
            st.write(f"Rolled a D{sides}: {result}")
        else:
            st.error("Please enter a positive integer.")
    except ValueError:
        st.error("Please enter a valid integer.")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("Changelogs:")
st.write("V1.0 Changelog: Created website")
st.write("V1.1 Changelog: Added Custom Dice Roller and moved changelogs to the bottom of the page")