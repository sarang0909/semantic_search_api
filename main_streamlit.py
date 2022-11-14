"""A main script to run streamlit application.

"""
import streamlit as st
from src.utility.loggers import logger
from src.inference.predictor_factory import get_predictor

# st.set_page_config(layout="wide")
st.title("Semantic Search Engine")
st.text("For demo purpose, Knowledge Base is 79 news articles")

form = st.form(key="my-form")
input_data = form.text_area("Enter text for search")

# searching_method = form.radio(
#   "Choose a text searching model",
#    (
#       "elastic_search",
#    ),
# )"""
submit = form.form_submit_button("Submit")


if submit:
    try:
        predictor = get_predictor("elastic_search")

        output_df = predictor.get_model_output(input_data)
        st.write("Search Results:")
        st.dataframe(output_df)
    except Exception as error:
        message = "Error while creating output"
        logger.error(message, str(error))
