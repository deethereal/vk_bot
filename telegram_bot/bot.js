const fs = require('fs');
const TgBot = require('node-telegram-bot-api');
let token = '';

let start = new Promise((resolve, reject) => {
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
                //if нужен, чтобы не обрабатывать пересылаемые сообщения
                if(msg.forward_from_chat === undefined && commands.indexOf(msg.text) == -1){
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