from docx import Document
import os
import win32com.client


def convert_doc_to_docx(doc_file):
    # Create a COM instance of Word
    word = win32com.client.Dispatch("Word.Application")

    # Open the DOC file
    doc = word.Documents.Open(os.path.abspath(doc_file))

    extracted_text = ""

    # extracting text from doc
    for paragraph in doc.Paragraphs:
        extracted_text += paragraph.Range.Text + '\n'

    # Close the documents and Word application
    doc.Close()
    word.Quit()

    return extracted_text


def docx2txt(doc_file, file_extension):
    extracted_text = ''
    if file_extension == 'doc':
        extracted_text = convert_doc_to_docx(doc_file)
    else:
        doc = Document(doc_file)
        for paragraph in doc.paragraphs:
            extracted_text += paragraph.text + '\n'
    print(extracted_text)
    return extracted_text
