# coding:utf-8
try:
    from flask import Flask, render_template, request
except ModuleNotFoundError:
    import os
    os.system("python -m pip install flask")
    from flask import Flask, render_template, request
import corona

app = Flask(__name__)


@app.route("/")
def home():
    result = corona.run()
    return render_template("home.html", result=result)


@app.route("/", methods=["POST"])
def covid():
    commande = request.form['commande']
    result, name = corona.run(commande)
    if commande == 'all':
        return render_template("allCountry.html", result=result)
    else:
        return render_template('oneCountry.html', result=result, name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
