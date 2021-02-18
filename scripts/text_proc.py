import re
my_ponct='!#&*,;\^_`{}'
with open ('/Users/denis/Documents/vk_bot/data/a.txt', 'r') as f:
    text=f.read()
sentences = text.split('\n')
print(len(sentences))
print(sentences[-5:-1])
new_sentences = []
parasites = ["сука", "блин", '((((', '))))', '))0)']
for el in sentences:
    el = re.sub('[%s]' % re.escape(my_ponct), '', el).replace('🌚', ' 🌚')
    if len(el)>3 and el not in parasites:
        if el[-1]=='?':
            new_sentences.append(el.replace('?', ' ?.'))
        else:
            new_sentences.append(el+". ")
print(len(new_sentences))
print((new_sentences[0:30]))
with open ('/Users/denis/Documents/vk_bot/data/old_chat.txt','a') as nf:
    for el in new_sentences:
        nf.write(el)