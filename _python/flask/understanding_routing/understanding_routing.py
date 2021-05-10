from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    return f"Hi {name}"

@app.route('/repeat/<num>/<act>')
def repeat(num, act):
    h=""
    for i in range (int(num)):
        h+=f" <p>Hello {act}</p> "
    return h

if __name__=="__main__":
    app.run(debug=True)