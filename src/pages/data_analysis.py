# -*- coding:utf-8 -*-
"""
:Date: 2023-02-18 23:58:23
:LastEditTime: 2023-02-19 14:01:40
:Description: 
"""
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
import PIL
import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objects as go
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from sklearn.model_selection import train_test_split


def pandas_profiling_report(df):
    df_report = ProfileReport(df, explorative=True)
    return df_report


def write():
    # Global Variables
    theme_plotly = None # None or streamlit

    # Layout
    # st.title('Data Exploratory Analysis')
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Data Exploratory Analysis</p>', unsafe_allow_html=True)

    # Data Sources
    
    font_css = """
    <style>
    button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
    font-size: 22px;
    }
    </style>
    """

    st.write(font_css, unsafe_allow_html=True)

    # tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
    # Content
    tab_overview, tab_opendata, tab_mydata = st.tabs(['Overview', 'OpenSourceDataset', 'MyDataset'])

    with tab_overview:
        st.subheader('Overview') 

    with tab_opendata:
        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')
        df_report = pandas_profiling_report(df)
        st_profile_report(df_report)
        # train_df, test_df = train_test_split(df, train_size=0.8)

        # report = sweetviz.compare(source=train_df, compare=test_df, target_feat="Progression")
        # report.show_html()



    with tab_mydata:
        # Upload CSV data
        st.header('1. Upload your CSV data')
        uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
        st.markdown("""
        [Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
        """)

        # Pandas Profiling Report
        if uploaded_file is not None:
            @st.cache
            def load_csv():
                csv = pd.read_csv(uploaded_file)
                return csv
            df = load_csv()
            pr = ProfileReport(df, explorative=True)
            st.header('**Input DataFrame**')
            st.write(df)
            st.write('---')
            st.header('**Pandas Profiling Report**')
            st_profile_report(pr)
        else:
            st.info('Awaiting for CSV file to be uploaded.')
            if st.button('Press to use Example Dataset'):
                # Example data
                @st.cache
                def load_data():
                    a = pd.DataFrame(
                        np.random.rand(100, 5),
                        columns=['a', 'b', 'c', 'd', 'e']
                    )
                    return a
                df = load_data()
                pr = ProfileReport(df, explorative=True)
                st.header('**Input DataFrame**')
                st.write(df)
                st.write('---')
                st.header('**Pandas Profiling Report**')
                st_profile_report(pr)