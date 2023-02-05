from flask import Flask,redirect,request,url_for,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "hi

@app.route('/two')
def two():
    return "hello"






if __name__=='__main__':
    app.run(debug=True)
