import re
import markovify
import zipfile
import os

my_ponct='!#&*,;\^_`{}'
mac_way='/Users/denis/Documents/vk_bot/data/'
def proc():
    for i in range(1,4):
        with open ('/Users/denis/Documents/vk_bot/data/part'+str(i)+'.txt', 'r') as f:
            text=f.read()
        sentences = text.split('\n')
        new_sentences = []
        parasites = ["сука", "блин", '((((', '))))', '))0)']
        for el in sentences:
            el = re.sub('[%s]' % re.escape(my_ponct), '', el)
            if len(el)>3 and el not in parasites:
                el=el.replace('🌚', ' 🌚')
                el=el.replace('😎', ' 😎')
                if el[-1]=='?':
                    new_sentences.append((el.replace('?', ' ?. ')).lower())
                else:
                    new_sentences.append((el+". ").lower())
        print(len(new_sentences))
        print((new_sentences[0:10]))
        with open ('/Users/denis/Documents/vk_bot/data/part'+str(i)+'.txt','w') as nf:
           for el in new_sentences:
            el.replace('🌚', ' 🌚')
            nf.write(el)
def create_one():
    for i in range(1,4):
        with open(mac_way+'part'+str(i)+'.txt', "r") as ch:
            text = ch.read()
        with open(mac_way+'text_model_1'+str(i)+'.json', "w") as f:
            f.write(markovify.Text(text, state_size=1,retain_original=False).to_json())
        with zipfile.ZipFile(mac_way+'z1.zip', 'a') as z1:
            z1.write(mac_way+'text_model_1'+str(i)+'.json',arcname='text_model_1'+str(i)+'.json',compress_type=zipfile.ZIP_DEFLATED)
        os.remove(mac_way+'text_model_1'+str(i)+'.json')
def create_two():
    for i in range(1, 4):
        with open(mac_way + 'part' + str(i) + '.txt', "r") as ch:
            text = ch.read()
        with open(mac_way + 'text_model_2' + str(i) + '.json', "w") as f:
            f.write(markovify.Text(text, state_size=2, retain_original=False).to_json())
        with zipfile.ZipFile(mac_way + 'z2.zip', 'a') as z1:
            z1.write(mac_way + 'text_model_2' + str(i) + '.json', arcname='text_model_2' + str(i) + '.json',
                     compress_type=zipfile.ZIP_DEFLATED)
        os.remove(mac_way + 'text_model_2' + str(i) + '.json')
def delete_old():
    with open (mac_way+'chat.txt') as ch:
        text=ch.read()
    sentences = text.split('. ')
    print(sentences[5])
    new_sentences = []
    old_start= False
    old_beg='лещев сергей валерьевич'
    old_end='а умные люди думают об одном'
    for el in sentences:
        if el == old_beg:
            old_start=True
            print('перестал писать')
        if not old_start:
            new_sentences.append(el+'. ')
        if el == old_end:
            old_start=False
            print('снова начал писать')
    print(len(new_sentences))
    with open('/Users/denis/Documents/vk_bot/data/chat.txt', 'w') as nf:
        for el in new_sentences:
            nf.write(el)

def move_trash():
    for i in range(1,3):
        for j in range(1,4):
            os.remove('/Users/denis/Documents/vk_bot/scripts/text_model_'+str(i)+str(j)+'.json')
move_trash()