from flask import Flask, render_template, request
from betting_2 import main as bet
from betsc import main as safe

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST" and request.form.get('one_bet') is not None:
        one = request.form.get('one_bet')
        two = request.form.get('two_bet')
        cross = request.form.get('cross_bet')
        if one is not None and "," in one:
            one = one.replace(",", ".")
        if two is not None and "," in two:
            two = two.replace(",", ".")
        if cross is not None and "," in cross: 
            cross = cross.replace(",", ".")
        chars = "abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ"    
        for i in chars:
            if i in one or i in two or i in cross:
                return render_template("index.html", bettson=["Fel","", "", ""])
        bonus = request.form.get('bonus')
        bettson = bet(float(one),float(cross),float(two), float(bonus))
        return render_template("index.html", bettson=bettson)
    elif request.method == "POST" and request.form.get('one_bet_t') is not None:
        one = request.form.get('one_bet_t')
        two = request.form.get('two_bet_t')
        cross = request.form.get('cross_bet_t')
        if one is not None and "," in one:
            one = one.replace(",", ".")
        if two is not None and "," in two:
            two = two.replace(",", ".")
        if cross is not None and "," in cross: 
            cross = cross.replace(",", ".")
        chars = "abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ"    
        for i in chars:
            if i in one or i in two or i in cross:
                return render_template("index.html", bettson=["Fel","", "", ""])
        bonus = request.form.get('bonus_t')
        bettson = safe(float(one),float(cross),float(two), float(bonus))
        return render_template("index.html", bettson=bettson)
    
    else:
        return render_template("index.html", bettson="")
if __name__ == '__main__':
    app.run(debug=True)
