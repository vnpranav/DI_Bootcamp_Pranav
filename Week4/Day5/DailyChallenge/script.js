bottles = Number(prompt("Enter number of bottles to start with:"))

let count = 0;

while (bottles > 0) {
    let grammar = "bottle";
    if (bottles > 1){
        grammar = grammar + "s" 
    }
    count = count + 1  
    console.log(`${bottles} ${grammar} of beer on the wall`)
    console.log(`${bottles} ${grammar} of beer`)
    
    if (count == 1) {
        console.log(`Take ${count} down , pass it around`)
    } else {
        console.log(`Take ${count} down , pass them around`)
    }
    bottles = bottles - 1
        
}
console.log("no bottle of beer on the wall :(")
