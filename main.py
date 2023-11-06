import fitz
import pandas as pd
from get_data_with_fitz import *
from get_data_with_tabula import *

# Path to your PDF file
PATH = r"C:/Study/research/fintech/pdf_to_table/new_pdfs/shell-annual-report-2022.pdf"
page_number = int(input("Enter the Page Number: "))


try:
    table_data = extract_data_given_page_number_with_tabula(PATH, page_number)
    print(table_data)
except Exception as e:
    print(f"Tanula ran into Exception {e}")
    print("Trying with Fitz...")
    try:
        table_data = get_table_data(PATH, page_number)
        dataframe = convert_to_dataframe(table_data)
        print(dataframe)
    except Exception as e:
        print(f"Tanula ran into Exception {e}")
