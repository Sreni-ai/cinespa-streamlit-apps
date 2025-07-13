import streamlit as st

st.set_page_config(page_title="Home Automation Quiz by Cinespa")

st.title("🧠 Home Automation Quiz")
st.subheader("Presented by Luxury Home Automation by Cinespa")

score = 0

with st.form("quiz_form"):
    q1 = st.radio("1. What is the primary purpose of a home automation system?", 
                  ["Entertainment only", 
                   "Increase electricity bills", 
                   "Enhance comfort, convenience, and control", 
                   "Reduce internet speed"])

    q2 = st.radio("2. Which of the following is a commonly automated system in smart homes?", 
                  ["Wall paint", 
                   "Curtains", 
                   "Roofing", 
                   "Flooring"])

    q3 = st.radio("3. What type of network is most commonly used in wireless home automation?", 
                  ["LAN", 
                   "WAN", 
                   "Zigbee/Z-Wave", 
                   "HDMI"])

    q4 = st.radio("4. Which device typically acts as the 'brain' of a smart home system?", 
                  ["Wi-Fi router", 
                   "Smartphone", 
                   "Central Controller/Hub", 
                   "Bluetooth speaker"])

    q5 = st.radio("5. What is the benefit of geofencing in home automation?", 
                  ["Tracks internet usage", 
                   "Provides backup power", 
                   "Automates actions based on your location", 
                   "Increases manual work"])

    submitted = st.form_submit_button("Submit Answers")

if submitted:
    answers = [q1, q2, q3, q4, q5]
    correct_answers = [
        "Enhance comfort, convenience, and control",
        "Curtains",
        "Zigbee/Z-Wave",
        "Central Controller/Hub",
        "Automates actions based on your location"
    ]

    for i in range(5):
        if answers[i] == correct_answers[i]:
            score += 1

    st.markdown("---")
    st.success(f"✅ Your Score: {score} / 5")

    if score == 5:
        st.balloons()
        st.success("🎉 Excellent! You're a home automation pro!")
    elif score >= 3:
        st.info("👍 Good job! You're on your way to mastering smart homes.")
    else:
        st.warning("🤔 Keep learning! Visit Cinespa for an immersive experience.")