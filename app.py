from flask import Flask, render_template, request, redirect, flash
from conversion import try_conversion_and_set_rate

app = Flask(__name__)
app.config["SECRET_KEY"] = "123SECRET_PHASE456"


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/currency", methods=["POST"])
def currency():
    # get form data
    c_from = request.form.get("convert-from", "USD").upper()
    c_to = request.form.get("convert-to", "MXN").upper()
    amount = request.form.get("amount", 1)  # str

    rate = try_conversion_and_set_rate(c_from, c_to, amount)

    if rate["message"] == "success":
        return render_template("currency.html", conversion=rate["conversion"])
    else:
        flash(rate["message"], "error")
        return redirect('/')
