import streamlit as st
import random

st.title('Random Number Generator')
st.subheader('Get a random number between 1 and 4')

if st.button('Generate'):
    number = random.randint(1, 4)
    st.write(f'The generated number is: {number}')
