import os
import streamlit as st
from PIL import Image
import google.generativeai as genai

genai.configure(api_key = os.getenv('gemini_api_key'))

model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    print("here is the response")
    print(response)
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type" : uploaded_file.type,
                "data" : bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file was uploaded")
    

st.set_page_config(page_title = "Multilanguage Invoice Extractor")

st.header("Multilanguage Invoice Extractor")

input = st.text_input("Input Prompt: ", key = "input")
uploaded_file = st.file_uploader("Choose an imagw...", type = ["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "Uploaded Image", use_column_width = True)

submit = st.button("Submit")

input_prompt = """Give me all the information about the ulpaded image that is asked from you. """


if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.header("the response is: ")
    st.write(response)