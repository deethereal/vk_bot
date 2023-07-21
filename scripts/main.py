import json
import random
import re
from collections import defaultdict
from datetime import date
from os.path import exists
from pickle import dump, load
from typing import Dict

import click
import numpy as np
import openai
import pandas as pd
import yaml
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll

with open("token.txt") as f:
    openai.api_key = f.readline()

CHANCE = 17
y_words = [
    "уеба",
    "уёба",
    "yеба",
    "уебa",
    "уeба",
    "yeба",
    "yебa",
    "уeбa",
    "yeба",
    "yёба",
    "уёбa",
    "yёбa",
    "yeбa",
]


@click.command()
@click.option("--debug/--no-debug", default=False)
def main(debug):
    with open("config.yml") as f_c:
        config = yaml.safe_load(f_c)
    token = config["token"]
    groupID = config["group_id"]  # id сообщества (не чата)
    vk_session = VkApi(token=token)  # авторизация
    longpoll = VkBotLongPoll(vk_session, groupID)
    global VK, PEER_ID, history
    VK = vk_session.get_api()
    chat_id = int(config["chat_id"])
    if debug:
        chat_id = 4
    PEER_ID = 2000000000 + chat_id
    with open(config["user_ids_json"], "r", encoding="utf-8") as fh:
        dicts = json.load(fh)
    if debug:
        send("Работаем")
    try:
        with open("history.pkl", "rb") as f:
            history = load(f)
    except FileNotFoundError:
        history = defaultdict(list)

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
            print(event)
            if (
                event.object["message"]["action"]["type"] == "chat_kick_user"
                and event.object["message"]["action"]["member_id"] == 207227130
            ):
                VK.messages.editChat(chat_id=chat_id, title="Matvey Inc. 3.1 - Семья снова без Матвея")
                send("На страже актуальности названия!")
            if (
                event.object["message"]["action"]["type"] == "chat_invite_user"
                and event.object["message"]["action"]["member_id"] == 207227130
            ):
                VK.messages.editChat(chat_id=chat_id, title="Matvey Inc. 3.1 - Семья снова c Матвеем")
                send("На страже актуальности названия!")

            message_text = event.object["message"]["text"].lower()
            if findWordInList(message_text, y_words):
                if event.object["message"]["from_id"] != dicts["Matvey_inc_dict"]["purple"][0]:
                    send(
                        msg="Сам ты у е б а, пашел нахуй",
                        attach="photo-178950051_457239159",
                    )
                    kick(
                        event.object["message"]["peer_id"],
                        event.object["message"]["from_id"],
                    )
                    send("Возвращайте этого пидора сами")
                else:
                    send("Этого пидораса я кикнуть не могу, он слишком тяжелый:(")

            bI_pos = findbI(message_text)
            command_text = message_text.rstrip()
            if message_text[:5] == "бля а":
                send(generate_answer(event.object["message"]["text"][6:], event.object["message"]["from_id"]))
                with open("history.pkl", "wb") as f:
                    dump(history, f)
            if bool(bI_pos):
                send(bI_pos)
            if command_text == "/член":
                outcome_text = calculate_dick_size(str(event.object["message"]["from_id"]), dicts["users"])
                send(outcome_text)
            if command_text == "/члены":
                outcome_text = show_pisulki(dicts["users"])
                send(outcome_text)
            if command_text == "кринж":
                send(oh_no_cringe(), attach="photo-178950051_457239221")
            if command_text == "статус кринжа":
                send(cringe_status())
            if findWord(message_text, "бот"):
                words = message_text.split()
                if len(words) == 3 and words[1] == "позови":
                    if words[2] == "влада":
                        outcome_text = f'@freebadman({random.choice(dicts["Matvey_inc_dict"]["purple"][1])})'
                    elif (
                        (words[2] == "семена") or (words[2] == "семёна") or (words[2] == "cёму") or (words[2] == "cему")
                    ):
                        outcome_text = f'@voidrad({random.choice(dicts["Matvey_inc_dict"]["green"][1])})'
                    elif words[2] == "сашу":
                        outcome_text = f'@id_alejandr0({random.choice(dicts["Matvey_inc_dict"]["sasha"][1])})'
                    elif words[2] == "никиту":
                        outcome_text = f'@08kuy({random.choice(dicts["Matvey_inc_dict"]["orange"][1])})'
                    elif words[2] == "колю":
                        outcome_text = f'@k_o_l_y_a_24({random.choice(dicts["Matvey_inc_dict"]["yellow"][1])})'
                    elif (words[2] == "мотю") or (words[2] == "матвея"):
                        outcome_text = f'@whitewolf185({random.choice(dicts["Matvey_inc_dict"]["red"][1])})'
                    elif (words[2] == "ирку") or (words[2] == "шлюху") or (words[2] == "иру"):
                        outcome_text = f'@zhur__zhur({random.choice(dicts["Matvey_inc_dict"]["shluha"][1])})'
                    elif (words[2] == "диню") or (words[2] == "дениса"):
                        outcome_text = f'@deeenizka({random.choice(dicts["Matvey_inc_dict"]["blue"][1])})'
                    if outcome_text is not None:
                        attach = "photo-178950051_457239218" if words[2] == "никиту" else None
                        send(outcome_text, attach=attach)
            if message_text.startswith("/дать"):
                if len(words) == 3 and words[2] in range [-30:30]:
                    if (words[1] == "владу") or (words[1] == "владику") or (words[1] == "владиславу"):
                        outcome_text = calculate_social_rating(str(event.object["message"]["from_id"]), dicts["Matvey_inc_dict"]["purple"][0], words[2], dicts["users"])
                    elif (
                        (words[1] == "семену") or (words[1] == "семёну") or (words[1] == "cёме") or (words[1] == "cеме")or (words[1] == "semen")
                    ):
                        outcome_text = calculate_social_rating(str(event.object["message"]["from_id"]), dicts["Matvey_inc_dict"]["green"][0], words[2], dicts["users"])
                    elif (words[1] == "саше") or (words[1] == "александру"):
                        outcome_text = calculate_social_rating(str(event.object["message"]["from_id"]), dicts["Matvey_inc_dict"]["sasha"][0], words[2], dicts["users"])
                    elif words[1] == "никите":
                        outcome_text = calculate_social_rating(str(event.object["message"]["from_id"]), dicts["Matvey_inc_dict"]["orange"][0], words[2], dicts["users"])
                    elif (words[1] == "коле") or (words[1] == "николаю"):
                        outcome_text = calculate_social_rating(str(event.object["message"]["from_id"]), dicts["Matvey_inc_dict"]["yellow"][0], words[2], dicts["users"])
                    elif (words[1] == "моте") or (words[1] == "матвею"):
                        outcome_text = calculate_social_rating(str(event.object["message"]["from_id"]), dicts["Matvey_inc_dict"]["red"][0], words[2], dicts["users"])
                    elif (words[1] == "ирке") or (words[1] == "шлюхе") or (words[1] == "ире"):
                        outcome_text = calculate_social_rating(str(event.object["message"]["from_id"]), dicts["Matvey_inc_dict"]["shluha"][0], words[2], dicts["users"])
                    elif (words[1] == "дине") or (words[1] == "денису"):
                        outcome_text = calculate_social_rating(str(event.object["message"]["from_id"]), dicts["Matvey_inc_dict"]["blue"][0], words[2], dicts["users"])
                else: outcome_text = "Нет, не дам"
                send(outcome_text)
            if command_text == "/рейтинг":
                outcome_text = show_social_rating(dicts["users"])
                send(outcome_text)
            if command_text == "/рис":
                outcome_text = show_rice(str(event.object["message"]["from_id"]), dicts["users"])
                send(outcome_text)
            if message_text.startswith("/го дота") or command_text == "/го дота":
                residual_words = message_text.split(" ")[2:]
                additon = ""
                if len(residual_words) > 0:
                    if residual_words[0] in ("через", "в", "вечером"):
                        additon = " " + " ".join(residual_words)
                doters = dicts["doters"]
                outcome_message = go_dota(doters, str(event.object["message"]["from_id"]))
                pic_chance = np.random.rand()
                attach = None
                if pic_chance < 0.17:
                    attach = "photo-178950051_457239222"
                send(outcome_message + additon + "?", attach=attach)


