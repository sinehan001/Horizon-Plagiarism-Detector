import openpyxl
import xlrd


def convert_xls_to_xlsx(file_path):
    extracted_text = ''
    # Open the .xls file
    workbook = xlrd.open_workbook(file_path)

    # Select a specific sheet by name (replace 'Sheet1' with the actual sheet name)
    sheet = workbook.sheet_by_name('Sheet1')

    # Initialize a list to store the data
    data = []

    # Iterate through rows and columns to read data
    for row_index in range(sheet.nrows):
        row_data = []
        for col_index in range(sheet.ncols):
            cell_value = sheet.cell_value(row_index, col_index)
            row_data.append(cell_value)
        data.append(row_data)
    extracted_text = data
    return extracted_text


def xls2txt(file_path, file_extension):
    extracted_text = ''
    if file_extension == 'xls':
        extracted_text = convert_xls_to_xlsx(file_path)
    else:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        data = []
        for row in sheet.iter_rows(values_only=True):
            data.append(row)
        extracted_text = data
    return extracted_text
