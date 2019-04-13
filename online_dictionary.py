#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 12:58:12 2019

@author: jaipal
"""

import urllib
import re

diction = {}

url = 'https://www.dictionary.com/browse/'

while True:
    term = input('Enter term: ')
    try:
        mean = diction[term]
        print(mean)
    except:
        #check online
        url = urllib.request.urljoin(url,term)
        try:
            page = urllib.request.urlopen(url)
            page = page.read()
            mean = re.findall('<div id="synonyms".*?>(.*?)</div>',str(page))
            mean = re.findall('<a .*?>(.*?)</a>',mean[0])
            diction[term] = mean
            print('mean: ',mean)
        except:
            print('wrong term')

        
        



