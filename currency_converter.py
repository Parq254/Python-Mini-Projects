from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.currencyapi.com"
API_KEY = "cur_live_vAsg8euOYay1p0iMST2aE9mv1WtQNFDaLLpH3nYv"

printer = PrettyPrinter()


def get_currencies():
    endpoint = f'/v3/currencies?apikey={API_KEY}'
    url = BASE_URL + endpoint
    data = get(url).json()

    printer.pprint(data)

get_currencies()
