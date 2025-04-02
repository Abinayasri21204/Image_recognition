import google.generativeai as genai
import gradio as gr
from PIL import Image

# Set up Gemini API key
genai.configure(api_key="AIzaSyBPgzQmLqhGsTHVo-6YvwCkQR-3BDO3RUs")  

def generate_caption(image):
    """Generate a caption for the uploaded image using Google Gemini Pro Vision API."""

    model = genai.GenerativeModel("gemini-1.5-flash")

    img = Image.open(image)

    response = model.generate_content(
        [img, "Describe the contents of this image in detail."]
    )
    
    caption = response.text
    return caption

iface = gr.Interface(
    fn=generate_caption,
    inputs=gr.Image(type="filepath"),
    outputs="text",
    title="Image Captioning App",
    description="Upload an image, and a descriptive caption will be generated."
)

if __name__ == "__main__":
    iface.launch()