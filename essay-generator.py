import os
import streamlit as st
from langchain.llms import GooglePalm
from langchain.prompts import PromptTemplate


page_icon = "🦜️"
layout = "centered"
page_title = "Essay Generator"
caption_text = "By <a href=\"https://github.com/rpatra332\" target=\"_blank\" rel=\"noopener noreferrer\" class=\"mycaption\">Rohit Patra</a>"


st.set_page_config(page_icon=page_icon, page_title=page_title, layout=layout)
st.title(body='🦜️ Essay Generator', help="Made With LangChain And Google PaLm 2 API")
st.caption(caption_text, unsafe_allow_html=True)


# --- DATA FROM UI ---
with st.form(key="form"):
    topic = st.text_input(label="Enter the topic for the essay.", placeholder="Example: Bird")
    words = st.selectbox(options=["100", "200", "300", "400", "500", "600"], label="Number Of Words")
    submit = st.form_submit_button(label="Generate")


# --- PROMPT TEMPLATES ---
essay_template = PromptTemplate(
    input_variables=['topic', 'words'],
    template="Write me an essay about '{topic}' within {words} words."
)


# --- LLM ---
_GOOGLE_GENERATIVE_API_KEY = os.environ['GOOGLE_GENERATIVE_API_KEY']
llm = GooglePalm(google_api_key=_GOOGLE_GENERATIVE_API_KEY, temperature=0.9)


# --- RESULT VIEW ---
if submit and topic and words:
    essay = llm(prompt=essay_template.format( topic=topic, words=words))
    with st.container():
        st.write(F"## **{topic}**")
        st.divider()
        st.write(essay)


# --- CSS PROPERTIES ---
caption_css_change = """
<style>
    .mycaption{
        color: rgba(250, 250, 250, 0.8) !important;
        text-decoration: none;
    }
</style>
"""
st.markdown(caption_css_change, unsafe_allow_html=True)
