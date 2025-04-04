import gradio as gr
def add_numbers(Num1, Num2):
    return Num1 + Num2

def concat(str_1, str_2):
    return str_1 + str_2
# Define the interface
demo = gr.Interface(
    fn=add_numbers, 
    inputs=[gr.Textbox(), gr.Textbox()], 
    outputs=gr.Textbox() 
)
# Launch the interface
demo.launch(server_name="127.0.0.1", server_port= 7860)