def generate_answer(prompt, from_id):
    if prompt == "забудь все":
        history[from_id].clear()
        return "История очищена"
    try:
        history[from_id].append({"role": "user", "content": prompt})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=history[from_id],
            max_tokens=1000,
            temperature=0.5,
        )
        answer_text = response.get("choices")[0]["message"]["content"]
        answer = f"Prompt: {prompt}\n\nAnswer: {answer_text}"
        if len(history[from_id]) > 3:
            history[from_id].pop(0)
        history[from_id].append({"role": "assistant", "content": answer_text})
    except Exception as e:
        answer = f"Иди нахуй. Ошибка {e}"
    return answer


def go_dota(doters: Dict[int, str], from_id: str) -> str:
    """Send DotA invitation for all players except org

    Args:
        doters (Dict[int,str]):
        from_id (str): Organizer id

    Returns:
        str: Message for all
    """

    if from_id in list(doters.keys()):
        doter_2_kick = set([doters[from_id]])
        doters_2_poke = list(set(list(doters.values())) - doter_2_kick)
        amount_of_doters = len(doters_2_poke)
        mes = ""
        possible_phrase = ["го дота", "го сосать", "погнали гействовать", "как насчет мужского секса", "го на мид"]
        splited_phrase = list(random.choice(possible_phrase))
        for item in enumerate(np.array_split(splited_phrase, amount_of_doters)):
            mes += doters_2_poke[item[0]] + "(" + "".join(item[1]) + ")"
        return mes
    return "Тебе не разрешено звать всех в доту, иди нахуй"


