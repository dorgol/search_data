import os
import uuid

import streamlit as st
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]


def indexing(split=False, **kwargs):
    # Load and process the text files
    loader = DirectoryLoader('queries/', glob="./*.txt", loader_cls=TextLoader)
    documents = loader.load()

    if split:
        # splitting the text into
        # chunk_size = 1000, chunk_overlap = 200
        text_splitter = RecursiveCharacterTextSplitter(**kwargs)
        documents = text_splitter.split_documents(documents)

    # Embed and store the texts
    # Supplying a persist_directory will store the embeddings on disk
    persist_directory = 'db'

    embedding = OpenAIEmbeddings(openai_api_key=os.environ['OPENAI_API_KEY'],
                                 openai_organization=os.environ['OPENAI_ORGANIZATION'])

    vectordb = Chroma.from_documents(documents=documents,
                                     embedding=embedding,
                                     persist_directory=persist_directory)

    # persist the db to disk
    vectordb.persist()


def load_db():
    persist_directory = 'db'
    embedding = OpenAIEmbeddings(openai_api_key=os.environ['OPENAI_API_KEY'],
                                 openai_organization=os.environ['OPENAI_ORGANIZATION'])
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)
    return vectordb


def get_db_ids(db):
    ids = db._collection.get()['ids']
    return ids


def add_item_to_db(db, documents):
    ids = [str(uuid.uuid1()) for _ in documents]
    db._collection.add(
        documents=documents,
        ids=ids
    )


def delete_document(db, document_ids):
    db._collection.delete(ids=document_ids)


if __name__ == '__main__':
    indexing(split=True, chunk_size=2000, chunk_overlap=400)
