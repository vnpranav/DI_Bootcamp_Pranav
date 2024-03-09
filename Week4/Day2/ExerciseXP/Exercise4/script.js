const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

const shoppingList = [
    "banana",
    "orange",
    "apple"
    ]
    
function myBill() {
    let bill = 0;
    for (let item of shoppingList) {
        if (Object.keys(stock).includes(item)){
            if (stock[item] != 0) {
                stock[item] = stock[item] - 1;
                bill = bill + prices[item];
            }
            // if (stock[item] == 0) {
                // how to remove pair
            // }
        }
    }
    return bill;
}
console.log(myBill())