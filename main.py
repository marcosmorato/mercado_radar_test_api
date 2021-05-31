# while True:
#         print(request_coin())
#         time.sleep(100)
import requests
import time
import json


def main():
    while True:
        # print(requests.get("https://mercado-radar-test-request-api.herokuapp.com/").json())
        print(requests.get("http://127.0.0.1:5000/").json())

        time.sleep(5)


if __name__ == "__main__":
    main()
