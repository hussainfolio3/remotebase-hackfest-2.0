import streamlit as st
st.set_page_config(page_title="View Previous Record", page_icon="👁️")
from PIL import Image
from datetime import datetime

from db import get_data, GET_SPECIFIC_ENTRY

if "logged_in_user" in st.session_state:

    body_part = st.selectbox(
        'Select Body Part',
        ('Face', 'Hands', 'Legs'))

    date = st.date_input("Date")
   
    date=date.strftime('%m-%d-%Y')
    
    # df = get_data(
    #     GET_SPECIFIC_ENTRY.format(
    #         body_part = body_part,
    #         patient_username = st.session_state["logged_in_user"],
    #         date = date
    #     )
    # )
    if st.button("Find"):
        st.image("res.jpeg")
else:
    st.header("Please Login!")


