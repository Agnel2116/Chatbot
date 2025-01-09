import os
from decouple import config

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.huggingface import HuggingFaceEmbeddings

os.environ['HUGGINGFACE_API_KEY'] = config('HUGGINGFACE_API_KEY')

if __name__ == '__main__':
    file_path = '/app/rag/dados/Eu.pdf' # O caminho do arquivo PDF que será carregado

    loader = PyPDFLoader(file_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    chunks = text_splitter.split_documents(docs)

    persist_directory = '/app/chorma_data'

    embedding = HuggingFaceEmbeddings()
    vector_store = Chroma(
        embedding_function=embedding,
        persist_directory=persist_directory,
    )

    vector_store.add_documents(chunks)