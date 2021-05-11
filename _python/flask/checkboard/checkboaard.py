from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def index(x=8,y=8,color1="red",color2="blue"):
    return render_template("index.html",x=x,y=y,color1=color1,color2=color2)	

if __name__=="__main__":
    app.run(debug=True)
