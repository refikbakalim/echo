from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html") 

@app.route('/echo', methods=['POST'])
def echo():
    message = request.form["usermsg"]
    return message

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")