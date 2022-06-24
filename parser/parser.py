"""
Program helps with:
 - parsing data from the file
 - counting amount of data repeats
 - exporting data to .csv file
"""
import random
import http
import ipaddress
import datetime
import pandas as pd


# Mock log data
def random_ip_address(seed):
    random.seed(seed)
    return str(ipaddress.IPv4Address(random.getrandbits(32)))


def set_timestamp(start, delta, seed_1, seed_2):
    """
    :param start:  %d-%m-%Y %H:%M:%S
    :param delta:  durations in days
    :param seed_1:   randomize start
    :param seed_2:   randomize end
    :return:       %d-%m-%Y %H:%M:%S within set time and delta period
    """
    random.seed(random.randint(seed_1, seed_2))
    time_format = '%d-%m-%Y %H:%M:%S'
    start_time = datetime.datetime.strptime(start, time_format)
    duration = datetime.timedelta(days=float(delta),
                                  minutes=float(random.randint(0, 50)),
                                  seconds=float(random.randint(0, 59)))
    return start_time + duration


def random_http_statuses(seed_1, seed_2):
    random.seed(random.randint(seed_1, seed_2))
    status_list = [f'{x.name}: {x.value}' for x in http.HTTPStatus]
    return random.choice(status_list)


def random_dict(rows, start_date, duration, seed_1, seed_2):
    categories_dict = {
                       'ip': [random_ip_address(x) for x in range(rows)],
                       'timestamp': [set_timestamp(start_date, duration, seed_1, seed_2) for x in range(rows)],
                       'status': [random_http_statuses(seed_1, seed_2) for x in range(rows)]
                       }
    return categories_dict


# print(random_dict(20, '01-01-2010 0:0:0', 20, 100))

def generate_dataframe(rows, start_date, duration, seed_1, seed_2):
    data = random_dict(rows, start_date, duration, seed_1, seed_2)
    df = pd.DataFrame(data)
    return df


print(generate_dataframe(20, '01-01-2010 0:0:0', 20, 5, 300))



