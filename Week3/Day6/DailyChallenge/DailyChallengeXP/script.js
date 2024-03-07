var lines = Number(prompt("Enter number of lines: " ));

// part 1
var stars = "";
for (let line = 0; line < lines; line++){
    stars = stars + "*" + " ";
    console.log(stars);
}

console.log("--------------------------------------------------------");

// part 2
for (let line = 0; line < lines; line++){
    let star = ""
    for(let l = 0; l < line + 1; l ++){
        star = star + "*" + " ";
    }
    console.log(star);
}