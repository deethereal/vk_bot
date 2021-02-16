import markovify
way='/home/ubuntu/bot/vk_bot/data/chat.txt'
def learn(par):
    if par  in (1,2):
        with open (way,"r") as ch:
            text=ch.read()
        text_model = markovify.Text(text, state_size=par)
        result=text_model.make_sentence(max_overlap_ratio=0.5)
        while result is None:
            result = text_model.make_sentence(max_overlap_ratio=0.5)
        return result.capitalize()
    else:
        return 'Доступные параметры: "1" или "2"'
def long_sent(par,leng):
    if leng>10:
        with open(way, "r") as ch:
            text = ch.read()
        text_model = markovify.Text(text, state_size=par)
        result = text_model.make_short_sentence(min_chars=leng,max_chars=5*leng,max_overlap_ratio=0.5)
        for i in range(30):
            if result is not None:
                return result.capitalize()
            else:
                result = text_model.make_short_sentence(min_chars=leng,max_chars=5*leng,max_overlap_ratio=0.5)
        return "Мне не удалось сгенерировать предложение длины:" +str(leng)
    return "Укажите большую длину"
def sent_s(par,word,st=False):
    with open(way, "r") as ch:
        text = ch.read()
    text_model = markovify.Text(text, state_size=par)
    try:
        result = text_model.make_sentence_with_start(word,strict=st,max_overlap_ratio=0.5)
        while result is None:
            result = text_model.make_sentence_with_start(word,strict=st,max_overlap_ratio=0.5)
        return result.capitalize()
    except KeyError:
        return f"Слова {word} нет в тексте, задайте другое"
    except markovify.text.ParamError:
        if st:
            return f"Слово {word} нет является началом ни в одном предложении, задайте другое. Либо я долбоеб и не смог построить предложение минимальной длины."
        else:
            return f"Извините, я долбоеб и не смог построить предложение минимальной длины."
def simulate(par,id):
    with open('/home/ubuntu/bot/vk_bot/data/'+str(id)+'.txt','r') as f:
        text=f.read()
    text_model=markovify.Text(text, state_size=par)
    result = text_model.make_sentence()
    while result is None:
            result = text_model.make_sentence()
    return result.capitalize()