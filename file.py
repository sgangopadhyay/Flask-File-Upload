from flask import Flask, render_template, url_for, request, redirect
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'C:/Users/suman/Desktop/india/img'
app.config['SECRET_KEY'] = 'suman@india'
ALLOWED_EXTENSIONS = set(['png', 'jpeg', 'jpg'])

@app.route('/', methods = ['GET', 'POST'])
def index():
    if (request.method == 'POST'):    
        file = request.files['file']    
        if ('file' not in request.files):            
            return redirect('/')        
        elif (file.filename == ''):
            return("<script>alert('File Not Selected')</script>")
        elif (file):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/')
        else:
            return redirect(request.url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)