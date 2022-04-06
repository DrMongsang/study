import streamlit as st
import time

st.title('Steamlt 超入門')

st.write('プログレスパーの表示')
'Start!!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'

left_column, right_colum = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_colum.write('ここは右カラム')

expander1 = st.expander('Q&1')
expander1.write('Q&Aの内容をかく')
expander2 = st.expander('Q&A2')
expander2.write('Q&Aの内容をかく')
expander3 = st.expander('Q&A3')
expander3.write('Q&Aの内容をかく')

# text = st.text_input('あなたの趣味を教えてください')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味:、',text, 'です。'
# 'コンディション:',condition


# st.checkbox('Show Image'):
#     img = Image.open('Sample.png')
#     st.image(img, caption= 'Tangoya', use_column_width=True)