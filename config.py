import os
import streamlit as st
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"
os.environ['REDASH_URL'] = 'https://redash.lightricks.com/queries'
model_name = 'gpt-3.5-turbo-0613'
os.environ['OPENAI_API_KEY'] = st.secrets["OPENAI_API_KEY"]