import json
import random
import re
from datetime import date

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
    groupID = config['group_id']  # id сообщества (не чата)
    vk_session = VkApi(token=token)  # авторизация
    longpoll = VkBotLongPoll(vk_session, groupID)
    global VK, PEER_ID
    VK = vk_session.get_api()
    chat_id = int(config['chat_id'])
    if debug:
        chat_id = 4
    PEER_ID = 2000000000 + chat_id
    with open(config['user_ids_json'], 'r', encoding='utf-8') as fh:
        dicts = json.load(fh)
    if debug:
        send("Работаем")
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
            print(event)
            message_text = event.object['message']['text'].lower()
            if message_text == '/член':
                calculate_dick_size(
                    str(event.object['message']['from_id']), dicts['users'])
            if findWord(message_text, "бот"):
                words = message_text.split()
                if len(words) == 3 and words[1] == 'позови':
                    if (words[2] == 'влада'):
                        outcome_text = f'@freebadman({random.choice(dicts["Matvey_inc_dict"]["purple"][1])})'
                    elif (words[2] == 'семена') or (words[2] == 'семёна') or (words[2] == 'cёму') or (words[2] == 'cему'):
                        outcome_text = f'@voidrad({random.choice(dicts["Matvey_inc_dict"]["green"][1])})'
                    elif (words[2] == 'сашу'):
                        outcome_text = f'@id_alejandr0({random.choice(dicts["Matvey_inc_dict"]["sasha"][1])})'
                    elif (words[2] == 'никиту'):
                        outcome_text = f'@08kuy({random.choice(dicts["Matvey_inc_dict"]["orange"][1])})'
                    elif (words[2] == 'колю'):
                        outcome_text = f'@k_o_l_y_a_24({random.choice(dicts["Matvey_inc_dict"]["yellow"][1])})'
                    elif (words[2] == 'мотю') or (words[2] == 'матвея'):
                        outcome_text = f'@whitewolf185({random.choice(dicts["Matvey_inc_dict"]["red"][1])})'
                    elif (words[2] == 'ирку') or (words[2] == 'шлюху') or (words[2] == 'иру'):
                        outcome_text = f'@zhur__zhur({random.choice(dicts["Matvey_inc_dict"]["shluha"][1])})'
                    elif (words[2] == 'диню') or (words[2] == 'дениса'):
                        outcome_text = f'@deeenizka({random.choice(dicts["Matvey_inc_dict"]["blue"][1])})'
                    if outcome_text != None:
                        send(outcome_text)
            if message_text == '/го дота':
                doters = dicts['doters']
                outcome_message = go_dota(doters, str(
                    event.object['message']['from_id']))
                send(outcome_message)


def go_dota(doters, from_id):
    if from_id in list(doters.keys()):
        doter_2_kick = set([doters[from_id]])
        doters_2_poke = list(set(list(doters.values()))-doter_2_kick)
        mes = ''
        words = ['го', " д", "о", "т", "а"]
        for i in range(len(doters_2_poke)):
            mes += doters_2_poke[i]+'('+words[i]+')'
        return mes
    return 'Тебе не разрешено звать всех в доту, иди нахуй'


def calculate_dick_size(user_id, id_2_name):
    today = date.today().strftime("%d/%m/%Y")
    try:
        dicks = pd.read_csv('dicks_sizes.csv')
        if dicks['ymd'] == today:
            length = int(dicks[user_id].values[0])
        else:
            raise Exception
    except KeyError:
        length = write_pisulku(dicks, user_id, today)
    finally:
        dicks = pd.DataFrame(index=[0])
        length = write_pisulku(dicks, user_id, today)
    if length < 10:
        emoji = '😥'
    elif length < 15:
        emoji = '😔'
    elif length < 17:
        emoji = '😯'
    elif length < 20:
        emoji = '😎'
    elif length < 25:
        emoji = '😳'
    elif length <= 30:
        emoji = '😧'
    elif length <= 35:
        emoji = '😨'
    possible_text = ['твой удав целых', 'авторитет у тебя целых', 'твой членохер аж',
                     "дудулька твоя целых", "твой чупа-чупс длиной", "твоя колбаска аж",
                     'твоя мясная пушка длиной', "ты можешь дать прикурить сигаретку длиной",
                     "твоя писюлька целых", "твоя волшебная палочка", "с таким дрыном шутки плохи -- целых"]
    message_outcome = id_2_name[user_id] + ', ' + \
        random.choice(possible_text) + ' ' + str(length) + 'см ' + emoji
    send(message_outcome)


def write_pisulku(dicks, user_id, today):
    length = random_dick_size()
    dicks[user_id] = length
    dicks['ymd'] = today
    dicks.to_csv('dicks_sizes.csv', index=True)
    return length


def random_dick_size():
    chance = random.randint(1, 20)
    if chance < 15:
        return random.randint(1, 24)
    elif chance < 20:
        return random.randint(25, 30)
    else:
        return random.randint(31, 35)


def send(msg):
    return VK.messages.send(random_id=random.randint(0, 999999), message=msg, peer_id=PEER_ID)


def findWord(msg, word):
    raw = '\\b'+word+',?\\b'
    result = re.search(r''+raw, msg)
    return result != None


if __name__ == '__main__':
    main()
