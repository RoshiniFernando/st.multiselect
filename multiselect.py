# Importing Streamlit
import streamlit as st

# Header text
st.header('st.multiselect')

# Description
st.write('''_Displays a multiselect widget._''')

# Creating multiple selection box
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

# Display selected options
st.write('You selected:', options)