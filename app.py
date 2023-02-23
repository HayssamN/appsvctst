from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def index():
    headers: dict=request.headers
    headers_str:str=''
    for k,v in headers.items():
        headers_str+=f"<p><b>{k}:</b> {v}</p>"
    return f"<h3>All Headers</h3> <div>{headers_str} </div>"


