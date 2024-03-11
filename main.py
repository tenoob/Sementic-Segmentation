#streamlit app
import streamlit as st
from PIL import Image
import numpy as np
from shape import display_legend_item
from constant import CATEGORIES,color_code
from util import get_prediction


st.title("Satalite Image Segmentation Project")

st.header("Upload Satalite image")

image = st.file_uploader("",type=['jpeg','jpg','png'])
if  image is not None:
    prediction = get_prediction(image)
    if prediction is not None :
        st.text("Categories")
        for i in range(6):
          display_legend_item(CATEGORIES[i],color_code[i])
        st.image(prediction,output_format="JPEG")

        
