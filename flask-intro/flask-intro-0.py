import os
from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html")

@app.route('/ftoc')
def render_ftoc():
    return render_template('ftoc.html')

@app.route('/ftoc_result')
def render_ftoc_result():
    try:
        ftemp_result = float(request.args['fTemp'])
        ctemp_result = ftoc(ftemp_result)
        return render_template('ftoc_result.html', fTemp=ftemp_result, cTemp=ctemp_result)
    except ValueError:
        return "Sorry: something went wrong."

if __name__ == "__main__":
    app.run(port=5000)
