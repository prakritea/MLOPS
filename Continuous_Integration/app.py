import streamlit as st

#streamlit UI
st.title("Power Calculator")
st.write("enter a number to calculate its square, cube, and fifth power.")

#get user input
n = st.number_input("enter an integer: ", value=1, step=1)

#calculate results
square = n ** 2
cube = n ** 3
fifth_power = n ** 5

#display results
st.write(f"the square of {n} is: {square}")
st.write(f"the cube of {n} is: {cube}")
st.write(f"the fifth power of {n} is: {fifth_power}")