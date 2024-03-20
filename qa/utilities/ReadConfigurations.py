# Read Configurations here we add code for read configurations from config file
import os
from configparser import ConfigParser


def read_configuration(category, key):
    # Get the absolute path of the directory where the script is located
    script_directory = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(script_directory, "./../configurations", "config.ini")
    config = ConfigParser()
    config.read(config_file_path)
    return config.get(category, key)
