import json
import random
import re
import sys
from datetime import date
from os.path import exists
from typing import Dict, List

import numpy as np
import pandas as pd
import yaml
from loguru import logger
from mubert import generate_music
from vkbottle.bot import Bot, Message
from vkbottle.dispatch.rules import ABCRule
from vkbottle.dispatch.rules.base import CommandRule
from vkbottle.tools import VoiceMessageUploader

logger.remove()
logger.add(sys.stderr, level="INFO")


class bICount(ABCRule[Message]):
    def __init__(self, max_bI=7):
        self.ceiling = max_bI

    async def check(self, event: Message) -> int:
        result = re.search(r"\bы+\b", event.text)
        randi = random.randint(0, self.ceiling)
        bI = randi
        if result is not None:
            if result.group(0) == "ы":
                return 1
            else:
                return bI
        return 0


class TextInMessage(ABCRule[Message]):
    def __init__(self, substrings: List[str]):
        self.patterns = substrings

    async def check(self, event: Message) -> bool:
        for word in self.patterns:
            raw = "\\b" + word + ",?\\b"
            result = re.search(r"" + raw, event.text)
            if result:
                return True
        return False


class MatveyIncBot(Bot):
    def __init__(self) -> None:
        with open("config.yml") as f_c:
            config = yaml.safe_load(f_c)
        with open(config["user_ids_json"], "r", encoding="utf-8") as fh:
            dicts = json.load(fh)
        super().__init__(token=config["token"])
        self.doters = dicts["doters"]
        self.vm_uploader = VoiceMessageUploader(self.api)  # see uploaders types in "Uploaders documentation" above

        self.CHANCE = 17
        self.y_words = [
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
        logger.info("Bot initialized!")

    def kick(self, user_id, chat_id):
        self.api.messages.remove_chat_user(chat_id=chat_id, user_id=user_id)

    def go_dota(self, from_id: str) -> str:
        """Send DotA invitation for all players except org

        Args:
            doters (Dict[int,str]):
            from_id (str): Organizer id

        Returns:
            str: Message for all
        """
        if from_id in list(self.doters.keys()):
            doter_2_kick = set([self.doters[from_id]])
            doters_2_poke = list(set(list(self.doters.values())) - doter_2_kick)
            amount_of_doters = len(doters_2_poke)
            mes = ""
            possible_phrase = [
                "го дота",
                "го сосать",
                "погнали гействовать",
                "как насчет мужского секса",
            ]
            splited_phrase = list(random.choice(possible_phrase))
            for item in enumerate(np.array_split(splited_phrase, amount_of_doters)):
                mes += doters_2_poke[item[0]] + "(" + "".join(item[1]) + ")"
            return mes
        return "Тебе не разрешено звать всех в доту, иди нахуй"

    def calculate_dick_size(self, user_id: int, id_2_name: Dict[int, str]) -> str:
        """Sends random dick size for user

        Args:
            user_id (int): User to calculate dick size
            id_2_name (Dict[int, str]): Dictionary with mmapping id:name

        Returns:
            str: Message for all
        """

        today = date.today().strftime("%d/%m/%Y")
        path_to_file = "dicks_sizes.csv"
        if exists(path_to_file):
            dicks = pd.read_csv(path_to_file)
        else:
            dicks = pd.DataFrame(index=[0])
            dicks["ymd"] = pd.to_datetime("01/01/1970", format="%d/%m/%Y")
        if dicks["ymd"].values[0] == today and user_id in dicks.columns:
            length = int(dicks[user_id].values[0])
        else:
            length = self.write_pisulku(dicks, user_id, today)

        if length < 10:
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

    def write_pisulku(self, dicks: pd.DataFrame, user_id: int, today: date) -> int:
        """Creates new actual user's dick size

        Args:
            dicks (pd.DataFrame): Dataframe with all dicks
            user_id (int): vk_id of user
            today (date): Todays date

        Returns:
            int: Dick size of user
        """
        length = self.random_dick_size()
        if dicks["ymd"].values[0] != today:
            dicks["ymd"] = today
            dicks = pd.DataFrame(dicks["ymd"])
        dicks[user_id] = length
        dicks.to_csv("dicks_sizes.csv", index=False)
        return length

    def random_dick_size(self):
        chance = random.randint(1, 20)
        if chance < 15:
            return random.randint(1, 24)
        elif chance < 20:
            return random.randint(25, 30)
        else:
            return random.randint(31, 35)

    def show_pisulki(self, dicts):
        today = date.today().strftime("%d/%m/%Y")
        path_to_file = "dicks_sizes.csv"
        file_exists = exists(path_to_file)
        print(file_exists)
        if file_exists:
            dicks = pd.read_csv(path_to_file)
        else:
            return "Записей о хуях нет"
        if dicks["ymd"].values[0] == today:
            return self.print_dicks(dicks, dicts)
        else:
            return "Сегодня хуями никто не мерился"

    def print_dicks(self, dicks, dicts):
        dt = dicks["ymd"].values[0]
        message = f"Ситуация на {dt}:\n"
        tmp_df = dicks.drop(columns="ymd").T.sort_values(by=0, ascending=False)
        for ind in tmp_df.index:
            message += f"{dicts[ind]} -- {tmp_df.loc[ind].values[0]} см\n"
        return message

    def send_track(self, prompt):
        # await generate_music(prompt)
        generate_music(prompt)


bot = MatveyIncBot()
bot.labeler.custom_rules["in_message"] = TextInMessage
bot.labeler.custom_rules["bI_in_message"] = bICount


@bot.on.message(CommandRule("трек", args_count=1, sep=","))
async def send_track(message: Message, args) -> str:
    logger.info(f"Generating song with prompt {args[0]}")
    bot.send_track(args[0])
    if exists("tmp_track.wav"):
        attachment = await bot.vm_uploader.upload(file_source="tmp_track.wav", title=args[0], peer_id=message.peer_id)
        await message.answer(args[0], attachment=attachment)
    else:
        await message.answer(f"Не удалось сгенерировать {args[0]}. Попробуйте еще раз")


@bot.on.message(command=("го дота", 0))
async def go_dota(message: Message) -> str:
    await message.answer(bot.go_dota(message.from_id))


@bot.on.message(command=("член", 0))
async def random_dick(message: Message) -> str:
    await message.answer(bot.calculate_dick_size(message.from_id))


@bot.on.message(command=("члены", 0))
async def show_actual_dicks(message: Message) -> str:
    await message.answer(bot.show_pisulki())


@bot.on.message(text="проверка жопы")
async def hi_handler(message: Message):
    users_info = await bot.api.users.get(message.from_id)
    await message.answer(f"Привет, {users_info[0].first_name}")


bot.run_forever()
