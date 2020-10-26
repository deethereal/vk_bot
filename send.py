import time
import requests as r
from openpyxl import load_workbook

MY_TOKEN='' #токен

ids=[]
passwords=[]
logins=[]
p=''
l=''
table='' #имя таблицы
wb = load_workbook(table)
sheet = wb.get_sheet_by_name('Лист1')


for i in range(0,3):
    passwords.append(sheet['E'+str(2+i)].value)
    logins.append(sheet['C'+str(2+i)].value)
    ids.append(sheet['F'+str(2+i)].value)
print(ids)

print(passwords)
print(logins)
id=''
counter=0

for i in range(0, 3):
    id=str(ids[i]);
    p=str(passwords[i])
    l=str(logins[i])
    message = '' #текст письма
    send = 'https://api.vk.com/method/messages.send?peer_id=' + id + '&message=' + message + '&access_token=' + MY_TOKEN + '&v=5.89'
    response=r.get(send)
    if response.status_code==200:
        counter+=1
    time.sleep(0.25)
print('скрипт закончил работу, результат '+str(counter)+'/11')
#print(response.status_code)
