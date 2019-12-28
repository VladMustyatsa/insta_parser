import requests
import json
import re
import os
import sys
from bs4 import BeautifulSoup as BS

while True:
    login = input()
    r = requests.get('https://www.instagram.com/' + login)
    if str(r) != '<Response [404]>':
        break
    else:
        print('login is incorrect!!!')

html = BS(r.content,'html.parser')
script_tag = html.find('script', text=re.compile('window\._sharedData'))
shared_data = script_tag.string.partition('=')[-1].strip(' ;')
path = os.getcwd() + "\\" + login

try:
    os.mkdir(path)
except FileExistsError: 
    while True:
        to_choose = input('do you want to rewrite {}? y/n '.format(path) )
        if  to_choose == 'y':
            print('rewrite')
            break
        elif to_choose == 'n':
            print('Bye')
            sys.exit()
        else:
            print('Write y/n')

os.chdir(path)
with open('qraphql_info.json','w') as f2:
    f2.write(str(shared_data))

with open('qraphql_info.json','r') as f2:
    info = json.load(f2)


data = info['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']
count = 1

for i in data:
    img = i['node']['display_url']
    r2 = requests.get(img)
    soup =  BS(r2.content,'html.parser', from_encoding="iso-8859-1")
    print('photo{}.jpg is downloaded:)'.format(count))
    with open('photo' + str(count) +'.jpg', 'wb') as fp:
        fp.write(r2.content)
        count += 1

print('Bye')
