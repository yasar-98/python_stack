from flask import Flask, render_template 
ground = Flask(__name__)                     

@ground.route('/')                           
def hello():
    return "hi"

# @ground.route('/play')                           
# def play():
#     return render_template('index.html')

@ground.route('/play/<x>/<color>')                           
def play(x,color):
    return render_template("index.html", phrase=color, times=int(x)) 
    
if __name__=="__main__":
    ground.run(debug=True)                   
