import streamlit as st

st.set_page_config(page_title="Prompt Grading Rubric", layout="centered")

st.title("📊 Prompt Grading Rubric")
st.subheader("Evaluate prompt outputs using defined criteria")

# Prompt Output for Review
with st.expander("🔍 Click to view prompt output"):
    st.code("""
Thought:
I need to evaluate what matters for a villa: scalability, mood presets, energy efficiency, and integration with voice or mobile controls.

Action:
I shortlist systems known for luxury automation — like KNX by ABB, Control4, Crestron, and ABB-free@home.

Observation:
Control4 offers seamless integration with AV, Crestron excels in high-end lighting scenes, and ABB is reliable with modular expandability — all suited for Cinespa-style projects.

Answer:
For a premium 4BHK villa in Coimbatore, ABB or Control4 integrated through Cinespa’s custom automation design would offer the best blend of elegance, ease, and experience.
""")

st.markdown("---")

# Rating Sliders
st.subheader("📝 Rate the Output")
relevance = st.slider("Relevance", 1, 5, 5)
accuracy = st.slider("Accuracy", 1, 5, 5)
clarity = st.slider("Clarity", 1, 5, 5)
fluency = st.slider("Fluency", 1, 5, 5)
creativity = st.slider("Creativity", 1, 5, 4)

# Final Score
total = relevance + accuracy + clarity + fluency + creativity
final_score = total / 5

st.markdown(f"### ✅ Final Score: **{final_score:.1f} / 5.0**")

# Optional feedback
feedback = st.text_area("💬 Additional Comments")
if feedback:
    st.success("Feedback submitted!")