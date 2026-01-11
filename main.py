import gradio as gr
from app.ui import create_ui

if __name__ == "__main__":
    demo = create_ui()
    demo.launch(share=True, theme=gr.themes.Soft())
