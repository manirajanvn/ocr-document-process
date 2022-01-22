import cv2
import json
import pytesseract
import streamlit as st
from PIL import Image
import numpy as np

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
options = "--psm 10"


def get_text(shapes, img, imgH, imgW, dataH, dataW):
    x1 = int(((shapes['points'][0][0]) / dataW) * imgW)
    y1 = int(((shapes['points'][0][1]) / dataH) * imgH)
    x2 = int(((shapes['points'][1][0]) / dataW) * imgW)
    y2 = int(((shapes['points'][1][1]) / dataH) * imgH)

    name_img = img[y1:y2, x1:x2]
    text = pytesseract.image_to_string(name_img, config=options)
    return text


with open('D:/study/RPA/demo/emp_form.json', 'r') as f:
    data = json.load(f)

st.subheader("IPA - Document Process with OCR")
image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])
if image_file is not None:
    img = Image.open(image_file)
    img = img.save("img.jpg")
    # OpenCv Read
    img = cv2.imread("img.jpg")
    imgH = img.shape[0]
    imgW = img.shape[1]
    name = get_text(data['shapes'][0], img, imgH, imgW, data['imageHeight'], data['imageWidth'])
    date = get_text(data['shapes'][1], img, imgH, imgW, data['imageHeight'], data['imageWidth'])
    address1 = get_text(data['shapes'][2], img, imgH, imgW, data['imageHeight'], data['imageWidth'])
    city = get_text(data['shapes'][3], img, imgH, imgW, data['imageHeight'], data['imageWidth'])
    st.text("Name: " + name)
    st.text("Date: " + date)
    st.text("Adderss: " + address1)
    st.text("email: " + city)

# cv2.waitKey(0)
#cv2.destroyAllWindows()
