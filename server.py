from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():

    return render_template('main.html')






if __name__ == '__main__': 
    pass
    app.run(debug=True, host='0.0.0.0')