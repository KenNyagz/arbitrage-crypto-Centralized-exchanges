from flask import Flask, render_template, request, url_for, redirect #jsonify
import os
import sys
import re
from datetime import datetime, timedelta
from authentication import user

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def login():
    return render_template('login.html')

@app.route('/sign_up', strict_slashes=False)
def sign_up():
    return render_template('signUp.html')

@app.route('/sign_up/add_user', strict_slashes=False, methods=['POST'])
def add_user():
    username = request.form.get('username')
    password = request.form.get('password')

    try:
        if user.add_user(username, password):
            return redirect(url_for('homepage'))
    except ValueError:
        return '''
            <body style="background: url('/static/images/error.jpg') no-repeat center center fixed;
                        background-size: 90% 90%;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        margin: 0;
                        padding-top: 100px;
                    ">
                <h1 style="text-align: center">Oops! User already exists</h1>
            </body>
        '''
        #return '<body background="/static/images/error.jpg">\
        #            <h1 style="text-align: center;">Oops! User already exists</h1>\
        #        </body>'
    else:
        return '''
            <body style="background: url('/static/images/error.jpg') no-repeat center center fixed;
                        background-size: 90% 90%;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        margin: 0;
                        padding-top: 100px;
                    ">
                <h1 style="text-align: center">Oops! Failed to create user</h1>
            </body>
        '''

@app.route('/home', strict_slashes=False)
def homepage():
    return render_template('home.html')

@app.route('/verify_login', strict_slashes=False, methods=['POST'])
def verify_credentials():
    username = request.form.get('username')
    password = request.form.get('password')

    if user.user_auth(username, password):
        return redirect(url_for('homepage'))
    else:
        return '''
            <body style="background: url('/static/images/error.jpg') no-repeat center center fixed;
                        background-size: 90% 90%;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        margin: 0;
                        padding-top: 100px;
                    ">
                <h1 style="text-align: center"> Invalid Credentails</h1>
            </body>
        '''
    
@app.route('/arbitrage', strict_slashes=False)
def arbitrage():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    from arbitrage import main
    main() # Call main to get the arbitrage opportunities

    # Read the arbitrage data written to file by main()

    directory = 'ticker_arbs'
    # pattern = r'^(\d{4}-\d{2}-\d{2}_\d{2}\.\d{2}\.\d{2})$'
    pattern = r'^(\d{4}-\d{2}-\d{2}_\d{2}\.\d{2})\.\d{2}$' # Captures upto minutes ignores seconds

    latest_file = None        # Initialize variables to track
    latest_timestamp = None   # the latest file

    for filename in os.listdir(directory):
        match = re.match(pattern, filename)
        if match:
            timestamp_str = match.group(1) # Extract timestamp from filename(ignoring seconds)
                                # Ignoring seconds because fetching arbitrage data takes more than a second, infact takes ~20s

            timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d_%H.%M') # Convert timestamp to a datetime object

            timestamp_with_allowance = timestamp + timedelta(minutes=1)  # Add 1 min allowance to timestamp as minute may change b4 data retrieval is complete
            
            # Update the latest file if there is newer(with the change in min allowance)
            if latest_timestamp is None or timestamp_with_allowance > latest_timestamp:
                latest_timestamp = timestamp_with_allowance
                latest_file = filename

    if latest_file:
        file_path = os.path.join(directory, latest_file)
        with open(file_path, 'r') as file:
            content = file.read()
    else:
        content = '''
            <body style="background: url('/static/images/error.jpg') no-repeat center center fixed;
                        background-size: 90% 90%;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        margin: 0;
                        padding-top: 100px;
                ">
                <h1 style="text-align: center">Oops! Error collecting data. Please Try again</h1>
            </body>
        '''
    
    #with open('ticker_arbs/2024-08-17_10.33.35', 'r') as f:  # For testing
    #    content = f.read()                                   # purposes only

    return content


if __name__ == '__main__':
    app.run(port=5000, debug=True)