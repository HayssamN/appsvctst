from flask import Flask,request
import requests
app = Flask(__name__)

@app.route("/")
def index():
    headers: dict=request.headers
    headers_str:str=''
    cookies_str:str=''
    for k,v in headers.items():
        headers_str+=f"<p><b>{k}:</b> {v}</p>"
    for k,v in request.cookies.items():
        cookies_str+=f"<p><b>{k}:</b> {v}</p>"
    return f"<h2>Headers</h2> <div>{headers_str} </div><h2>Cookies</h2> <div>{cookies_str} </div>"


@app.route("/hello")
def hello():
    headers: dict=request.headers
    if "X-Ms-Client-Principal-Name" not in headers or "AppServiceAuthSession" not in request.cookies:
        return "Sorry, you are not logged in, please <a href=\".auth/login/aad\">login</a>"

    userEmail=headers["X-Ms-Client-Principal-Name"]
    req=requests.get(f'https://{headers["Disguised-Host"]}/.auth/me',cookies=request.cookies)
    return f"<div><p>Hi {userEmail}, <a href=\".auth/logout\">Logout</a></p></div>" + req.text