def calculate_dick_size(user_id: int, id_2_name: Dict[int, str]) -> str:
    """Sends random dick size for user

    Args:
        user_id (int): User to calculate dick size
        id_2_name (Dict[int, str]): Dictionary with mmapping id:name

    Returns:
        str: Message for all
    """

    today = date.today().strftime("%d/%m/%Y")
    path_to_file = "dicks_sizes.csv"
    file_exists = exists(path_to_file)
    print(file_exists)
    if file_exists:
        dicks = pd.read_csv(path_to_file)
    else:
        dicks = pd.DataFrame(index=[0])
        dicks["ymd"] = pd.to_datetime("01/01/1970", format="%d/%m/%Y")
    if dicks["ymd"].values[0] == today and user_id in dicks.columns:
        length = int(dicks[user_id].values[0])
    else:
        length = write_pisulku(dicks, user_id, today)

    if length < 5:
        emoji = "🌚🌚🌚"
    elif length < 10:
        emoji = "😥"
    elif length < 15:
        emoji = "😔"
    elif length < 17:
        emoji = "😯"
    elif length < 20:
        emoji = "😎"
    elif length < 25:
        emoji = "😳"
    elif length <= 30:
        emoji = "😧"
    elif length <= 35:
        emoji = "😨"
    possible_text = [
        "твой удав целых",
        "авторитет у тебя целых",
        "твой членохер аж",
        "дудулька твоя целых",
        "твой чупа-чупс длиной",
        "твоя колбаска аж",
        "твоя мясная пушка длиной",
        "ты можешь дать прикурить сигаретку длиной",
        "твоя писюлька целых",
        "твоя волшебная палочка",
        "с таким дрыном шутки плохи -- целых",
    ]
    message_outcome = id_2_name[user_id] + ", " + random.choice(possible_text) + " " + str(length) + "см " + emoji
    return message_outcome


def write_pisulku(dicks: pd.DataFrame, user_id: int, today: date) -> int:
    """Creates new actual user's dick size

    Args:
        dicks (pd.DataFrame): Dataframe with all dicks
        user_id (int): vk_id of user
        today (date): Todays date

    Returns:
        int: Dick size of user
    """
    length = random_dick_size()
    if dicks["ymd"].values[0] != today:
        dicks["ymd"] = today
        dicks = pd.DataFrame(dicks["ymd"])
    dicks[user_id] = length
    dicks.to_csv("dicks_sizes.csv", index=False)
    return length


def random_dick_size():
    chance = random.randint(1, 20)
    if chance < 15:
        return random.randint(1, 24)
    elif chance < 20:
        return random.randint(25, 30)
    else:
        return random.randint(31, 35)


