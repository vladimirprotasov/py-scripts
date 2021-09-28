"""Program for downloading files by single link or a list of URLs stored in a file"""

import requests
from multiprocessing.pool import ThreadPool
import os


# For downloading a single file
def download_file(url):
    filename_start = url.rfind('/')+1
    filename = url[filename_start:]
    os.chdir('downloaded')
    print('Готовлюсь скачать {}.'.format(filename))

    r = requests.get(url, stream=True)
    if r.status_code == requests.codes.ok:
        print('Файл доступен для скачивания.')
        with open(filename, 'wb') as file:
            for data in r:
                file.write(data)
    print('Скачивание файла {} завершено.'.format(filename))
    return url


def import_list(pool_file):
    with open(pool_file) as imp_file:
        imported_list = imp_file.read().splitlines()
        print(type(imported_list))
        print(imported_list)
        return imported_list


# Multiple urls check
print('Если вы хотите скачать один файл, то введите "1", а если несколько файлов, то нажмите "2"')
check = input()
if check == '1':
    ask = input('Укажите ссылку на скачивание файла: ')
    download_file(ask)
elif check == '2':
    query = input('Укажите имя файла со списком ссылок на скачивание: ')
    import_list(query)
    list_size = len(import_list(query))
    print('{} files to download.'.format(list_size))
    result = ThreadPool(5).imap_unordered(
        download_file,
        import_list(query),
    )
    for item in result:
        print(item)
