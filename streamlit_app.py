import streamlit as st
import time
import code1
import streamlit as st
import time
import code1
import code2
import code3
import code4
import code5

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

def run_task4():
    st.session_state.result4 = None
    with st.spinner("generating shop..."):
        res = code4.run_task4()
    st.session_state.result4 = res

def run_task5():
    st.session_state.result5 = None
    with st.spinner("generating encounter..."):
        res = code5.run_task5()
    st.session_state.result5 = res

if "result" not in st.session_state:
    st.session_state.result = None
if "result2" not in st.session_state:
    st.session_state.result2 = None
if "result3" not in st.session_state:
    st.session_state.result3 = None
if "result4" not in st.session_state:
    st.session_state.result4 = None
if "result5" not in st.session_state:
    st.session_state.result5 = None
# Button that runs Python code when pressed
st.write("Random Generators:")

st.button("Generate NPC", on_click=run_task)

if st.session_state.result is not None:
    st.success("NPC completed")
    st.write(st.session_state.result)

st.button("Generate Shop", on_click=run_task4)
if st.session_state.result4 is not None:
    st.success("Shop Generated")
    st.write(st.session_state.result4)

st.button("Generate encounter", on_click=run_task5)
if st.session_state.result5 is not None:
    st.success("Encounter Generated")
    st.write(st.session_state.result5)

st.write("")
st.write("")
st.write("")
st.write("Dice Rollers:")

st.button("Roll D20", on_click=run_task2)
if st.session_state.result2 is not None:
    st.success("Rolled")
    st.write(st.session_state.result2)

st.button("Roll D100", on_click=run_task3)
if st.session_state.result3 is not None:
    st.success("Rolled")
    st.write(st.session_state.result3)

st.text_input("custom dice", key="dice_input")
st.text_input("dice amount", key="dice_amount_input")
if st.session_state.dice_input:
    st.button("Roll Custom Dice", on_click=st.write("press to roll again:"))
    try:
        sides = int(st.session_state.dice_input)
        if sides > 0:
            if st.session_state.dice_amount_input:
                amount = int(st.session_state.dice_amount_input)
                if amount > 0:
                    results = [code3.roll_custom_dice(sides) for _ in range(amount)]
                    st.write(f"Rolled {amount} D{sides}:")
                    for result in results:
                        st.write(result)
                else:
                    st.error("Please enter a positive integer for the amount of dice.")
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
st.write("V1.2 Changelog: Added multi-dice rolling for the custom dice roller")
st.write("V1.3 Changelog: Added shop generator")