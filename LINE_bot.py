import requests
from bs4 import BeautifulSoup
import os

url="https://tenki.jp/forecast/5/26/5110/23100/"
res=requests.get(url)
soup=BeautifulSoup(res.content,'html.parser')

wc=soup.find(class_='today-weather')
ws = [i.strip() for i in wc.text.splitlines()]
wl = [i for i in ws if i != ""]


message=("\n"+"名古屋市:"+wl[0]+"\n"+wl[1]+"\n"+wl[2]+":"+wl[3]+"\n"+wl[5]+":"+wl[6]+"\n"+"降水確率"+"\n"+wl[9]+":"+wl[14]+"\n"+wl[10]+":"+wl[15]+"\n"+wl[11]+":"+wl[16]+"\n"+wl[12]+":"+wl[17])

line_notify_token = 'あなたのTOKENを記述してください。'
line_notify_api = 'https://notify-api.line.me/api/notify'

#LINENotifyへ通知の記述
payload = {'message': message}
headers = {'Authorization': 'Bearer ' + line_notify_token} 
line_notify = requests.post(line_notify_api, data=payload, headers=headers)

print('dirname:     ', os.path.dirname(__file__))