function hotelCost(nights) {
    do {
        if ((isNaN(nights) === false) && (nights != 0) && (typeof(nights) == "number")) {
            break;
        } else {
            nights = Number(prompt("Enter number of nights correctly: "));
        }
    } while (true)
    return 140 * nights;
}

function planeRideCost(destination) {
    do {
        if ((destination != "") && (destination != undefined) && (typeof(destination) == "string")){
            break
        } else {
            destination = prompt("Enter travel destination correctly: ")
        }
    } while (true)
    
    switch (destination.toLowerCase()) {
        case "london":
            return 183;
            break;
        case "paris":
            return 220;
            break;
        default:
            return 300;
    }
}

function rentalCarCost(days) {
    do {
        if ((isNaN(days) === false) && (days != 0) && (typeof(days) == "number")) {
            break;
        } else {
            days = Number(prompt("Enter number of days correctly: "));
        }
    } while (true)
    
    if (days > 10) {
        return 0.95 * 40 * days;
    }
    
    return days * 40;
}

function totalVacationCost() {
    let travelDetails = String(prompt("Enter number of nights, travel destination and number of days to rent a car,  all followed by commas: ")).replaceAll(" ", "").split(",");
    console.log(travelDetails);
    
    let sum = 0;
    let hotel = hotelCost(Number(travelDetails[0]));
    let plane = planeRideCost(travelDetails[1]);
    let car = rentalCarCost(Number(travelDetails[2]));
    sum = hotel + plane + car
    
    console.log("Hotel cost:$", hotel);
    console.log("Plane cost:$", plane),
    console.log("Car cost:$", car);
    console.log("Total cost:$", sum);
}

totalVacationCost();
