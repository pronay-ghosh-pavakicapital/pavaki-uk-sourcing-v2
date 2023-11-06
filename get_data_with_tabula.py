import tabula
import streamlit as st
import pandas as pd

# pdf_file = PATH


def extract_data_given_page_number_with_tabula(pdf_file, page_number):
    return_table = 0
    # Use the read_pdf function without specifying area to extract all tables on the page
    extracted_tables = tabula.read_pdf(pdf_file, pages=page_number)

    # If tables are found on the specified page, extracted_tables will contain the table(s)
    if extracted_tables:
        # Access the tables (as a list) on the specified page
        for table in extracted_tables:
            print(table)
            return_table = table
            # table.to_csv("./data_barret.csv")
    else:
        print("No tables found on page", page_number)
    return pd.DataFrame(return_table)
