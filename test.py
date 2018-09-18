#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: Mxyzptlk
# Date: 2018-09-18

from bs4 import BeautifulSoup
import requests

url = 'https://www.tripadvisor.cn/Attractions-g190454-Activities-Vienna.html'

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')

titles = soup.select('div.item.name > a')
imgs = soup.select('img[width="200"]')
cates = soup.select('#taplc_attraction_coverpage_attraction_0 > div > div:nth-of-type(1) > div > div > div.shelf_item_container > div:nth-of-type(4) > div.poi > div > div:nth-type(3)')



print(titles,imgs,cates, sep='\n\n----------------------------------------------'
                       '---------------------------------------------\n\n')