def show_pisulki(dicts):
    today = date.today().strftime("%d/%m/%Y")
    path_to_file = "dicks_sizes.csv"
    file_exists = exists(path_to_file)
    print(file_exists)
    if file_exists:
        dicks = pd.read_csv(path_to_file)
    else:
        return "Записей о хуях нет"
    if dicks["ymd"].values[0] == today:
        return print_dicks(dicks, dicts)
    else:
        return "Сегодня хуями никто не мерился"


def print_dicks(dicks, dicts):
    dt = dicks["ymd"].values[0]
    message = f"Ситуация на {dt}:\n"
    tmp_df = dicks.drop(columns="ymd").T.sort_values(by=0, ascending=False)
    for ind in tmp_df.index:
        message += f"{dicts[ind]} -- {tmp_df.loc[ind].values[0]} см\n"
    return message

def calculate_social_rating(from_user_id: int, to_user_id: int, rice: int, dicts) -> str:
    """Updates and sends user's social rating

    Args:
        from_user_id (int): User who gives rice
        to_user_id (int): User who rice is given to (or taken from)
        rice (int): How much rice to given(eaten)
        dicts: Matvey Inc dicts 
    Returns:
        str: Message for all
    """
    id_2_name = dicts["users"]
    today = date.today().strftime("%d/%m/%Y")
    path_to_rating_file = "social_rating.csv"
    rating_file_exists = exists(path_to_rating_file)
    print(rating_file_exists)
    if rating_file_exists:
        rating = pd.read_csv(rating_file_exists)
    else:
        rating = pd.DataFrame(index=[0])
        rating[dicts["Matvey_inc_dict"]["red"][0]].values[0]=100
        rating[dicts["Matvey_inc_dict"]["orange"][0]].values[0]=100
        rating[dicts["Matvey_inc_dict"]["yellow"][0]].values[0]=100
        rating[dicts["Matvey_inc_dict"]["green"][0]].values[0]=100
        rating[dicts["Matvey_inc_dict"]["sasha"][0]].values[0]=100
        rating[dicts["Matvey_inc_dict"]["blue"][0]].values[0]=100
        rating[dicts["Matvey_inc_dict"]["purple"][0]].values[0]=100
        rating[dicts["Matvey_inc_dict"]["shluha"][0]].values[0]=100
    if rating[from_user_id].values[3] != today: # 0: rating, 1: rice left to give, 2: rice left to take(eat), 3: last time changed someone's rating
        if rating[from_user_id].values[0] >= 0:
            rating[from_user_id].values[1] = 30
            rating[from_user_id].values[2] = 30
        else:
            rating[from_user_id].values[1] = 0
            rating[from_user_id].values[2] = 0
        rating[from_user_id].values[3] = today
    if (rice>0):
        if rating[from_user_id].values[0] >= 0:
            if rating[from_user_id].values[1] - rice >= 0:
                rating[from_user_id].values[1] -= rice
                rating[to_user_id].values[0] += rice 
                message_outcome = id_2_name[to_user_id] + ", твой социальный рейтинг теперь "+rating[to_user_id].values[0]
            else:
                message_outcome = "Не хватает риса для завершения транзакции"
        else:
            message_outcome = "Гражданам с отрицательным социальным рейтингом запрещено раздавать рис!"
    elif (rice<0):
        if rating[from_user_id].values[0] >= 0:
            if rating[from_user_id].values[2] - rice <= 0:
                rating[from_user_id].values[2] += rice
                rating[to_user_id].values[0] += rice 
                message_outcome = id_2_name[to_user_id] + ", твой социальный рейтинг теперь "+rating[to_user_id].values[0]
            else:
                message_outcome = "Ты не сможешь столько съесть!"
        else:
            message_outcome = "Гражданам с отрицательным социальным рейтингом запрещено забирать рис у других!"
    else:
        length = random.randint(1,3)
        if dicks["ymd"].values[0] != today:
            dicks["ymd"] = today
            dicks = pd.DataFrame(dicks["ymd"])
        dicks[from_user_id] = length
        dicks.to_csv("dicks_sizes.csv", index=False)
        possible_text = [
        "твой удав целых",
        "авторитет у тебя целых",
        "твой членохер аж",
        "дудулька твоя целых",
        "твой чупа-чупс длиной",
        "твоя колбаска аж",
        "твоя мясная пушка длиной",
        "ты можешь дать прикурить сигаретку длиной",
        "твоя писюлька целых",
        "твоя волшебная палочка",
        "с таким дрыном шутки плохи -- целых",
        ]
        message_outcome = "Пошутил, да? ну держи\n"+id_2_name[from_user_id] + ", " + random.choice(possible_text) + " " + str(length) + "см 🌚🌚🌚"
    rating.to_csv("social_rating.csv", index=False)
    return message_outcome

