## До того, как начать работать
В первую очердь надо `conv.pu` и `begin.sh` засунуть в папку с сообщениями. То есть добавить в папку _messages_. 

Далее запустить скрипт `begin.sh` (лучше всего запускать на линуксе или маке).

Далее можно запускать из корня проекта `words.js`, но перед этим нужно поменять там значения переменных `time`, `begin` и `messages_to_pars`.
В комментариях все написано что за что отвечает. 

## Доработки, которые я буду делать в скрипте
* буду исправлять автоматическое асинхронное выполнение js.
* сделать более общий поиск с выяснением кто написал сообщение.