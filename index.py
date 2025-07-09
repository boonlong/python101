from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify(message="hello world")

@app.route('/', methods=['GET'])
def root():
    return 'สวัสดี'

if __name__ == '__main__':
    app.run(debug=True) 
