import random
from os.path import exists
from typing import Dict

import pandas as pd

from .dick_sizer import DickSizer
from .utils import get_today


class RiceRatingCounter:
    def __init__(
        self,
        id_2_name: Dict[str, str],
        rating_file_path: str,
        dicks_file_path: str,
        default_rice: int = 100.0,
        max_daily_reward: int = 30.0,
        max_daily_punish: int = 30.0,
    ) -> None:
        self._id_2_name = id_2_name
        self._rating_file_path = rating_file_path
        self._dicks_file_path = dicks_file_path
        self.default_rice = default_rice
        self.max_daily_reward = max_daily_reward
        self.max_daily_punish = max_daily_punish
        self._today = None

    def calculate_social_rating(self, from_user_id: str, to_user_id: str, rice: str) -> str:
        """Updates and sends user's social rating

        Args:
            from_user_id (str): User who gives rice
            to_user_id (str): User who rice is given to (or taken from)
            rice (str): How much rice to given(eaten)
        Returns:
            str: Message for all
        """
        try:
            rice = int(rice)
        except ValueError:
            return "Неверное значение рис, попробуйте ввести число"

        self._today = get_today()
        if exists(self._rating_file_path):
            rating = pd.read_csv(self._rating_file_path, index_col=0)
        else:
            rating = self._init_rating()
        if rating.loc["last_change", from_user_id] != self._today:
            rating = self._daily_left_rice_update(rating, from_user_id)
        if rice == 0 or from_user_id == to_user_id:
            message_outcome = self._punish_joker(from_user_id)
        elif rating.loc["rating", from_user_id] >= 0:
            column_to_decrease = "reward_left" if rice > 0 else "punish_left"
            if rating.loc[column_to_decrease, from_user_id] - abs(rice) >= 0:
                rating.loc[column_to_decrease, from_user_id] -= abs(rice)
                rating.loc["rating", to_user_id] += rice
                message_outcome = (
                    f"{self._id_2_name[to_user_id]}, "
                    f"твой социальный рейтинг теперь {int(rating.loc['rating',to_user_id])}"
                )
            else:
                if rice > 0:
                    message_outcome = "Не хватает риса для завершения транзакции"
                elif rice < 0:
                    message_outcome = "Ты не сможешь столько съесть!"
        else:
            if rice > 0:
                action = "раздавать рис"
            elif rice < 0:
                action = "забирать рис у других"
            message_outcome = f"Гражданам с отрицательным социальным рейтингом запрещено {action}!"
        rating.to_csv(
            self._rating_file_path,
        )
        return message_outcome

    def show_rice(self, user_id: str) -> str:
        self._today = get_today()
        if exists(self._rating_file_path):
            rating = pd.read_csv(self._rating_file_path, index_col=0)
        else:
            rating = self._init_rating()
        if rating.loc["last_change", user_id] != self._today:
            rating = self._daily_left_rice_update(rating, user_id)

        if rating.loc["rating", user_id] >= 0:
            message_outcome = (
                f"{self._id_2_name[user_id]}, сегодня тебе можно:\n"
                f"- раздать рисинок: {int(rating.loc['reward_left',user_id])}\n"
                f"- забрать рисинок:  {abs(int(rating.loc['punish_left',user_id]))}"
            )
        else:
            message_outcome = (
                f"{self._id_2_name[user_id]}, ваш социальный"
                "рейтинг отрицателен, раздавать и забирать рис вам запрещено!"
            )
        rating.to_csv(
            self._rating_file_path,
        )
        return message_outcome

    def show_social_rating(self) -> str:
        self._today = get_today()
        if exists(self._rating_file_path):
            rating = pd.read_csv(self._rating_file_path, index_col=0)
        else:
            rating = self._init_rating()

        message = "Таблица социального рейтинга на сегодня такова:\n"
        for column in rating.columns:
            message += f"{self._id_2_name[column]}: \n"
            rice = rating.loc["rating", column]
            if rice >= 10000:
                message += f"-- {int(rice//10000)} гордость партии\n"
                rice = rice % 10000
            if rice >= 1000:
                message += f"-- {int(rice//1000)} кошка жена\n"
                rice = rice % 1000
            if rice >= 100:
                message += f"-- {int(rice//100)} миска рис\n"
                rice = rice % 100
            if rice > 0:
                message += f"-- {int(rice)} рисинок\n"
            if rice < 0:
                message += f"Позорник, должен партии {abs(int(rice))} рисинок\n"
        rating.to_csv(
            self._rating_file_path,
        )
        return message

    def _init_rating(self) -> pd.DataFrame:
        rating = pd.DataFrame(index=["rating", "reward_left", "punish_left", "last_change"])
        for user in self._id_2_name:
            rating[user] = [self.default_rice, self.max_daily_reward, self.max_daily_punish, self._today]
        return rating

    def _punish_joker(self, joker_id: str) -> str:
        length = random.randint(1, 3)
        if exists(self._dicks_file_path):
            dicks = pd.read_csv(self._dicks_file_path)
        else:
            dicks = pd.DataFrame(index=[0])
            dicks["ymd"] = self._today
        if dicks["ymd"].values[0] != self._today:
            dicks["ymd"] = self._today
            dicks = pd.DataFrame(dicks["ymd"])
        dicks[joker_id] = length
        dicks.to_csv(self._dicks_file_path, index=False)
        message_outcome = (
            "Пошутил, да? ну держи\n"
            f"{self._id_2_name[joker_id]}, {random.choice(DickSizer.POSSIBLE_TEXTS)} {length} см 🌚🌚🌚"
        )
        return message_outcome

    def _daily_left_rice_update(self, rating: pd.DataFrame, from_user_id: str) -> pd.DataFrame:
        """Updates reward and punish left for user depending on his rating

        Args:
            rating (pd.DataFrame): Social rating df
            from_user_id (str): whose rating to update

        Returns:
            pd.DataFrame: Updated social rating df
        """
        if rating.loc["rating", from_user_id] >= 0:
            daily_value = self.max_daily_reward
        else:
            daily_value = 0
        rating.loc["reward_left", from_user_id] = daily_value
        rating.loc["punish_left", from_user_id] = daily_value
        rating.loc["last_change", from_user_id] = self._today
        return rating
