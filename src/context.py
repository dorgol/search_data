from langchain.prompts import PromptTemplate


question_prompt_template = """Use the following portion of a long document to see if any of the text is relevant to 
answer the question. 
Explain what this query doing
{context}
Question: Where can I find data about {question}
"""

QUESTION_PROMPT = PromptTemplate(
    template=question_prompt_template, input_variables=["context", "question"]
)


combine_prompt_template = """
You are an expert in SQL.
Given the following extracted parts of a long document and a question, create a final 
answer with references ("SOURCES"). 
If you don't know the answer, just say that you don't know. Don't try to make up an answer.
ALWAYS return a "SOURCES" part in your answer.
if you answer with a query number put it in the following format: "https://redash.lightricks.com/queries/ID".
The ID can be found at the beginning of every query
if you don't have a direct answer, but you have close answer say it and stress out that's it wasn't the exact answer.
Explain why did you choose this query.
If you see several relevant queries say it to the user.


QUESTION: Where can I find data about {question}
=========
{summaries}
=========
"""

COMBINE_PROMPT = PromptTemplate(
    template=combine_prompt_template, input_variables=["summaries", "question"]
)
