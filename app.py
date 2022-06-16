# -*- coding: utf-8 -*-
from flask import Flask,render_template,request,Response,url_for,send_from_directory,redirect
import requests,json,os
from line import Line

app = Flask(__name__)
app.secret_key = 'app2app'  #最好要指定这个参数

@app.route("/")
def index():
    return redirect(url_for('static', filename="html/input.html") )

@app.route("/maker",methods=['GET', 'POST'])
def maker():
    text=request.form["text"]
    sec=text.splitlines()
    while "" in sec:
        sec.remove("")
    secs=[]
    for num,line in enumerate(sec):
        secs.append(Line(num,line))
    return render_template("text.html",secs=secs,nums=len(secs))


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__=="__main__":
    app.run(port= 5000,debug=True)