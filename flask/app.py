from p1 import *
from flask import *
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "hello world"
@app.route("/api",methods=['GET'])
def home(): 
  inputchr=request.args['query']
  result = calculate(inputchr)
  output = {'output': result}
  return jsonify(output)

if __name__ == '__main__':
   app.run()

 