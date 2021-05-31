# while True:
#         print(request_coin())
#         time.sleep(100)
import requests
import time
import json


def main():
    while True:
        print(
            requests.get("https://mercado-radar-test-request-api.herokuapp.com/").json()
        )

        time.sleep(5)


if __name__ == "__main__":
    main()
