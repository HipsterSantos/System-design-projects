from flask import Flask,render_template, url_for,request

app = Flask(__name__)

#first attempt
@app.route('/')
def renderHello():
    return "Hello world"

#dynamic url
@app.route('/names/<name>')
def renderName(name):
    return f"rendering name {name}"

#formating url
@app.route('/user/<user>')
def showUser(user):
    return "this user is = {} and <a href='{}'>Go to my profile</a>".format("Jayjay",url_for('showUser',user="Tetiana"))

#specifying methods
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        """ changing to auth logic"""
        return "we're handing get request"
    else:
        return "we're handling post request"

if __name__ == '__main__':
    app.run(debug=True)