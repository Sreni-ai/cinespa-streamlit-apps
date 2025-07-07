import streamlit as st

st.set_page_config(page_title="Guest Preference", page_icon="📝", layout="centered")

st.title("📝 Guest Preference")

# Name input
name = st.text_input("Name")

# Beverage Selection
beverage = st.selectbox("Beverage Choice", ["None", "Coffee", "Tea"])

beverage_type = ""
beverage_sugar = ""
juice = "None"
juice_sugar = ""

# Beverage sub-options
if beverage == "Coffee":
    beverage_type = st.selectbox("Coffee Type", ["Black Coffee", "Milk Coffee"])
    beverage_sugar = st.radio("Sugar in Coffee?", ["With Sugar", "Without Sugar"])

elif beverage == "Tea":
    beverage_type = st.selectbox("Tea Type", ["Black Tea", "Milk Tea", "Masala Tea"])
    beverage_sugar = st.radio("Sugar in Tea?", ["With Sugar", "Without Sugar"])

# Juice options shown only if beverage is "None"
if beverage == "None":
    juice = st.selectbox("Juice Choice", ["None", "Lemon", "Pomegranate", "Watermelon"])
    juice_sugar = st.radio("Sugar in Juice?", ["With Sugar", "Without Sugar"])

# Snacks selection
snack = st.selectbox("Preferred Snack", ["None", "Samosa", "Grilled Sandwich"])

# Submit Button
if st.button("Submit"):
    st.success("✅ Preference Recorded!")

    st.markdown("### 🧾 Guest Summary:")
    st.markdown(f"- **Name:** {name if name else 'Not Provided'}")

    if beverage != "None":
        st.markdown(f"- **Beverage:** {beverage} ({beverage_type}, {beverage_sugar})")
    else:
        st.markdown(f"- **Juice:** {juice} ({juice_sugar})")

    st.markdown(f"- **Snack:** {snack}")