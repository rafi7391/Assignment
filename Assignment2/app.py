from flask import Flask, request, render_template
import pdf_extractor
app = Flask(__name__)
@app.route('/extract', methods=['POST'])
def extract():
    pdf_file = request.files['pdf_file']
    data = pdf_extractor.extract_data(pdf_file)
    return render_template('results.html', data=data)
@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run()
