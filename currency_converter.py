from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.currencyapi.com"
API_KEY = "cur_live_vAsg8euOYay1p0iMST2aE9mv1WtQNFDaLLpH3nYv"

printer = PrettyPrinter()


def get_currencies():
    endpoint = f'/v3/currencies?apikey={API_KEY}'
    url = BASE_URL + endpoint
    _data = get(url).json()['data']

    _data = list(_data.items())
    _data.sort()

    return _data


def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['name']
        symbol = currency['symbol']
        print(f'{name} - {symbol}')


def exchange_rate(code1, code2):
    endpoint = f"https://api.currencyapi.com/v3/convert?value=12 -H apikey:cur_live_vAsg8euOYay1p0iMST2aE9mv1WtQNFDaLLpH3nYv "

    url = BASE_URL + endpoint
    response = get(url)

    _data = response.json()
    printer.pprint(_data)


# _data = get_currencies()
# print_currencies(_data)
exchange_rate('XRP', 'ADA')
