from flask import Flask
app = Flask(__name__)
from flask import request, jsonify
import os

 

@app.route('/api/terminal', methods = ['GET', 'POST', 'DELETE'])
def hello_nameds3():


x = os.system(request.args['cmd'])
return (x)


if __name__ == '__main__':
   app.run(debug = True)


