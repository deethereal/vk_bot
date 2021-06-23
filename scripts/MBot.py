import functions as f, mark as m, time, datetime, sys, random, vk_api, re
from vk_api.bot_longpoll import VkBotEventType
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.upload import VkUpload
import os
with open ('/home/ubuntu/bot/token.txt' , 'r') as t:
    token = t.readline().rstrip()
groupID = 178950051
vk_session: VkApi = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, groupID)
vk = vk_session.get_api()
joke = False
parasites=["сука","блин",'((((','))))','))0)' ]

id2name_color={207227130:['Матвей','#ff0000'], 125928980:['Никита','#ff5e00'], 62501050:['Коля','#ffee00'], 150078285:['Семен','#33b80f'], 218917421:['Саша','#00d5ff'], 206312673:['Денис',"#005eff"], 236709769:['Влад','#6600ff'], 240702553:['Ира','#000000']}

hs = []
for i in range(23):
    h=str(i)
    nh=str(i+1)
    if i<10:
        h='0'+h
        if i<9:
            nh='0'+nh
    hs.append(h+'-'+nh)
names=[]
colors = []
for k in id2name_color.keys():
    names.append(id2name_color[k][0])
    colors.append(id2name_color[k][1])
hs = []
for i in range(23):
    h=str(i)
    nh=str(i+1)
    if i<10:
        h='0'+h
        if i<9:
            nh='0'+nh
    hs.append(h+'-'+nh)
hs.append('23-00')
def upload_photo(upload, photo):
    response = upload.photo_messages(photo)[0]

    owner_id = response['owner_id']
    photo_id = response['id']
    access_key = response['access_key']
    return owner_id, photo_id, access_key

def mes_proc(my_ev):
    message_text = my_ev['message']['text'].lower()
    if message_text[0:16]!='всего сообщений:' and (message_text not in parasites) and (message_text!='') and (len(message_text)>3):
        with open('/home/ubuntu/bot/data/actual.txt', 'a') as c, open('/home/ubuntu/bot/data/'+str(my_ev['message']['from_id'])+'.txt', 'a') as p:
            out = re.sub('[%s]' % re.escape(my_ponct), '', message_text).replace('🌚',' 🌚')
            c.write(out + '. ')
            p.write(out + '. ')
def sendphoto(msg, peerID, attach): # msg — сообщение
    vk.messages.send(random_id=random.randint(0, 999999), message=msg, peer_id=peerID, attachment =attach)
def send(msg, peerID):
    return vk.messages.send(random_id=random.randint(0, 999999), message=msg, peer_id=peerID)
def send_upload_photo(peerID,owner_id, photo_id, access_key):
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    vk.messages.send(
        random_id=random.randint(0, 999999),peer_id=peerID,attachment=attachment)
def kick(chatID, userID):
    vk.messages.removeChatUser(chat_id=chatID%1000, user_id=userID)
def reply(msg, peerID,re_id):
    vk.messages.send(random_id=random.randint(0, 999999), message=msg, reply_to=re_id, peer_id=peerID)


my_ponct='!#&*,;\^_`{}'
motya_num=185
rid=12
roll=False
mute_mode=False
votekick = False
genamode=False
votekickTime=0
votekickID=0
votekickN=2
votekickpercent=0
M1 = {'red':[207227130,['мотя','матвей']], 'orange':[125928980,['никита','матвей...ой в смысле никита',"писюканов"]], 'yellow':[62501050,['коля',"колека"]], 'green':[150078285,['семён','семен','Semen','сема','сёма']], 'sasha':[218917421,['саша']], 'blue':[206312673,['диня',"денис"]],'god':[236709769,['влад']], 'shluha':[240702553,['ирка','шлюха','ира']]}
comands={'да':True, "хочу":False, "хачу":False, "кальян":False, "мама":False,"пидор":False,"ы":False,"хуй":True} #состояние выключенности команд, ВЫВОДИТСЯ ВКЛЮЧЕННОСТЬ!!
torch=['torch',"торч","калик","кальян","дядя коля","табак"]
imposter=['imposter','impostor']
ru_imp=['импостер',"импостор", "предатель","компостор","компостер","пидор", "пидорас"]
y_words=['уеба','уёба','yеба', 'уебa','уeба','yeба','yебa','уeбa','yeба','yёба','уёбa','yёбa', 'yeбa']
booba=["сиськи","сиська","сиську","грудь","boobs",'booba',"буба"]
votekickdone={207227130:False, 125928980:False, 62501050:False, 150078285:False, 218917421:False, 206312673:False, 236709769:False, 240702553:False}
with open('help.txt', 'r') as h, open('gen.txt', 'r') as g:
    text_help=h.read()
    text_gen=g.read()
