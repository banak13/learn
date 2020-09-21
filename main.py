from flask import Flask, send_file, render_template, request

app = Flask(__name__)

@app.route('/mypage/contact', methods=['GET', 'POST'])
def form():

    if request.method == 'GET':
        print("We received GET")

    elif request.method == 'POST':
        print("We received POST")
        requestt = request.form.get('textarea')
        print(request.form)

    return render_template("form.html")

@app.route('/mypage/me', methods=['GET'])
def o_mnie():
    if request.method =='GET':


    return render_template("Omnie.html")



@app.route('/message', methods=['GET', 'POST'])
def message():
   if request.method == 'GET':
       print("We received GET")
       return render_template("form.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")

app.run(port=3000, host="0.0.0.0")