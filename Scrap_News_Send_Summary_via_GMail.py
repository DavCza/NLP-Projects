# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 14:36:53 2019

@author: david
"""
### Get news
import requests
from bs4 import BeautifulSoup
import MyTextSummerizer

##### Get FAZ news ####
def get_news_list_FAZ():
    url = 'http://www.faz.de'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    output = []
    ## Get Title + HyperLinks
    for article in soup.find_all(class_='tsr-Base_ContentWrapperInner teaserInner linkable'):
        #print(links.find_all('a'))
        for link in article.findAll('a'):
            #output.append(link.get('title'))
            output.append(link.get('title'))
            output.append(link.get('href'))
    return '\n'.join(output)

def get_news_content_FAZ():
    url = 'http://www.faz.de'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    output = []
    for single_article in soup.find_all(class_='tsr-Base_ContentWrapperInner teaserInner linkable'):
        liste = {link.get('title') : link.get('href') for link in single_article.findAll('a')}
        for single_url in liste:
            output.append('\n')
            output.append(single_url)
            output.append(' ')
            output.append(liste[single_url])
            next_url = requests.get(liste[single_url])
            next_soup = BeautifulSoup(next_url.text, 'lxml') 
            for each_paragraph in next_soup.find_all(class_='atc-TextParagraph'):
                #temp = []
                output.append(each_paragraph.text.replace("\n", " ").strip())
                temp = each_paragraph.text.replace("\n", " ").strip()
                output.append(MyTextSummerizer.generate_summary(temp))         
    
    return '\n'.join(output)


###### Get SZ news ####
def get_news_list_SZ():
    url = 'http://www.sz.de'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    output = []
    ## Get Title + HyperLinks
    for article in soup.find_all(class_='sz-teaserlist-element sz-teaserlist-element--separator-line'):
        #print(article.find_all('h'))
        for _ in article.findAll('h3'):
            output.append(_.contents[0].strip())
        for _ in article.findAll('a'):
            output.append(_.get('href'))
    
    for article in soup.find_all(class_='sz-teaserlist-element sz-teaserlist-element--separator-space'):
        #print(article.find_all('h'))
        for _ in article.findAll('h3'):
            output.append(_.contents[0].strip())
        for _ in article.findAll('a'):
            output.append(_.get('href'))
 
        return '\n'.join(output[:-10])


def get_news_content_SZ():
    url = 'http://www.sz.de'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    output = []
    for single_article in soup.find_all(class_='sz-teaserlist-element sz-teaserlist-element--separator-line'):
        liste = {title.contents[0].strip() : link.get('href')
                for title in single_article.findAll('h3')
                for link in single_article.findAll('a')}
                    
        for single_url in liste:
            output.append('\n')
            output.append(single_url)
            output.append(' ')
            output.append(liste[single_url])
            next_url = requests.get(liste[single_url])
            next_soup = BeautifulSoup(next_url.text, 'lxml') 
            for paragraph in next_soup.find_all('p'): ### nur auf 'p' zu filtern, bringt auch shit mit!!!
                output.append(paragraph.text.replace("\n", " ").strip())  
    return '\n'.join(output[20:-40])


'''
url2 = 'http://www.sz.de'
r2 = requests.get(url2)

soup2 = BeautifulSoup(r2.text)
for headline2 in soup2.find_all(class_="sz-teaser__title"): 
    #if headline2.a: 
    #print(headline2.a.text.replace("\n", " ").strip())
    #else: 
    print(headline2.contents[0].strip())

url = 'http://www.sz.de'
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
output = []
## Get Title + HyperLinks
        #output.append(link.get('title'))
        #output.append(link.get('href'))

url = 'http://www.sz.de'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
output = []
for single_article in soup.find_all(class_='sz-teaserlist-element sz-teaserlist-element--separator-line'):
    liste = {title.contents[0] : link.get('href')
            for title in single_article.findAll('h3')
            for link in single_article.findAll('a')}
                
    for single_url in liste:
        output.append('\n')
        output.append(single_url)
        output.append(' ')
        output.append(liste[single_url])
        
        next_url = requests.get(liste[single_url])
        next_soup = BeautifulSoup(next_url.text, 'lxml


url = 'http://www.faz.de'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
output = []
for single_article in soup.find_all(class_='tsr-Base_ContentWrapperInner teaserInner linkable'):
    liste = {link.get('title') : link.get('href') for link in single_article.findAll('a')}



url_requested = request.urlopen('http://www.heise.de')
if 200 == url_requested.code:
    html_content = str(url_requested.read())') 
        for paragraph in next_soup.find_all('p'): 
             output.append(paragraph.text[30:-30]) 
   
    print(paragraph.text) 

for paragraph in next_soup.find_all('articleBody'):
    print('>.*?<', paragraph.text) 
#    print(paragraph.text.replace("\n", " ").strip()) 

re.findall('>.*?<', result)

    main_content = soup.find('div', {'id': 'user-repositories-list'})

'''

######################################
from datetime import datetime
now = datetime.now()
date = now.strftime("%d.%m.%Y")
time = now.strftime("%H:%M")

import yagmail

### FAZ
yag = yagmail.SMTP("davcza@googlemail.com",oauth2_file="client_secret_yagmail.json")
EMAIL_TO = 'spyz@gmx.de' 
EMAIL_SUBJECT = 'FAZ Artikel am ' + date + ' um ' + time
EMAIL_BODY = get_news_content_FAZ()
yag.send(to=EMAIL_TO, subject=EMAIL_SUBJECT, contents=EMAIL_BODY)

### SZ
#EMAIL_SUBJECT2 = 'SZ Artikel am ' + date + ' um ' + time
#EMAIL_BODY2 = get_news_content_SZ()
#yag.send(to=EMAIL_TO, subject=EMAIL_SUBJECT2, contents=EMAIL_BODY2)



