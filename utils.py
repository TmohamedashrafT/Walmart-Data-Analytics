import concurrent.futures
import multiprocessing
import configparser
import os
import sys
import os

config = configparser.ConfigParser(allow_no_value=True)
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'config.ini'))
config.read(config_path)

def get_config_value(i_section, i_key):
    return config[i_section][i_key]

def threads(target_func, iterator, max_workers=multiprocessing.cpu_count()):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        return executor.map(target_func, iterator)
