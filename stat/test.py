import requests
from datetime import datetime 
import time
import gc
import pandas as pd, numpy as np
with open ('/home/ubuntu/bot/token.txt' , 'r') as t:
    TOKEN = t.readline().rstrip()
id2name_color={207227130:['Матвей','#ff0000'], 125928980:['Никита','#ff5e00'], 62501050:['Коля','#ffee00'], 150078285:['Cемен','#33b80f'], 218917421:['Саша','#00d5ff'], 206312673:['Денис',"#005eff"], 236709769:['Влад','#6600ff'], 240702553:['Ира','#000000']}
checked_online={207227130:False, 125928980:False, 62501050:False, 150078285:False, 218917421:False, 206312673:False, 236709769:False, 240702553:False}
now = datetime.now() 
last_h = (int(now.strftime("%H"))+3)%24
while (True):
	now = datetime.now() 
	current_h = (int(now.strftime("%H"))+3)%24
	if last_h<current_h or (current_h==0 and last_h!=0):
		last_h=current_h
		for k in checked_online.keys():
			checked_online[k]=False
	ids=''
	for k in checked_online.keys():
	    if not checked_online[k]:
	        ids=ids+str(k)+','
	if ids!='':
	    ids=ids[:-1]
	    temp = requests.get(f"https://api.vk.com/method/users.get?user_ids={ids}&fields=online&access_token={TOKEN}&v=5.131").json()['response']
	    df = pd.read_csv('dataframe.csv')
	    df=df.set_index('hours')
	    for j in range(len(temp)):
	        if not checked_online[temp[j]['id']] and temp[j]['online']==1:
	            checked_online[temp[j]['id']]=True
	            h=str(current_h)
	            nh=str((current_h+1)%24)
	            if current_h<10:
	                h='0'+h
	                if current_h<9:
	                    nh='0'+nh
	            if current_h==23:
	            	nh='00'
	            df.loc[f'{h}-{nh}',id2name_color[temp[j]['id']][0]]+=1
	    df.to_csv('dataframe.csv')
            del df
            gc.collect()
	print("Готово")
	time.sleep(300)

