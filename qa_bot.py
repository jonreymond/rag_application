from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.metanames import EmbedTextParamsMetaNames
from ibm_watsonx_ai import Credentials, APIClient
from langchain_ibm import WatsonxLLM, WatsonxEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter, LatexTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.chains import RetrievalQA
import gradio as gr
import json
import pathlib

from enum import Enum


import hydra
from hydra.utils import get_original_cwd, to_absolute_path, instantiate, get_method

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')




def getCredentials(credential_path):
    with open(credential_path) as f:
        cred = json.load(f)

    credentials = Credentials(
                    url = cred['url'],
                    api_key=cred['api_key']
                    )
    project_id = cred['project_id']
    return APIClient(credentials), project_id



# QA Chain
def retriever_qa(file, query, splitter, embedding_model, llm):
    # Document Load and Split
    print(file)
    splits = PyPDFLoader(file).load()

    chunks = splitter.split_documents(splits)

    # Vector database
    vectordb = Chroma.from_documents(chunks, embedding_model)
    retriever = vectordb.as_retriever()

    # qa bot
    qa = RetrievalQA.from_chain_type(llm=llm, 
                                    chain_type="stuff", 
                                    retriever=retriever, 
                                    return_source_documents=False)
    response = qa.invoke(query)
    return file + "   " + response['result']


class Task(Enum):
    display_raw = "Display raw document content"
    display_splits_latex = "Display document latex splits"
    display_embedding = "Display embeddings"
    similarity_search = "Similarity search"
    retriever = "Retriever"
    QA_bot = "QA bot"



def fetcher(file, query:str, splitter, task:Task, embedding_model:WatsonxEmbeddings, llm:WatsonxLLM):
    if task == Task.display_embedding:
        return embedding_model.embed_query(query)[:5]
        
    
    suffix = pathlib.Path(file).suffix
    if suffix == ".pdf":
        splits = PyPDFLoader(file).load()

    elif suffix == ".txt":
        splits = TextLoader(file).load()
        
    else:
        raise ValueError("Unsupported file type. Please upload a .pdf or .txt file.")
    
    if task == Task.display_raw:
        res = ""
        for doc in splits:
            res += doc.page_content
            if len(res) > 1000:
                break
        return res[:1000]
    
    if task == Task.display_splits_latex:
        latex_text = ""
        for doc in splits:
            latex_text += doc.page_content
        return LatexTextSplitter(chunk_size=100, chunk_overlap=20).split_text(latex_text)
    
    chunks = splitter.split_documents(splits)
    vectordb = Chroma.from_documents(chunks, embedding_model)
    if task == Task.similarity_search:
        res = vectordb.similarity_search(query, k=5)
        return [entry_res.page_content for entry_res in res]
    
    retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 2})
    if task == Task.retriever:
        return [entry_res.page_content for entry_res in retriever.invoke(query)]
    
    if task == Task.QA_bot:
        
        qa = RetrievalQA.from_chain_type(llm=llm, 
                                        chain_type="stuff", 
                                        retriever=retriever, 
                                        return_source_documents=False)
        response = qa.invoke(query)
        return response['result']
    
    else:
        return 
        




@hydra.main(version_base=None, config_path="configs", config_name="qa_bot_config")
def main(config):
    #API client and project id linked to Watsonx account
    api_client, project_id = getCredentials(config['credential_path'])

    # LLM
    llm = WatsonxLLM(
            project_id = project_id,
            model_id = config['llm']['model_id'],
            watsonx_client = api_client,
            params = {
                GenParams.MAX_NEW_TOKENS: config['llm']['MAX_NEW_TOKENS'],
                GenParams.TEMPERATURE: config['llm']['TEMPERATURE']}
    )
    
    # Embedding
    embedding_model = WatsonxEmbeddings(
        project_id=project_id,
        model_id=config['embed']['model_id'],
        watsonx_client=api_client,
        params={
        EmbedTextParamsMetaNames.TRUNCATE_INPUT_TOKENS: config['embed']['TRUNCATE_INPUT_TOKENS'],
        EmbedTextParamsMetaNames.RETURN_OPTIONS: dict(config['embed']['RETURN_OPTIONS'])
        }
    )

    # Text splitter
    splitter = instantiate(config["splitter"])

     

    fn = lambda file, query: retriever_qa(file, query, splitter, embedding_model, llm)

    # Create Gradio interface
    rag_application = gr.Interface(
        fn=fn,
        allow_flagging="never",
        inputs=[
            gr.File(label="Upload PDF File", file_count="single", file_types=['.pdf'], type="filepath"), 
            gr.Textbox(label="Input Query", lines=2, placeholder="Type your question here...")
        ],
        outputs=gr.Textbox(label="Output"),
        title=config['gradio']['title'],
        description=config['gradio']['description']
    )
    # Launch the app
    rag_application.launch(server_name=config['gradio']['server_name'], server_port=config['gradio']['server_port'])




if __name__ == "__main__":
    main()
    print('done')