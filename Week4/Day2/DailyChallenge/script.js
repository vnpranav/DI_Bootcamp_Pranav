// Online Javascript Editor for free
// Write, Edit and Run your Javascript code using JS Online Compiler

// Online Javascript Editor for free
// Write, Edit and Run your Javascript code using JS Online Compiler

function rectangle(words) {
    let wordList = words.replaceAll(" ", "").split(",");
    let maxWord = wordList.reduce(function (a,b) {
        return a.length > b.length ? a : b;
    }).length;
    
    let line = "*".repeat(maxWord + 4);
    console.log(line)
    for (let word of wordList) {
        line = word
        line = line.padEnd(maxWord, " ");
        line = "* " + line + " *"
        console.log(line)
    }
    line = "*".repeat(maxWord+4)
    console.log(line)
}

let words = prompt("Enter a series of words, seperated by commas: ");
rectangle(words);