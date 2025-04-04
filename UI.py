import gradio as gr
import OllamaDeepSeek


def test_method(name):
    print(f"Name Received is {name}")
    return name



interface1 = gr.Interface(
   fn=OllamaDeepSeek.call_deepseek,
   inputs=gr.Textbox(label="Ask a question"),
   outputs=gr.Text(label="Result"),
   title="SAT RAG AI Testing Interface",
   description="Interface to communicate with Model: DeepSeek",
)

interface2 = gr.Interface(
   fn=OllamaDeepSeek.describe_image,
   inputs= [
      gr.Textbox(label="Name/Path of the image file"),
      gr.Textbox(label="Question you want to ask about the image")
   ],
   outputs=gr.Text(label="Result"),
   title="SAT RAG AI Testing Interface",
   description="Interface to communicate with Model: DeepSeek",
)

#interface1.launch(server_port=8000)
interface2.launch(server_port=8001)