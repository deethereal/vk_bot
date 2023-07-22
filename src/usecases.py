import random
from datetime import date
from pickle import dump, load
from typing import Dict

import numpy as np


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


def go_dota(doters: Dict[int, str], from_id: str) -> str:
    """vk_client.send DotA invitation for all players except org

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


def set_motya_left_title(vk_client):
    vk_client.change_title("Matvey Inc. 3.1 - Семья без Матвея")
    vk_client.send("На страже актуальности названия!")


def set_motya_comeback_title(vk_client):
    vk_client.change_title("Matvey Inc. 3.1 - Семья снова c Матвеем")
    vk_client.send("На страже актуальности названия!")
