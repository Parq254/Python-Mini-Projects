from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.currencyapi.com"
API_KEY = "cur_live_vAsg8euOYay1p0iMST2aE9mv1WtQNFDaLLpH3nYv"

printer = PrettyPrinter()


def get_currencies():
    endpoint = f'/v3/currencies?apikey={API_KEY}'
    url = BASE_URL + endpoint
    currency_data = get(url).json()['data']

    currency_data = list(currency_data.items())
    currency_data.sort()

    return currency_data


def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['CurrencyName']
        _id = currency['id']
        symbol = currency.get('currencySymbol', '')
        print(f'{_id} - {name} - {symbol}')



currency_data = get_currencies()
printer.pprint(currency_data)

