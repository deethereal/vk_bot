import random
import re
from datetime import date

import openai


def date2int(dt_time):
    return 10000 * dt_time.year + 100 * dt_time.month + dt_time.day


def int2date(dt):
    year = int(dt / 10000)
    month = int((dt % 10000) / 100)
    day = int(dt % 100)

    return date.strftime(date(year, month, day), "%d/%m/%y")


def get_today():
    return date2int(date.today())


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


def generate_answer(prompt, from_id, history):
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
