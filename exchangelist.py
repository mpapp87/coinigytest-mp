import json
import urllib
import requests
import time

# This code should return a list of all the exchanges
# With the correct API key this returns the following output: {u'err_msg': u'Invalid API Key', u'err_num': u'1055-00-01'}

#I know the API keys are accurate because I tested them from a unix shell with the following code

#curl -H "X-API-KEY:inputkeyhere" -H "X-API-SECRET:inputsecretkeyhere" -X POST "https://www.coinigy.com/api/v1/exchanges"


headers = {
    'contenttype' : 'application/json',
    'apikey' : 'inputcoinigykeyhere',
    'apisecret' : 'inputsecretcoinigykeyhere'
}

r = requests.get('https://www.coinigy.com/api/v1/exchanges', headers=headers)

#response_body = requests.get(r)
print(r).json()
