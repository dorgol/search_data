import sys

from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.chat_models import ChatOpenAI

from context import QUESTION_PROMPT, COMBINE_PROMPT

sys.path.append('../search_data')

from config import model_name


def create_condition(operator, *conditions):
    """
    Create a dictionary with conditions based on the specified operator.

    Args:
        operator (str): The logical operator ('$or' or '$and').
        *conditions: Variable number of condition dictionaries.

    Returns:
        dict: The generated condition dictionary.
    """
    return {operator: list(conditions)}


def create_contains_condition(field, value):
    """
    Create a dictionary with a '$contains' condition.

    Args:
        field (str): The field name to check for containment.
        value (str): The value to search for.

    Returns:
        dict: The generated contains condition dictionary.
    """
    return {"$contains": f"{field}: {value}"}


# def filter_db(db, query_text, conditions):
#     """
#     Filter the ChromaDB based on the specified conditions.
#
#     Args:
#         db: The ChromaDB object.
#         query_text (str): The query text to search for.
#         conditions (list): List of condition dictionaries.
#
#     Returns:
#         ChromaDB: Filtered ChromaDB object containing the filtered results.
#     """
#     where_document = create_condition("$or", *conditions)
#     filtered_results = db._collection.query(query_texts=query_text, where_document=where_document)
#     filtered_db = ChromaDB(filtered_results)
#     return filtered_db


def get_relevant(db, filter_input):
    retriever = db.as_retriever(search_kwargs={"k": 5})
    docs = retriever.get_relevant_documents(filter_input)
    return retriever, docs


def summary_query(docs, question):
    llm = ChatOpenAI(model_name=model_name, temperature=0.5)
    summary_chain = load_qa_with_sources_chain(llm=llm, chain_type="map_reduce", return_intermediate_steps=True,
                                               question_prompt=QUESTION_PROMPT, combine_prompt=COMBINE_PROMPT)
    summary_response = summary_chain({"input_documents": docs, "question": question}, return_only_outputs=False)
    return summary_response


def get_response(chain, question):
    llm_response = chain(question)
    return llm_response
