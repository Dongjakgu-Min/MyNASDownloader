import requests
import json


def file_select(url: str, path: str, sid: str):
    file_list = _file_list(url, path, sid)

    while True:
        file_name = input('write filename want to download : ')
        if file_name not in file_list:
            print('[ERROR] file not found')
        else:
            break

    return file_name


def _file_list(url: str, path: str, sid: str):
    file_list = []

    download_query = {
        'api': 'SYNO.FileStation.List',
        'version': 2,
        'method': 'list',
        'folder_path': path,
        '_sid': sid
    }

    response = requests.get(url + "/webapi/entry.cgi", params=download_query)
    data = json.loads(response.content)

    print('---------------------')
    print('      FILENAME       ')
    print('---------------------')

    for item in data['data']['files']:
        file_list.append(item['name'])
        print(item['name'])

    print('---------------------')
    return file_list
