#Imports
import streamlit as st
import time

#Title of the chatbot
st.title("Course Assistant")
st.divider()

#Greetings
with st.chat_message(name="assistant"):
    st.write(""" Hi there  
    What can i do for you today ?  """)
with st.chat_message(name="assistant"):
    st.text("My job is to provide you necessary information regarding Dr. B.C Roy Engineering College.")

#Creating messages(array) and level(integer)- to track tree destinations
if "messages" not in st.session_state:
    st.session_state.messages= []

if "level" not in st.session_state:
    st.session_state.level = 0

#Displays the msgs in the messages key value of the session_state(gives the application memory)
for msg in st.session_state.messages:
    with st.chat_message(name= msg["role"]) :
        st.text(msg["content"])#allows usage of \n , st.chat() doesnt allow \n


#Required Datas
info ="""
Established in 2000, BCREC is a Private college.   
The college is accredited by NBA, NAAC, AICTE, MAKAUT WB.   
Dr. B.C. Roy Engineering College offers 19 courses across 5 streams".  
"""
programmes = {
    "B-Tech": ["Civil Engineering","Computer Science and Design","Computer Science and Engineering","Computer Science and Engineering (Artificial Intelligence and Machine Learning)","Computer Science and Engineering (Data Science)","Electrical Engineering","Electronics and Communication Engineering","Information Technology","Mechanical Engineering"],
    "M-Tech":["Computer Science and Engineering","Mechanical Engineering","Electronics and Communication Engineering","Electrical Engineering"]}
prog_keys = list(programmes.keys())
address = "The full address of Dr. B.C Roy Engineering College is - \nJemua Road, Fuljhore, Durgapur,\nWest Bengal - 713206"
contact_info = """Call for Admission : 9333928874/ 9832131164/ 9932245570 / 9434250472\n Any Query related to payment contact Accounts Department BCREC and BCRECAPC
\nMobile – 7001380141 / Phone - 0343-2501353 extn. 278
\nEmail : accounts@bcrec.ac.in"""

#Gives typewriter effect while printing the texts of the chatbot
def typewriter(msg2 , delay=0.02):
    with st.spinner("Thinking..."):
        time.sleep(1)
    placeholder = st.empty() #consider this as an empty box in the ui
    typed_text = ""
    for char in msg2:
        typed_text = typed_text + char #adds characters to the typed_text on a per-character basis
        placeholder.text(typed_text)
        time.sleep(delay)
    st.session_state.messages.append({"role": "assistant", "content": msg2})#finally adds the string to the messages array and is displayed under the AI

#Converts an array of strings into strings (all strings in separate lines)
def stringify(arr):
    result = ""
    for item in arr:
        result+= item + "\n"
    return result

#Button Functionalities
if st.session_state.level==0:
    if st.button("Info"):
        st.session_state.messages.append({"role": "user", "content": "Info"})
        typewriter(info)
        st.session_state.level = 0.1
        st.rerun()
    if st.button("Courses Offered"):
        st.session_state.messages.append({"role": "user", "content": "Courses offered"})
        typewriter(f"The courses offered are as follows :-\n{prog_keys[0]}\n{prog_keys[1]}")
        st.session_state.level = 1.1
        st.rerun()

elif st.session_state.level==0.1:
    if st.button("Address"):
        st.session_state.messages.append({"role":"user","content":"Address"})
        typewriter(address)
        st.session_state.level =0.2
        st.rerun()

elif st.session_state.level == 0.2:
    if st.button("Contact Info."):
        st.session_state.messages.append({"role":"user","content":"Contact Info."})
        typewriter(contact_info)
        st.session_state.level=2
        st.rerun()

elif st.session_state.level==1.1:
    for i, keys in enumerate(programmes):
        if st.button(keys, key=f"btn_{i}"):
            subjects = stringify(programmes[keys])
            st.session_state.messages.append({"role": "user", "content": keys})
            typewriter(f"The courses offered for {keys} are as follows :-")
            typewriter(subjects)
            st.session_state.level = 2
            st.rerun()

elif st.session_state.level==2:
    if st.button("Thank You"):
        st.session_state.messages.append({"role":"user","content":"Thank You!"})
        typewriter("Glad to help!")
        st.session_state.level = 5
        st.rerun()

if st.session_state.level>0:
    if st.button("Main Menu"):
        with st.spinner("Thinking..."):
            time.sleep(1)
        st.session_state.messages.append({"role":"user","content":"Main Menu"})
        st.session_state.level = 0
        st.rerun()



