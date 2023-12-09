# Horizon Plagiarism Detector

**⚠️Warning: This application is currently under development & compatible only with Windows 7 and above. We are actively working on extending support to other operating systems, and appreciate your patience. Stay tuned for updates as our development process progresses. Thank you for your understanding!**

## Overview

Horizon Plagiarism Detector is a Python-based tool that allows users to check for plagiarism in various types of files, including documents, presentations, and PDFs. The tool extracts text from different file formats and compares it against pre-availed datasets to identify potential instances of plagiarism. The underlying algorithm for plagiarism detection is based on TF-IDF (Term Frequency-Inverse Document Frequency) vectors.

### TF-IDF for Plagiarism Detection

The Horizon Plagiarism Detector uses TF-IDF vectors to identify similarities between the input text and the pre-availed datasets. TF-IDF is a numerical statistic that reflects the importance of a word in a document relative to a collection of documents. It helps in determining the relevance of words and phrases in the context of plagiarism detection.

## Getting Started

Follow the steps below to seamlessly integrate the Horizon Secure PDF Signing and Verification Tool into your workflow.

## Features

- Text extraction from DOCX, PPTX, PDF, and other file formats.
- Plagiarism detection using TF-IDF vectors and pre-availed datasets.
- Web interface powered by Flask for easy interaction.

## Prerequisites

Before running the Horizon Plagiarism Detector, make sure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- Flask
- pywin32


## Installation

### Method 1

1. Clone the Horizon repository to your local machine:

   ```bash
   git clone https://github.com/sinehan001/Horizon-Plagiarism-Detector.git
   cd Horizon-Plagiarism-Detector
   ```

2. Install Dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

3. Access the application:

Visit http://localhost:5000 in your web browser.

### Method 2
 
 1. Install the PyCharm

   - [PyCharm](https://www.jetbrains.com/pycharm/)

 2. Setup the Virtual Environment for running python3 in PyCharm

 3. Search **Git** in the Toolbar (or) Search **Help -> Git** in Toolbar 

 4. Find the **GitHub -> Create Pull Request**, then Enter the Git URL - https://github.com/sinehan001/Horizon-Plagiarism-Detector.git, click OK, Then click on Create Pull Request.

 5. Once, all files has been pulled from GitHub, Click the **Terminal** tab, which is located bottom toolbar of the page.

 6. Then, execute the below command in the terminal.
   ```bash
   pip install -r requirements.txt
   ```

 7. Then, click ▶ to run the project, To access the application: Visit http://localhost:5000 in your web browser.

## Dependencies

- Flask
- Scikit Learn
- pywin32 & So on.

Here the Dependencies are availed in **requirements.txt** file.

## Application Structure

- `venv/`: Contains the virtual environment for running Python-based application.
## URL Reference

#### To check plagiarism

```http
  GET http://localhost:5000/
```

## Authors

- [@sinehan001](https://www.github.com/sinehan001)


## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. Your feedback is highly appreciated!


## License 

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). See the LICENSE file for details.



## FAQ

#### 1. Is this app safe to use?

Yes, it is entirely safe to use this application.

#### 2. Is it free or does it cost anything to use?

It is completely free to use.

#### 3. Where the files are stored?

Here in default, files are  stored in our Server.


## Feedback

If you have any feedback, please reach out to us at sinehan22@gmail.com

