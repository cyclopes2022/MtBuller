# -*- coding:utf-8 -*-
"""
:Date: 2023-02-18 23:49:03
:LastEditTime: 2023-02-18 23:49:37
:Description: 
"""
import pandas as pd
import streamlit as st

def write():
    # st.markdown(""" <style> .font {
    # font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    # </style> """, unsafe_allow_html=True)
    # st.markdown('<p class="font">Learn Python for Data Science</p>', unsafe_allow_html=True)

    st.subheader('Import Data into Python')
    st.markdown('To start a data science project in Python, you will need to first import your data into a Pandas data frame. Often times we have our raw data stored in a local folder in csv format. Therefore let\'s learn how to use Pandas\' read_csv method to read our sample data into Python.')

    #Display the first code snippet
    code = '''import pandas as pd #import the pandas library\ndf=pd.read_csv(r'C:\\Users\\13525\\Desktop\\ecourse_app\\ecourse_streamlit\\data.csv') #read the csv file into pandas\ndf.head() #display the first 5 rows of the data'''
    st.code(code, language='python')

    #Allow users to check the results of the first code snippet by clicking the 'Check Results' button
    df=pd.read_csv(r'src/data/test_data.csv')
    df_head=df.head()
    if st.button('Check Results', key='1'):
        st.write(df_head)
    else:
        st.write('---')

    #Display the second code snippet
    code = '''df.tail() #display the last 5 rows of the data'''
    st.code(code, language='python')

    #Allow users to check the results of the second code snippet by clicking the 'Check Results' button
    df=pd.read_csv(r'src/data/test_data.csv')
    df_tail=df.tail()
    if st.button('Check Results', key='2'):
        st.write(df_tail)
    else:
        st.write('---')     

    #Display the third code snippet
    st.write('   ')
    st.markdown('After we import the data into Python, we can use the following code to check the information about the data frame, such as number of rows and columns, data types for each column, etc.')
    code = '''df.info()''' 
    st.code(code, language='python')

    #Allow users to check the results of the third code snippet by clicking the 'Check Results' button
    import io 
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    if st.button('Check Results', key='3'):
        st.text(s)
    else:
        st.write('---')
    #     )