"""
Program for downloading files by single link or a list of URLs stored in a file.

There are 2 ways to download files:
    - (1) download 1 file by indicating one link;
    - (2) download multiple files by creating a downloading list file.

Before starting the script create the folder 'downloaded' in the directory of the script.

(1) Execute the file with in a console by ```python downloader.py```.

(2) To download a multiple files please create a simple .txt file and fill it with download links
with absolute path to files (one link per row). Please the file along with the download.py script
"""


import requests
from multiprocessing.pool import ThreadPool
import os


# For downloading a single file
from requests.exceptions import MissingSchema


def download_file(url):
    filename_start = url.rfind('/')+1
    filename = url[filename_start:]
    os.chdir('downloaded')
    # print('Preparing to download {}.'.format(filename))

    r = requests.get(url, stream=True)
    if r.status_code == requests.codes.ok:
        print('The file is ready for downloading.')
        with open(filename, 'wb') as file:
            for data in r:
                file.write(data)
    print('Downloading {} has been finished.'.format(filename))
    return url


# For importing downloading list
def import_list(pool_file):
    with open(pool_file) as imp_file:
        imported_list = imp_file.read().splitlines()
        print(type(imported_list))
        print(imported_list)
        return imported_list


def clear_console():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')


# Input checker
check = None

# Script interface start
print("\n\n=======================================================================\n"
      "Hello dear friend! I'm a download helper.\n"
      "Would you like to get some files.\n")
while check != '0':
    print('If you want to:\n\n'
          '  - get one file         type "1",\n'
          '  - get multiple files   type "2"\n'
          '  - exit                 type "0"\n\n'
          'and press "Enter"')
    check = input()
    if check == '1':
        ask = input('Insert a download URL and press Enter: ')
        try:
            download_file(ask)
        except MissingSchema:
            print('\nThe download URL is missing.\n')

    elif check == '2':
        query = input('Insert a filename (e.g. download.txt) with a list of direct links: ')
        import_list(query)
        list_size = len(import_list(query))
        print('{} files to download.'.format(list_size))
        result = ThreadPool(5).imap_unordered(
            download_file,
            import_list(query),
        )
        for item in result:
            print(item)

    elif check == '0':
        break

    else:
        clear_console()
        print('Please choose downloading method ("1" or "2") or chose "0" to exit\n'
              '====================================================================')
