from flask import Flask, render_template, request
from betting_2 import main as bet

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        one = request.form.get('one_bet')
        two = request.form.get('two_bet')
        cross = request.form.get('cross_bet')
        if "," in one:
            one = one.replace(",", ".")
        if "," in two:
            two = two.replace(",", ".")
        if "," in cross: 
            cross = cross.replace(",", ".")
        chars = "abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ"    
        for i in chars:
            if i in one or i in two or i in cross:
                return render_template("index.html", bettson=["Fel","", "", ""])
        bonus = request.form.get('bonus')
        bettson = bet(float(one),float(cross),float(two), float(bonus))
        return render_template("index.html", bettson=bettson)
    else:
        return render_template("index.html", bettson="")
if __name__ == '__main__':
    app.run(debug=True)
