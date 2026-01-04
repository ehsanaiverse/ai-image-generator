import gradio as gr
from app.generator import generate_image


def create_ui():
    with gr.Blocks(theme=gr.themes.Soft()) as demo:
        gr.Markdown("# Ehsan AI Image Generator")
        gr.Markdown("Generate images from text using Stable Diffusion XL")
        
        with gr.Row():
            with gr.Column(scale=1):
                prompt_input = gr.Textbox(
                    label="Enter your prompt",
                    placeholder="A serene mountain landscape at sunset...",
                    lines=3
                )
                
                generate_btn = gr.Button("Generate Image", variant="primary", size="lg")
                
                gr.Markdown("### Example Prompts")
                gr.Examples(
                    examples=[
                        ["A majestic lion made of colorful origami paper, studio lighting"],
                        ["Futuristic cyberpunk city at night, neon lights, rain"],
                        ["A peaceful Japanese garden with cherry blossoms and koi pond"],
                        ["An astronaut floating in space, Earth in background, realistic"],
                        ["A cozy coffee shop interior, warm lighting, plants by window"]
                    ],
                    inputs=prompt_input
                )
            
            with gr.Column(scale=1):
                output_image = gr.Image(label="Generated Image", type="pil")
                status_text = gr.Textbox(label="Status", lines=2)
        
        generate_btn.click(
            fn=generate_image,
            inputs=prompt_input,
            outputs=[output_image, status_text]
        )
    
    return demo
