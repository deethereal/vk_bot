
import random
import re
import datetime



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
def printdic(dic):
    s=''
    dk=dic.keys()
    for key in dk:
        s+=key+' -- ' +str(not dic.get(key))+' \n'
    return s
def malina():
    now=datetime.datetime.now()
    if (now.minute%10==0):
        with open ('semen.txt','r') as f:
            line=f.read()
            if line!=str(now.day):
                s='@voidrad(как) там малинка?'
                newline=now.day
                with open ('semen.txt','w') as f:
                    f.write(str(newline))
                return s
    return False
def findWordInList(msg, words):
    for word in words:
        raw='\\b'+word+',?\\b'
        result = re.search(r''+raw, msg)
        if result!=None:
            return True
    return False
def ha4u(msg):
    words=msg.split()
    if len(words) in [1,2,3]:
        f=words.index("хачу")
        return words[f-1].upper()+' ХAЧУ'
    return False
def ho4u(msg):
    words=msg.split()
    if len(words) in [1,2,3]:
        f=words.index("хочу")
        return words[f-1].upper()+' ХОЧУ'
    return False
def findWord(msg,word):
    raw='\\b'+word+',?\\b'
    result = re.search(r''+raw, msg)
    #print (result)
    if result!= None:
        return True
    else:
        return False
def findIII(msg):
    result = re.search(r'\bы+\b', msg)
    randi=random.randint(0,7)
    I='Ы'
    I*=randi
    if result!= None:
        if result.group(0)=='ы':
            return 'Ы'
        else:
            return I
    else:
        return False
