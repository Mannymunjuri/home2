from flask import Flask,redirect,url_for,render_template
app = Flask(__name__)

@app.route('/username', methods=['GET, POST'])
def username():
    return "username"

@app.route('/password')
def password():
    return "password"


if __name__ == '__main__':
   app.run(debug = True)
