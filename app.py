import requests
import json
import ipdb
import time


def request_valor():
    teste = requests.get(
        "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC&tsyms=USD"
    )

    testando = json.loads(teste._content)

    btc = testando["BTC"]
    eth = testando["ETH"]
    ltc = testando["LTC"]

    x = teste._content

    y = json.loads(x)

    ipdb.set_trace()

    print(y)

    return "funcionou"


request_valor()
# request_valor()

# while True:
#     request_valor()
#     time.sleep(10)
