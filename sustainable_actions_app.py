import streamlit as st

st.set_page_config(page_title="🌍 Climate Change Awareness", layout="centered")

st.title("🌱 Multi-Step Research: Climate Change & Solutions")
st.subheader("Step 1: Top 5 Causes of Climate Change")

# Display causes
causes = [
    "1. Burning of fossil fuels (coal, oil, gas)",
    "2. Deforestation and land use changes",
    "3. Industrial emissions and factory waste",
    "4. Agricultural practices and livestock methane",
    "5. Transportation emissions (cars, airplanes, ships)"
]

for cause in causes:
    st.markdown(f"- {cause}")

st.divider()
st.subheader("Step 2: 5 Practical Solutions Individuals Can Adopt")

solutions = [
    "✅ Switch to renewable energy sources (e.g., solar, wind)",
    "✅ Use public transportation, cycle, or carpool",
    "✅ Adopt a plant-based or low-meat diet",
    "✅ Reduce, reuse, and recycle consistently",
    "✅ Support and plant more trees (reforestation)"
]

for sol in solutions:
    st.markdown(f"- {sol}")

# Optional quiz
st.divider()
st.subheader("🌍 Quick Quiz: Are You Climate Conscious?")
score = 0

with st.form("climate_quiz"):
    q1 = st.radio("Do you turn off lights when not in use?", ["Always", "Sometimes", "Never"])
    q2 = st.radio("Do you use public transport at least once a week?", ["Yes", "No"])
    q3 = st.radio("Do you recycle paper, plastic, and e-waste properly?", ["Yes", "No", "Rarely"])
    
    submitted = st.form_submit_button("Submit")

    if submitted:
        if q1 == "Always": score += 1
        if q2 == "Yes": score += 1
        if q3 == "Yes": score += 1

        st.markdown("---")
        st.write(f"### 🌟 Your Score: {score}/3")

        if score == 3:
            st.success("Fantastic! You're climate conscious. 🌍🌟")
        elif score == 2:
            st.info("Good job! But there’s room to do more 🌿")
        else:
            st.warning("Let’s start building better habits today. Every step counts!")

st.divider()
st.caption("Created with ❤️ using Streamlit | Cinespa Sustainability Prompts")