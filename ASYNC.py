import vk_api
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent, VkBotEvent
import asyncio
import random

async def timer(event, flag):
    send('пук', event.object['message']['peer_id'])
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 15
    while flag==False:

        for event in longpoll.listen():
            if loop.time() > end_time:
                send('15 секунд прошли', event.object['message']['peer_id'])
                flag = True
                break
            if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
                message_text = event.object['message']['text']
                if message_text == 'матвей':
                    send('пидор', event.object['message']['peer_id'])
            await asyncio.sleep(0.5)



async def main(event,flag):
    await timer(event,flag)



flag = False

BOT_TOKEN='632b29aa0814da3b42f343258974cc04b9eae751e0b533ce8ba36363d70f8f076fe09386f072f7d9f8c09'


groupID = 197390242
vk_session: VkApi = vk_api.VkApi(token=BOT_TOKEN)
longpoll = VkBotLongPoll(vk_session, groupID)
vk = vk_session.get_api()


def send(msg, peerID):
    vk.messages.send(random_id=random.randint(0, 999999), message=msg, peer_id=peerID)


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
        message_text = event.object['message']['text']
        if message_text == 'матвей':
            send('пидор',event.object['message']['peer_id'])
        if message_text == 'запусти таймер':
            asyncio.run(main(event,flag))
            flag = False





