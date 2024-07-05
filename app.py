import asyncio
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

def get_pdf_text(pdf_file):
    text = ""
    pdf_reader = PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    prompt_template = """
    In dental medicine, provide detailed answers to the following questions:

    Context:
    {context}?

    Question:
    {question}

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain()
    try:
        response = chain.invoke({"input_documents": docs, "question": user_question}, return_only_outputs=True)
        st.write("Reply: ", response["output_text"])
    except genai.types.StopCandidateException as e:
        st.error(f"Generation process stopped: {e}")

async def main_async():
    st.set_page_config("VA FOR DENTAL")
    st.header("GEN AI BASED VA FOR DENTAL SCIENCES")

    # Process single PDF file named 'pdfs.pdf' from the current directory
    pdf_file = 'pdfs.pdf'

    with st.spinner("Getting ready"):
        raw_text = get_pdf_text(pdf_file)
        text_chunks = get_text_chunks(raw_text)
        get_vector_store(text_chunks)
        st.success("Start asking questions")

    st.subheader("FAQ Queries:")
    faq_queries = [
        "How often should I visit the dentist?",
        "How to do the self-examination for oral cancer?",
        "What is the difference between plaque and tartar?",
        "How can I prevent cavities?",
        "What are the symptoms of gum disease?"
    ]
    for query in faq_queries:
        if st.button(query):
            user_input(query)

    st.subheader("Ask Me:")

    user_question = st.text_input("Ask a question")
    if user_question:
        user_input(user_question)

def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main_async())

if __name__ == "__main__":
    main()
