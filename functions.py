
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
    hn=24
    if now.hour<13:
        hn=12
    if (now.minute%10==0):
        with open ('semen.txt','r') as f:
            line=f.readlines()
            if line[0]!=str(now.day)+'\n':
                s='@voidrad(как) там малинка?'
                h=24
                if now.hour<13:
                    h=12
                with open ('semen.txt','w') as f:
                    f.write(str(now.day)+"\n"+str(h))
                return s
            elif hn!=int(line[1]):
                s='@voidrad(как) там малинка?'
                with open ('semen.txt','w') as f:
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
def ha4u(msg):
    words=msg.split()
    if len(words) in [2,3]:
        f=words.index("хачу")
        if len(words)==2:
            if (words[f-1]=='хачу' or words[f-1]=='хочу'):
                return False
            return words[f-1].upper()+' ХAЧУ'
        return words[f-2].upper()+' '+words[f-1].upper()+' ХAЧУ'
    return False
def ho4u(msg):
    words=msg.split()
    if len(words) in [2,3]:
        f=words.index("хочу")
        if len(words)==2:
            if (words[f-1]=='хачу' or words[f-1]=='хочу'):
                return False
            return words[f-1].upper()+' ХOЧУ'
        return words[f-2].upper()+' '+words[f-1].upper()+' ХOЧУ'
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
    I+="ы"*(randi-1)
    if result!= None:
        if result.group(0)=='ы':
            return 'Ы'
        else:
            return I
    else:
        return False