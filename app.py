from flask import Flask, render_template, request
from transformers import BartForConditionalGeneration, BartTokenizer
import io
import PyPDF2

app = Flask(__name__)

model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    uploaded_file = request.files['pdf_file']
    if uploaded_file:
        try:
            pdf_file = io.BytesIO()
            pdf_file.write(uploaded_file.read())
            pdf_file.seek(0)

            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text_content = ''
            for page in pdf_reader.pages:
                text_content += page.extract_text()

            summary = summarize_text(text_content)
            return render_template('result.html', text_content=text_content, summary=summary)
        except Exception as e:
            return str(e)
        finally:
            pdf_file.close()
    else:
        return "No file uploaded."

def summarize_text(text_content):
    try:
        inputs = tokenizer.encode("summarize: " + text_content, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = model.generate(inputs, max_length=350, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
    except Exception as e:
        return "Error generating summary: " + str(e)

if __name__ == '__main__':
    app.run(port=5001)