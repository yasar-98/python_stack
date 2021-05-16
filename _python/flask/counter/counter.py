from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def welcome():
    if 'count' in session:
        session['count']+=1
    else:
        session['count']=1
    return render_template("index.html", count = session["count"])

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    if 'count' in session:
        session.clear()

    return redirect('/')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)                   
