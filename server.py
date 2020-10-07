from flask import Flask, render_template

@app.route('/')
def homepage:

    render_template('main.html')






if __name__ == 'main':
    app.run(debug=True, host='0.0.0.0')