import pickle
import streamlit as st
from pandas import DataFrame

cache_path = 'pickled_file_path'  # file_path from page_parser script 

st.sidebar.header("Chanels")
endpoint_choices = ['Chanel1',]
endpoint = st.sidebar.selectbox("Choose a Chanel", endpoint_choices)

st.title(f"Videos Explorer")

if endpoint == 'Chanel1':
    with open(cache_path, 'rb') as f:
        raw_videos = f.read()
        videos = pickle.loads(raw_videos)
    videos_df = DataFrame(videos)
    st.dataframe(
        data=videos_df.transpose(),
    )