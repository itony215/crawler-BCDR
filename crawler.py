import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os
if not os.path.isdir('download'):
    os.mkdir('download')
for num in range(1,1011):
    url = "http://bcdr.inegi.up.pt/patient/"+ str(num)
    res = requests.get(url,cookies={'bcdr':'kp6fam2ub27p9aknmtlnqv6441'})
    soup = BeautifulSoup(res.text,'html.parser')
    tag_name = 'div#segmentation_image a'
    if not soup.select(tag_name):
        continue
    articles = soup.select(tag_name)
    image = 'http://bcdr.inegi.up.pt'+articles[0]['href']
    print(image,num)
    #urlretrieve(image,num)