import json
import random
import warnings
from collections import defaultdict
from pickle import dump, load

import hydra
import numpy as np
from vk_api.bot_longpoll import VkBotEventType

import src.use_cases as use_cases
import src.utils as utils
from src import DickSizer, RiceRatingCounter, VkClient

warnings.filterwarnings("ignore", category=UserWarning)


@hydra.main(config_name="config")
def main(config):
    chat_id = int(config["chat_id"])
    if config.debug:
        chat_id = 4
    vk_client = VkClient(token=config.vk_token, group_id=config.group_id, chat_id=chat_id)
    with open(config.user_ids_json, "r", encoding="utf-8") as fh:
        dicts = json.load(fh)
    if config.debug:
        vk_client.send("Работаем")
    try:
        with open("history.pkl", "rb") as f:
            history = load(f)
    except FileNotFoundError:
        history = defaultdict(list)

    dick_sizer = DickSizer(config.dicks_path, id_2_name=dicts["users"])
    social_rating_counter = RiceRatingCounter(id_2_name=dicts["users"], **config.social_rating_settings)

    for event in vk_client.longpoll.listen():
        if (
            event.type == VkBotEventType.MESSAGE_NEW
            and event.from_chat
            and event.object["message"]["peer_id"] == vk_client.peer_id
        ):
            outcome_text = None
            from_id = event.object["message"]["from_id"]
            print(event)
            if "action" in event.object["message"]:
                action = event.object["message"]["action"]
                if action["member_id"] == dicts["Matvey_inc_dict"]["red"][0]:
                    if action["type"] == "chat_kick_user":
                        use_cases.set_motya_left_title(vk_client)
                if action["type"] == "chat_invite_user" and action["member_id"] == dicts["Matvey_inc_dict"]["red"][0]:
                    use_cases.set_motya_comeback_title(vk_client)
            message_text = event.object["message"]["text"].lower()
            if utils.find_word_in_list(message_text, utils.Y_WORDS):
                if from_id != dicts["Matvey_inc_dict"]["purple"][0]:
                    vk_client.send(
                        msg="Сам ты у е б а, пашел нахуй",
                        attach=utils.IMAGE_2_ID["kick"],
                    )
                    vk_client.kick(from_id)
                    if from_id == dicts["Matvey_inc_dict"]["red"][0]:
                        use_cases.set_motya_left_title(vk_client)
                    vk_client.send("Возвращайте этого пидора сами")

                else:
                    vk_client.send("Этого пидораса я кикнуть не могу, он слишком тяжелый:(")

            bI_pos = utils.find_bI(message_text)
            command_text = message_text.rstrip()
            if message_text[:5] == "бля а":
                vk_client.send(utils.generate_answer(event.object["message"]["text"][6:], from_id, history))
                with open("history.pkl", "wb") as f:
                    dump(history, f)
            if bool(bI_pos):
                vk_client.send(bI_pos)
            if command_text == "/член":
                outcome_text = dick_sizer.calculate_dick_size(str(from_id))
                vk_client.send(outcome_text)
            if command_text == "/члены":
                outcome_text = dick_sizer.print_dicks()
                vk_client.send(outcome_text)
            if command_text == "кринж":
                vk_client.send(use_cases.oh_no_cringe(), attach=utils.IMAGE_2_ID["cringe"])
            if command_text == "статус кринжа":
                vk_client.send(use_cases.cringe_status())
            if utils.find_word(message_text, "бот"):
                words = message_text.split()
                if len(words) == 3 and words[1] == "позови":
                    if words[2] in ("влада", "владика", "владека"):
                        outcome_text = f'@freebadman({random.choice(dicts["Matvey_inc_dict"]["purple"][1])})'
                    elif words[2] in ("семена", "семёна", "сёму", "сему"):
                        outcome_text = f'@voidrad({random.choice(dicts["Matvey_inc_dict"]["green"][1])})'
                    elif words[2] == "сашу":
                        outcome_text = f'@id_alejandr0({random.choice(dicts["Matvey_inc_dict"]["sasha"][1])})'
                    elif words[2] == "никиту":
                        outcome_text = f'@08kuy({random.choice(dicts["Matvey_inc_dict"]["orange"][1])})'
                    elif words[2] == "колю":
                        outcome_text = f'@k_o_l_y_a_24({random.choice(dicts["Matvey_inc_dict"]["yellow"][1])})'
                    elif words[2] in ("мотю", "матвея"):
                        outcome_text = f'@whitewolf185({random.choice(dicts["Matvey_inc_dict"]["red"][1])})'
                    elif words[2] in ("ирку", "шлюху", "иру"):
                        outcome_text = f'@zhur__zhur({random.choice(dicts["Matvey_inc_dict"]["shluha"][1])})'
                    elif words[2] in ("диню", "дениса"):
                        outcome_text = f'@deeenizka({random.choice(dicts["Matvey_inc_dict"]["blue"][1])})'
                    if outcome_text is not None:
                        attach = utils.IMAGE_2_ID["nikita"] if words[2] == "никиту" else None
                        vk_client.send(outcome_text, attach=attach)
            if message_text.startswith("/дать"):
                words = message_text.split()
                if len(words) == 3:
                    color = None
                    if words[1] in ("владу", "владику", "владиславу"):
                        color = "purple"
                    elif words[1] in ("семену", "семёну", "сёме", "семе", "semen"):
                        color = "green"
                    elif words[1] in ("саше", "александру"):
                        color = "sasha"
                    elif words[1] == "никите":
                        color = "orange"
                    elif words[1] in ("коле", "николаю"):
                        color = "yellow"
                    elif words[1] in ("моте", "матвею"):
                        color = "red"
                    elif words[1] in ("ирке", "шлюхе", "ире"):
                        color = "shluha"
                    elif words[1] in ("дине", "денису"):
                        color = "blue"

                if color is not None:
                    outcome_text = social_rating_counter.calculate_social_rating(
                        str(from_id),
                        str(dicts["Matvey_inc_dict"][color][0]),
                        words[2],
                    )
                    vk_client.send(outcome_text)
            if command_text == "/рейтинг":
                outcome_text = social_rating_counter.show_social_rating()
                vk_client.send(outcome_text)
            if command_text == "/рис":
                outcome_text = social_rating_counter.show_rice(str(from_id))
                vk_client.send(outcome_text)
            if message_text.startswith("/го дота") or command_text == "/го дота":
                residual_words = message_text.split(" ")[2:]
                additon = ""
                if len(residual_words) > 0:
                    if residual_words[0] in ("через", "в", "вечером"):
                        additon = " " + " ".join(residual_words)
                doters = dicts["doters"]
                outcome_message = use_cases.go_dota(doters, str(from_id))
                pic_chance = np.random.rand()
                attach = None
                if pic_chance <= config.pic_chance:
                    attach = utils.IMAGE_2_ID["dota"]
                vk_client.send(outcome_message + additon + "?", attach=attach)


if __name__ == "__main__":
    main()
