const morse = `{
   "0": "-----",
   "1": ".----",
   "2": "..---",
   "3": "...--",
   "4": "....-",
   "5": ".....",
   "6": "-....",
   "7": "--...",
   "8": "---..",
   "9": "----.",
   "a": ".-",
   "b": "-...",
   "c": "-.-.",
   "d": "-..",
   "e": ".",
   "f": "..-.",
   "g": "--.",
   "h": "....",
   "i": "..",
   "j": ".---",
   "k": "-.-",
   "l": ".-..",
   "m": "--",
   "n": "-.",
   "o": "---",
   "p": ".--.",
   "q": "--.-",
   "r": ".-.",
   "s": "...",
   "t": "-",
   "u": "..-",
   "v": "...-",
   "w": ".--",
   "x": "-..-",
   "y": "-.--",
   "z": "--..",
   ".": ".-.-.-",
   ",": "--..--",
   "?": "..--..",
   "!": "-.-.--",
   "-": "-....-",
   "/": "-..-.",
   "@": ".--.-.",
   "(": "-.--.",
   ")": "-.--.-"
 }`;

 function toJs(morseString) {
   return new Promise((resolve, reject) => {
       const morseJS = JSON.parse(morseString);
       if (Object.keys(morseJS).length === 0) {
           reject("The Morse JavaScript object is empty.");
       } else {
           resolve(morseJS);
       }
   });
}

function toMorse(morseJS) {
   return new Promise((resolve, reject) => {
       const userInput = prompt("Enter a word or sentence:").toLowerCase();
       const morseTranslation = [];

       for (let char of userInput) {
           if (morseJS[char]) {
               morseTranslation.push(morseJS[char]);
           } else if (char === " ") {
               morseTranslation.push("");  // Using empty string for spaces between words
           } else {
               reject(`Character "${char}" doesn't exist in the Morse JavaScript object.`);
               return;
           }
       }

       resolve(morseTranslation);
   });
}

function joinWords(morseTranslation) {
   const morseString = morseTranslation.join('\n');
   document.body.innerHTML = `<pre>${morseString}</pre>`;
}

toJs(morseString)
    .then(morseJS => toMorse(morseJS))
    .then(morseTranslation => joinWords(morseTranslation))
    .catch(error => console.log(error));