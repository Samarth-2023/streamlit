import streamlit as st
import time
st.header("Digi-Clock")
def app_logic(hours, mins, secs):
  while True:
    time.sleep(1)
    if secs == 59:
      if mins==59:
        hours=(hours+1)%24
      else:
        mins+=1
    else:
      secs+=1
    st.subheader(f"Time : {hours}:{mins}:{secs}")
      
hours=st.number_input('Hour', min_value=0, max_value=23, step=1)
mins=st.number_input('Minutes', min_value=0, max_value=59, step=1)
secs=st.number_input('Seconds', min_value=0, max_value=59, step=1)
app_logic(hours, mins, secs)
  
