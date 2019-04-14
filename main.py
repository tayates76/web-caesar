from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config["DEBUG"] = True

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            
            textarea {{
                margin: 10px 0px;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/", method="post">
            <label for="rotation">Rotate by:</label>
            <input id="rotation" type="text" name="rot" placeholder="0" />
            <br>
            <textarea name="text">
            {0}
            </textarea>
            <br>
            <input type="submit" value="Submit Query" />
        </form>
    </body>
</html>

"""

@app.route("/", methods=["POST"])
def encrypt():
    rot = int(request.form["rot"])
    text = request.form["text"]
    encrypted_text = rotate_string(rot, text)
    return form.format(encrypted_text)

@app.route("/")
def index():
    return form.format("")

@app.route("/hello", methods=["POST"])
def hello():
    first_name = request.form["first_name"]
    return "<h1>Hello, " + first_name + "</h1>"


app.run()