def show_rice(user_id: int, id_2_name: Dict[int, str]):
    today = date.today().strftime("%d/%m/%Y")
    path_to_rating_file = "social_rating.csv"
    file_exists = exists(path_to_rating_file)
    print(file_exists)
    if file_exists:
        rating = pd.read_csv(path_to_rating_file)
    else:
        return "Записей о рисе нет"
    if rating[user_id].values[3] != today:
        if rating[user_id].values[0] >= 0:
            rating[user_id].values[1] = 30
            rating[user_id].values[2] = 30
        else:
            rating[user_id].values[1] = 0
            rating[user_id].values[2] = 0
        rating[user_id].values[3] = today
    if rating[user_id].values[0] >= 0:
        message_outcome = id_2_name[user_id]+", риса доступно для раздачи: " + rating[user_id].values[1] + ", риса можно забрать: " + rating[user_id].values[2]
    else:
        message_outcome = id_2_name[user_id]+", ваш социальный рейтинг отрицателен, раздавать и забирать рис вам запрещено!"
    return message_outcome

def show_social_rating(dicts):
    path_to_rating_file = "social_rating.csv"
    file_exists = exists(path_to_rating_file)
    print(file_exists)
    if file_exists:
        rating = pd.read_csv(path_to_rating_file)
    else:
        return "Записей о рейтинге нет"
    message = f"Таблица социального рейтинга на сегодня такова:"
    for column in rating.columns:
        message += f"{dicts[column]}: "
        rice = rating[column].values[0]
        if rice>=10000:
            message += f"\n----{rice//10000} Гордость партии"
            rice = rice % 10000
        if rice>=1000:
            message += f"\n----{rice//1000} Кошка жена"
            rice = rice % 1000
        if rice>=100:
            message += f"\n----{rice//100} Миска рис"
            rice = rice % 100
        if rice>0:
            message += f"\n----{rice} рисинка"
        if rice<=0:
            message += f"Позорник, должен партии {abs(rice)} рисинок"
    return message
    
def send(msg: str, attach: str = None):
    VK.messages.send(
        random_id=random.randint(0, 999999),
        message=msg,
        peer_id=PEER_ID,
        attachment=attach,
    )


def findbI(msg):
    result = re.search(r"\bы+\b", msg)
    randi = random.randint(0, 7)
    bI = "Ы"
    bI += "ы" * (randi - 1)
    if result is not None:
        if result.group(0) == "ы":
            return "Ы"
        else:
            return bI
    return False


def cringe_status(file_name="last_cringe_day"):
    # try:
    with open(file_name, "rb") as f:
        last_date = load(f)
    days_without_cringe = (date.today() - last_date).days
    return f"Дней без кринжа: {days_without_cringe}."
    # except FileNotFoundError:
    #    return "Кринжа не было уже 10 тысяч лет!"


def oh_no_cringe(file_name="last_cringe_day"):
    old_status = cringe_status(file_name)
    with open(file_name, "wb") as f:
        dump(date.today(), f)
    return old_status + "\nСчётчик обнулен!"


def findWordInList(msg, words):
    for word in words:
        result = findWord(msg, word)
        if result:
            return True
    return False


def findWord(msg, word):
    raw = "\\b" + word + ",?\\b"
    result = re.search(r"" + raw, msg)
    return result is not None


def kick(chatID, userID):
    VK.messages.removeChatUser(chat_id=chatID % 1000, user_id=userID)


if __name__ == "__main__":
    main()
