import streamlit as st
import langchain_helper

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine",('Indian','mexican','American','Taiwan','italian','French'))

if cuisine:
    response = langchain_helper.get_rest_name(cuisine)
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("--",item)

