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
   - Create an [API key](https://cloud.ibm.com/docs/account?topic=account-userapikey&interface=ui)
   - Navigate to **Manage > Services & Integrations**
   - Add **Watson Machine Learning**

## Notes
You can find the project instructions in the docs folder.


