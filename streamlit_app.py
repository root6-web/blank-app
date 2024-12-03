import streamlit as st
import time
st.title("Lova Sarobidy❤️👨🏾‍💻")
st.header("Hello Malaysia")
st.subheader("Welcome to my streamlit")
st.text("Hello everyone, thanks for visited here.")
st.write("This is my first streamlit💪.")
st.markdown("My **adventure**")
st.markdown("## My dreams")
st.markdown("### My experiences")
st.markdown("[markdown cheat sheet] (https://getemoji.com/)")
st.markdown("""
    1. Study
    2. Family
    3. Travel
        - I like   
        - Ok
        ✍️
            """)
st.markdown("### html")
html_code = """
    <head>
        <style>
            body {
                background-color: darkslategrey;
                color: azure;
                font-size: 1.1em;
            }
            h1 {
                color: coral;
            }
            #intro {
                font-size: 1.3em;
            }
            h2 {
                color: orange;
            }
        </style>
    </head>
    <body>
 """
st.markdown(html_code, unsafe_allow_html= True)
st.markdown("---")
st.markdown("## Latex code")
st.latex("d=√(x₁ – x₂)² + (y₁ – y₂)²")
st.latex("2x2+5xy+4yz+2y+3= x")
st.title("Exemple input text")
name = st.text_input("Enter your name")
Feedback = st.text_area("Enter your feedback")
#time = st.time_input("Select your time")
date = st.date_input("Date")
age = st.number_input("Enter your age")

st.write("Name :", name)
st.write("Feedback :", Feedback)
st.write("Age :", age)
#st.write("time :", time)
#st.write("date :", date)
color = st.color_picker("Pick your color")
html_code ="""
<h1 style= "color: {};" >Embedded Styles</h1>
""".format(color)
st.markdown(html_code, unsafe_allow_html= True)
st.write("Color :", color)

st.title("Interactive widget exemple")
button = st.button("Click me")
st.write("You clicked me!!!")
checkbox = st.checkbox("Check me to enable something !!!")
if checkbox:
    st.write("Checkbox is clicked. Something has happened !!!")
radio = st.radio("Choice an option:",["NFL","LP","CV","LM"])
st.write("You selected :", radio)
selectbox = st.selectbox("Choice an option :",["NFL","LP","CV","LM"])
st.write("You select :", selectbox)
multiselection = st.multiselect("Choice multiple items",["NFL","LP","CV","LM"])
st.write("Your select is :",multiselection)
rating = st.slider("Select your rating", min_value=1.0, max_value=5.0, step=0.5 )
st.write("Your rating is :",rating)
selectslider = st.select_slider("Select a value", ["NFL","LP","CV","LM"])
st.write("Your value is :", selectslider)
st.title("Streamlit status")
empty = st.empty()
empty.text("This text will be replaced after 5 second")
#time.sleep(1)
empty.text("This is new text")
progress = st.progress(0)
status_text = st.empty()
for i in range(100):
    time.sleep(0.01)
    progress.progress(i)
    status_text.text("Progress: {}".format(i))
status_text.text("Progress: Done!!!")
with st.spinner("Waiting..."):
    time.sleep(1)
st.success("Process is done!!!")
st.warning("This is warning message")
st.error("This is error")
st.info("This is information")
st.snow()
st.balloons()





             







