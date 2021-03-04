from flask import Flask, redirect,url_for
app=Flask(__name__)

@app_route('/')
def hello_kanyi():
    return "Hello Kanyi"
if __name__== "__main__":
    app.run()