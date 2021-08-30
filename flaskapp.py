from os import error
import fitz
from utils import sudachiModule
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello():
    return render_template('index.html', error='', fname='')

@app.route('/extract', methods=['GET', 'POST'])
def extract():
    if request.method == 'POST':
        try:
            tag = request.form['text']
            if tag == '':
                return render_template('index.html', error='No text received', fname='')
            nouns = sudachiModule.get('名詞', tag)
            verbs = sudachiModule.get('動詞', tag)
            adjectives = sudachiModule.get('形容詞', tag)
            len_nouns = len(nouns)
            len_verbs = len(verbs)
            len_adj = len(adjectives)
            return render_template('index.html', error='', fname='', nouns=nouns, adjectives=adjectives, verbs=verbs, len_nouns=len_nouns, len_adj=len_adj, len_verbs=len_verbs)
        except:
            return render_template('index.html', error='', fname='')

ALLOWED_EXTENSIONS = ['txt', 'csv', 'rtf']#, 'pdf']
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error='No file uploaded')

        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', error='No selected file')

        if file and allowed_file(file.filename):
            # if file.filename[-4:] == '.pdf':
            #     with fitz.open(file) as doc:
            #         text = ''
            #         for page in doc:
            #             text += page.getText()
            # else:
            text = file.read().decode('utf-8')

            nouns = sudachiModule.get('名詞', text)
            verbs = sudachiModule.get('動詞', text)
            adjectives = sudachiModule.get('形容詞', text)
            len_nouns = len(nouns)
            len_verbs = len(verbs)
            len_adj = len(adjectives)
            
            return render_template('index.html', error='', fname=file.filename, nouns=nouns, adjectives=adjectives, verbs=verbs, len_nouns=len_nouns, len_adj=len_adj, len_verbs=len_verbs)
            
        return render_template('index.html', error='Invalid filetype. Supported filetypes: .csv, .txt, .rtf')

    return render_template('index.html', error='No file uploaded')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')