import getpass
import os
import argparse

from dotenv import load_dotenv
from datetime import datetime

from auth import authenticate
from download import download
from exception import ParameterNotFoundException
from file_list import file_select


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description='NAS File Downloader')
    parser.add_argument('-F', '--file', help='file path you want to download')
    parser.add_argument('-M', '--manual', help='find file manually', default=False, action='store_true')
    parser.add_argument('-p', '--path', help='file list path', default=False, required=False)

    args = parser.parse_args()

    url = os.environ.get('NAS_URL')
    username = os.environ.get('NAS_USERNAME')
    password = os.environ.get('NAS_PASSWORD')

    file_path, manual, dir_path = args.file, args.manual, args.path

    if dir_path is None:
        raise ParameterNotFoundException()

    if file_path is None and manual is False:
        file_path = '{0}/{1}'.format(os.environ.get('FILE_PATH'), datetime.now().strftime('%Y.%m.%d.ppt'))

    if url is None or username is None or password is None:
        url = input('Synology NAS의 주소를 입력하세요 : ')
        username = input('사용자 이름을 입력하세요 : ')
        password = getpass.getpass('사용자 비밀번호를 입력하세요 : ')
        file_path = input('다운로드 받을 파일의 경로를 입력하세요 : ')

    sid = authenticate(url, username, password)

    if manual:
        filename = file_select(url, dir_path, sid)
        download(url, '{0}/{1}'.format(dir_path, filename), sid)
    else:
        download(url, file_path, sid)


if __name__ == '__main__':
    main()
