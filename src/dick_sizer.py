import random
from os.path import exists
from typing import Dict

import pandas as pd

from .utils import get_today, int2date


class DickSizer:
    POSSIBLE_TEXTS = [
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

    def __init__(self, file_path: str, id_2_name: Dict[str, str]) -> None:
        self._path_to_file = file_path
        self._id_2_name = id_2_name
        self._today = None

    def print_dicks(self) -> str:
        self._today = get_today()
        if exists(self._path_to_file):
            dicks = pd.read_csv(self._path_to_file)
        else:
            return "Записей о хуях нет"
        if dicks["ymd"].values[0] == self._today:
            return self._get_actual_dicks(dicks)
        else:
            return "Сегодня хуями никто не мерился"

    def calculate_dick_size(self, user_id: int) -> str:
        """Sends random dick size for user

        Args:
            user_id (int): User to calculate dick size
        Returns:
            str: Message for all
        """
        self._today = get_today()
        if exists(self._path_to_file):
            dicks = pd.read_csv(self._path_to_file)
        else:
            dicks = pd.DataFrame(index=[0])
            dicks["ymd"] = self._today
        if dicks["ymd"].values[0] == self._today and user_id in dicks.columns:
            length = int(dicks[user_id].values[0])
        else:
            length = self._write_pisulku(dicks, user_id)

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

        message_outcome = f"{self._id_2_name[user_id]} {random.choice(self.POSSIBLE_TEXTS)} {length} см {emoji}"
        return message_outcome

    def _write_pisulku(
        self,
        dicks: pd.DataFrame,
        user_id: int,
    ) -> int:
        """Creates new actual user's dick size

        Args:
            dicks (pd.DataFrame): Dataframe with all dicks
            user_id (int): vk_id of user
            self._today (date): Todays date

        Returns:
            int: Dick size of user
        """
        length = DickSizer._random_dick_size()
        if dicks["ymd"].values[0] != self._today:
            dicks["ymd"] = self._today
            dicks = pd.DataFrame(dicks["ymd"])
        dicks[user_id] = length
        dicks.to_csv(self._path_to_file, index=False)
        return length

    @staticmethod
    def _random_dick_size() -> int:
        chance = random.randint(1, 20)
        if chance < 15:
            return random.randint(1, 24)
        elif chance < 20:
            return random.randint(25, 30)
        else:
            return random.randint(31, 35)

    def _get_actual_dicks(self, dicks) -> str:
        dt = dicks["ymd"].values[0]
        message = f"Ситуация на {int2date(dt)}:\n"
        tmp_df = dicks.drop(columns="ymd").T.sort_values(by=0, ascending=False)
        for ind in tmp_df.index:
            message += f"{self._id_2_name[ind]} -- {tmp_df.loc[ind].values[0]} см\n"
        return message
