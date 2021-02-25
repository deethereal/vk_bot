import re
my_ponct='!#&*,;\^_`{}'

for i in range(1,4):
    with open ('/Users/denis/Documents/vk_bot/data/part'+str(i)+'.txt', 'r') as f:
        text=f.read()
    sentences = text.split('\n')
    new_sentences = []
    parasites = ["сука", "блин", '((((', '))))', '))0)']
    for el in sentences:
        el = re.sub('[%s]' % re.escape(my_ponct), '', el)
        if len(el)>3 and el not in parasites:
            el=el.replace('🌚', ' 🌚')
            el=el.replace('😎', ' 😎')
            if el[-1]=='?':
                new_sentences.append((el.replace('?', ' ?. ')).lower())
            else:
                new_sentences.append((el+". ").lower())
    print(len(new_sentences))
    print((new_sentences[0:10]))
    with open ('/Users/denis/Documents/vk_bot/data/part'+str(i)+'.txt','w') as nf:
       for el in new_sentences:
        el.replace('🌚', ' 🌚')
        nf.write(el)