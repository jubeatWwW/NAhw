#!/usr/bin/env python2.7

import urllib, urllib2, json
from bs4 import BeautifulSoup as BS
import argparse

class Youtube:


    def __init__(self, searchStr):
        BASEURL = "https://www.youtube.com/results?"
        self.searchStr = searchStr
        responseHTML = urllib2.urlopen( BASEURL + urllib.urlencode({'search_query':searchStr}) ).read()
        self.__originHTML = responseHTML
        #soup = BeautifulSoup(responseHTML, 'html.parser')
        soup = BS(responseHTML, 'html.parser')
        temp = soup.find(class_="yt-lockup-title")
        print temp
        print temp.next_siblings


a = Youtube("BGM")

