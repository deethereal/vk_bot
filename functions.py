import random
import re
import time
import datetime
import vk_api
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll#, VkBotEventType
token = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' # Здесь ввести token сообщества (не удаляя апострофы)
groupID = 178950051
vk_session: VkApi = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, groupID)
vk = vk_session.get_api()
vk = vk_session.get_api()
def sendphoto(msg, peerID, attach): # msg — сообщение
    vk.messages.send(random_id=random.randint(0, 999999), message=msg, peer_id=peerID, attachment =attach)
def send(msg, peerID):
    vk.messages.send(random_id=random.randint(0, 999999), message=msg, peer_id=peerID)
def kick(chatID, userID):
    vk.messages.removeChatUser(chat_id=chatID%1000, user_id=userID)

def add(userID,chatID, timeout):
    time.sleep(timeout)
    vk.messages.addChatUser(user_id=userID, chat_id=chatID)
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
def printdic(dic):
    s=''
    dk=dic.keys()
    for key in dk:
        s+=key+' -- ' +str(not dic.get(key))+' \n'
    return s
def malina():
    now=datetime.datetime.now()
    if (now.minute%10==0):
        with open ('semen.txt','r') as f:
            line=f.read()
            if line!=str(now.day):
                send('@voidrad(как) там малинка?',event.object['message']['peer_id'] )
                newline=now.day
                with open ('semen.txt','w') as f:
                    f.write(str(newline))
def findWordInList(msg, words):
    for word in words:
        raw='\\b'+word+',?\\b'
        result = re.search(r''+raw, msg)
        if result!=None:
            return True
    return False
def ha4u(msg):
    words=msg.split()
    if len(words) in [1,2,3]:
        f=words.index("хачу")
        sendphoto(words[f-1].upper()+' ХАЧУ',event.object['message']['peer_id'],'photo-178950051_457239175')
def ho4u(msg):
    words=msg.split()
    if len(words) in [1,2,3]:
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
