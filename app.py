from flask import Flask, render_template, request, jsonify
import os
from filecheck import extract_text
from process import check_plagiarism

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check_plagiarism', methods=['POST'])
def check_plagiarism_route():
    documents = request.files.getlist('documents')
    project_name = request.form['project_name']
    college_name = request.form['college_name']

    # Define a folder to save the uploaded files
    upload_folder = 'uploads'
    os.makedirs(upload_folder, exist_ok=True)

    result = ''

    for document in documents:
        if document.filename != '':
            # Save the uploaded file to the upload folder
            file_path = os.path.join(upload_folder, document.filename)
            document.save(file_path)
            document_path = '/'.join([upload_folder, document.filename])
            extracted_text = extract_text(document_path)
            result += check_plagiarism(extracted_text, document.filename, document.filename, project_name, college_name)
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(debug=True)
