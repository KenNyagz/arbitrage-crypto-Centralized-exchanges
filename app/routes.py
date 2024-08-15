from flask import Flask, render_template, request, url_for, redirect, jsonify
import os
import sys

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def login():
    return render_template('login.html')

@app.route('/home', strict_slashes=False)
def homepage():
    return render_template('home.html')

@app.route('/verify_login', strict_slashes=False, methods=['POST'])
def verify_credentials():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'user' and password == 'pass':
        return redirect(url_for('homepage'))
    else:
        return "Invalid Credentails", 403
    
@app.route('/arbitrage', strict_slashes=False)
def arbitrage():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    from arbitrage import main
    arb_data = main()
    return arb_data


if __name__ == '__main__':
    app.run(port=5000, debug=True)
