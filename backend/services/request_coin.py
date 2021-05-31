from backend.serializers import serializer_request_coin
import requests


def request_coin():

    res = requests.get(
        "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC&tsyms=USD"
    )

    serializer = serializer_request_coin(res._content)

    return serializer
