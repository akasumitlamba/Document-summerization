# Document Summarization with Flask

This web application allows users to upload PDF files, extract text content, and generate a summary using the Facebook BART model. It is built using Flask, a Python web framework.



## How it Works

1. **Upload PDF**: Users can upload PDF files through the web interface.
2. **Text Extraction**: The application extracts the text content from the uploaded PDF using the PyPDF2 library.
3. **Summarization**: The extracted text is then passed to the Facebook BART model for summarization. The model generates a concise summary of the input text.
4. **Display Results**: Users can view both the original text content and the generated summary on the result page.

## Getting Started


### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/akasumitlamba/Document-summerization.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python app.py
    ```

4. Access the web application at [http://localhost:5001/](http://localhost:5001/).

### Usage

1. Upload a PDF file using the provided form.
2. Click on the "Summarize" button to generate a summary.
3. View the original text content and the generated summary on the result page.

## Dependencies

- Flask
- transformers
- PyPDF2

Install dependencies using:

```bash
pip install flask transformers PyPDF2
```
This README file provides clear instructions and formatting for users to understand the project and get started quickly.
