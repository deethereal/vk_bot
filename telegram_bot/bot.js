const fs = require('fs');
const TgBot = require('node-telegram-bot-api');
let token = '';

function OK (msg){
    // массив проблемных мест
    let array = ["forward_from_chat", "sticker", "photo"];
    for (let i = 0; i < array.length; ++i){
        if(msg[array[i]] !== undefined){
            return false;
        }
    }
    return true;
}

let start = new Promise((resolve, reject) => {
    //изменять слеш, если работает бот на винде
    fs.readFile(__dirname + '/token.txt', 'utf8', (err, data) => {
        if (err) {
            reject(err);
        }
        resolve(data);
    })
})


start
    .then(
        starting_proc => {
            token = starting_proc;

            const bot = new TgBot(token,{
                polling: true
            })

            //тут вводить список команд, которые используются ботом
            const commands = ["/check"];

            bot.onText(/\/check/, (msg) => {
                const {id} = msg.chat;
                bot.sendMessage(id, "Im работать");
            })

            bot.on('message', (msg) => {
                // console.log(msg);
                //if нужен, чтобы не обрабатывать пересылаемые сообщения
                let haveComands = commands.indexOf(msg.text) == -1;
                if(OK(msg) && haveComands){
                    let result = '';
                    if(msg.text.split(" ").length > 1){
                        let url = msg.text.match(/\bhttp.+\b/);
                        let tmp = msg.text.toLowerCase();
                        tmp = tmp.replace(/[!#&\*,;\\^_`{}]/g," ");
                        tmp = tmp.replace(/\bhttp.+\b/,url);
                        tmp = tmp.replace(/\s+/g," ");
                        (tmp[tmp.length - 1] != ".") ? result += tmp + "." : result += tmp;
                        console.log(result);
                        fs.appendFileSync(__dirname + '/words.txt', `\n${result}`)
                    }
                }

                if(msg.photo !== undefined && haveComands){
                    let result = '';
                    if(msg.caption.split(" ").length > 1){
                        let url = msg.caption.match(/\bhttp.+\b/);
                        let tmp = msg.caption.toLowerCase();
                        tmp = tmp.replace(/[!#&\*,;\\^_`{}]/g," ");
                        tmp = tmp.replace(/\bhttp.+\b/,url);
                        tmp = tmp.replace(/\s+/g," ");
                        (tmp[tmp.length - 1] != ".") ? result += tmp + "." : result += tmp;
                        console.log(result);
                        fs.appendFileSync(__dirname + '/words.txt', `\n${result}`)
                    }
                }
            })

//--------------end----------------
        },

        //если что-то пошло не так с токеном.
        error => {
            console.log("Cannot find token. Please check your path to token.\n" +
                "Now your dirname is " + __dirname + "\n\n");
            throw error;
        }
    )