#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


import urllib, urllib2, json
from bs4 import BeautifulSoup as BS
import argparse

class Youtube:


    def __init__(self, searchStr, cnt):
        BASEURL = "https://www.youtube.com/results?"
        self.searchStr = searchStr
        responseHTML = urllib2.urlopen( BASEURL + urllib.urlencode({'search_query':searchStr}) ).read()
        self.__originHTML = responseHTML

        soup = BS(responseHTML, 'lxml')
        titles = soup.find_all("a", attrs={"class": "yt-uix-tile-link"}, limit=cnt)
        dess = soup.find_all("div", attrs={"class": "yt-lockup-description"}, limit=cnt)
        self.__watches = []

        for i in range(0,len(titles)):
            title = BS(str(titles[i]), 'lxml')
            des = BS(str(dess[i]), 'lxml')
            self.__watches.append(self.Watch(title.a['title'],des.get_text(),title.a['href']))

    def __str__(self):
        return self.searchStr

    def Print(self):
        for i in self.__watches:
            print i.title+" ("+i.link+")\n"
            print i.description+"\n"
            print "Like: "+i.like+", Dislike: "+i.dislike+"\n\n\n"

    class Watch:
        def __init__(self, title, description, link):
            self.title = title
            self.description = description
            self.link = "https://www.youtube.com"+link
            linkInfoHTML = urllib2.urlopen( self.link).read()
            linkSoup = BS(linkInfoHTML, 'lxml')
            like = linkSoup.find("button", attrs={"class": "like-button-renderer-like-button"}, recursive=True)
            dislike = linkSoup.find("button", attrs={"class": "like-button-renderer-dislike-button"}, recursive=True)
            self.like = BS(str(like), 'lxml').span.get_text()
            self.dislike = BS(str(dislike), 'lxml').span.get_text()

if __name__ == "__main__":
    a = Youtube("the beginning",3)
    a.Print()
