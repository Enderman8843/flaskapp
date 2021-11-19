from flask import Flask
app = Flask(__name__)
from flask import request, jsonify

x = None
PrimeVerify = None
number = None
i = None

inputnumber = None
PrimeVerify = None
number = None
i = None

def upRange(start, stop, step):
  while start <= stop:
    yield start
    start += abs(step)

def downRange(start, stop, step):
  while start >= stop:
    yield start
    start -= abs(step)

# Describe this function...
def primenumberfinder(inputnumber):
  global PrimeVerify, number, i
  PrimeVerify = 0
  number = inputnumber
  for i in (1 <= float(inputnumber)) and upRange(1, float(inputnumber), 1) or downRange(1, float(inputnumber), 1):
    if 0 == inputnumber % i:
      PrimeVerify = PrimeVerify + 1
  if PrimeVerify == 1 + 1:
    if PrimeVerify == 1 + 1:
      return 'true'
  return 'false'

factono = None
Factors = None
i = None

def upRange(start, stop, step):
  while start <= stop:
    yield start
    start += abs(step)

def downRange(start, stop, step):
  while start >= stop:
    yield start
    start -= abs(step)

# Describe this function...
def find_factors(factono):
  global Factors, i
  Factors = []
  for i in (1 <= float(factono)) and upRange(1, float(factono), 1) or downRange(1, float(factono), 1):
    if 0 == factono % i:
      Factors.insert(0, factono / i)
  return Factors

numb = None

# Describe this function...
def isodd(numb):
  if 0 == numb % 2:
    if 0 == numb % 2:
      return 'true'
  return 'false'



 
@app.route('/api/v1/sum/',methods = ['POST', 'GET'])


name = request.args.get('num')

def hello_name(name):

  response = {
        "Is_It_Prime": primenumberfinder('name'),
        "List_of_factors": str(find_factors('name'))[1:-1],
        "Is_It_Even":isodd('name')
    }
 
  return jsonify(response)

if __name__ == '__main__':
   app.run(debug = True)
