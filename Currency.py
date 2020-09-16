from flask import Flask, request, render_template, redirect, url_for
import csv

app = Flask(__name__)

@app.route("/currency_calc", methods = ["GET","POST"])
def currency():
    if request.method == "POST":
        data = request.form
        currency = data.get("currency")
        amount = data.get("quantity")
        with open("bank_currencies.csv") as csv_file:
            csv_reader = csv.DictReader("bank_currencies.csv", delimiter = ';')
            csv_reader = [row for row in csv_reader if row]
            for row in csv_reader:
                print(row['currency'])
                if row['currency'] == currency:
                    price = float(amount) * float(row['ask'])
                    print(f"for {amount} {currency} you will pay {price} pln ")
                    return render_template("currency_sum_template.html")

    else:
        return render_template("currency_template.html")