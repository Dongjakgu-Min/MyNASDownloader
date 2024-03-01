import getpass
import os
import argparse
import pathlib

from dotenv import load_dotenv
from datetime import datetime

from auth import authenticate
from download import download


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description='NAS File Downloader')

    url = os.environ.get('URL')
    username = os.environ.get('USERNAME')
    password = os.environ.get('PASSWORD')
    path = os.environ.get('FILE_PATH')

    if path is None:
        path = parser.add_argument('-F', '--file', help='file path you want to download')

    if url is None or username is None or password is None:
        url = input('Synology NAS의 주소를 입력하세요 : ')
        username = input('사용자 이름을 입력하세요 : ')
        password = getpass.getpass('사용자 비밀번호를 입력하세요 : ')
        path = input('다운로드 받을 파일의 경로를 입력하세요 : ')

    sid = authenticate(url, username, password)
    download(url, path, sid)


if __name__ == '__main__':
    main()
