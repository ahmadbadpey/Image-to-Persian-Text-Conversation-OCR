import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request
from converting_blueprint import converting_blueprint

app = Flask(__name__, template_folder='../templates', static_folder='../static')

app.register_blueprint(converting_blueprint)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    fn = secure_filename(file.filename)
    file.save(os.path.join('../uploads', fn))
    return {
        "success": True,
        "message": fn
    }


if __name__ == '__main__':
    app.run()
