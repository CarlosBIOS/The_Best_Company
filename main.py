import streamlit as st
import pandas

data: dict = pandas.read_csv('data.csv').to_dict()
print(data)

st.set_page_config(layout='wide')

st.title('The Best Company')
st.write('oioipoio')
st.subheader('Our Team')

col1, _, col2, _, col3 = st.columns([2, 0.5, 2, 0.5, 2])

with col1:
    for index in range(4):
        st.header(data['first name'][index].title() + ' ' + data['last name'][index].title())
        st.write(data['role'][index])
        st.image(f'images/{data['image'][index]}')

with col2:
    for index in range(4, 8):
        st.header(data['first name'][index].title() + ' ' + data['last name'][index].title())
        st.write(data['role'][index])
        st.image(f'images/{data['image'][index]}')

with col3:
    for index in range(8, 12):
        st.header(data['first name'][index].title() + ' ' + data['last name'][index].title())
        st.write(data['role'][index])
        st.image(f'images/{data['image'][index]}')
