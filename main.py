import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスパー表示')
'Start!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i:1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ１')
expander1.write('問い合わせ１内容を書く')
expander2 = st.expander('問い合わせ２')
expander2.write('問い合わせ１内容を書く')

#text = st.text_input('あなたの趣味を教えてください')
#'あなたの趣味は、', text, 'です'

#condition = st.slider('あなたの今の調子は？',0,100,50)
#'コンディション：', condition


#option = st.selectbox(
#    'あなたが好きな数字を教えてください',
#    list(range(1,11))
#)
#'あなたの好きな数字は、', option,'です'

#if st.checkbox('Show Image') :
#    img = Image.open('KODAMA_03.jpg')
#    st.image(img, caption='Atsuo Kodama', use_column_width=True)
