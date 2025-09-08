import pandas as pd
from streamlit_modal import Modal
import streamlit as st

# with open('styles.css') as f:
#     css = f.read()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles.css")

# Inject the Font Awesome CSS
st.markdown("""
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap">
""", unsafe_allow_html=True)


with st.popover("..."):
    with st.container(key="popover-container"):
        rename_open_modal = st.button("Rename", key="rename-button")
        delete_open_modal = st.button("Delete", key="delete-button")

# Rename Modal
renameModal = Modal("Rename Topic", key="rename-modal")
if rename_open_modal:
    renameModal.open()
if renameModal.is_open():
    with renameModal.container():
        with st.container(key="rename-modal-content"):
            st.write("Are you sure you want to rename this topic?")
        with st.container(key="rename-modal-buttons"):
            if st.button("Cancel", key="rename-cancel-button"):
                renameModal.close()
            if st.button("Save", key="rename-save-button"):
                renameModal.close()

# Delete Modal
deleteModal = Modal("Confirmation", key="delete-modal")
if delete_open_modal:
    deleteModal.open()
if deleteModal.is_open():
    with deleteModal.container():
        with st.container(key="delete-modal-content"):
            st.write("Are you sure you want to delete this topic?")
        with st.container(key="delete-modal-buttons"):
            if st.button("Cancel", key="delete-cancel-button"):
                deleteModal.close()
            if st.button("Confirm", key="delete-confirm-button"):
                deleteModal.close()

