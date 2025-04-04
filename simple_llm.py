from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai import Credentials
from langchain_ibm import WatsonxLLM
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

import json
import gradio as gr



with open('credentials.json') as f:
    cred = json.load(f)

credentials = Credentials(
                   url = cred['url'],
                   api_key=cred['api_key']
                  )

client = APIClient(credentials)



model_id = 'mistralai/mixtral-8x7b-instruct-v01'

parameters = {
    GenParams.MAX_NEW_TOKENS: 256,  # Specifying the max tokens you want to generate
    GenParams.TEMPERATURE: 0.5, # This randomness or creativity of the model's responses
}

llm = WatsonxLLM(
    project_id=cred['project_id'],
    model_id=model_id,
    watsonx_client=client,
    params=parameters,

   )


def generate_response(prompt):
    return llm.invoke(prompt)



chat_application = gr.Interface(
    fn=generate_response,
    allow_flagging="never",
    inputs=gr.Textbox(label="Input", lines=2, placeholder="Type your question here..."),
    outputs=gr.Textbox(label="Output"),
    title="Watsonx.ai Chatbot",
    description="Ask any question and the chatbot will try to answer."
)
# Launch the app
chat_application.launch(server_name="127.0.0.1", server_port= 7860)