#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import urllib, urllib2, json
import argparse

class Weather:
    def __init__(self,location,unit="f"):
        BASEURL = "https://query.yahooapis.com/v1/public/yql?"

        if unit != "c" and unit != "f":
            raise NameError("Invalid Unit!")
        self.unit = unit
        query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text=\""+location+"\")and u='"+unit+"'"
        yqlUrl = BASEURL + urllib.urlencode({'q':query}) + "&format=json"
        content = json.loads(urllib2.urlopen(yqlUrl).read())['query']['results']['channel']
        self.__item = content['item']
        self.__location = content['location']['city']
        self.__astronomy = content['astronomy']


    def __str__(self):
        return str(self.__location)

    def GetForecast(self,cnt):
        if int(cnt) > 5:
            print("Number is too large")
            return
        forecast = [i for i in self.__item['forecast'][:int(cnt)]]
        for day in forecast:
            print(day['date']+" "+day['day']+" "+day['low']+"~"+day['high']+self.unit.upper()+" "+day['text'])

    def GetCurrent(self):
        condition = self.__item['condition']
        print(self.__location+", "+condition['text']+", "+condition['temp']+self.unit.upper())

    def GetSun(self):
        print("sunrise: "+self.__astronomy['sunrise']+", sunset: "+self.__astronomy['sunset'])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='weather.py', usage='python weather.py [-h] [-l location] [-u unit] [-a | -c | -d day | -s]')

    parser.add_argument('-l', metavar="location",required=True, help="locations")
    parser.add_argument('-u', metavar="unit", choices=['f','c'], default='f', help="unit")
    parser.add_argument('-a', action='store_true', help="equal to -c -d 5 -s")
    parser.add_argument('-c', action='store_true', help="current condition")
    parser.add_argument('-d', metavar="day", help="forecast")
    parser.add_argument('-s', action="store_true", help="sunset/sunrise")

    args = parser.parse_args()
    results = vars(args)

    if not results['a'] and not results['c'] and not results['d'] and not results['s']:
        parser.error("Need at least one information type")

    weather = Weather(results['l'], results['u'])

    if results['a']:
        weather.GetCurrent()
        weather.GetForecast(5)
        weather.GetSun()
    else:
        if results['c']:
            weather.GetCurrent()
        if results['d'] != None:
            weather.GetForecast(results['d'])
        if results['s']:
            weather.GetSun()


