import functions as f
import time
import datetime
from vk_api.bot_longpoll import VkBotEventType
import sys
import random

COMAND=False
roll=False
mute_mode=False
votekick = False
votekickTime=0
votekickID=0
votekickN=2
votekickpercent=0
M1 = {'red':[207227130,['Мотя','Матвей']], 'orange':[125928980,['Никита','Матвей...ой в смысле Никита',"Писюканов"]], 'yellow':[62501050,['Коля',"Колека"]], 'green':[150078285,['Cемён','Семен','Semen']], 'sasha':[218917421,['Саша']], 'blue':[206312673,['Диня',"Денис"]],'god':[236709769,['Влад']], 'shluha':[240702553,['Ирка','Шлюха','Ира']]}
comands={'да':False, "хочу":False, "хачу":False, "кальян":False, "мама":False,"пидор":False,"ы":False,"хуй":False} #состояние выключенности команд, ВЫВОДИТСЯ ВКЛЮЧЕННОСТЬ!!
torch=['torch',"торч","калик","кальян","дядя коля","табак"]
imposter=['imposter','impostor','импостер',"импостор", "предатель","компостор","компостер","пидорас","пидор"]
y_words=['уеба','уёба','yеба', 'уебa','уeба','yeба','yебa','уeбa','yeба','yёба','уёбa','yёбa', 'yeбa']
booba=["сиськи","сиська","сиську","грудь","boobs",'booba',"буба"]
votekickdone={207227130:False, 125928980:False, 62501050:False, 150078285:False, 218917421:False, 206312673:False, 236709769:False, 240702553:False}

f.send('Дарова, я живой нахуууууй', 2000000001)
month=datetime.datetime.now().month
if month == 11:
    f.send("Сегодня небритябрь/недрочабрь, так что не дрочите и/или не брейтесь, пацаны", 2000000001)
