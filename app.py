import streamlit as st
import boto3
from PIL import Image

st.title('Hand Writing Recognition')
client=boto3.client('textract')

img_file=st.file_uploader('Upload Image',type=['png','jpg','jpeg'])

if img_file is not None:
    file_details={}
    file_details['type']=img_file.type
    file_details['size']=img_file.size
    file_details['name']=img_file.name
    st.write(file_details)
    st.image(Image.open(img_file),width=250)

    with open('test.png','wb') as f:
        f.write(img_file.getbuffer())
    
    imageSource=open('test.png','rb')

    response=client.detect_document_text(Document={'Bytes':imageSource.read()})
    # st.write(response)
    for i in response['Blocks']:
        if(i['BlockType']=='LINE'):
            st.write(i['Text'])