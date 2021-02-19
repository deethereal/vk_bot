const cheerio = require('cheerio');
const fs = require('fs');

let arrdata = '';
console.log(arrdata);
const begin_pars = 13000; // тут надо написать число, с которого надо парсить
const messages_to_pars = 22000; // сюда нужно написать число сколько сообщений в беседе
let data = 'lol';
const time = 1000; // время для setTimeout

for (let cur = begin_pars; cur < messages_to_pars; cur+=50) {
    fs.readFile(__dirname + '\\Archive\\messages\\2000000095\\mmessages'+cur+'.html', 'utf8', (err, data) => {
        if (err) throw err;
        let $ = cheerio.load(data);

        for (let i = 0; i < 50 || data !== undefined; i++) {

            data = $('.message')[i].childNodes[3].childNodes[0].nodeValue;

            if (data !== null && data !== undefined) {
                arrdata += data+'\n';
            }
        }

        console.log('step '+cur+' completed')
    });
}
console.log(arrdata);

setTimeout(() => fs.writeFile('a.txt', arrdata, function (err) {
    if (err) return console.log(err);
    console.log(arrdata + ' > a.txt');
}), time); // тут ебаный js пытается записать в файл когда захочет, поэтому надо ставить таймаут
                    // на время парсинга. После добавлю сюда asinc await для контролирования ассинхона.

