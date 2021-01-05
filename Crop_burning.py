### Importing all necessarry packages
from selenium import webdriver
from bs4 import BeautifulSoup
import numpy as np
from itertools import tee
import collections
import re
from datetime import date
import pandas as pd
import os

os.chdir("C:/Users/Sayyam/Desktop/Newspaper")

### Extracting all links; For extracting words later
driver = webdriver.Chrome()
parent_URL = "https://timesofindia.indiatimes.com/india"
driver.get(parent_URL)
html = driver.page_source
soup = BeautifulSoup(html)
li = soup.find_all("div",{"id":"c_wdt_list_1"})
lin = BeautifulSoup(str(li))
link = lin.select("a")
links = []
for i in link:
    y= i.attrs["href"]
    links.append(y)
pages = list(range(2,13))
for page in pages:
    current_URL = parent_URL + "/" + str(page)
    driver.get(current_URL)
    html = driver.page_source
    soup = BeautifulSoup(html)
    li = soup.find_all("div",{"id":"c_wdt_list_1"})
    lin = BeautifulSoup(str(li))
    link = lin.select("a")
    for i in link:
        y= i.attrs["href"]
        links.append(y)

rm = ['/india','/india/2','/india/3','/india/4','/india/5','/india/6','/india/7','/india/8','/india/9','/india/10','/india/11','/india/12']
links = [ele for ele in links if ele not in rm]
driver.quit()




#################### Choosing the words ######################### 


### Add desired words here
words =["crop burning","crops burning",
"Burning crop","Burning crops",
"Residue burning",
"Biowaste burning",
"Air pollution",
"Pollution",
"Burning rice",
"Burning wheat",
"Stubble burning",
"Straw burning",
"Crop residue","Crops residue",
"agricultural smoke",
"agricultural biomass",
"Rice residue",
"Wheat residue",
"Emission from crop burning","Emissions from crop burning",
"Emissions of air pollutants","Emissions of air pollutant", "Emission of air pollutant", "Emissions from air pollutants",
"Emission from air pollutant","Emission from air pollutants", "Emissions from air pollutant",
"Agricultural fires", 
"Agricultural fire", 
"Toxic smog",
"Open agricultural burning",
"Burning fields", "Burning field", 
"Fields on fire","Field on fire",
"Illegal fires" ,"Illegal fire" ,
"Crop waste", "Crop wastage"]

#### Just makes them to lower for recognition purposes
chosen_words = []
for word in words:
    words = word.lower()
    chosen_words.append(words)





##### Opening driver for extracting words
from datetime import date
today = date.today()
driver = webdriver.Chrome()
bad_links = []
text = []
count = 0
name = today.strftime("%m_%d_%y")
file1 = open("{}_TOI.txt".format(name),"w",encoding="utf-8")
parent_URL = "https://timesofindia.indiatimes.com/india"
## Combining links together
for i in links[1:len(links)]:
    req_URL= parent_URL + str(i)
    driver.get(req_URL)
    html = driver.page_source
    soup = BeautifulSoup(html)
    
## finding text 
    link_t = soup.find("div",{"class":"_3YYSt clearfix"})  
    div = soup.find("div",{"class":"_3tXYS"})
    if div != None:
        div.decompose()
    
## Storing bad links
    if link_t == None:
        bad_links.append(req_URL)
          
    else: 
        x = link_t.text
        file1.write(x)

file1.close()


with open('12_17_20_TOI.txt',encoding="utf-8") as f:    ### Change to current date
    for line in f:
        words = re.findall('\w+', line.lower())
        count = collections.Counter(words)
from itertools import tee
phrases = chosen_words
fw1, fw2 = tee(words)   
next(fw2)
for w1,w2 in zip(fw1, fw2):
    phrase = ' '.join([w1, w2])
    if phrase in phrases:
        count[phrase] += 1