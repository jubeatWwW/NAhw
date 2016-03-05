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

    def Print(self, p):
        i = self.__watches[p]
        print i.title+" ( "+i.link+" )\n"
        print i.description+"\n"
        print "Like: "+i.like+", Dislike: "+i.dislike+"\n\n\n"

    def PrintAll(self):
        for i in self.__watches:
            print i.title+" ( "+i.link+" )\n"
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

            shortenUrl = urllib2.urlopen("https://developer.url.fit/api/shorten?"+urllib.urlencode({'long_url':self.link})).read()
            self.link = "https://url.fit/"+json.loads(shortenUrl)['url']

if __name__ == "__main__":
    #parser = argparse.ArgumentParser(prog='youtube.py', usage='python youtube.py [-h] [-n] keyword')
    parser = argparse.ArgumentParser(prog='youtube.py')

    parser.add_argument('-n', metavar='N', type=int, help='number of search result. default is 5', default=5)
    parser.add_argument('-p', metavar="P", type=int, help='page that you parse', default=0)
    parser.add_argument('keyword')
    results = vars(parser.parse_args())

    a = Youtube(results['keyword'],results['n'])
    if results['p'] > 0:
        a.Print(results['p'])
    else:
        a.PrintAll()
