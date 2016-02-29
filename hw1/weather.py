#!/bin/python2.7

import urllib, urllib2, json

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
        if cnt > 5:
            print("Number is too large")
            return
        forecast = [i for i in self.__item['forecast'][:cnt]]
        for day in forecast:
            print(day['date']+" "+day['day']+" "+day['low']+"~"+day['high']+self.unit.upper()+" "+day['text'])

    def GetCurrent(self):
        condition = self.__item['condition']
        print(self.__location+", "+condition['text']+", "+condition['temp']+self.unit.upper())

    def GetSun(self):
        print("sunrise: "+self.__astronomy['sunrise']+", sunset: "+self.__astronomy['sunset'])
