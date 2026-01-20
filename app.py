import streamlit as st

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b

st.title("🧮 Simple Calculator Application")
st.write("Perform basic arithmetic operations using Python and Streamlit")

num1 = st.number_input("Enter First Number", value=0.0, format="%.2f")
num2 = st.number_input("Enter Second Number", value=0.0, format="%.2f")

operation = st.selectbox(
    "Select Operation",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

if st.button("Calculate"):
    if operation == "Addition":
        result = add(num1, num2)
    elif operation == "Subtraction":
        result = subtract(num1, num2)
    elif operation == "Multiplication":
        result = multiply(num1, num2)
    elif operation == "Division":
        result = divide(num1, num2)

    st.success(f"Result: {result}")