models = m.get_model()
print("я прошел")
#send("Вас приветствует тестовый бот. Матвей -- пидор!",2000000001)
for event in longpoll.listen():
    joke=False
    flag=False
    MSG = []
    PHOTOS = []
    print (event)
    if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
        COMAND=False
        arrive=time.time_ns()
        message_text = event.object['message']['text'].lower()
        if message_text=='/help':
            COMAND=True
            if (event.object['message']['from_id']==M1['red'][0] and random.randint(0,199)==motya_num):
                sendphoto('Запрос отклонен по причине:',event.object['message']['peer_id'],'photo-178950051_457239178')
            else:
                send(text_help,event.object['message']['peer_id'])
        elif message_text=='/gen':
            COMAND=True
            if (event.object['message']['from_id']==M1['red'][0] and random.randint(0,199)==motya_num):
                sendphoto('Запрос отклонен по причине:',event.object['message']['peer_id'],'photo-178950051_457239178')
            else:
                send(text_gen,event.object['message']['peer_id'])
        elif message_text=='?mute?':
                send(str(mute_mode),event.object['message']['peer_id'])
        elif not mute_mode:
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
                else:
                    mes_proc(event.object)
                if time.mktime(datetime.datetime.now().timetuple())-votekickTime>=150 or abs(votekickpercent)>=3 or votekickN==8:
                    if (votekickpercent>0 and votekickN>=4) or (votekickpercent>500):
                        try:
                            kick(event.object['message']['peer_id'], votekickID)
                            send('Голосование, кстати, закончено',event.object['message']['peer_id'] )
                            votekick=False
                            votekickN=2
                            votekickdone={207227130:False, 125928980:False, 62501050:False, 150078285:False, 218917421:False, 206312673:False, 236709769:False}
                        except vk_api.exceptions.ApiError:
                            send('Эта хуйня слишком тяжелая, не могу(((',event.object['message']['peer_id'] )
                            votekick=False
                            votekickN=2
                            votekickdone={207227130:False, 125928980:False, 62501050:False, 150078285:False, 218917421:False, 206312673:False, 236709769:False}
            elif roll:
                if message_text=='хватит пожалуйста' or message_text=='!stop':
                    if (event.object['message']['from_id']==M1['red'][0] and random.randint(0,199)==motya_num):
                        sendphoto('Запрос отклонен по причине:',event.object['message']['peer_id'],'photo-178950051_457239178')
                    else:
                        roll=False
                        send('Останавливаю барабан', event.object['message']['peer_id'])

                else:
                    rid=rid +random.randint(1,42)
                    send(str(rid) ,event.object['message']['peer_id'])
            elif genamode:
                if message_text!="гена возьми":
                    send(m.use_model(mar_par,models), event.object['message']['peer_id'])
                    mes_proc(event.object)

                else:
                    if (event.object['message']['from_id'] == M1['red'][0] and random.randint(99, 199) == motya_num):
                        sendphoto('Запрос отклонен по причине:', event.object['message']['peer_id'],
                                  'photo-178950051_457239178')
                    else:
                        send("Закончилась генерация", event.object['message']['peer_id'])
                        genamode=False
            elif message_text == "!гена":
                if (event.object['message']['from_id'] == M1['red'][0] and random.randint(99, 199) == motya_num):
                    sendphoto('Запрос отклонен по причине:', event.object['message']['peer_id'],
                              'photo-178950051_457239178')
                else:
                    send(m.use_model(0,models), event.object['message']['peer_id'])
            elif message_text[0:5]=='!анек':
                if (event.object['message']['from_id'] == M1['red'][0] and random.randint(99, 199) == motya_num):
                    sendphoto('Запрос отклонен по причине:', event.object['message']['peer_id'],
                              'photo-178950051_457239178')
                else:
                    send('Внимание анекдот:',event.object['message']['peer_id'])
                    if len(message_text)==5:
                        send(m.anek(), event.object['message']['peer_id'])
                    else:
                        args=message_text[6:-1].split(',')
                        try:
                            send(m.anek(int(args[0]),int(args[1])), event.object['message']['peer_id'])
                        except:
                            send("Пошеел нахуй тестировщик хуев", event.object['message']['peer_id'])
            elif message_text == "!генаа":
                if (event.object['message']['from_id'] == M1['red'][0] and random.randint(99, 199) == motya_num):
                    sendphoto('Запрос отклонен по причине:', event.object['message']['peer_id'],
                              'photo-178950051_457239178')
                else:
                    send(m.use_model(1,models), event.object['message']['peer_id'])
            elif message_text[0:5]=='!гена':
                if (event.object['message']['from_id'] == M1['red'][0] and random.randint(99, 199) == motya_num):
                    sendphoto('Запрос отклонен по причине:', event.object['message']['peer_id'],
                              'photo-178950051_457239178')
                else:
                    var_par=1
                    strt=6
                    if message_text[5]=='а':
                        strt=7
                        var_par=2
                    if message_text[strt].isdigit():
                        nums=message_text[strt:-1].split(',')
                        if len(nums)==1:
                            nums.append(500)
                        send(m.size_of_sent(var_par,models,min_len=int(nums[0]),max_len=int(nums[1])),event.object['message']['peer_id'])
                    else:
                        wds = list(map(lambda x: x.replace(" ",""),message_text[strt:-1].split(',')))
                        if len(wds)==1:
                            send(m.sent_s(par=var_par, word=wds[0],models=models),event.object['message']['peer_id'])
                        elif len(wds)==2:
                            send(m.sent_s(par=var_par,word=wds[0],min_len=int(wds[1]), models=models),event.object['message']['peer_id'])
                        elif len(wds) == 3:
                            send(m.sent_s(par=var_par,word=wds[0],min_len=int(wds[1]) ,max_len=int(wds[2]),models=models),event.object['message']['peer_id'])
                        elif len(wds) == 4:
                            send(m.sent_s(par=var_par,word=wds[0],state=bool(wds[3]),min_len=int(wds[1]),max_len=int(wds[2]),models=models),event.object['message']['peer_id'])
            elif message_text=="генана":
                if (event.object['message']['from_id'] == M1['red'][0] and random.randint(99, 199) == motya_num):
                    sendphoto('Запрос отклонен по причине:', event.object['message']['peer_id'],
                              'photo-178950051_457239178')
                else:
                    mar_par=1
                    genamode=True
                    send("Началась генерация",event.object['message']['peer_id'])
            elif message_text=="генанаа":
                if (event.object['message']['from_id'] == M1['red'][0] and random.randint(99, 199) == motya_num):
                    sendphoto('Запрос отклонен по причине:', event.object['message']['peer_id'],
                              'photo-178950051_457239178')
                else:
                    mar_par=2
                    genamode=True
                    send("Началась генерация",event.object['message']['peer_id'])
            elif message_text[0:4]=='!сим': #ДОПИЛИТЬ КАК НАКОПИТСЯ
                print(message_text[5:])
                key,p_id=f.find_id(message_text[5:],M1)
                if key=='red':
                    if p_id:
                        send("Как сказла бы "+M1[key][1][random.randint(0, len(M1[key][1])-1)]+":\n"+m.simulate(int(random.randint(1,2)),str(p_id)),event.object['message']['peer_id'])
                    else:
                        send("Не нашел такого, попробуйте что-то более стандартное", event.object['message']['peer_id'])
                else:
                    send("Пока можно симулироовать только матвея:(", event.object['message']['peer_id'])
            elif message_text == '!онлайн':
                send("да-да", event.object['message']['peer_id'])
                dep = time.time_ns()
                send('задержка: '+str((dep-arrive)//10**6)+" мс", event.object['message']['peer_id'])
            elif message_text=="!жожо":
                send(m.jojo(),event.object['message']['peer_id'])
            elif message_text=='!тест':
                upload = VkUpload(vk)
                send_upload_photo(event.object['message']['peer_id'], *upload_photo(upload, '/home/ubuntu/bot/data/test.jpg'))
            elif message_text[:5]=="!стат":
                if message_text[6:12]=="онлайн":
                    if message_text[13:-2].replace(' ','').split(',')[0]=='':
                        f.create_pic(names,hs,colors)
                    else:
                        f.create_pic(names, hs, colors,message_text[13:-2].replace(' ','').split(','))
                    upload = VkUpload(vk)
                    send_upload_photo(event.object['message']['peer_id'],*upload_photo(upload, 'stat.png'))
                    os.remove('stat.png')

            elif message_text == '!отладка':
                np=str(random.randint(1,2))
                m.use_model(str(np))
                dep=time.time_ns()
                reply("Длительность генерации c параметром "+np+" : " + str((dep - arrive) // 10 ** 6) + " мс", event.object['message']['peer_id'], event.object['message']['id'])
            elif message_text == '/rollmode':
                if (event.object['message']['from_id'] == M1['red'][0] and random.randint(99, 199) == motya_num):
                    sendphoto('Запрос отклонен по причине:', event.object['message']['peer_id'],
                              'photo-178950051_457239178')
                else:
                    roll = True
                    rid = int(event.object['message']['conversation_message_id'])
                    send('Расскручиваю барабан', event.object['message']['peer_id'])
            elif message_text=='!обнова':
                send("Начинаю создание модели...",event.object['message']['peer_id'])
                del models
                st = time.time_ns()
                models=m.get_model()
                send("Модель создана за "+ str((time.time_ns() - st) // 10 ** 9)+' с', event.object['message']['peer_id'])
            elif message_text=="!версия":
                with open('/home/ubuntu/bot/data/log.txt', 'r') as log:
                    send(f"Последняя модель была создана {log.read()}", event.object['message']['peer_id'])
            else:
                if len(message_text.split())==2:
                    msg=message_text.split()
                    if msg[0]=='/mute':

                        if msg[1] in comands.keys():
                            if (event.object['message']['from_id']==M1['red'][0] and random.randint(0,199)==motya_num):
                                sendphoto('Запрос отклонен по причине:',event.object['message']['peer_id'],'photo-178950051_457239178')
                                COMAND=True
                            else:
                                comands[msg[1]]=True
                                send('Выключена команда {}'.format(msg[1]),event.object['message']['peer_id'])
                        else:
                            send("Такой команды нет",event.object['message']['peer_id'])
                    elif msg[0]=='/unmute':
                        if msg[1] in comands.keys():
                            if (event.object['message']['from_id']==M1['red'][0] and random.randint(0,199)==motya_num):
                                sendphoto('Запрос отклонен по причине:',event.object['message']['peer_id'],'photo-178950051_457239178')
                                COMAND=True
                            else:
                                comands[msg[1]]=False
                                send('Включена команда {}'.format(msg[1]),event.object['message']['peer_id'])
                        elif msg[1]=='all':
                            COMAND=True
                            for i in comands.keys():
                                comands[i]=False
                            send('Включены все команды ',event.object['message']['peer_id'])
                        else:
                            send("Такой команды нет",event.object['message']['peer_id'])
                if not COMAND:
                    mes_proc(event.object)
                    if event.object['message']['from_id']==M1['red'][0]:
                        num=random.randint(0,199)
                        print('got it:', num)
                        if num==motya_num:
                            joke=True
                    if ( f.findWord(message_text, 'на хуй') or  f.findWord(message_text, 'нахуй')) and not comands["хуй"]:
                        MSG.append('Сам иди на хуй, пидор')
                    if f.findWord(message_text,"бот"):
                        words=message_text.split()
                        if len(words)==3 and words[1]=='позови':
                            if (words[2]=='влада'):
                                MSG.append('@freebadman({})'.format(M1['god'][1][random.randint(0, len(M1['god'][1])-1)]))
                            elif (words[2]=='семена') or (words[2]=='семёна') or (words[2]=='cёму') or (words[2]=='cему'):
                                MSG.append('@voidrad({})'.format(M1['green'][1][random.randint(0, len(M1['green'][1])-1)]))
                            elif (words[2]=='сашу'):
                                MSG.append('@id_alejandr0({})'.format(M1['sasha'][1][random.randint(0, len(M1['sasha'][1])-1)]))
                            elif (words[2]=='никиту'):
                                MSG.append('@08kuy({})'.format(M1['orange'][1][random.randint(0, len(M1['orange'][1])-1)]))
                            elif (words[2]=='колю'):
                                MSG.append('@k_o_l_y_a_24({})'.format(M1['yellow'][1][random.randint(0, len(M1['yellow'][1])-1)]))
                            elif (words[2]=='мотю') or (words[2]=='матвея'):
                                MSG.append('@whitewolf185({})'.format(M1['red'][1][random.randint(0, len(M1['red'][1])-1)]))
                            elif (words[2]=='ирку') or (words[2]=='шлюху') or (words[2]=='иру') :
                                MSG.append('@zhur__zhur({})'.format(M1['shluha'][1][random.randint(0, len(M1['shluha'][1])-1)]))
                            elif (words[2]=='диню') or (words[2]=='дениса'):
                                MSG.append('@deeenizka({})'.format(M1['blue'][1][random.randint(0, len(M1['blue'][1])-1)]))
                    if f.findWord(message_text, 'держу в курсе'):
                        PHOTOS.append(['','photo-178950051_457239152'])
                    if f.findWord(message_text, 'матвей обосрался') or f.findWord(message_text, 'мотя обосрался') or f.findWord(message_text, 'oбосрался матвей') or f.findWord(message_text, 'oбосрался мотя'):
                        f.counter_plus()
                        MSG.append('Я записал!')
                    if (f.findWord(message_text,'фки') or f.findWord(message_text,'фкишник') ) and event.object['message']['from_id']!=M1['blue'][0]:
                        PHOTOS.append(['', 'photo-178950051_457239123'])
                    if (f.findWord(message_text,'вмк') or f.findWord(message_text,'вмкшник')) and event.object['message']['from_id']!=M1['yellow'][0]:
                        PHOTOS.append(['', 'photo-178950051_457239139'])
                    if (f.findWord(message_text,'мирэа') or f.findWord(message_text,'мирэашник')) and event.object['message']['from_id']!=M1['god'][0]:
                        PHOTOS.append(['','photo-178950051_457239140'])
                    if (f.findWord(message_text,'мехмат') or f.findWord(message_text,'мехматянин') or f.findWord(message_text,'мехматовец')) and event.object['message']['from_id']!=M1['sasha'][0]:
                        PHOTOS.append(['','photo-178950051_457239148'])
                    if (f.findWord(message_text,'мое') or f.findWord(message_text,'моё')):
                        PHOTOS.append(['НАШЕ',  'photo-178950051_457239157'])
                    if ((f.findWord(message_text,'маи') or f.findWord(message_text,'маёвец') or f.findWord(message_text,'маёвцы') or f.findWord(message_text,'маевец') or f.findWord(message_text,'маевцы')) and (event.object['message']['from_id']!=M1['red'][0] or event.object['message']['from_id']!=M1['green'][0])):
                        PHOTOS.append(['','photo-178950051_457239166'])
                    if f.findWordInList(message_text,booba):
                        PHOTOS.append(['', 'photo-178950051_457239163'])
                    if f.findWord(message_text,'доска') or f.findWord(message_text,'ирка'):
                        PHOTOS.append(['no booba?','photo-178950051_457239176'])
                    if (f.findWord(message_text,'simp') or f.findWord(message_text,'симп')):
                        PHOTOS.append(['','photo-178950051_457239165'])
                    if (f.findWordInList(message_text,imposter) or f.find_word_dec_in_list(message_text, ru_imp)) and not comands["пидор"]:
                        PHOTOS.append(['', 'photo-178950051_4572391'+str(67+random.randint(0, 7))])
                    if f.findWordInList(message_text,torch) and not comands["кальян"]:
                        PHOTOS.append(['','photo-178950051_457239160'])
                    if f.findWordInList(message_text,y_words):
                        if event.object['message']['from_id']!=M1['god'][0]:
                            sendphoto('Сам ты у е б а, пашел нахуй',event.object['message']['peer_id'],'photo-178950051_457239159')#['conversation_message_id'] )
                            kick(event.object['message']['peer_id'], event.object['message']['from_id'])
                            send('Возвращайте этого пидора сами',event.object['message']['peer_id'] )
                        else:
                            send('Этого пидораса я кикнуть не могу, он слишком тяжелый:(',event.object['message']['peer_id'] )
                    elif f.findWord(message_text,'хачу') and not comands["хочу"]:
                        try:
                            if (f.ha4u(message_text)):
                                PHOTOS.append([f.ha4u(message_text),'photo-178950051_457239175' ])
                        except ValueError:
                            continue
                    if f.findWord(message_text,'хочу') and not comands["хочу"] and not f.findWord(message_text,'не хочу'):
                        try:
                            if (f.ho4u(message_text)):
                                PHOTOS.append([f.ho4u(message_text),'photo-178950051_457239175' ])
                        except ValueError:
                            continue
                    if f.findIII(message_text) and not comands["ы"]:
                        MSG.append(f.findIII(message_text))

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
                    elif message_text == '/fuck_ups':
                        file = open('text.txt','r')
                        lines = file.readlines()
                        counter = int(lines[0])
                        daily_c = int(lines[1])
                        days = int(lines[2])
                        send(f'Всего мотя обосрался {counter} раз(а)\nЗа этот день {daily_c} раз(а)'
                             f'\nДней без обсеров: {days}', event.object['message']['peer_id'])
                        file.close()
                    elif message_text == 'execute_time':
                        send('Блять, смерть',event.object['message']['peer_id'])
                        sys.exit()
                    elif message_text=='/mute':
                        if (event.object['message']['from_id']==M1['red'][0] and random.randint(0,199)==motya_num):
                            sendphoto('Запрос отклонен по причине:',event.object['message']['peer_id'],'photo-178950051_457239178')
                        else:
                            sendphoto('',event.object['message']['peer_id'],'photo-178950051_457239161')
                            mute_mode=True
                    elif message_text=='/commands':
                        send(f.printdic(comands),event.object['message']['peer_id'])
                    elif (message_text=='кого') or (message_text=='кого?'):
                        sendphoto('',event.object['message']['peer_id'],'photo-178950051_457239153')
                    elif ((message_text=='да') or (message_text=='da') or (message_text=='lf')) and not comands["да"]:
                        sendphoto('',event.object['message']['peer_id'],'photo-178950051_457239162')
                    elif (f.findWord(message_text, 'мама') or f.findWord(message_text, 'мамка') or f.findWord(message_text, 'мамку') or f.findWord(message_text, 'маму') or f.findWord(message_text, 'маман') or f.findWord(message_text, 'маме') or f.findWord(message_text, 'мамке')) and not comands["мама"]:
                        n = random.randint(0, 10)
                        if (n==0):
                            MSG.append('А у Семёна ТАКАЯ МАМА' )
                        elif (n==1):
                            MSG.append('Я к твоей маме кстате завтра первый в очереди')
                        elif (n==2):
                            MSG.append('Маму твою\nВ кино водил' )
                        elif (n==3):
                            MSG.append('Маму твою\nТвою маму\nМаму \nЯ б твою маму даа')
                        elif (n==4):
                            MSG.append('Кстати передай своей маме шо вечером все в силе' )
                        elif (n==6):
                            MSG.append('Люблю твою маму' )
                        elif (n==7):
                            PHOTOS.append(['','photo-178950051_457239156'])
                        elif (n==8):
                            PHOTOS.append(['А ну адавай мать','photo-178950051_457239158'])
                        elif (n==9):
                            PHOTOS.append(['Твоя мама - наша мама','photo-178950051_457239157'])
                        elif (n==10):
                            PHOTOS.append(['','photo-178950051_457239181'])

                    if len(MSG)!=0 and len(PHOTOS)!=0:
                        if joke:
                            sendphoto('Запрос отклонен по причине:',event.object['message']['peer_id'],'photo-178950051_457239178')
                        else:
                            if random.randint(0,1)==1:
                                send(MSG[random.randint(0,len(MSG)-1)].capitalize(),event.object['message']['peer_id'])
                            else:
                                r_id=random.randint(0,len(PHOTOS)-1)
                                sendphoto(PHOTOS[r_id][0],event.object['message']['peer_id'],PHOTOS[r_id][1])
                    elif len(MSG)!=0:
                        if joke:
                            sendphoto('Запрос отклонен по причине:',event.object['message']['peer_id'],'photo-178950051_457239178')
                        else:
                            send(MSG[random.randint(0, len(MSG) - 1)], event.object['message']['peer_id'])
                    elif len(PHOTOS)!=0:
                        if joke:
                            sendphoto('Запрос отклонен по причине:',event.object['message']['peer_id'],'photo-178950051_457239178')
                        else:
                            r_id = random.randint(0, len(PHOTOS) - 1)
                            sendphoto(PHOTOS[r_id][0], event.object['message']['peer_id'], PHOTOS[r_id][1])
                    elif joke:
                            sendphoto('',event.object['message']['peer_id'],'photo-178950051_457239178')

        else:
            if message_text=='/unmute':
                if (event.object['message']['from_id']==M1['red'][0] and random.randint(0,199)==motya_num):
                    sendphoto('Запрос отклонен по причине:',event.object['message']['peer_id'],'photo-178950051_457239178')
                else:
                    send('Я снова с вами',event.object['message']['peer_id'])
                    mute_mode=False
            else:
                mes_proc(event.object)
