import fitz
import pandas as pd


def get_table_data(pdf_path, page_number):
    # Open the PDF
    pdf_document = fitz.open(pdf_path)
    # Get a specific page
    page = pdf_document.load_page(page_number - 1)
    # Extract text from the page
    text = page.get_text("text")
    # Get table data by splitting the text based on newline and space
    table_data = [line.split() for line in text.split("\n") if line.strip()]
    pdf_document.close()
    return table_data


def convert_to_dataframe(table_data):
    # Assuming the table has the same number of columns for each row
    max_columns = max(len(row) for row in table_data)
    table_data = [row + [""] * (max_columns - len(row)) for row in table_data]
    df = pd.DataFrame(table_data)
    return df
