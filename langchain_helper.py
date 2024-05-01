from langchain_google_genai import GoogleGenerativeAI
from langchain.document_loaders.csv_loader import CSVLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA


API_KEY = "YOUR_API_KEY"
DB_PATH = "faiss_index"


llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=API_KEY, temperature=0.7)
embedding = HuggingFaceEmbeddings()


def create_vector_db():
    loader = CSVLoader(file_path='faqs.csv', source_column='prompt')
    data = loader.load()
    vectordb = FAISS.from_documents(documents=data, embedding=embedding)
    vectordb.save_local(DB_PATH)
    

def get_qa_chain():
    vectordb = FAISS.load_local(DB_PATH, embedding, allow_dangerous_deserialization=True)
    retriever = vectordb.as_retriever()
    
    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.
    
    CONTEXT: {context}
    
    QUESTION: {question}"""
    
    PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain_type_kwargs = {"prompt": PROMPT}
    
    chain = RetrievalQA.from_chain_type(llm=llm, 
                                        chain_type="stuff", 
                                        retriever=retriever, 
                                        input_key="query", 
                                        return_source_documents=True, 
                                        chain_type_kwargs=chain_type_kwargs)
    
    return chain

if __name__ == "__main__":
    create_vector_db()