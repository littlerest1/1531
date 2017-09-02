import csv
from flask import Flask, redirect, render_template, request, url_for
from server import app, user_input

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        zID = int(request.form["zID"])
        url = request.form["URL"]
        
        with open('login.csv','a') as csv_out:
              writer = csv.writer(csv_out)
              writer.writerow([name, zID,url])
        user_input.append([name, zID, url])

        return redirect(url_for("hello"))
    return render_template("login.html")

@app.route("/Hello")
def hello():
    r=[]
    with open('login.csv','r') as csv_in:
          reader = csv.reader(csv_in)
          for row in reader:
             r.append(row)
          
    return render_template("hello.html")


