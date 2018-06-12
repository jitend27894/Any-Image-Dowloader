#beautiful soup allows us to crawl through web pages ,tags and attributes.
from bs4 import BeautifulSoup
#reuest module allows us to get URL
import requests
#urllib.request library is used for opening URL
import urllib.request
#random module generate random No. between the given range
import random
x=input()
url='https://www.pexels.com/search/' + str(x)
#Getting URL
y=requests.get(url)
#it will get only HTML content
z=y.content
#html.parser for pulling data out of html and other files
rawat=BeautifulSoup(z,'html.parser')
link = []
#find_all allows us to find specific data from all data.
for i in rawat.find_all('a'):
    try:
#attrs[] tags will get text inside pertcular tag attribute
        z= i.attrs['href']
        if "images.pexel" in z:
            link.append(z)
#except will ignore errors
    except KeyError:
        continue

#function defined
def download(i):
#random.randrange will generate random number
    name = random.randrange(1, 1000)
    fullname = str(name) + '.jpg'
#opener is used when a perticular website doesnot allows us to navigate through the sie and
#so this will how the site that request for data is given by mozilla browser
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
#it will retreive data from website
    urllib.request.urlretrieve(i,fullname)
for i in link:
    print(i)
    download(i)






