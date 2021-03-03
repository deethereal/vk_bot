import re
import markovify
import zipfile
import os

my_ponct='!#&*,;\^_`{}'
lin_way='/home/ubuntu/bot/vk_bot/data/'
mac_way='/Users/denis/Documents/vk_bot/data/'
T_lin_way='/home/ubuntu/test_bot/data/'
def proc():
    for i in range(1,5):
        with open (lin_way+'part'+str(i)+'.txt', 'r') as f:
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
        with open (lin_way+'part'+str(i)++str(i)+'.txt','w') as nf:
           for el in new_sentences:
            el.replace('🌚', ' 🌚')
            nf.write(el)
def create_one():
    for i in range(1,5):
        with open(lin_way+'part'+str(i)+'.txt', "r") as ch:
            text = ch.read()
        with open(lin_way+'text_model_1'+str(i)+'.json', "w") as f:
            f.write(markovify.Text(text, state_size=1,retain_original=False).to_json())
def create_two():
    for i in range(1, 5):
        with open(lin_way + 'part' + str(i) + '.txt', "r") as ch:
            text = ch.read()
        with open(lin_way + 'text_model_2' + str(i) + '.json', "w") as f:
            f.write(markovify.Text(text, state_size=2, retain_original=False).to_json())



def delete_old():
    with open (mac_way+'part4.txt') as ch:
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
    with open('/data/part4.txt', 'w') as nf:
        for el in new_sentences:
            nf.write(el)

def move_trash():
    for i in range(1,3):
        for j in range(1,4):
            os.remove('/Users/denis/Documents/vk_bot/scripts/text_model_'+str(i)+str(j)+'.json')
create_one()
create_two()
