import random
import re
import vk_api
import time
import datetime
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import sys
#from constants import counter, flag

groupID = 178950051
token = 'АААААААААААААААААААААААА' # Здесь ввести token сообщества (не удаляя апострофы)
roll=False
mute_mode=False
votekick = False
votekickTime=0
votekickID=0
votekickN=2
votekickpercent=0
M1 = {'red':[207227130,['Мотя','Матвей']], 'orange':[125928980,['Никита','Матвей...ой в смысле Никита',"Писюканов"]], 'yellow':[62501050,['Коля',"Колека"]], 'green':[150078285,['Cемён','Семен','Semen']], 'sasha':[218917421,['Саша']], 'blue':[206312673,['Диня',"Денис"]],'god':[236709769,['Влад']], 'shluha':[240702553,['Ирка','Шлюха','Ира']]}

torch=['torch',"торч","калик","кальян","дядя коля","табак"]
imposter=['imposter','impostor','импостер',"импостор", "предатель","компостор","компостер","пидорас","пидор"]
y_words=['уеба','уёба','yеба', 'уебa','уeба','yeба','yебa','уeбa','yeба','yёба','уёбa','yёбa', 'yeбa']
booba=["сиськи","сиська","сиську","грудь","boobs",'booba']
votekickdone={207227130:False, 125928980:False, 62501050:False, 150078285:False, 218917421:False, 206312673:False, 236709769:False, 240702553:False}
vk_session: VkApi = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, groupID)
vk = vk_session.get_api()
def counter_plus():
    with open('text.txt', "r") as file:
        lines = file.readlines()
        counter = int(lines[0])
        daily_c = int(lines[1])
        for i in range(3):
            del lines[2 - i]
        counter += 1
        daily_c += 1
        days=0
        lines.insert(0, str(counter))
        lines.insert(1, '\n')
        lines.insert(2, str(daily_c))
        lines.insert(3, '\n')
        lines.insert(4, str(days))
        lines.insert(5, '\n')
    with open("text.txt", "w") as file:
        file.writelines(lines)
def sendphoto(msg, peerID, attach): # msg — сообщение
    vk.messages.send(random_id=random.randint(0, 999999), message=msg, peer_id=peerID, attachment =attach)
def send(msg, peerID):
    vk.messages.send(random_id=random.randint(0, 999999), message=msg, peer_id=peerID)
def kick(chatID, userID):
    vk.messages.removeChatUser(chat_id=chatID%1000, user_id=userID)

def add(userID,chatID, timeout):
    time.sleep(timeout)
    vk.messages.addChatUser(user_id=userID, chat_id=chatID)
def findWordInList(msg, words):
    for word in words:
        raw='\\b'+word+',?\\b'
        result = re.search(r''+raw, msg)
        if result!=None:
            return True
    return False
def ha4u(msg):
    words=msg.split()
    if len(words)>1:
        f=words.index("хачу")
        sendphoto(words[f-1].upper()+' ХАЧУ',event.object['message']['peer_id'],'photo-178950051_457239175')
def ho4u(msg):
    words=msg.split()
    if len(words)>1:
        f=words.index("хочу")
        sendphoto(words[f-1].upper()+' ХОЧУ',event.object['message']['peer_id'],'photo-178950051_457239175')
def findWord(msg,word):
    raw='\\b'+word+',?\\b'
    result = re.search(r''+raw, msg)
    #print (result)
    if result!= None:
        return True
    else:
        return False
def findIII(msg):
    result = re.search(r'\bы+\b', msg)
    randi=random.randint(0,7)
    I='Ы'
    for i in range(randi):
        I+='ы'
    if result!= None:
        if result.group(0)=='ы':
            return 'Ы'
        else:
            return I
    else:
        return False
send('Дарова, я живой нахуууууй', 2000000001)
month=datetime.date.today().month
if month == 11:
    send("Сегодня небритябрь/недрочабрь, так что не дрочите и/или не брейтесь, пацаны", 2000000001)
