import base64
import hashlib
import hmac
import json
import time
from urllib.request import urlopen, Request

class CoinoneApi:
    ACCESS_TOKEN = None
    SECRET_KEY = None
    UPPERCASE_SECRET_KEY = None
    HOST = 'https://api.coinone.co.kr/'

    def __init__(self, token, key):
        self.ACCESS_TOKEN = token;
        self.SECRET_KEY = key;
        self.UPPERCASE_SECRET_KEY = key.upper()
        pass

    def get_base_payload(self):
        return {
            'access_token': self.ACCESS_TOKEN,
        }


    def str_2_byte(self, s, encode='utf-8'):
        return bytes(s, encode)


    def get_encoded_payload(self, payload):
        payload['nonce'] = int(time.time()*1000)
        dumped_json = json.dumps(payload)
        encoded_json = base64.b64encode(self.str_2_byte(dumped_json))
        return encoded_json


    def get_signature(self, encoded_payload):
        signature = hmac.new(self.str_2_byte(self.UPPERCASE_SECRET_KEY), encoded_payload, hashlib.sha512)
        return signature.hexdigest()

    def create_payload(self, data):
        payload = self.get_base_payload()
        payload.update(data)
        return payload

    def get_response(self, url, payload):
        encoded_payload = self.get_encoded_payload(payload)
        signature = self.get_signature(encoded_payload)
        headers = {
            'Content-Type': 'application/json',
            'X-COINONE-PAYLOAD': encoded_payload,
            'X-COINONE-SIGNATURE': signature,
        }
        api_url = self.HOST + url
        req = Request(api_url, data=encoded_payload, headers=headers, method='POST')

        with urlopen(req) as res:
            data = res.read().decode('utf-8')
            return json.loads(data)
