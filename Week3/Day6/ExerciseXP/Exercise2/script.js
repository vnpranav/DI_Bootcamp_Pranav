var colors = ["red", "blue", "yellow", "green", "purple"];

for (let col = 0; col < 5; col++){
    console.log(`my #${col+1} choice is ${colors[col]}`);
}

// bonus
console.log("------------------------");
var rankings = ["1st", "2nd", "3rd", "4th", "5th"];
for (let col = 0; col < 5; col++){
    console.log(`my ${rankings[col]} choice is ${colors[col]}`);
}