for event in longpoll.listen():
    flag=False
    print (event)

    if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
       # print(event.object['message']['action'])
        #if event.object['message']['from_id'] == 207227130 and event.object['message']['action']:
           # if event.object['message']['action']['type'] == 'chat_kick_user' and  event.object['message']['action']['type']['member_id']== 207227130:
               # counter_plus()
               # send('+1 обсёр в копилку',event.object['message']['peer_id'])
        get=int(round(time.time() * 1000))
        message_text = event.object['message']['text'].lower()
        if message_text=='?mute?':
                send(str(mute_mode),event.object['message']['peer_id'])
        if not mute_mode:
            if votekick:
                if message_text=='f1':
                    if not votekickdone[event.object['message']['from_id']]:
                        votekickN+=1
                        votekickpercent+=1
                        votekickdone[event.object['message']['from_id']]=True
                        send('Голос принят',event.object['message']['peer_id'] )
                elif message_text=='f2':
                    if not votekickdone[event.object['message']['from_id']]:
                        votekickN+=1
                        votekickpercent-=1
                        votekickdone[event.object['message']['from_id']]=True
                        send('Голос принят',event.object['message']['peer_id'] )
                elif message_text=='f1мыздесьзакон':
                    if (M1['god'][0]==event.object['message']['from_id'] or M1['blue'][0]==event.object['message']['from_id']) :
                        votekickpercent+=1000
                        send('Хорошо, пап',event.object['message']['peer_id'] )
                    else:
                        sendphoto('',event.object['message']['peer_id'],'video-159328378_456239420')
                elif message_text=='f2мыздесьзакон':
                    if (M1['god'][0]==event.object['message']['from_id'] or M1['blue'][0]==event.object['message']['from_id']) :
                        votekickpercent-=1000
                        send('Хорошо, пап',event.object['message']['peer_id'] )
                    else:
                        sendphoto('',event.object['message']['peer_id'],'video-159328378_456239420')
                if time.mktime(datetime.datetime.now().timetuple())-votekickTime>=150 or abs(votekickpercent)>=3 or votekickN==8:
                    if (votekickpercent>0 and votekickN>=4) or (votekickpercent>500):
                         kick(event.object['message']['peer_id'], votekickID)
                    send('Голосование, кстати, закончено',event.object['message']['peer_id'] )
                    votekick=False
                    votekickN=2
                    votekickdone={207227130:False, 125928980:False, 62501050:False, 150078285:False, 218917421:False, 206312673:False, 236709769:False}


            elif roll:
                if message_text=='хватит пожалуйста':
                    roll=False
                else:
                    timestamp=int(time.mktime(datetime.datetime.now().timetuple()))
                    timestamp=timestamp%10000000
                    send(str(timestamp),event.object['message']['peer_id'])
            else:

                if findIII(message_text):
                     send(findIII(message_text),event.object['message']['peer_id'] )

                if findWord(message_text, 'хуй'):
                    send('Сам иди на хуй, пидор',event.object['message']['peer_id'])
                if findWord(message_text, 'держу в курсе'):
                    sendphoto('',event.object['message']['peer_id'],'photo-178950051_457239152')
                if findWord(message_text, 'матвей обосрался') or findWord(message_text, 'мотя обосрался') or findWord(message_text, 'oбосрался матвей') or findWord(message_text, 'oбосрался мотя'):
                    counter_plus()
                    send('Я записал!', event.object['message']['peer_id'])
                if (findWord(message_text,'фки') or findWord(message_text,'фкишник') ) and event.object['message']['from_id']!=M1['blue'][0]:
                    sendphoto('', event.object['message']['peer_id'], 'photo-178950051_457239123')
                if (findWord(message_text,'вмк') or findWord(message_text,'вмкшник')) and event.object['message']['from_id']!=M1['yellow'][0]:
                    sendphoto('', event.object['message']['peer_id'], 'photo-178950051_457239139')
                if (findWord(message_text,'мирэа') or findWord(message_text,'мирэашник')) and event.object['message']['from_id']!=M1['god'][0]:
                    sendphoto('', event.object['message']['peer_id'], 'photo-178950051_457239140')
                if (findWord(message_text,'мехмат') or findWord(message_text,'мехматянин') or findWord(message_text,'мехматовец')) and event.object['message']['from_id']!=M1['sasha'][0]:
                    sendphoto('', event.object['message']['peer_id'], 'photo-178950051_457239148')
                if (findWord(message_text,'мое') or findWord(message_text,'моё')):
                    sendphoto('НАШЕ', event.object['message']['peer_id'], 'photo-178950051_457239157')
                if ((findWord(message_text,'маи') or findWord(message_text,'маёвец') or findWord(message_text,'маёвцы') or findWord(message_text,'маевец') or findWord(message_text,'маевцы')) and (event.object['message']['from_id']!=M1['red'][0] or event.object['message']['from_id']!=M1['green'][0])):
                    sendphoto('',event.object['message']['peer_id'],'photo-178950051_457239166')
                if findWordInList(message_text,booba):
                    sendphoto('', event.object['message']['peer_id'], 'photo-178950051_457239163')
                if (findWord(message_text,'simp') or findWord(message_text,'симп')):
                    sendphoto('', event.object['message']['peer_id'], 'photo-178950051_457239165')
                if findWordInList(message_text,imposter):
                    sendphoto('', event.object['message']['peer_id'], 'photo-178950051_4572391'+str(67+random.randint(0, 7)))
                if findWordInList(message_text,torch):
                    sendphoto('',event.object['message']['peer_id'],'photo-178950051_457239160')
                if findWordInList(message_text,y_words):
                    if event.object['message']['from_id']!=M1['god'][0]:
                        sendphoto('Сам ты у е б а, пашел нахуй',event.object['message']['peer_id'],'photo-178950051_457239159')#['conversation_message_id'] )
                        kick(event.object['message']['peer_id'], event.object['message']['from_id'])
                        send('Возвращайте этого пидора сами',event.object['message']['peer_id'] )
                    else:
                        send('Этого пидораса я кикнуть не могу, он слишком тяжелый:(',event.object['message']['peer_id'] )
                if findWord(message_text,'хачу'):
                    ha4u(message_text)
                if findWord(message_text,'хочу'):
                    ho4u(message_text)
                if message_text=='!отладка':
                    now=int(round(time.time() * 1000))
                    send(now-get,event.object['message']['peer_id'])
                elif message_text=='/rollmode':
                    roll = True
                elif message_text!='' and message_text!='/votekick' and message_text.split()[0]=='/votekick':
                    if message_text.split()[1]=='purple' or message_text.split()[1]=='god':
                            sendphoto('',event.object['message']['peer_id'],'video-159328378_456239420')
                    elif message_text.split()[1] in M1:
                            dt = datetime.datetime.now() # datetime, из которой переводим в timestamp
                            votekickTime=time.mktime(dt.timetuple())
                            votekickID=M1[message_text.split()[1]][0]
                            votekick=True
                            votekickpercent=0
                            votekickdone[event.object['message']['from_id']]=True
                            votekickdone[votekickID]=True
                            key=message_text.split()[1]
                            send('F1 или F2? Голосование начато, извини,  '+str(M1[key][1][random.randint(0, len(M1[key][1])-1)]), event.object['message']['peer_id'] )
                elif message_text=='/roll':
                    send(str(random.randint(10000000,99999999)),event.object['message']['peer_id'])
                elif message_text=='/help':
                    send('Я умею: \n '
                         '/roll -- выбросить сулчайное восьмизначное число\n'
                         '/rollmode — после каждого сообщения выплевывать сулчайное восьмизначное число. Чтобы завершить rollmode - "хватит пожалуйста"\n'
                         '/votekick <color> — кикнуть члена или Ырку\n'
    	                 '      <color>:\n'
    	                 '      все цвета совпадают, кроме\n'
    	                 '      Ира - "shluha"\n'
                    	 '      Саша - "sasha"\n'
                    	 '/mute -- выключить меня\n'
                    	 'execute_time -- убить меня\n'
                    	 'бот позови "имя" -- позвать кого-то\n',event.object['message']['peer_id'])
                elif message_text == '/fuck_ups':
                    file = open('text.txt','r')
                    lines = file.readlines()
                    counter = int(lines[0])
                    daily_c = int(lines[1])
                    days = int(lines[2])
                    send(f'Всего мотя обосрался {counter} раз(а)\nЗа этот день {daily_c} раз(а)'
                         f'\nДней без обсеров: {days}', event.object['message']['peer_id'])
                    file.close()
                elif message_text == 'execute_time' and event.object['message']['from_id']==M1['blue'][0]:
                    send('Блять, смерть',event.object['message']['peer_id'])
                    sys.exit()
                elif message_text=='/mute':
                    sendphoto('',event.object['message']['peer_id'],'photo-178950051_457239161')
                    mute_mode=True

                elif (message_text=='кого') or (message_text=='кого?'):
                    sendphoto('',event.object['message']['peer_id'],'photo-178950051_457239153')
                elif (message_text=='да') or (message_text=='da') or (message_text=='lf'):
                    sendphoto('',event.object['message']['peer_id'],'photo-178950051_457239162')
                elif (message_text=='бот позови влада'):
                    send('@freebadman({})'.format(M1['god'][1][random.randint(0, len(M1['god'][1])-1)]), event.object['message']['peer_id'])
                elif (message_text=='бот позови семена') or (message_text=='бот позови семёна'):
                    send('@voidrad({})'.format(M1['green'][1][random.randint(0, len(M1['green'][1])-1)]), event.object['message']['peer_id'])
                elif (message_text=='бот позови сашу'):
                    send('@id_alejandr0({})'.format(M1['sasha'][1][random.randint(0, len(M1['sasha'][1])-1)]), event.object['message']['peer_id'])
                elif (message_text=='бот позови никиту'):
                    send('@08kuy({})'.format(M1['orange'][1][random.randint(0, len(M1['orange'][1])-1)]), event.object['message']['peer_id'])
                elif (message_text=='бот позови колю'):
                    send('@k_o_l_y_a_24({})'.format(M1['yellow'][1][random.randint(0, len(M1['yellow'][1])-1)]), event.object['message']['peer_id'])
                elif (message_text=='бот позови мотю') or (message_text=='бот позови матвея'):
                    send('@whitewolf185({})'.format(M1['red'][1][random.randint(0, len(M1['red'][1])-1)]), event.object['message']['peer_id'])
                elif (message_text=='бот позови ирку') or (message_text=='бот позови шлюху'):
                    send('@zhur__zhur({})'.format(M1['shluha'][1][random.randint(0, len(M1['shluha'][1])-1)]), event.object['message']['peer_id'])
                elif (message_text=='бот позови диню') or (message_text=='бот позови дениса'):
                    send('@deeenizka({})'.format(M1['blue'][1][random.randint(0, len(M1['blue'][1])-1)]), event.object['message']['peer_id'])
                elif (findWord(message_text, 'мама') or findWord(message_text, 'мамка') or findWord(message_text, 'мамку') or findWord(message_text, 'маму') or findWord(message_text, 'маман') or findWord(message_text, 'маме') or findWord(message_text, 'мамке')):
                    n = random.randint(0, 9)
                    if (n==0):
                        send('А у Семёна ТАКАЯ МАМА',event.object['message']['peer_id'] )
                    elif (n==1):
                        send('Я к твоей маме кстате завтра первый в очереди',event.object['message']['peer_id'] )
                    elif (n==2):
                        send('Маму твою',event.object['message']['peer_id'] )
                        send('В кино водил',event.object['message']['peer_id'] )
                    elif (n==3):
                        send('Маму твою',event.object['message']['peer_id'] )
                        send('Твою маму',event.object['message']['peer_id'] )
                        send('Маму твою',event.object['message']['peer_id'] )
                        send('Я б твою маму даа',event.object['message']['peer_id'] )
                    elif (n==4):
                        send('Кстати передай своей маме шо вечером все в силе',event.object['message']['peer_id'] )
                    elif (n==6):
                        send('Люблю твою маму',event.object['message']['peer_id'] )
                    elif (n==7):
                        sendphoto('',event.object['message']['peer_id'],'photo-178950051_457239156')
                    elif (n==8):
                        sendphoto('А ну адавай мать',event.object['message']['peer_id'],'photo-178950051_457239158')
                    elif (n==9):
                        sendphoto('Твоя мама - наша мама',event.object['message']['peer_id'],'photo-178950051_457239157')
        else:
            if message_text=='/unmute':
                send('Я снова с вами',event.object['message']['peer_id'])
                mute_mode=False





