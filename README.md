# rag_application
First RAG application with coursera IBM

## Installation
You will first need to install Conda or Anaconda.
Then please run in your terminal at the root of the project **conda env create -f environment.yml**. Then select it as your python environment. You can test if it was successfully installed by executing the file **gradio_demo.py**.

After that, to be able to use the IBM's models contained in the project, you will have to create our own [API key](https://cloud.ibm.com/docs/account?topic=account-userapikey&interface=ui).
1. access to a code to create your IBM account : the coursera course "Introduction to Cloud Computing" created by IBM, module 2, Optional : create you IBM account helps you to do that
2. from the ibm cloud page, go to the IBM watsonX, create a project, store the ID, then click on this project, create an API key, store it, then go to manage/Services & Integration, then add WatsonMachineLearning, and then you are good to go
