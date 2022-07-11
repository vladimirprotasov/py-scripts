"""
Program helps with:
 - parsing data from the file
 - counting amount of data repeats
 - exporting data to .csv file

 Example 1:
 HTTP log: data = generate_dataframe(1000, '01-01-2010 0:0:0', 20, 5, 300)

 Example 2:


"""
import random
import http
import ipaddress
import datetime
import pandas as pd
import re


# Mock log data - pandas
def random_ip_address(seed):
    random.seed(seed)
    return str(ipaddress.IPv4Address(random.getrandbits(32)))


def random_float(start, end):
    result = random.uniform(start, end)
    return round(result, 2)


def set_timestamp(start, delta, seed_1, seed_2, time_format='%d-%m-%y %H:%M:%S'):
    """
    :param start:  %d-%m-%Y %H:%M:%S
    :param delta:  durations in days
    :param seed_1:   randomize start
    :param seed_2:   randomize end
    :param time_format: datetime format, default = '%d-%m-%Y %H:%M:%S'
    :return:       %d-%m-%Y %H:%M:%S within set time and delta period
    """
    random.seed(random.randint(seed_1, seed_2))
    start_time = datetime.datetime.strptime(start, time_format)
    duration = datetime.timedelta(days=float(delta),
                                  minutes=float(random.randint(0, 50)),
                                  seconds=float(random.randint(0, 59)))
    return start_time + duration


def random_http_statuses(seed_1, seed_2):
    random.seed(random.randint(seed_1, seed_2))
    status_list = [f'{x.name}: {x.value}' for x in http.HTTPStatus]
    return random.choice(status_list)


def ip_dict(rows, start_date, duration, seed_1, seed_2):
    data_dict = {
       'ip': [random_ip_address(x) for x in range(rows)],
       'timestamp': [set_timestamp(start_date, duration, seed_1, seed_2, '%d-%m-%Y %H:%M:%S') for _ in range(rows)],
       'status': [random_http_statuses(seed_1, seed_2) for _ in range(rows)]
    }
    return data_dict


def frequency_dict(rows, start_date, duration, seed_1, seed_2):
    data_dict = {
        'frequency': [random_float(seed_1, seed_2) for _ in range(rows)],
        'date': [set_timestamp(start_date, duration, seed_1, seed_2, '%Y-%m-%d %H:%M:%S') for _ in range(rows)],
        'region_id': [random.randint(1, 3) for _ in range(rows)]

    }
    return data_dict


# def get_url_dict(amount):
#     # format: Image_URL;needed_amount_of_shows;category1;category2;category3; … ;category N
#     categories = {
#         1: ['flight', 'airplane'],
#         2: ['show', 'britain', 'sketches', 'tv'],
#         3: ['games', 'minecraft', 'blocks', 'sandbox'],
#         4: ['onlycategory']
#     }
#     url_list = [f'http://localhost:8080/static/'
#                 f'image1.jpg;'
#                 f'500;'
#                 f'flight;airlplane']


def generate_dataframe(dict_name, rows, start_date, duration, seed_1, seed_2):
    """
    :param dict_name: dictionary name
    :param rows: amount of records
    :param start_date: log time start in dd-mm-YYYY H:M:S format
    :param duration: duration in days
    :param seed_1: seed range start
    :param seed_2: seed range end
    :return: dataframe
    """
    df = pd.DataFrame(dict_name(rows, start_date, duration, seed_1, seed_2))
    return df


def df_get_csv(df: pd.DataFrame, filename: str = 'data.csv', separator: str = '\t', encode: str = 'utf-8'):
    """

    :param df: Pandas DataFrame
    :param filename: like "data.csv"
    :param separator: like "\t"
    :param encode: like "utf-8"
    :return: CSV file
    """
    return df.to_csv(filename, sep=separator, encoding=encode)


# data = generate_dataframe(ip_dict, 1000, '01-01-2021 0:0:0', 5, 50, 300)
data = generate_dataframe(frequency_dict, 300, '2022-07-20 0:0:0', 10, 20, 125)
df_get_csv(data)
