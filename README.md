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
 Serves the home page

**Request**
- Method: `GET`
- Endpoint: `/home`

- Compulsory parameters - None


**`[POST] /`**  
 Serves the login/sign-up page

**Request**
- Method: `GET`
- Endpoint: `/`

- Compulsory parameters - None


**`[GET] /verify`**  
 Serves the home page

**Request**
- Method: `POST`
- Endpoint: `/verify_login`

- Compulsory parameters - 'username' and 'password'

<!--Fun fact: you can force a line break by adding two spaces at the end of the line you intend to not be conjoined with the next -->