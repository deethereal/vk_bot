import random

from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll


class VkClient:
    def __init__(self, token, group_id, chat_id) -> None:
        vk_session = VkApi(token=token)  # авторизация
        self.longpoll = VkBotLongPoll(vk_session, group_id)
        self._instance = vk_session.get_api()
        self._chat_id = chat_id
        self.peer_id = 2000000000 + chat_id

    def send(self, msg: str, attach: str = None) -> None:
        self._instance.messages.send(
            random_id=random.randint(0, 999999),
            message=msg,
            peer_id=self.peer_id,
            attachment=attach,
        )

    def kick(self, user_id) -> None:
        self._instance.messages.removeChatUser(chat_id=self._chat_id, user_id=user_id)

    def change_title(self, new_title) -> None:
        self._instance.messages.editChat(chat_id=self._chat_id, title=new_title)
