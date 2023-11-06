import streamlit as st
import fitz
import pandas as pd
from get_data_with_fitz import *
from get_data_with_tabula import *
import os

# Path to your PDF file
st.header("Pavaki Capitals PDF Extractor")
PATH = st.file_uploader("Choose your .pdf file", type="pdf")
# uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if PATH is not None:
    file_details = {"FileName": PATH.name, "FileType": PATH.type, "FileSize": PATH.size}
    st.write(file_details)
    st.write("Preview of the PDF:")
    st.write(PATH)
    root_dir = os.getcwd()
    save_path = os.path.join(root_dir, "./data.pdf")
    with open(save_path, "wb") as f:
        f.write(PATH.getbuffer())
    st.success(f"Downloaded data.pdf to the root directory")


def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")


PATH = r"./data.pdf"
if PATH is not None:
    page_number = st.number_input(
        "Enter the Page Number: ", min_value=1, value=1, step=1
    )
    # page_number = int(page_number_text)

    if st.button("Extract Table"):
        # table_data = get_table_data(pdf_file_path, page_number)
        # dataframe = convert_to_dataframe(table_data)
        # st.write(dataframe)
        try:
            table_data = extract_data_given_page_number_with_tabula(PATH, page_number)
            st.dataframe(table_data)
            original_balance_sheet_data = convert_df(table_data)
            # final_standerdized_balance_sheet_data = convert_df(standerdized_data)
            st.download_button(
                label="Download Data",
                data=original_balance_sheet_data,
                file_name="original_data.csv",
                mime="text/csv",
            )
        except Exception as e:
            print(f"Tanula ran into Exception {e}")
            print("Trying with Fitz...")
            try:
                table_data = get_table_data(PATH, page_number)
                dataframe = convert_to_dataframe(table_data)
                print(dataframe)
                st.dataframe(dataframe)
                original_balance_sheet_data = convert_df(dataframe)
                # final_standerdized_balance_sheet_data = convert_df(standerdized_data)
                st.download_button(
                    label="Download Data",
                    data=original_balance_sheet_data,
                    file_name="original_data.csv",
                    mime="text/csv",
                )
            except Exception as e:
                print(f"Tanula ran into Exception {e}")
