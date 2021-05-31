import json
import ipdb
import requests

import time, threading


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

    # ipdb.set_trace()
    print(teste)

    return y


# request_valor()


def verificando():
    return "Marcos"


class SetInterval:
    def __init__(self, interval, action):
        self.interval = interval
        self.action = action
        self.stopEvent = threading.Event()
        thread = threading.Thread(target=self.__setInterval)
        thread.start()

    def __setInterval(self):
        next_time = time.time() + self.interval
        while not self.stopEvent.wait(next_time - time.time()):
            next_time += self.interval
            self.action

    def cancel(self):
        self.stopEvent.set()


while True:
    request_valor()
    time.sleep(10)

inter = SetInterval(0.6, verificando)
t = threading.Timer(5, inter.cancel)
t.start()
print(inter.action)
