from flask import Flask
from datetime import date

app = Flask(__name__)

current_date = str(date.today())

@app.route("/")
def hello_world():
    return """
            <p>Hello, World!</p>
            <p>This is the test page of Emile Girard's NET4255 Project (v0.1), hosted <a href="http://172.17.0.2:5000">here</a></p>
            <p>Today is """ + current_date + """</p>"""