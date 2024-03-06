console.log("you will be asked to keep entering numbers until you enter a number greater than 10");


do {
    var isnum = false;
    var num;
    do {
        num = prompt("Enter a number: ");
        if ((isNaN(num) === false) && (typeof(num) != undefined) && (typeof(num) != null) && (num != "")){
            isnum = true;
            // does not detect blanks?
        } 
        else {
            console.log("Not a number");
        }
    } while (isnum === false);
    
    if (num < 10){
        console.log("number is less than 10")
    } else {
        break;
    }
} while (true);