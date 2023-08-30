import streamlit as st
import time
st.header("Digi-Clock")
def app_logic(hours, mins, secs):
  time.sleep(1)
  if secs == 59:
    if mins==59:
      hours=(hours+1)%24
      mins=0
    else:
      mins=(mins+1)
      secs=0
  else:
    secs+=1

  return(hours, mins, secs)    
      
while True:
  (hours, mins, secs)=app_logic(0, 0, 0)
  st.header(f"Time : {hours}:{mins}:{secs}")
