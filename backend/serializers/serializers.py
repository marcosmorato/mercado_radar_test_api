import json
import locale


def serializer_request_coin(dict):

    serializer = json.loads(dict)

    for value in serializer.values():

        locale.setlocale(locale.LC_ALL, "en_US.utf8")
        dolar = locale.currency(value["USD"], grouping=True)

        value["USD"] = dolar

    return serializer
