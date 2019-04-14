from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config["DEBUG"] = True

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            
            #textarea {
                margin: 30px 0px 10px 0px;
                width: 540px;
                height: 120px; 
            }
        </style>
    </head>
    <body>
        <form action="/", method="post">
            <label for="rotation">Rotate by:</label>
            <input id="rotation" type="text" name="rot" placeholder="0" />
            <br>
            <input type="textarea" id="textarea" name="text" />
            <br>
            <input type="submit" value="Submit Query" />
        </form>

"""

@app.rout("/", methods=["POST"])
def encrypt(rot, text):
    encrypted_text = rotate_string(rot, text)
    return "<h1>" + encrypted_text + "</h1>"

@app.route("/")
def index():
    return form

@app.route("/hello", methods=["POST"])
def hello():
    first_name = request.form["first_name"]
    return "<h1>Hello, " + first_name + "</h1>"


app.run()

