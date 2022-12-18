#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 11:37:25 2022

@author: danefolk
"""


#Purpose: Query database using SQL
#Name: Dane Folk
#Date: 31 July 2022
#   Run BuildWeatherDB.py to build weather database before running this program

import sqlite3
import pandas as pd


#file names for database and output file
dbFile = "weather.db"

#format output
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)

#connect to and query weather database 
conn = sqlite3.connect(dbFile)
#Create SQL command
selectCmd = "SELECT temperature, windspeed, textDescription FROM observations where textDescription = 'Clear'; "                
                
#print out the query
result = pd.read_sql_query(selectCmd, conn)
print(result)
