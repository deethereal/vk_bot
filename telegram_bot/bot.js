const fs = require('fs');
const TgBot = require('node-telegram-bot-api');
let token = '';

let start = new Promise((resolve, reject) => {
    fs.readFile(__dirname + '\\token.txt', 'utf8', (err, data) => {
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

            bot.on('message', (msg) => {
                if(msg.forward_from_chat === undefined){
                    console.log(msg.text);
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