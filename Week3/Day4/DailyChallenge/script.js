var sentence = 'This dinner is not that bad ! You cook well';
var wordNot = sentence.indexOf("not");
var wordBad = sentence.indexOf("bad");
// console.log(wordNot);
// console.log(wordBad);
 if (wordBad > wordNot) {
     console.log("aila");
     var removed = sentence.slice(wordNot, wordBad + 3);
     console.log(sentence.replace(removed, "good"));
 } else{
     console.log(sentence);
 }