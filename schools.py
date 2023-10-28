#-  https://isd110.org/our-schools/laketown-elementary/staff-directory

import requests
from bs4 import BeautifulSoup
from utilities import *

class LakeTown:

    def __init__(self):
        self.main_url ='https://isd110.org/our-schools/laketown-elementary/staff-directory'
        self.main_content =[]

    def scrape(self):
        url = self.main_url
        page = 1
        while True:
            req = requests.get(url)
            soup = BeautifulSoup(req.content)
            content =dict()
            try:
                content['school_name'] = soup.find('title').text.split('|')[-1].strip()
            except:
                content['school_name'] = ''
            try:
                content['address'] = ' '.join(soup.find('div',attrs={'class':'field location label-above'}).find('div',attrs={'class':'field-content'}).text.replace('Directions','').split())
            except:
                content['address'] = ''
            if content['address'] != '':
                content['state'] =content['address'].split()[-2]
                content['zip'] = content['address'].split()[-1]
            else:
                content['state'] = ''
                content['zip'] = ''
            content['first_name'] =''
            content['last_name'] = ''
            content['title'] = ''
            content['phone'] =''
            content['email'] =''

            for i in soup.findAll('div',attrs={'class':'views-row'}):
                data = content.copy()
                try:
                    title = i.find('h2',attrs={'class','title'}).text.split()
                except:
                    title = ['lastname','firstname']
                data['first_name'] = title[-1]
                data['last_name'] = title[0]
                try:
                    data['title'] = i.find('div',attrs={'class','field job-title'}).text.strip()
                except:
                    data['title'] = 'job title'
                try:
                    data['phone'] = i.find('div',attrs={'class','field phone'}).text.strip()
                except:
                    data['phone'] ='phone'
                try:
                    data['email'] = i.find('div',attrs={'class','field email'}).text.strip()
                except:
                    data['email'] = 'email'
                self.main_content.append(data)

            # write_csv(obj.main_content,'file/schools.csv')
            # filepath = 'collections/page{}'.format(page)
            # write_json(main_content,filepath)
            page += 1
            try:
                href = soup.find('li',attrs={'class':'item next'}).find('a')['href']
            except:
                href =''
            if href:
                url = self.main_url+href
            else:
                break
        write_csv(self.main_content,'file/schools.csv')

obj = LakeTown()
obj.scrape()
# write_csv(obj.main_content,'file/schools.csv')





