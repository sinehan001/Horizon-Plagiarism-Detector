from utils.pdf_reader import pdf2txt
from utils.doc_reader import docx2txt
from utils.xls_reader import xls2txt
from utils.ppt_reader import ppt2txt


def extract_data(file_path):
    file_extension = file_path.split('.')[-1].lower()

    if file_extension in ('doc', 'docx'):
        extracted_text = docx2txt(file_path, file_extension)
        return extracted_text

    elif file_extension == 'pdf':
        extracted_text = pdf2txt(file_path)
        return extracted_text

    elif file_extension in ('xlsx', 'xls'):
        extracted_text = xls2txt(file_path, file_extension)
        return extracted_text

    elif file_extension in ('pptx', 'ppt'):
        extracted_text = ppt2txt(file_path, file_extension)
        return extracted_text

    else:
        return "Unsupported file format"


def extract_text(file_path):
    extracted_data = extract_data(file_path)
    return extracted_data
