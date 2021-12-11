from flask import Flask
app = Flask(__name__)
from flask import request, jsonify

from chemlib import Compound

from chemlib import Element
import requests
from bs4 import BeautifulSoup
import flask
from googlesearch import search
s = None


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

@app.route('/', methods=['GET'])
def home():
    return "<h1>A Open-sourced Python Flask Project by funlrn.</p>"




 
@app.route('/api/v1/numbers/find_details/', methods = ['GET', 'POST', 'DELETE'])
def hello_name999():
  num = int(request.args['num'])
  response = {
        "Is_It_Prime": primenumberfinder(num),
        "List_of_factors": str(find_factors(num))[1:-1],
        "Is_It_Even":isodd(num)
    }
 
  return jsonify(response)


    

s = None


@app.route('/api/v1/chemical/findcompound/', methods = ['GET', 'POST', 'DELETE'])
def hello_name98():
  
  num = (request.args['element'])
  xenon = Element(num) #Instantiate with symbol of Element

  return jsonify(xenon.properties)


@app.errorhandler(500)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return ("<h1> Invalid Input Check with your Input Or some server error Contact with adminstrator for help")
     
@app.errorhandler(400)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return ("<h1> No Input Error Code 400 contact adminstrator for help")



@app.route('/api/v1/chemical/findformula/', methods = ['GET', 'POST', 'DELETE'])
def hello_name9889():
  
  num = (request.args['chemical'])

  
  water = Compound(num)
  form = water.formula
  molar = water.molar_mass()
  val = str(molar)
  response = ('{"formula" : ' + form + ", Molar :" + str.format(val) + "}" )
  
 

  return response

@app.route('/api/v1/findtitle/', methods = ['GET', 'POST', 'DELETE'])
def hello_name():


 for j in search((request.args['query']), tld="co.in", num=1, stop=1, pause=2):


# using the BeaitifulSoup module

# displaying the title

  for title in BeautifulSoup(requests.get(j).text, 'html.parser').find_all('title'):
   return (title.get_text())


if __name__ == '__main__':
   app.run(debug = True)


