from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True
@app.route('/', methods=['POST'])
def web_encrypt():
    rotnumber = int(request.form['rot'])
    etext = request.form['text']
    encrypted_text = encrypt(etext, rotnumber)
    return form.format(encrypted_text)
    

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
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="post">
            <label for="rot">Rotate By:</label>
            <input type="text" name="rot" value="0">
            <br>
            <textarea type="text" name="text">{0}</textarea>
            <br>
            <input type="submit">
        </form> 
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

app.run()