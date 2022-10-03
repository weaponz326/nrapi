import requests
import json


def create_customer(email):
    url = "https://api.paystack.co/customer"
    data = {'email': email}
    headers = {'Content-type': 'application/json', 'Authorization': 'Bearer sk_test_5e9093c634e69b7a52bd3a5cda91fa5c18f0b910'}
    r = requests.post(url, data=json.dumps(data), headers=headers)

    return r.json()

def create_subscription(subscription):
    url = "https://api.paystack.co/customer"
    data = {'customer': subscription['customer_code'], 'plan': subscription['plan']}
    headers = {'Content-type': 'application/json', 'Authorization': 'Bearer sk_test_5e9093c634e69b7a52bd3a5cda91fa5c18f0b910'}
    r = requests.post(url, data=json.dumps(data), headers=headers)

    return r.json()

def innitialize_transaction(transaction):
    url = "https://api.paystack.co/transaction/initialize"
    data = {'email': transaction['email'], 'plan': transaction['plan'], 'amount': 99}
    headers = {'Content-type': 'application/json', 'Authorization': 'Bearer sk_test_5e9093c634e69b7a52bd3a5cda91fa5c18f0b910'}
    r = requests.post(url, data=json.dumps(data), headers=headers)

    return r.json()