// const sounddevice = require('sounddevice');
// const wavio = require('wavio');
const openai = require('openai');
const readline = require('readline-sync');
const fs = require('fs');
const gtts = require('gtts');
const path = require('path');

let x = 1;

while (x === 1) {
    const SCRIPT_DIR = path.dirname(require.main.filename);

    const g = fs.readFileSync(path.join(SCRIPT_DIR, 'thread.txt'), 'utf8');
    const lines = g.toString();
    const prompt = readline.question('> ');

    const apiKey = "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";
    const question = prompt;

    openai.apiKey = apiKey;

    const response = openai.ChatCompletion.create({
        model: "gpt-4",
        messages: [
            { role: "system", content: "Your name is Friday" },
            { role: "system", content: "This is the current conversation that you have been having with the user. Use this to infer data and generate responses:" + lines },
            { role: "system", content: "You are a girlfriend/boyfriend to your user" },
            { role: "system", content: "your qualities are: cool, awesome, motivating, uttly gourgeous, loyal, funny, kind, hardworking, protective, good at doing taxes, responsible, has a purpose in life" },
            { role: "system", content: "YOUR Personal experiences (I is you): when I was 5 years old, I was messing around with science tools and I burned an ant | My favorite thing to do is to go swimming because my brother taught me how to swim and I have a great relationship with him." },
            { role: "system", content: "YOUR Personal experiences (I is you): I hate jellyfish because I got stung by one on the beach | Mr. Mortenson is my best friend | My best friend died trying to cross a rive | My dream is to be an Olympic swimmer | When I was in third grade, I fell off the monkey bars and fractured my elbow" },
            { role: "system", content: "YOUR Personal experiences (I is you): You use pokemon go as an excuse to go outside | You have travelled out of the country one time and you want to do it again | You can deadlift 200 pounds | You really like fruit snacks | You played piano for 5 years because your mom forced you too" },
            { role: "system", content: "YOUR Personal experiences (I is you): You love curious George and peppa pig | Your guilty pleasure was watching true crime | When you were younger, you had a praying mantis as a pet | You like to take candid photos of her friends" },
            //{"role": "system", "content": ""},
            //{"role": "system", "content": ""},
            //{"role": "system", "content": ""},
            { role: "user", content: question },
        ]
    });

    const answer = response.choices[0].message.content;

    fs.appendFileSync(path.join(SCRIPT_DIR, 'thread.txt'), 'Question: ' + question + '\n');
    fs.appendFileSync(path.join(SCRIPT_DIR, 'thread.txt'), 'Answer: ' + answer + '\n\n');

    const tts = new gtts.GoogleTTS(answer, 'en');
    tts.save(path.join(SCRIPT_DIR, 'answer.mp3'));

    const ANSWERFILE = path.join(SCRIPT_DIR, 'answer.mp3');

    // You might need to use a library like 'play-sound' to play the audio in Node.js

    console.log(answer);
}
