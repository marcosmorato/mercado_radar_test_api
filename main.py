import requests
import time
import json


def main():
    while True:
        print(
            requests.get("https://mercado-radar-test-request-api.herokuapp.com/").json()
        )

        time.sleep(100)


if __name__ == "__main__":
    main()
