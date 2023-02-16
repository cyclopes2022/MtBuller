import streamlit as st
# from constants import *
# from data_check import data_check
# from mytsne import mytsne
# from shap_explain import shap_explain
# from lime_image import lime_image
# from mycam import mycam
import src.pages.home
# import src.pages.resources
# import src.pages.gallery.index
# import src.pages.vision
# import src.pages.about


st.set_page_config(
        page_title="MtBuller",
        # page_icon="⛰️",
    )

PAGES = {
    "Home": src.pages.home,
    # "Resources": src.pages.resources,
    # "Gallery": src.pages.gallery.index,
    # "Vision": src.pages.vision,
    # "About": src.pages.about,
}

def main():
    """Main function of the App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        page.write()
# demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
# page_names_to_funcs[demo_name]()

if __name__ == 'main':
    main()