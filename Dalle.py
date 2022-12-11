import openai
import urllib.request
from PIL import Image
import cv2
import streamlit as st  //UI

openai.api_key = "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"

def generate_image(image_description):
    
    img_response = openai.Image.create(
        prompt = image_description,
        n=1,
        size="512x512")
    
    img_url = img_response['data'][0]['url']
    
    urllib.request.urlretrieve(img_url, "img.png")
    
    img = Image.open("img.png")
    
    return img


st.title('DALL.E - Image Generation - OpenAI')

img_description = st.text_input('Image Description')

if st.button('Generate Image'):
    generated_img = generate_image(img_description)
    st.image(generated_img)
    
    
