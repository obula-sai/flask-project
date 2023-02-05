from flask import Flask,redirect,request,url_for,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("web1.html")

@app.route('/two')
def two():
    return render_template("web.html")






if __name__=='__main__':
    app.run(debug=True)