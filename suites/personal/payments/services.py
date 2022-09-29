import requests
import json


def initialize_transaction(transaction):
    url = "https://api.paystack.co/transaction/initialize"
    data = {'email': transaction['email'], 'plan': transaction['plan'], 'quantity': transaction['quantity'], 'amount': 99}
    headers = {'Content-type': 'application/json', 'Authorization': 'Bearer sk_test_5e9093c634e69b7a52bd3a5cda91fa5c18f0b910'}
    r = requests.post(url, data=json.dumps(data), headers=headers)

    return r
