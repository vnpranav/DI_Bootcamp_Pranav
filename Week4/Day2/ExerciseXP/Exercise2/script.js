function calculateTip() {
    let bill = Number(prompt("Enter your bill: $"));
    let tip;
    switch (true) {
        case (bill < 50):
            tip = 1.2;
            break;
        case (bill < 200):
            tip = 1.15;
            break;
        default:
            tip = 1.1
    }
    console.log("tip amount: $", (tip-1)*bill)
    console.log("final bill: $", tip*bill)
}

calculateTip()
