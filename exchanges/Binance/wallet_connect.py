from binance.client import Client
import time


def get_keys(file_api_secret, file_api_key):
	if type(file_api_key) != str or type(file_api_secret) != str:
		raise TypeError("Filenames must be strings")

	with open(file_api_secret, 'r') as f: 
        	exchange_secret = f.read()
	        exchange_secret = exchange_secret.strip()# Clean new line character

	with open(file_api_key, 'r') as f:
		exchange_key = f.read()
		exchange_key = exchange_key.strip() # Clean new line character

	return [exchange_secret, exchange_key]


def wallet_connect(exchange_key, exchange_secret):
	client = Client(exchange_key, exchange_secret)

	withdrawal = client.withdraw(
 				asset='BNB',
				address='', # address to
				amount='0.001',
				network='BEP20'
				)
	time.sleep(30) # Sleep for a short time to ensure tx goes

	account_info = client.get_account()
	balances = account_info['balances']
	bals = []
	for balance in balances: # Fetch available balances
		if float(balance['free']) > 0:
			bals.append(balance)
 			#print(f"{balance['asset']} : {balance['free']}")

	return bals
	

[api_secret, api_key] = get_keys('api_secret', 'api_key')
balances = wallet_connect(api_key, api_secret)
print(balances)
