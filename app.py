from flask import Flask,request
import requests
app = Flask(__name__)

@app.route("/")
def index():
    headers: dict=request.headers
    headers_str:str=''
    for k,v in headers.items():
        headers_str+=f"<p><b>{k}:</b> {v}</p>"
    return f"<h3>All Headers</h3> <div>{headers_str} </div>"


@app.route("/hello")
def hello():
    headers: dict=request.headers
    if "X-Ms-Client-Principal-Name" not in headers:
        return "Sorry, you are not logged in, please <a href=\".auth/aad\">login</a>"
    
    req=requests.get('/.auth/me')
    return req.body
