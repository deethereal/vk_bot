import markovify
import time
import random

lin_way='/home/ubuntu/bot/data/'
mac_way='/Users/denis/Documents/vk_bot/data/'
T_lin_way='/home/ubuntu/test_bot/data/'

def get_model():
    combined_model = [None,None]
    for j in range(0,2):
        for i in range(1, 6):
            print("Cоздаю модель "+str(j+1) + " номер "+str(i))
            with open(lin_way+'text_model_'+str(j+1)+str(i)+'.json',"r") as f:
                model = markovify.Text.from_json(f.read())
                if combined_model[j]:
                    combined_model[j] = markovify.combine(models=[combined_model[j], model])
                else:
                    combined_model[j] = model
            print("Cоздал модель " + str(j + 1) + " номер " + str(i))
        with open(lin_way + 'actual.txt',"r") as f:
            model = markovify.Text(f.read(), state_size=j+1, retain_original=False)
        combined_model[j] = markovify.combine(models=[combined_model[j], model])
    print("Cоздал оригинал")
    with open('/home/ubuntu/bot/data/log.txt', "w") as f:
        seconds=time.time()+3600*3
        now=time.ctime(seconds)
        x = ' '.join(now.split()[1:-1])[0:-3]
        f.write(x)
    return combined_model
def use_model(par,models):
    par-=1
    model=models[par]
    result=model.make_sentence()
    if result is not None:
        return result.capitalize().replace('.', ' ').replace(" ?", "? ")
    for _ in range(150):
        if result is not None:
            return result.capitalize().replace('.', ' ').replace(" ?", "? ")
        else:
            result = model.make_sentence()
    return "мне не хватило 150 итераци, давай еще"


def sent_s(par,word,models,min_len=1, max_len=500,state=False):
    st = time.time_ns()
    if min_len<1:
        return "Укажите большую длину "
    else:
        model = models[par-1]
        if st:
            try:
                result = model.make_sentence_with_start(beginning=word, max_words=max_len,strict=state, min_words=min_len, max_overlap_ratio=0.49)
                if result is not None:
                    return result.capitalize().replace('.', ' ').replace(" ?", "? ")
                for _ in range(150):
                    result = model.make_sentence_with_start(beginning=word, max_words=max_len, min_words=min_len,
                                                            strict=state, max_overlap_ratio=0.49)
                    if result is not None:
                        return result.capitalize().replace('.', ' ').replace(" ?", "? ")
                return "мне не хватило 150 итераци, давай еще"
            except KeyError:
                return f"Слова {word} нет в тексте, задайте другое"
            except markovify.text.ParamError:
                return f"Слово {word} не является началом ни в одном предложении, задайте другое. Либо я долбоеб и не смог построить предложение минимальной длины."
        else:
            try:
                result = model.make_sentence_with_start(beginning=word, max_words=max_len, min_words=min_len,strict=st, max_overlap_ratio=0.49)
                while result is None:
                    result = model.make_sentence_with_start(beginning=word, max_words=max_len, min_words=min_len,strict=st, max_overlap_ratio=0.49)
                return result.capitalize().replace('.', ' ').replace(" ?", "? ")
            except KeyError:
                return f"Слова {word} нет в тексте, задайте другое"
            except markovify.text.ParamError:
                result = model.make_sentence_with_start(beginning=word, max_words=max_len, min_words=min_len,strict=st, max_overlap_ratio=0.49)
                for _ in range(50):
                    if result is not None:
                        return result.capitalize().replace('.', ' ').replace(" ?", "? ")
                    else:
                        result = model.make_sentence_with_start(beginning=word, max_words=max_len, min_words=min_len,strict=st, max_overlap_ratio=0.49)
                return f"Слово {word} нет является началом ни в одном предложении, задайте другое. Либо я долбоеб и не смог построить предложение минимальной длины."


def size_of_sent(par,models,min_len=1, max_len=500):
    if min_len<1:
        return "Введите положительную длину"
    else:
        st = time.time_ns()
        par -= 1
        model = models[par]
        result = model.make_sentence(max_words=max_len, min_words=min_len)
        if result is not None:
            return result.capitalize().replace('.', ' ').replace(" ?", "? ")
        for _ in range(150):
            if result is not None:
                return result.capitalize().replace('.', ' ').replace(" ?", "? ")
            else:
                result = model.make_sentence(max_words=max_len, min_words=min_len)
        return "мне не хватило 150 итераци, давай еще"
def simulate(par,id):
    with open(lin_way+'ids/'+str(id)+'.txt','r') as f:
        text=f.read()
    text_model=markovify.Text(text, state_size=par)
    result = text_model.make_sentence()
    while result is None:
            result = text_model.make_sentence()
    return result.capitalize().replace('.', ' ').replace(" ?", "? ")
def jojo():
    with open(lin_way+'jojo.txt','r') as f:
        jjtext=f.read()
    text_model = markovify.NewlineText(jjtext, state_size=random.randint(1,2))
    result = text_model.make_sentence()
    while result is None:
        result = text_model.make_sentence()
    return result.capitalize()
def anek(par=2, num=5):
    if par>4:
        return "Слишком сильная связь, нужна цифра до 5"
    if num>50:
        return "Никаких лонгридов в мою смену(максимум 50 строк)"
    else:
        with open('/home/ubuntu/bot/data/anekdot.txt','r') as a:
            text = a.read()
        text_model=markovify.NewlineText(text,state_size=par)
        anek=''

        for i in range(num):
            result = text_model.make_sentence()
            while result is None or (i==0 and (result[0]=='-' or result[0].islower())):
                result = text_model.make_sentence()
            anek+=result+'\n'
        return anek

