import requests
from .serializers import serializer_request_coin


def request_coin():

    teste = requests.get(
        "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC&tsyms=USD"
    )

    testando = serializer_request_coin(teste._content)
