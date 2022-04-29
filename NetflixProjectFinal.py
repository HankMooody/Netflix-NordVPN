#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import os
import time
import requests
import json
import subprocess as sp
import webbrowser

netflixData = pd.read_csv('Netflix_Data.tsv', sep='\t')
countrySpeed = pd.read_csv('Country_Speed.csv', sep=',')

netflixData_Short = netflixData[["results.title", "results.synopsis"]]
pd.set_option('display.max_colwidth', 10000)

def searchMovie(countrySpeed):
    x = 0
    searchMovie = input("Enter Movie or TV Show Name: ")
    display(netflixData_Short.loc[netflixData_Short['results.title'].str.contains(searchMovie, case=False)])
    movieSelect = input("Select Movie ID (Far left on search result): ")
    movieSelect1 = netflixData.iloc[[movieSelect]]
    movieID = movieSelect1.iat[0, 3]
    countries = movieSelect1.iat[0, 14]
    countries = str(countries)
    country = ""
    while country == "":
        if countrySpeed.iat[x, 0] in countries:
            country = countrySpeed.iat[x, 0]
        else:
        
            x = x + 1
    country = countrySpeed.iat[x, 0]

    nordDir = 'C:\\Program Files\\NordVPN\\'
    current = os.getcwd()
    
#connect to nord server
    os.chdir(nordDir)
    try:
        sp.check_output('nordvpn -c -g \"'+country + '\"' ,shell=True)

    except sp.CalledProcessError as e:
        print("\nConnecting to "+country)
    os.chdir(current)
    time.sleep(3)
    webbrowser.open('https://www.netflix.com/title/'+str(movieID)+"?", new=2)

#To Update Country Speeds, otherwise pulls from file:
countrySpeed = pd.read_csv('Country_Speed.csv', sep=',')

searchMovie(countrySpeed)

#---Uncomment to update Country Speed
#----------------------------------------------------------------
#countries1 = [['Argentina', 'ar42.nordvpn.com', ""], ['Australia', 'au641.nordvpn.com', ""], 
#              ['Belgium', 'be183.nordvpn.com', ""], ['Brazil', 'br86.nordvpn.com', ""], ['Canada', 'ca1334.nordvpn.com', ""],
#              ['France', 'fr840.nordvpn.com', ""], ['Greece', 'gr43.nordvpn.com', ""], ['Hong Kong', 'hk289.nordvpn.com', ""],
#              ['Iceland', 'is48.nordvpn.com', ""], ['India', 'in138.nordvpn.com', ""], ['Israel', 'il54.nordvpn.com', ""], 
#              ['Japan', 'jp585.nordvpn.com', ""], ['Malaysia', 'my42.nordvpn.com', ""], ['Mexico', 'mx91.nordvpn.com', ""], 
#              ['Netherlands', 'nl893.nordvpn.com', ""], ['Portugal', 'pt64.nordvpn.com', ""],
#              ['Singapore', 'sg478.nordvpn.com', ""], ['Sweden', 'se537.nordvpn.com', ""], 
#              ['Thailand', 'th21.nordvpn.com', ""], ['Turkey', 'tr53.nordvpn.com', ""], 
#              ['United Kingdom', 'uk1897.nordvpn.com', ""], ['United States', 'us8114.nordvpn.com', ""]]
#countries1 = pd.DataFrame(countries1, columns = ['Country', 'Server', 'Ping'])
#y=0
#while y<22:
#    output = sp.getoutput('ping ' + countries1.iat[y,1])
#    print(output)    
#    if str('=') in str(output[-5:-2]):
#        countries1.iat[y,2] = int(output[-4:-2])
#    else:
#        countries1.iat[y,2] = int(output[-5:-2])
#    y = y + 1

#countrySpeed = countries1.sort_values(by='Ping', ascending=True) 
#countrySpeed.to_csv('Country_Speed.csv', encoding='utf-8', index=False)
#--------------------------------------------

