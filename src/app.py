import os
import streamlit as st
from indexing import load_db
from generate import get_relevant, summary_query

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["OPENAI_ORGANIZATION"] = st.secrets["OPENAI_ORGANIZATION"]

user_input = st.text_input("I'm looking for data about",
                           "number of installations per period in Facetune2")

vectordb = load_db()
retriever, docs = get_relevant(vectordb, user_input)
st.write(vectordb.search("hello"))
response = summary_query(docs, user_input)

st.write(response['output_text'])
with st.expander("See sources"):
    st.write(response['input_documents'])

with st.expander("See explanations"):
    st.write(response['intermediate_steps'])
