import markovify
import time
import zipfile
import os

lin_way='/home/ubuntu/bot/vk_bot/data/'
mac_way='/Users/denis/Documents/vk_bot/data/'
T_lin_way='/home/ubuntu/test_bot/vk_bot/data/'
def create_model():
    start = time.time_ns()
    with open(T_lin_way+'chat.txt', "r") as ch:
        text = ch.read()
    with open(T_lin_way+'text_model_1.json', "w") as f:
        f.write(markovify.Text(text, state_size=1).to_json())
    with zipfile.ZipFile(T_lin_way+'z1.zip', 'w') as z1:
        z1.write(T_lin_way+'text_model_1.json',arcname='text_model_1.json',compress_type=zipfile.ZIP_DEFLATED)
    os.remove(T_lin_way+'text_model_1.json')
    with open(T_lin_way+'/text_model_2.json', "w") as f:
        f.write(markovify.Text(text, state_size=2).to_json())
    with zipfile.ZipFile(T_lin_way + 'z2.zip', 'w') as z2:
        z2.write(T_lin_way+'text_model_2.json', arcname='text_model_2.json',compress_type=zipfile.ZIP_DEFLATED)
    os.remove(T_lin_way+'text_model_2.json')
    with open(T_lin_way+'log.txt', "w") as f:
        f.write(time.asctime())
    end=time.time_ns()
    return f"Модель создана за {(end-start)//10 ** 9} с"
def use_model(par='2'):
    with zipfile.ZipFile(T_lin_way+'z'+par+'.zip','r') as oz:
        oz.extractall()
    with open('text_model_'+par+'.json', "r") as f:
        text_model= markovify.Text.from_json(f.read())
    result = text_model.make_sentence(max_overlap_ratio=0.5)
    while result is None:
        result = text_model.make_sentence(max_overlap_ratio=0.5)
    os.remove('text_model_'+par+'.json')
    return result.capitalize().replace(' ?.','? ')
def long_sent(par,leng):
    if leng>10:
        with open(lin_way+str(par)+'.txt', "r") as f:
            text_model = markovify.Text.from_json(f.read())
        result = text_model.make_short_sentence(min_chars=leng,max_chars=5*leng,max_overlap_ratio=0.5)
        for i in range(50):
            if result is not None:
                return result.capitalize().replace(' ?.','? ').replace(".?","? ")
            else:
                result = text_model.make_short_sentence(min_chars=leng,max_chars=5*leng,max_overlap_ratio=0.5)
        return "Мне не удалось сгенерировать предложение длины:" +str(leng)
    return "Укажите большую длину"
def sent_s(par,word,st=False):
    with open(lin_way + str(par) + '.txt', "r") as f:
        text_model = markovify.Text.from_json(f.read())
    if st:
        try:
            result = text_model.make_sentence_with_start(word,strict=st,max_overlap_ratio=0.5)
            while result is None:
                result = text_model.make_sentence_with_start(word,strict=st,max_overlap_ratio=0.5)
            return result.capitalize().replace(' ?.','? ').replace(".?","? ")
        except KeyError:
            return f"Слова {word} нет в тексте, задайте другое"
        except markovify.text.ParamError:
            return f"Слово {word} нет является началом ни в одном предложении, задайте другое. Либо я долбоеб и не смог построить предложение минимальной длины."
    else:
        try:
            result = text_model.make_sentence_with_start(word, strict=st, max_overlap_ratio=0.5)
            while result is None:
                result = text_model.make_sentence_with_start(word, strict=st, max_overlap_ratio=0.5)
            return result.capitalize().replace(' ?.', '? ').replace(".?","? ")
        except KeyError:
            return f"Слова {word} нет в тексте, задайте другое"
        except markovify.text.ParamError:
            result = text_model.make_sentence_with_start(word, strict=st, max_overlap_ratio=0.5)
            for _ in range(50):
                if result is not None:
                    return result.capitalize().replace(' ?.', '? ').replace(".?","? ")
                else:
                    result = text_model.make_sentence_with_start(word, strict=st, max_overlap_ratio=0.5)
            return f"Слово {word} нет является началом ни в одном предложении, задайте другое. Либо я долбоеб и не смог построить предложение минимальной длины."
def simulate(par,id):
    with open(lin_way+str(id)+'.txt','r') as f:
        text=f.read()
    text_model=markovify.Text(text, state_size=par)
    result = text_model.make_sentence()
    while result is None:
            result = text_model.make_sentence()
    return result.capitalize().replace(' ?.', '? ').replace(".?","? ")
def anek(par=2, num=5):
    if par>4:
        return "Слишком сильная связь, нужна цифра до 5"
    else:
        with open('/home/ubuntu/bot/vk_bot/data/anekdot.txt','r') as a:
            text = a.read()
        text_model=markovify.NewlineText(text,state_size=par)
        anek=''

        for i in range(num):
            result = text_model.make_sentence()
            while result is None or (i==0 and (result[0]=='-' or result[0].islower())):
                result = text_model.make_sentence()
            anek+=result+'\n'
        return anek