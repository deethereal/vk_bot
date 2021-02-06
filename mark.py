import markovify
def learn(par):
    if par  in (1,2):
        with open ("chat.txt","r") as ch:
            text=ch.read()
        text_model = markovify.Text(text, state_size=par)
        return (text_model.make_sentence ()).capitalize()
    else:
        return 'Доступные параметры: "1" или "2"'
