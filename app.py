# -*- coding:utf-8 -*-
"""
:Date: 2023-02-18 23:39:47
:LastEditTime: 2023-02-18 23:44:52
:Description: 
"""
import streamlit as st

import src.pages.home
import src.pages.resources
import src.pages.data_analysis
import src.pages.model_analysis
import PIL
import streamlit as st
from streamlit_option_menu import option_menu

# Page Favicon
favicon = PIL.Image.open('src/assets/favicon.png')
st.set_page_config(page_title='MtBuller', page_icon=favicon, layout='wide', initial_sidebar_state='auto')
def main():

    apps = [
        {"func": src.pages.home, "title": "Home", "icon": "house"},
        {"func": src.pages.resources, "title": "Resources", "icon": "book"},
        {"func": src.pages.data_analysis, "title": "Data Analysis", "icon": "bar-chart-line"},
        {"func": src.pages.model_analysis, "title": "Model Analysis", "icon": "pie-chart"},
    ]

    titles = [app["title"] for app in apps]
    titles_lower = [title.lower() for title in titles]
    icons = [app["icon"] for app in apps]

    params = st.experimental_get_query_params()

    if "page" in params:
        default_index = int(titles_lower.index(params["page"][0].lower()))
    else:
        default_index = 0

    with st.sidebar:
        selected = option_menu(
            "Main Menu",
            options=titles,
            icons=icons,
            menu_icon="cast",
            default_index=default_index,
            # styles={
            # "container": {"padding": "5!important", "background-color": "#fafafa"},
            # "icon": {"color": "orange", "font-size": "25px"}, 
            # "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            # "nav-link-selected": {"background-color": "#24A608"}
            # }
        )

    st.sidebar.title("About")
    st.sidebar.info(
        """
        This web [app](https://share.streamlit.io/giswqs/streamlit-template) is maintained by [MtBuler](https://github.com/cyclopes2022). You can follow me on social media:
            [GitHub](https://github.com/cyclopes2022).
        
        Source code: <https://github.com/cyclopes2022/MtBuller>
        """
        )

    for app in apps:
        if app["title"] == selected:
            app["func"].write()
            break

if __name__ == '__main__':
    main()