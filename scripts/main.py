import json
import random
from email.mime import message
from email.policy import default
from os.path import exists

import click
import pandas as pd
import yaml
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll

CHANCE = 17

@click.command()
@click.option('--debug/--no-debug', default=False)
def main(debug):
    with open('config.yml') as f_c:
        config = yaml.safe_load(f_c)
    token = config['token']
    groupID = config['group_id'] # id сообщества (не чата)
    vk_session = VkApi(token=token) # авторизация
    longpoll = VkBotLongPoll(vk_session, groupID)
    global VK, PEER_ID
    VK = vk_session.get_api()
    chat_id = int(config['chat_id'])
    if debug:
        chat_id = 4
    PEER_ID = 2000000000 + chat_id
    with open(config['user_ids_json'], 'r', encoding='utf-8') as fh:  
        id_2_name = json.load(fh)     
    if debug:
        send("Работаем")
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
            print(event)
            message_text = event.object['message']['text'].lower()
            if message_text == '/член':
                calculate_dick_size(str(event.object['message']['from_id']), id_2_name)
                
                

def calculate_dick_size(user_id, id_2_name):
    if exists('dicks_sizes.csv'):
        dicks = pd.read_csv('dicks_sizes.csv')
        print(dicks)
        if user_id in dicks.columns:
            length = int(dicks[user_id].values[0])
        else:
            length = random_dick_size()
            dicks[user_id] = length
            dicks.to_csv('dicks_sizes.csv', index=True)
    else:
        dicks = pd.DataFrame(index=[0])
        length = random_dick_size()
        dicks[user_id] = length
        dicks.to_csv('dicks_sizes.csv', index=True)
    if length<10:
        emoji = '😥'
    elif length<15:
        emoji = '😔'
    elif length<17:
        emoji = '😯'
    elif length<20:
        emoji = '😎'
    elif length<25:
        emoji = '😳'
    elif length<=30:
        emoji = '😧'
    elif length<=35:
        emoji = '😨'
    possible_text = ['твой удав целых', 'авторитет у тебя целых', 'твой членохер аж',
        "дудулька твоя целых", "твой чупа-чупс длиной", "твоя колбаска аж",
        'твоя мясная пушка длиной', "ты можешь дать прикурить сигаретку длиной",
        "твоя писюлька целых", "твоя волшебная палочка", "с таким дрыном шутки плохи -- целых"]  
    message_outcome = id_2_name[user_id] + ', '+ random.choice(possible_text) + ' '+ str(length) + 'см ' + emoji
    send(message_outcome)

def random_dick_size():
    chance = random.randint(1,20)
    if chance<15:
        return random.randint(1,24)
    elif chance<20:
        return random.randint(25,30)
    else: 
        return random.randint(31,35)
def send(msg):
    return VK.messages.send(random_id=random.randint(0, 999999), message=msg, peer_id=PEER_ID)


if __name__ == '__main__':
    main()
