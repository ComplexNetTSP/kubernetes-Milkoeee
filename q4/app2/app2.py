from flask import Flask, request
import pymongo as pm
import datetime


ConnectionString="mongodb://root:example@mongo:27017/"
client=pm.MongoClient(ConnectionString)

db = client["Visitors"]
visitors = db["visitors"]
N=10
app = Flask(__name__)

print(list)
@app.route("/")
def hello_world():
    ip = request.remote_addr
    post = {

        "ip": ip,

        "date": datetime.datetime.now(tz=datetime.timezone.utc),
    }

    post_id = visitors.insert_one(post).inserted_id
    visits = """ \n """
    for visitor in visitors.find().sort('date', pm.DESCENDING).limit(N):
         visits += "<p>" + str(visitor) + "</p>" + "\n"
         
    return """
            <p>Hello, World!</p>
            <p>This is the test page of Emile Girard's NET4255 Project (V2), hosted <a href="http://127.0.0.1:5000">here</a></p>
            <p>Today is """ + str(datetime.date.today()) + """</p>
            <p>IP : """ + str(ip) + """</p>
            <p>Visitors : </p>""" + visits
