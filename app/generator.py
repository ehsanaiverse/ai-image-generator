from app.model import client

def generate_image(prompt):
    """Generate image from text prompt"""
    try:
        if not prompt or prompt.strip() == "":
            return None, "Please enter a prompt"
        
        image = client.text_to_image(prompt)
        return image, f"✅ Image generated successfully for: '{prompt}'"
    
    except Exception as e:
        return None, f"❌ Error: {str(e)}"