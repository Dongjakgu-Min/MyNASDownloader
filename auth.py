from exception import NetworkException
from getpass4 import getpass

import requests
import json


def authenticate(url: str, username: str, password: str) -> str:
    auth_query = {
        'api': 'SYNO.API.Auth',
        'method': 'login',
        'version': 3,
        'account': username,
        'passwd': password,
        'format': 'sid',
        'session': 'dsm_info'
    }

    with requests.get(url + '/webapi/auth.cgi', params=auth_query) as response:
        data = json.loads(response.content)

        if response.status_code == 200 and 'data' in data.keys():
            sid = data['data']['sid']
        else:
            raise NetworkException()

    return sid
