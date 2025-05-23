# AI RAG Assistant for Scientific Document Summarization

This project builds a Retrieval-Augmented Generation (RAG) AI assistant designed to support research professionals by automatically summarizing scientific documents and answering user queries in real-time using IBM Watson’s LLM and LangChain.

## Installation

### Prerequisites
- Install [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

### Setup

1. Create the Conda environment:
"""conda env create -f environment.yml"""
2. Activate the environment:
"""conda activate rag"""
3. Test the setup by running: 
"""python qa_boot.py"""

### IBM API Setup

To use IBM's foundation models, you’ll need to generate your own API key.

1. Create an IBM Cloud account (e.g., via the Coursera course *Introduction to Cloud Computing* by IBM, Module 2).  
2. Go to [IBM Cloud](https://cloud.ibm.com), navigate to **IBM watsonx**, and create a project.  
3. Inside your project:
   - Store your **project ID**
   - Create an **API key**
   - Navigate to **Manage > Services & Integrations**
   - Add **Watson Machine Learning**

## Notes
Youcan find the project instructions in the docs folder.


# rag_application
First RAG application with coursera IBM

## Installation
You will first need to install Conda or Anaconda.
Then please run in your terminal at the root of the project **conda env create -f environment.yml**. Then select it as your python environment. You can test if it was successfully installed by executing the file **gradio_demo.py**.

After that, to be able to use the IBM's models contained in the project, you will have to create our own [API key](https://cloud.ibm.com/docs/account?topic=account-userapikey&interface=ui).
1. access to a code to create your IBM account : the coursera course "Introduction to Cloud Computing" created by IBM, module 2, Optional : create you IBM account helps you to do that
2. from the ibm cloud page, go to the IBM watsonX, create a project, store the ID, then click on this project, create an API key, store it, then go to manage/Services & Integration, then add WatsonMachineLearning, and then you are good to go

