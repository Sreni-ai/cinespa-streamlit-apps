import streamlit as st

# Page Title
st.title("🔢 Fibonacci Number Generator")

# Input from user
n = st.number_input("Enter a number (n) to get the nth Fibonacci number:", min_value=0, value=5, step=1)

# Function to calculate Fibonacci
@st.cache_data
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b

# Calculate and display
if st.button("Generate"):
    result = fibonacci(n)
    st.success(f"The {n}th Fibonacci number is: {result}")