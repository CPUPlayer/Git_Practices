

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "<h1>WELCOME TO TURAN CYBER HUB and I wrote another extra</h1>"
           "<h2>A CONFLICT IWLL OCCUR SOON ENOUGH<h2>" 
            "<h3>amd this is the third line I craeted I think it looks good</h3>"
            "<h4>This is the fourth line i've created I now have 4 texts<h4>"
if __name__ == "__main__"
    app.run(host="0.0.0.0", port=80)
