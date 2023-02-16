"""Home page shown when the user enters the application"""
import streamlit as st


def write():
    st.write("# Welcome to Lucas analysis! 👋")
    st.sidebar.success("Select a demo above.")
    st.write(
        """        
        This is an app built specifically for Machine Learning and Data Science projects with streamlit.
        
        **👈 Select a demo from the sidebar** to see  what we can do!

        ### See how to use this app
        - Instructions [click here](https://iron-sheet-c6a.notion.site/App-8c6daa98ec984341ad54872cd5153fb2)
        
        ### Want to learn more about streamlit?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
            forums](https://discuss.streamlit.io)
        
        """
    )
    # st.shared.components.video_youtube(
    #         src="https://www.youtube.com/embed/B2iAodr0fOo"
    #     )
