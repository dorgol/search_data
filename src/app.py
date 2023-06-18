import streamlit as st
from indexing import load_db
from generate import get_relevant, summary_query, create_contains_condition

# filter_input = st.text_input("filter queries by this text (don't be too restrictive)", "installations in Facetune2")
user_input = st.text_input("I'm looking for data about",
                           "number of installations per period in Facetune2")

vectordb = load_db()
retriever, docs = get_relevant(vectordb, user_input)
response = summary_query(docs, user_input)

st.write(response['output_text'])
with st.expander("See sources"):
    st.write(response['input_documents'])

with st.expander("See explanations"):
    st.write(response['intermediate_steps'])