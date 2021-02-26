import markovify
import time
import zipfile
import os

lin_way='/home/ubuntu/bot/vk_bot/data/'
mac_way='/Users/denis/Documents/vk_bot/data/'
T_lin_way='/home/ubuntu/test_bot/vk_bot/data/'
def use_model(par='2'):
    st=time.time_ns()
    with zipfile.ZipFile(mac_way+'z'+par+'.zip','r') as oz:
        oz.extractall()
    combined_model = None
    for i in range(1,4):
        with open ('/Users/denis/Documents/vk_bot/scripts/text_model_'+par+str(i)+'.json') as f:
            model = markovify.Text.from_json(f.read())
        if combined_model:
            combined_model = markovify.combine(models=[combined_model, model])
        else:
            combined_model = model
        print("прошло " + str((time.time_ns() - st) // 10 ** 6)+" мс")
    with open(mac_way + 'chat.txt') as f:
        model = markovify.Text(f, state_size=int(par),retain_original=False)
    combined_model = markovify.combine(models=[combined_model, model])
    print("прошло "+str((time.time_ns() - st) // 10 ** 6)+" мс")
    result = combined_model.make_sentence()
    if result is not None:
        return result.capitalize().replace(' ?.', '? ').replace(".?", "? ") + " "+ str((time.time_ns() - st) // 10 ** 6)
    for _ in range(150):
        if result is not None:
            return result.capitalize().replace(' ?.', '? ').replace(".?", "? ")+ " "+str((time.time_ns() - st) // 10 ** 6)
        else:
            result = combined_model.make_sentence()
    return "мне не хватило 150 итераци, давай еще"
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
print("C параметром одын:")
print(use_model('1'))
print("C параметром два:")
print(use_model())