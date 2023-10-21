import random
import re
from datetime import date
from typing import Tuple

import openai

IMAGE_2_ID = {
    "dota": "photo-178950051_457239222",
    "nikita": "photo-178950051_457239218",
    "kick": "photo-178950051_457239159",
    "cringe": "photo-178950051_457239221",
}

Y_WORDS = [
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


def date2int(dt_time) -> int:
    return 10000 * dt_time.year + 100 * dt_time.month + dt_time.day


def int2date(dt) -> str:
    year = int(dt / 10000)
    month = int((dt % 10000) / 100)
    day = int(dt % 100)
    return date.strftime(date(year, month, day), "%y/%m/%d")


def get_today() -> int:
    return date2int(date.today())


def find_bI(msg) -> Tuple[str, bool]:
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


def find_word_in_list(msg, words) -> bool:
    for word in words:
        result = find_word(msg, word)
        if result:
            return True
    return False


def find_word(msg, word) -> bool:
    raw = "\\b" + word + ",?\\b"
    result = re.search(r"" + raw, msg)
    return result is not None


def generate_answer(prompt, from_id, history) -> str:
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
