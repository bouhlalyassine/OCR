import streamlit as st
from settings import *
from streamlit_lottie import st_lottie
import streamlit as st
import easyocr

# streamlit run OCR.py

st.set_page_config(page_title=TITLE,
    layout="wide")


st.markdown("<h2 style=\
    'text-align : center';\
    font-weight : bold ;\
    font-family : Arial;>\
    Optical Character Recognition (OCR)</h2>", unsafe_allow_html=True)
st.markdown("---")


with st.sidebar :
    uploaded_file3 = st.file_uploader("📌 Upload Image", key="fup3",type=["jpg", "jpeg", "png"], label_visibility="visible")

if uploaded_file3 :
    img = uploaded_file3.read()      
            
    colpiaz_1, colpiaz_2 = st.columns([35,65], gap="medium")
    with colpiaz_1 :
        st.markdown(f"<h5 style=\
        'text-align : center';\
        font-weight : bold ;\
        font-family : Arial;>\
        Uploaded Image :</h5>", unsafe_allow_html=True)

        st.image(image = img)

    with colpiaz_2 :
        if st.button("Extract Text") :
            
            with st.spinner("Extraction in progress, please wait...") :
                reader = easyocr.Reader(['en','fr','es'], gpu=False)
                result = reader.readtext(img)

            sentence = ""
            for detection in result: 
                text = detection[1]
                sentence += (" "+ text)
            st.write(sentence)

                
else:
    st.markdown("<br>", unsafe_allow_html=True)
    colpia_1, colpia_2 = st.columns([85, 15], gap="small")
    with colpia_1 :
        st.info("This tool allows you to extract text written on an image. It could be useful\
            for automatically transcribing text from an image instead of doing it manually\
            \n\n You can upload the image to be processed on the left menu")

    with colpia_2:
        lottie_pdf_text = load_lottiefile(lottie_pdf_text)
        st_lottie(
        lottie_pdf_text,
        speed=1,
        reverse=False,
        loop=True,
        quality="high", # medium ; high ; low
        height=125)
