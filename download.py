import requests

from tqdm import tqdm


def download(url: str, path: str, sid: str):
    download_query = {
        'api': 'SYNO.FileStation.Download',
        'version': 2,
        'method': 'download',
        'path': path,
        'mode': 'download',
        '_sid': sid
    }

    response = requests.get(url + "/webapi/entry.cgi", params=download_query, stream=True)
    total_size = int(response.headers.get("content-length", 0))

    with tqdm(total=total_size, unit='b', unit_scale=True) as progress_bar:
        with open(path.split('/')[-1], "wb") as f:
            for data in response.iter_content(1024):
                progress_bar.update(len(data))
                f.write(data)
