
import random
import re
import datetime
import numpy as np, pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
my_ponct='!#&*,;\^_`{}()🌚'
ho4u_words = ["хочу","хачу","я","ну","тоже", "а", "бля"]
def counter_plus():
    with open('text.txt', "r") as file:
        lines = file.readlines()
        counter = int(lines[0])
        daily_c = int(lines[1])
        for i in range(3):
            del lines[2 - i]
        counter += 1
        daily_c += 1
        days=0
        lines.insert(0, str(counter))
        lines.insert(1, '\n')
        lines.insert(2, str(daily_c))
        lines.insert(3, '\n')
        lines.insert(4, str(days))
        lines.insert(5, '\n')
    with open("text.txt", "w") as file:
        file.writelines(lines)

def find_id(name,dic):
    for item in dic:
        if name in dic[item][1]:
            return item, dic[item][0]
    return None

def printdic(dic):
    s=''
    dk=dic.keys()
    for key in dk:
        s+=key+' -- ' +str(not dic.get(key))+' \n'
    return s




def show_result(df, names, hs, colors, Name=None):
    int_hs = np.array([int(x[0:2]) for x in hs])
    if Name == None:
        fig, ax = plt.subplots(figsize=(20, 10))
        for i in range(len(names)):
            if i < 3:
                plt.bar(int_hs - ((3 - i) / 9), df[df.columns[i]].values, color=colors[i], label=names[i], width=1 / 9)
            else:
                plt.bar(int_hs + ((i - 3) / 9), df[df.columns[i]].values, color=colors[i], label=names[i], width=1 / 9)

        ax.set_xticks(int_hs)
        ax.set_xticklabels(hs)
        delta = timedelta(hours=3, minutes=0)
        now = datetime.now() + delta
        date_time_str = '2021-06-07 11:48'
        date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M%f')
        days = (now - date_time_obj).days
        data = "Данные с 07.06 11:48 по " + str(now.strftime("%d.%m %H:%M")) + "(" + str(days) + " целых дней)"
        plt.title(data, fontsize=16)
        plt.xlabel('Часы (левый включительно, правый нет)', fontsize=15)
        plt.ylabel('Количество дней, когда был онлайн больше 5 минут в это время', fontsize=15)
        plt.legend()
        plt.grid(True)
        plt.savefig('stat.jpg',dpi=100,bbox_inches='tight')
    else:
        valid_names = []
        invalid_names = []
        for name in Name:
            if name in df.columns:
                valid_names.append(name)
            else:
                invalid_names.append(name)
        if len(valid_names) != 0:
            true_val_names = []
            for teor_name in df.columns:
                if teor_name in valid_names:
                    true_val_names.append(teor_name)
            valid_names = true_val_names
            count = len(valid_names)
            fig, ax = plt.subplots(figsize=(20, 10))
            W = 2 / (3 * count)
            center = (count - 1) / 2
            for pair in enumerate(valid_names):
                if pair[1] == 'Семен':
                    c = colors[3]
                else:
                    c = colors[names.index(pair[1])]
                plt.bar(int_hs - 2 * (center - pair[0]) / (3 * count), df[pair[1]].values, color=c, label=pair[1],
                        width=W)
                plt.legend()

            ax.set_xticks(int_hs)
            ax.set_xticklabels(hs)
            delta = timedelta(hours=3, minutes=0)
            now = datetime.now() + delta
            date_time_str = '2021-06-07 11:48'
            date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M%f')
            days=(now - date_time_obj).days
            data = "Данные с 07.06 11:48 по " + str(now.strftime("%d.%m %H:%M"))+"("+str(days)+" целых дней)"
            plt.title(data, fontsize=16)
            plt.xlabel('Часы (левый включительно, правый нет)', fontsize=15)
            plt.ylabel('Количество дней, когда был онлайн больше 5 минут в это время', fontsize=15)
            plt.grid(True)
            plt.savefig('stat.jpg',dpi=100,bbox_inches='tight')
            if len(invalid_names) != 0:
                print("Я не нашел имена", *invalid_names)
        else:
            print("Я не нашел ни одного из данных имен")
def create_pic(names, hs, colors, Names=None):
    df = pd.read_csv('/home/ubuntu/bot/vk_bot/stat/dataframe.csv')
    df = df.set_index('hours')
    df = df.rename({'Cемен': 'Семен'}, axis=1)
    show_result(df, names,hs,colors,Names)
def malina():
    now=datetime.datetime.now()
    hn=24
    if now.hour<13:
        hn=12
    if (now.minute%10==0):
        with open ('150078285.txt','r') as f:
            line=f.readlines()
            if line[0]!=str(now.day)+'\n':
                s='@voidrad(как) там малинка?'
                h=24
                if now.hour<13:
                    h=12
                with open ('150078285.txt','w') as f:
                    f.write(str(now.day)+"\n"+str(h))
                return s
            elif hn!=int(line[1]):
                s='@voidrad(как) там малинка?'
                with open ('150078285.txt','w') as f:
                    f.write(str(now.day)+"\n"+str(hn))
                return s
    return False




def findWordInList(msg, words):
    for word in words:
        raw='\\b'+word+',?\\b'
        result = re.search(r''+raw, msg)
        if result!=None:
            return True
    return False






def ho4u(msg, par):
    if par == 'а':
        word = "хачу"
    else:
        word = "хочу"
    words = msg.split()
    words_len = len(words)
    if words_len > 1:
        f = words.index(word)
        if words_len < 6:
            ans = ''
            if f == words_len - 1:
                for i in range(words_len - 1):
                    words[i] = re.sub('[%s]' % re.escape(my_ponct), '', words[i])
                    if words[i] not in ho4u_words:
                        ans = ans + ' ' + words[i]
                if ans:
                    return ans.upper() + ' '+ word.upper()
            else:
                for i in range(f, len(words)):
                    words[i] = re.sub('[%s]' % re.escape(my_ponct), '', words[i])
                    if words[i] not in ho4u_words:
                        ans = ans + ' ' + words[i]
                if ans:
                    return ans.upper() + ' '+ word.upper()
    return False






def findIII(msg):
    result = re.search(r'\bы+\b', msg)
    randi=random.randint(0,7)
    I='Ы'
    I+="ы"*(randi-1)
    if result!= None:
        if result.group(0)=='ы':
            return 'Ы'
        else:
            return I
    else:
        return False

def find_word_dec_in_list(msg,arr):
    vowels='июоэаоеуыя'
    for word in arr:
        if (word[-1] not in vowels or word[-1]=='е' or word[-1]=='о') and second_dec(msg,word): #склоняет существительные второго склонения
            return True
    return False


def second_dec(msg,word):
    if findWord(msg, word ):
        return True
    if findWord(msg,word+'а'):
        return True
    if findWord(msg,word+'у'):
        return True
    if findWord(msg,word+'ом'):
        return True
    if findWord(msg,word+'е'):
        return True
    if findWord(msg,word+'ов'):
        return True
    if findWord(msg,word+'ам'):
        return True
    if findWord(msg,word+'ами'):
        return True
    if findWord(msg,word+'ах'):
        return True
    return False
