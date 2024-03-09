const prices = [0.25, 0.10, 0.05, 0.01];

function changeEnough(itemPrice, amountOfChange) {
    let sum = 0;
    for (let coin in amountOfChange){
        sum += amountOfChange[coin] * prices[coin];
    }
    
    if (sum >= itemPrice) {
        return true;
    }
    return false;
}

console.log(changeEnough(14.11, [2,100,0,0]));
console.log(changeEnough(0.75, [0,0,20,5]));