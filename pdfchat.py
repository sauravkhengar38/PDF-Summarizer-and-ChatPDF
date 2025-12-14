import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback

api_key = ""  # your API key

def main():
    st.set_page_config(page_title="PDF Summarizer")
    st.header("PDF Summarizer")

    pdf = st.file_uploader("Upload PDF file here", type="pdf")

    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        
        for page in pdf_reader.pages:
            text += page.extract_text()

        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len             
        )

        chunks = text_splitter.split_text(text)

        embeddings = OpenAIEmbeddings(
            openai_api_key=api_key,
            openai_api_base="https://openrouter.ai/api/v1"
        )

        knowledge_base = FAISS.from_texts(chunks, embeddings)
        user_question = st.text_input("Ask Question to uploaded PDF!")

        if user_question:
            docs = knowledge_base.similarity_search(user_question)

            llm = ChatOpenAI(
                openai_api_key=api_key,
                openai_api_base="https://openrouter.ai/api/v1",
                model_name="gpt-4o-mini"  # ✅ must be model_name
            )

            chain = load_qa_chain(llm, chain_type="stuff")

            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=user_question)
                print(cb)

            st.write(response)

main()
