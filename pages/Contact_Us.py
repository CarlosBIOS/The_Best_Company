import streamlit as st
from send_emails import send_emails

st.header('Contact Me')

with st.form(key='email_forms'):
    user_email = st.text_input('Your email Address')
    discust = st.selectbox('What topic do you want to discuss?', ['Job Inquires', 'Project Proposals', 'Other'],
                           index=0)
    user_message = st.text_area('Text')
    button = st.form_submit_button('Submit')
    if button:
        message = f"""\
Subject: Email from the Portfolio Website 
        

From: {user_email}
Topic: {discust}
{user_message}
"""
        send_emails(message.encode('utf-8'))
        st.info('Your email was succefully send it')
