import streamlit as st
import time
st.header("Digi-Clock")
def app_logic():
  clock_placeholder=st.empty()
  while True:
    curr_time=time.strftime('%H:%M:%S')
    clock_placeholder.text(f"Time : {curr_time}")
    time.sleep(1)

app_logic()
