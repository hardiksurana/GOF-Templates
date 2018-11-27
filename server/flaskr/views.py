from server.flaskr import app

from flask import Flask,render_template,redirect,url_for,flash, redirect, request, session, abort, jsonify, Response, send_from_directory,send_file
from werkzeug import secure_filename
import os
import datetime
import json
import sys
import tarfile

# sys.path.insert(0, '../../')
from GOF_templates import render

app.secret_key = 'secretkeyhereplease'

@app.route("/")
def home():
    return render_template("index.html",title="GOF-Templates")

@app.route("/state")
def state():
    return render_template("patterns/state.html", title="State", inpValueField1="States", inpValueField2="Functions")

@app.route("/strategy")
def strategy():
    return render_template("patterns/strategy.html", title="Strategy")

@app.route("/singleton")
def singleton():
    return render_template("patterns/singleton.html", title="Singleton")

@app.route("/decorator")
def decorator():
    return render_template("patterns/decorator.html", title="Decorator")

@app.route("/adapter")
def adapter():
    return render_template("patterns/adapter.html", title="Adapter")

@app.route("/mediator")
def mediator():
    return render_template("patterns/mediator.html", title="Mediator")

@app.route("/iterator")
def iterator():
    return render_template("patterns/iterator.html", title="Iterator")

@app.route("/codeCreate", methods=["POST"])
def codeCreate():
    statesList = request.form.getlist("statesList")[0].split(',')
    retType = request.form.getlist("retType")
    funcName = request.form.getlist("funcName")
    paramTypeList = request.form.getlist("paramTypeList")
    paramNameList = request.form.getlist("paramNameList")

    # create json to be passed to State class
    inpData = {}
    inpData['pattern'] = 'state'
    inpData['states'] = []
    for state in statesList:
        inpData['states'].append({'name': state})
    
    inpData['functions'] = []

    for i in range(len(funcName)):
        function = {}
        function['name'] = funcName[i]
        function['param_types'] = paramTypeList[i].split(',')
        function['param_names'] = paramNameList[i].split(',')
        function['return'] = retType[i]
        inpData['functions'].append(function)
    
    s = render.State(json.loads(json.dumps(inpData)))
    s.render()
    flash("Files for State Pattern are created!")
    # TODO Redirect to downloads URL
    return redirect(url_for("codeDownload",filename="State.tar.gz"))


@app.route("/codeDownload/<path:filename>",methods=["GET","POST"])
def codeDownload(filename):
    makeTarfile(os.path.join(app.config['CODE_DOWNLOAD_FOLDER'],filename),"./GOF_templates/templates/output/state")
    print("Path:",os.path.join(app.config['USER_DOWNLOAD_FOLDER'],filename))
    return send_from_directory(app.config['USER_DOWNLOAD_FOLDER'],filename,as_attachment=True)

def makeTarfile(outputFilename, sourceDir):
    with tarfile.open(outputFilename, "w:gz") as tar:
        tar.add(sourceDir, arcname=os.path.basename(sourceDir))