# ARBITRAGE COVE

The project aims to seek as many possible and legitimate arbitrage opportunities between centralized crytocurrency exchanges.

It collects data from various cryptocurrency exchanges via their API endpoints, processes and filters that data then stores the resulting symbols and their prices. It then proceeds to compare the price data two exchanges at a time. For the symbols that are common between the two exchanges being compared, the price difference is compared as a percentage. If it's above a certain threshold(3%) it is saved as a potential arbitrage opportunity. All potential arbitrage opportunities are then printed out.

### Set up
Clone the repository:
```bash
git clone https://github.com/KenNyagz/arbitrage-crypto-Centralized-exchanges.git
```

Navigate to the project directory
```bash
cd arbitrage-crpto-Centralized-exchanges
```
Create and run a virtual environment
```
python3 -m venv Virt
source Virt/bin/activate
```
Install dependencies
```
pip install -r requiremnts.txt
```

Start the server
```
python3 app/routes.py
```

### API
#### Base Url
https://romanruins.tech (Hosting not yet complete)

#### API endpoints:
1 **`[GET] /arbitrage`**  
 Retrieves the arbitrage opportunities between various centralized exchanges

*Request*
- Method: `GET`
- Endpoint: `/arbitage`

- Compulsory request parameters - None

*This is the main API endpoint and the only endpoint that can be used outside a browser*


2 **`[GET] /home`**  
 Serves the home/welcome page

**Request**
- Method: `GET`
- Endpoint: `/home`

- Compulsory request parameters - None


3 **`[GET] /`**  
 Serves the login page, which will redirect one to the sign-up page if they do not have an account

**Request**
- Method: `GET`
- Endpoint: `/`

- Compulsory request parameters - None


4 **`[POST] /verify_login`**  
 Verifies the user credentials submitted in the login form from the login page

**Request**
- Method: `POST`
- Endpoint: `/verify_login`

- Compulsory request parameters - 'username' and 'password'

5 **`[GET] /sign_up`**  
Serves the sign-up page/ sign-up form (Upon redirection from '/')

**Request**
- Method: `GET`
- Endpoint: `sign-up`

- Compulsory request parameters - None

6 **`[POST] /sign_up/add_user`**  
Submits the form data submitted in the sign-up form to the backend to create a new user in the database

**Request**
- Method: `POST`
- Endpoint: `sign_up/add_user`

- Compulsory request parameters - 'username' and 'password'
<br>
To get out of the virtual environment, run this command: `deactivate`

<!--Fun fact: you can force a line break by adding two spaces at the end of the line you intend to not be conjoined with the next -->