for event in f.longpoll.listen():
    flag=False
    f.malina()
    print (event)
    if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
       # print(event.object['message']['action'])
        #if event.object['message']['from_id'] == 207227130 and event.object['message']['action']:
           # if event.object['message']['action']['type'] == 'chat_kick_user' and  event.object['message']['action']['type']['member_id']== 207227130:
               # counter_plus()
               # f.send('+1 обсёр в копилку',event.object['message']['peer_id'])
        #get=int(round(time.time() * 1000))
        message_text = event.object['message']['text'].lower()
        if message_text=='/help':
                COMAND=True
                f.send('Я умею: \n '
                '/roll -- выбросить сулчайное восьмизначное число\n'
                '/rollmode — после каждого сообщения выплевывать сулчайное восьмизначное число. \nЧтобы завершить rollmode - "хватит пожалуйста"\n'
                '/votekick <color> — кикнуть члена или Ырку\n'
    	        '      <color>:\n'
    	        '      все цвета совпадают, кроме\n'
    	        '      Ира - "shluha"\n'
                '      Саша - "sasha"\n'
                '/mute -- выключить меня\n'
                '/unmute -- включить меня\n'
                'execute_time -- убить меня(может только денис)\n'
                '/comands -- состояние команд\n'
                '/mute команда_нейм -- выключить команду\n'
                '/unmute команда_нейм -- включить команду\n'
                'бот позови "имя" -- позвать кого-то\n',event.object['message']['peer_id'])
        elif message_text=='?mute?':
                f.send(str(mute_mode),event.object['message']['peer_id'])
        elif not mute_mode:
            if votekick:
                if message_text=='f1':
                    if not votekickdone[event.object['message']['from_id']]:
                        votekickN+=1
                        votekickpercent+=1
                        votekickdone[event.object['message']['from_id']]=True
                        f.send('Голос принят',event.object['message']['peer_id'] )
                elif message_text=='f2':
                    if not votekickdone[event.object['message']['from_id']]:
                        votekickN+=1
                        votekickpercent-=1
                        votekickdone[event.object['message']['from_id']]=True
                        f.send('Голос принят',event.object['message']['peer_id'] )
                elif message_text=='f1мыздесьзакон':
                    if (M1['god'][0]==event.object['message']['from_id'] or M1['blue'][0]==event.object['message']['from_id']) :
                        votekickpercent+=1000
                        f.send('Хорошо, пап',event.object['message']['peer_id'] )
                    else:
                        f.sendphoto('',event.object['message']['peer_id'],'video-159328378_456239420')
                elif message_text=='f2мыздесьзакон':
                    if (M1['god'][0]==event.object['message']['from_id'] or M1['blue'][0]==event.object['message']['from_id']) :
                        votekickpercent-=1000
                        f.send('Хорошо, пап',event.object['message']['peer_id'] )
                    else:
                        f.sendphoto('',event.object['message']['peer_id'],'video-159328378_456239420')
                if time.mktime(datetime.datetime.now().timetuple())-votekickTime>=150 or abs(votekickpercent)>=3 or votekickN==8:
                    if (votekickpercent>0 and votekickN>=4) or (votekickpercent>500):
                         f.kick(event.object['message']['peer_id'], votekickID)
                    f.send('Голосование, кстати, закончено',event.object['message']['peer_id'] )
                    votekick=False
                    votekickN=2
                    votekickdone={207227130:False, 125928980:False, 62501050:False, 150078285:False, 218917421:False, 206312673:False, 236709769:False}
            elif roll:
                if message_text=='хватит пожалуйста':
                    roll=False
                else:
                    timestamp=int(time.mktime(datetime.datetime.now().timetuple()))
                    timestamp=timestamp%10000000
                    f.send(str(timestamp),event.object['message']['peer_id'])
            else:
                if len(message_text.split())==2:
                    msg=message_text.split()
                    if msg[0]=='/mute':
                        COMAND=True
                        comands[msg[1]]=True
                        f.send('Выключена команда {}'.format(msg[1]),event.object['message']['peer_id'])
                    elif msg[0]=='/unmute':
                        COMAND=True
                        comands[msg[1]]=False
                        f.send('Включена команда {}'.format(msg[1]),event.object['message']['peer_id'])
                if not COMAND:
                    if f.findIII(message_text) and not comands["ы"]:
                         f.send(f.findIII(message_text),event.object['message']['peer_id'] )
                    if f.findWord(message_text, 'хуй') and not comands["хуй"]:
                        f.send('Сам иди на хуй, пидор',event.object['message']['peer_id'])
                    if f.findWord(message_text,"бот"):
                        words=message_text.split()
                        if len(words)==3 and words[1]=='позови':
                            if (words[2]=='влада'):
                                f.send('@freebadman({})'.format(M1['god'][1][random.randint(0, len(M1['god'][1])-1)]), event.object['message']['peer_id'])
                            elif (words[2]=='семена') or (words[2]=='семёна') or (words[2]=='cёму') or (words[2]=='cему'):
                                f.send('@voidrad({})'.format(M1['green'][1][random.randint(0, len(M1['green'][1])-1)]), event.object['message']['peer_id'])
                            elif (words[2]=='сашу'):
                                f.send('@id_alejandr0({})'.format(M1['sasha'][1][random.randint(0, len(M1['sasha'][1])-1)]), event.object['message']['peer_id'])
                            elif (words[2]=='никиту'):
                                f.send('@08kuy({})'.format(M1['orange'][1][random.randint(0, len(M1['orange'][1])-1)]), event.object['message']['peer_id'])
                            elif (words[2]=='колю'):
                                f.send('@k_o_l_y_a_24({})'.format(M1['yellow'][1][random.randint(0, len(M1['yellow'][1])-1)]), event.object['message']['peer_id'])
                            elif (words[2]=='мотю') or (words[2]=='матвея'):
                                f.send('@whitewolf185({})'.format(M1['red'][1][random.randint(0, len(M1['red'][1])-1)]), event.object['message']['peer_id'])
                            elif (words[2]=='ирку') or (words[2]=='шлюху'):
                                f.send('@zhur__zhur({})'.format(M1['shluha'][1][random.randint(0, len(M1['shluha'][1])-1)]), event.object['message']['peer_id'])
                            elif (words[2]=='диню') or (words[2]=='дениса'):
                                f.send('@deeenizka({})'.format(M1['blue'][1][random.randint(0, len(M1['blue'][1])-1)]), event.object['message']['peer_id'])
                    if f.findWord(message_text, 'держу в курсе'):
                        f.sendphoto('',event.object['message']['peer_id'],'photo-178950051_457239152')
                    if f.findWord(message_text, 'матвей обосрался') or f.findWord(message_text, 'мотя обосрался') or f.findWord(message_text, 'oбосрался матвей') or f.findWord(message_text, 'oбосрался мотя'):
                        f.counter_plus()
                        f.send('Я записал!', event.object['message']['peer_id'])
                    if (f.findWord(message_text,'фки') or f.findWord(message_text,'фкишник') ) and event.object['message']['from_id']!=M1['blue'][0]:
                        f.sendphoto('', event.object['message']['peer_id'], 'photo-178950051_457239123')
                    if (f.findWord(message_text,'вмк') or f.findWord(message_text,'вмкшник')) and event.object['message']['from_id']!=M1['yellow'][0]:
                        f.sendphoto('', event.object['message']['peer_id'], 'photo-178950051_457239139')
                    if (f.findWord(message_text,'мирэа') or f.findWord(message_text,'мирэашник')) and event.object['message']['from_id']!=M1['god'][0]:
                        f.sendphoto('', event.object['message']['peer_id'], 'photo-178950051_457239140')
                    if (f.findWord(message_text,'мехмат') or f.findWord(message_text,'мехматянин') or f.findWord(message_text,'мехматовец')) and event.object['message']['from_id']!=M1['sasha'][0]:
                        f.sendphoto('', event.object['message']['peer_id'], 'photo-178950051_457239148')
                    if (f.findWord(message_text,'мое') or f.findWord(message_text,'моё')):
                        f.sendphoto('НАШЕ', event.object['message']['peer_id'], 'photo-178950051_457239157')
                    if ((f.findWord(message_text,'маи') or f.findWord(message_text,'маёвец') or f.findWord(message_text,'маёвцы') or f.findWord(message_text,'маевец') or f.findWord(message_text,'маевцы')) and (event.object['message']['from_id']!=M1['red'][0] or event.object['message']['from_id']!=M1['green'][0])):
                        f.sendphoto('',event.object['message']['peer_id'],'photo-178950051_457239166')
                    if f.findWordInList(message_text,booba):
                        f.sendphoto('', event.object['message']['peer_id'], 'photo-178950051_457239163')
                    if f.findWord(message_text,'доска') or f.findWord(message_text,'ирка'):
                        f.sendphoto('no booba?', event.object['message']['peer_id'], 'photo-178950051_457239176')
                    if (f.findWord(message_text,'simp') or f.findWord(message_text,'симп')):
                        f.sendphoto('', event.object['message']['peer_id'], 'photo-178950051_457239165')
                    if f.findWordInList(message_text,imposter) and not comands["пидор"]:
                        f.sendphoto('', event.object['message']['peer_id'], 'photo-178950051_4572391'+str(67+random.randint(0, 7)))
                    if f.findWordInList(message_text,torch) and not comands["кальян"]:
                        f.sendphoto('',event.object['message']['peer_id'],'photo-178950051_457239160')
                    if f.findWordInList(message_text,y_words):
                        if event.object['message']['from_id']!=M1['god'][0]:
                            f.sendphoto('Сам ты у е б а, пашел нахуй',event.object['message']['peer_id'],'photo-178950051_457239159')#['conversation_message_id'] )
                            f.kick(event.object['message']['peer_id'], event.object['message']['from_id'])
                            f.send('Возвращайте этого пидора сами',event.object['message']['peer_id'] )
                        else:
                            f.send('Этого пидораса я кикнуть не могу, он слишком тяжелый:(',event.object['message']['peer_id'] )
                    if f.findWord(message_text,'хачу') and not comands["хочу"]:
                        try:
                            f.ha4u(message_text)
                        except ValueError:
                            continue
                    if f.findWord(message_text,'хочу') and not comands["хачу"]:
                        try:
                            f.ho4u(message_text)
                        except ValueError:
                            continue
                    if message_text=='!отладка':
                        #now=int(round(time.time() * 1000))
                        f.send("надо пофиксить",event.object['message']['peer_id'])
                    elif message_text=='/rollmode':
                        roll = True
                    elif message_text!='' and message_text!='/votekick' and message_text.split()[0]=='/votekick':
                        if message_text.split()[1]=='purple' or message_text.split()[1]=='god':
                                f.sendphoto('',event.object['message']['peer_id'],'video-159328378_456239420')
                        elif message_text.split()[1] in M1:
                                dt = datetime.datetime.now() # datetime, из которой переводим в timestamp
                                votekickTime=time.mktime(dt.timetuple())
                                votekickID=M1[message_text.split()[1]][0]
                                votekick=True
                                votekickpercent=0
                                votekickdone[event.object['message']['from_id']]=True
                                votekickdone[votekickID]=True
                                key=message_text.split()[1]
                                f.send('F1 или F2? Голосование начато, извини,  '+str(M1[key][1][random.randint(0, len(M1[key][1])-1)]), event.object['message']['peer_id'] )
                    elif message_text=='/roll':
                        f.send(str(random.randint(10000000,99999999)),event.object['message']['peer_id'])
                    elif message_text == '/fuck_ups':
                        file = open('text.txt','r')
                        lines = file.readlines()
                        counter = int(lines[0])
                        daily_c = int(lines[1])
                        days = int(lines[2])
                        f.send(f'Всего мотя обосрался {counter} раз(а)\nЗа этот день {daily_c} раз(а)'
                             f'\nДней без обсеров: {days}', event.object['message']['peer_id'])
                        file.close()
                    elif message_text == 'execute_time' and event.object['message']['from_id']==M1['blue'][0]:
                        f.send('Блять, смерть',event.object['message']['peer_id'])
                        sys.exit()
                    elif message_text=='/mute':
                        f.sendphoto('',event.object['message']['peer_id'],'photo-178950051_457239161')
                        mute_mode=True
                    elif message_text=='/comands':
                        f.send(f.printdic(comands),event.object['message']['peer_id'])
                    elif (message_text=='кого') or (message_text=='кого?'):
                        f.sendphoto('',event.object['message']['peer_id'],'photo-178950051_457239153')
                    elif ((message_text=='да') or (message_text=='da') or (message_text=='lf')) and not comands["да"]:
                        f.sendphoto('',event.object['message']['peer_id'],'photo-178950051_457239162')
                    elif (f.findWord(message_text, 'мама') or f.findWord(message_text, 'мамка') or f.findWord(message_text, 'мамку') or f.findWord(message_text, 'маму') or f.findWord(message_text, 'маман') or f.findWord(message_text, 'маме') or f.findWord(message_text, 'мамке')) and not comands["мама"]:
                        n = random.randint(0, 9)
                        if (n==0):
                            f.send('А у Семёна ТАКАЯ МАМА',event.object['message']['peer_id'] )
                        elif (n==1):
                            f.send('Я к твоей маме кстате завтра первый в очереди',event.object['message']['peer_id'] )
                        elif (n==2):
                            f.send('Маму твою',event.object['message']['peer_id'] )
                            f.send('В кино водил',event.object['message']['peer_id'] )
                        elif (n==3):
                            f.send('Маму твою',event.object['message']['peer_id'] )
                            f.send('Твою маму',event.object['message']['peer_id'] )
                            f.send('Маму твою',event.object['message']['peer_id'] )
                            f.send('Я б твою маму даа',event.object['message']['peer_id'] )
                        elif (n==4):
                            f.send('Кстати передай своей маме шо вечером все в силе',event.object['message']['peer_id'] )
                        elif (n==6):
                            f.send('Люблю твою маму',event.object['message']['peer_id'] )
                        elif (n==7):
                            f.sendphoto('',event.object['message']['peer_id'],'photo-178950051_457239156')
                        elif (n==8):
                            f.sendphoto('А ну адавай мать',event.object['message']['peer_id'],'photo-178950051_457239158')
                        elif (n==9):
                            f.sendphoto('Твоя мама - наша мама',event.object['message']['peer_id'],'photo-178950051_457239157')
        else:
            if message_text=='/unmute':
                f.send('Я снова с вами',event.object['message']['peer_id'])
                mute_mode=False
