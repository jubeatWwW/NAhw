#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


import urllib, urllib2, json
from bs4 import BeautifulSoup as BS
import argparse

class Youtube:


    def __init__(self, searchStr, cnt, page):
        BASEURL = "https://www.youtube.com/results?"
        self.searchStr = searchStr
        responseHTML = urllib2.urlopen( BASEURL + urllib.urlencode({'search_query':searchStr,'page':page}) ).read()
        self.__originHTML = responseHTML

        soup = BS(responseHTML, 'lxml')
        content = soup.find_all('div', attrs={"class": "yt-lockup-content"}, limit=cnt, recursive=True)
        self.__watches = []
        for i in content:
            data = BS(str(i), 'lxml')
            TagTitle = data.find("a", attrs={"class": "yt-uix-tile-link"})
            TagDes = data.find("div", attrs={"class": "yt-lockup-description"})
            if TagDes != None:
                realTitle = BS(str(TagTitle), 'lxml')
                realDes = BS(str(TagDes), 'lxml')
                self.__watches.append(self.Watch(realTitle.a['title'],realDes.get_text(), realTitle.a['href']))
            else:
                realTitle = BS(str(TagTitle), 'lxml')
                self.__watches.append(self.Watch(realTitle.a['title'],"**No description.**", realTitle.a['href']))


    def __str__(self):
        return self.searchStr

    def Print(self, p):
        i = self.__watches[p]
        print i.title+" ( "+i.link+" )\n"
        print i.description+"\n"
        print i.likeInfo

    def PrintAll(self):
        print "\n"
        for i in self.__watches:
            print i.title+" ( "+i.link+" )\n"
            print i.description+"\n"
            print i.likeInfo

    class Watch:
        def __init__(self, title, description, link):
            self.title = title
            self.description = description
            self.link = "https://www.youtube.com"+link

            linkInfoHTML = urllib2.urlopen( self.link).read()
            linkSoup = BS(linkInfoHTML, 'lxml')
            like = linkSoup.find("button", attrs={"class": "like-button-renderer-like-button"}, recursive=True)
            dislike = linkSoup.find("button", attrs={"class": "like-button-renderer-dislike-button"}, recursive=True)
            likeObj = BS(str(like), 'lxml')
            dislikeObj = BS(str(dislike), 'lxml')
            if likeObj.span == None or dislikeObj == None:
                self.likeInfo = "**We can't get this info**\n**It may cause by removed comment function or this is a link of youtube user**\n\n\n"
            else:
                self.likeInfo = "Like: "+likeObj.span.get_text()+", Dislike: "+dislikeObj.span.get_text()+"\n\n\n"

            shortenUrl = urllib2.urlopen("https://developer.url.fit/api/shorten?"+urllib.urlencode({'long_url':self.link})).read()
            self.link = "https://url.fit/"+json.loads(shortenUrl)['url']

if __name__ == "__main__":
    #parser = argparse.ArgumentParser(prog='youtube.py', usage='python youtube.py [-h] [-n] keyword')
    parser = argparse.ArgumentParser(prog='youtube.py')

    parser.add_argument('-n', metavar='N', type=int, help='number of search result. default is 5', default=5)
    parser.add_argument('-p', metavar="P", type=int, help='page that you parse', default=1)
    parser.add_argument('keyword')
    results = vars(parser.parse_args())

    a = Youtube(results['keyword'],results['n'], results['p'])
    a.PrintAll()
