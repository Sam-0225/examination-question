#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 12:14:12 2018

@author: sam0225
"""

import requests
from bs4 import BeautifulSoup

HTML_PARSER = "html.parser"
ROOT_URL = 'http://web.chehjh.kh.edu.tw/wk1/test/'
#TEXT_URL = 'http://web.chehjh.kh.edu.tw/wk1/test/test0623.htm'


def get_link_list(url):
    list_req = requests.get(url)
    if list_req.status_code == requests.codes.ok:
        soup = BeautifulSoup(list_req.content, HTML_PARSER)
        links_a_tags = soup.find_all('a', attrs={'target': '_blank'})

        links = []
        fileName = []
        for link in links_a_tags:
            fileName.append(link['href'])
            li = ROOT_URL + link['href']
            print(li)
            links.append(li)
            download_file(links,fileName)
            
def download_file(links,fileName):
    for i in range(len(links)):
        #url = "http://web.chehjh.kh.edu.tw/wk1/test/"+i
        r = requests.get(links[i])
        with open(fileName[i].replace("/","-"), "wb") as code:
            code.write(r.content)

            

if __name__ == '__main__':
    fileUrl=[]
    """
    for i in range(91,100):
        for j in range(1,3):
            for k in range(1,4):
                file = "test"+str(i)+str(j)+str(k)+".htm"
                print(file)
                fileUrl.append(file)
    """
    for i in range(7):
        for j in range(1,3):
            for k in range(1,4):
                file = "test0"+str(i)+str(j)+str(k)+".htm"
                print(file)
                fileUrl.append(file)
    for list_url in fileUrl:
        #if list_url != "test9111.htm":
        get_link_list(ROOT_URL+list_url)
