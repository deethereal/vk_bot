import markovify
def learn(par):
    if par  in (1,2):
        with open ("data/chat.txt","r") as ch:
            text=ch.read()
        text_model = markovify.Text(text, state_size=par)
        result=text_model.make_sentence()
        while result is None:
            result = text_model.make_sentence()
        return result.capitalize()
    else:
        return 'Доступные параметры: "1" или "2"'
