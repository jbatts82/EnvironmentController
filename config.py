###############################################################################
# File Name  : myConfig.py
# Date       : 08/24/2020
# Description: configuration 
###############################################################################

import os
import os.path
from os import path
from configparser import ConfigParser
import SupportFiles.File_Handler as fh
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MYT = 23

    # external configs
    CONFIG_FILE = '/home/mario/EnvironmentController/my_config.txt'

    # Data base Configurations, 
    # relative database needs /
    #database_loc = '/db_test.db'
    database_loc = '/home/mario/EnvironmentController/db_test.db'

    # Sensor Configurations
    sensor_cnt = 4
    sensor_configs = []
    sensor_configs.append({"name":"plant1", "data_pin":17, "assigned":False, "sensor_type":11})
    sensor_configs.append({"name":"plant2", "data_pin":26, "assigned":False, "sensor_type":11})
    sensor_configs.append({"name":"intake_air", "data_pin":27, "assigned":False, "sensor_type":11})
    sensor_configs.append({"name":"upper_room_air", "data_pin":22, "assigned":False, "sensor_type":11})
    
    

    time_table = []
    time_table.append({"hour":0, "name":'Late Night', "temp":68})
    time_table.append({"hour":4, "name":'Early Morning', "temp":72})
    time_table.append({"hour":8, "name":'Morning', "temp":74})
    time_table.append({"hour":12, "name":'After Noon', "temp":76})
    time_table.append({"hour":16, "name":'Evening', "temp":73})
    time_table.append({"hour":20, "name":'Night', "temp":70})


    def __init__(self):
        self.init_file()

    def init_file(self):
        print("Processing         : Config file")
        if path.exists(self.CONFIG_FILE):
            self.config = fh.get_from_file(self.CONFIG_FILE)
        else:
            self.config = fh.create_file(self.CONFIG_FILE)
        print("Success Processing : Config Object Created")
        
    def get_config_file(self):
        self.update_config()
        self.FAN_OVERRIDE = self.config[0]
        self.FAN_OVER_STATE = self.config[1]
        self.HUM_OVERRIDE = self.config[2]
        self.MAX_TEMP_THRESH = self.config[3]
        self.MIN_TEMP_THRESH = self.config[4]
        self.MAX_HUMIDITY_THRESH = self.config[5]
        self.MIN_HUMIDITY_THRESH = self.config[6]
    
    def update_config(self):
        self.config = fh.get_from_file(self.CONFIG_FILE)

    def get_from_file(self, in_file):
        # open file and put into list
        out_list = []
        with open(in_file, 'r') as filehandle:
            for line in filehandle:
                remove_new_line = line[:-1]
                out_list.append(remove_new_line)
        return out_list