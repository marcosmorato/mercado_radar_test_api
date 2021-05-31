import json
import ipdb
import locale


def serializer_request_coin(dict):

    # serializer = json.loads(dict)

    # serializer["B"]

    s = 37103.55

    locale.setlocale(locale.LC_ALL, "en_US.utf8")
    teste = locale.currency(s, grouping=True)

    ipdb.set_trace()

    # for k, v in serializer.items():
    #     coin = v["USD"]

    return "serializer"


serializer_request_coin("152")
