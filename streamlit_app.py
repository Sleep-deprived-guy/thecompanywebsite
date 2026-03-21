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
import random

st.title("THE COMPANY website V1.5")

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
st.write("Misc:")
st.text_input("list to pick from (use commas to separate items)", key="list_input")
st.button("Pick from list", on_click=st.write("press to pick again:"))
if st.session_state.list_input:
    items = st.session_state.list_input.split(",")
    if len(items) > 0:
        selected_item = random.choice(items)
        st.write(f"Selected item: {selected_item}")

st.write("")
st.text_input("timer (in minutes)", key="timer_input")
st.text_input("timer amount", key="timer_amount_input")
if st.session_state.timer_input:
    st.button("Add Timer", on_click=st.write("press to add again:"))
    try:
        minutes = int(st.session_state.timer_input)
        if minutes > 0:
            if st.session_state.timer_amount_input:
                amount = int(st.session_state.timer_amount_input)
                if amount > 0:
                    if "timers" not in st.session_state:
                        st.session_state.timers = {}
                    for i in range(amount):
                        timer_id = max(st.session_state.timers.keys()) + 1 if st.session_state.timers else 0
                        st.session_state.timers[timer_id] = {
                            "duration": minutes,
                            "start_time": time.time(),
                            "paused": False,
                            "pause_time": None
                        }
                else:
                    st.error("Please enter a positive integer for the timer amount.")
        else:
            st.error("Please enter a positive integer for the timer duration.")
    except ValueError:
        st.error("Please enter valid integers.")

if "timers" not in st.session_state:
    st.session_state.timers = {}

if st.session_state.timers:
    st.write("Active Timers:")
    for timer_id, timer_data in list(st.session_state.timers.items()):
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
        
        if timer_data["paused"]:
            elapsed = timer_data["pause_time"] - timer_data["start_time"]
        else:
            elapsed = time.time() - timer_data["start_time"]
        
        remaining = timer_data["duration"] * 60 - elapsed
        
        if remaining <= 0:
            st.session_state.timers.pop(timer_id)
            st.rerun()
        
        minutes_left = int(remaining // 60)
        seconds_left = int(remaining % 60)
        
        with col1:
            st.metric("Time Left", f"{minutes_left}m {seconds_left}s")
        
        with col2:
            if st.button("⏸ Pause" if not timer_data["paused"] else "▶ Resume", key=f"pause_{timer_id}"):
                if timer_data["paused"]:
                    elapsed_when_paused = timer_data["pause_time"] - timer_data["start_time"]
                    st.session_state.timers[timer_id]["start_time"] = time.time() - elapsed_when_paused
                    st.session_state.timers[timer_id]["paused"] = False
                else:
                    st.session_state.timers[timer_id]["pause_time"] = time.time()
                    st.session_state.timers[timer_id]["paused"] = True
                st.rerun()
        
        with col3:
            if st.button("🔄 Reset", key=f"reset_{timer_id}"):
                st.session_state.timers[timer_id]["start_time"] = time.time()
                st.session_state.timers[timer_id]["paused"] = False
                st.rerun()
        
        with col4:
            if st.button("❌ Stop", key=f"stop_{timer_id}"):
                st.session_state.timers.pop(timer_id)
                st.rerun()
        
        col_adjust1, col_adjust2, col_adjust3 = st.columns([1, 1, 2])
        with col_adjust1:
            mins_adjust = st.number_input(f"Min adjustment (Timer {timer_id})", value=0, step=1, key=f"min_adjust_{timer_id}")
        with col_adjust2:
            secs_adjust = st.number_input(f"Sec adjustment (Timer {timer_id})", value=0, step=1, max_value=59, key=f"sec_adjust_{timer_id}")
        with col_adjust3:
            if st.button("Apply Adjustment", key=f"apply_adjust_{timer_id}"):
                total_sec_adjustment = mins_adjust * 60 + secs_adjust
                if total_sec_adjustment != 0:
                    st.session_state.timers[timer_id]["duration"] = (remaining + total_sec_adjustment) / 60
                    st.session_state.timers[timer_id]["start_time"] = time.time()
                    if "adjust_tracking" not in st.session_state:
                        st.session_state.adjust_tracking = {}
                    st.session_state.adjust_tracking[f"min_adjust_{timer_id}"] = 0
                    st.session_state.adjust_tracking[f"sec_adjust_{timer_id}"] = 0
                    st.rerun()
        
        st.divider()
    
    if len(st.session_state.timers) > 0:
        time.sleep(1)
        st.rerun()
st.write("")
st.write("")
st.write("")
st.write("")
st.write("Changelogs:")
st.write("V1.0 Changelog: Created website")
st.write("V1.1 Changelog: Added Custom Dice Roller and moved changelogs to the bottom of the page")
st.write("V1.2 Changelog: Added multi-dice rolling for the custom dice roller")
st.write("V1.3 Changelog: Added shop generator")
st.write("V1.4 Changelog: Added random item picker that can pick from custom lists")
st.write("V1.5 Changelog: Added timer feature with pause, reset, and adjustment options")