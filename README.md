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
Create and run virtual environment
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
**`[GET] /arbitrage`**  
 Retrieves the arbitrage opportunities between various centralized exchanges

*Request*
- Method: `GET`
- Endpoint: `/arbitage`

- Compulsory request parameters - None


**`[GET] /home`**  
 Serves the home/welcome page

**Request**
- Method: `GET`
- Endpoint: `/home`

- Compulsory request parameters - None


**`[GET] /`**  
 Serves the login page, which will redirect one to sign-up page if they do not have an account

**Request**
- Method: `GET`
- Endpoint: `/`

- Compulsory request parameters - None


**`[POST] /verify_login`**  
 Verifies the user credentials submitted by the login form in the login page

**Request**
- Method: `POST`
- Endpoint: `/verify_login`

- Compulsory request parameters - 'username' and 'password'

**`[GET] /sign_up`**  
Serves the sign-up page/ sign-up form (Upon redirection from '/')

**Request**
- Method: `GET`
- Endpoint: `sign-up`

- Compulsory request parameters - None

**`[POST] /sign_up/add_user`**  
Submits form data to the backend to create a new user in the database

**Request**
- Method: `POST`
- Endpoint: `sign_up/add_user`

- Compulsory request parameters - 'username' and 'password'

To get out of the virtual environment, run this command: `deactivate`
<!--Fun fact: you can force a line break by adding two spaces at the end of the line you intend to not be conjoined with the next -->
