const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}
console.log("Number of floors in the building: ", building.numberOfFloors);
console.log("----------------------------------------------------");
console.log("Number of aparatments on Floor 1: ", building.numberOfAptByFloor.firstFloor);
console.log("Number of aparatments on Floor 3: ", building.numberOfAptByFloor.thirdFloor);
console.log("----------------------------------------------------");
console.log(`Second tenant ${building.nameOfTenants[1]} has ${building.numberOfRoomsAndRent.dan[0]} rooms`);
console.log("----------------------------------------------------");
if ((building.numberOfRoomsAndRent.david[1] + building.numberOfRoomsAndRent.sarah[1]) >building.numberOfRoomsAndRent.dan[1]) {
    console.log("Dan's rent was increased");
    building.numberOfRoomsAndRent.dan[1] = 1200;
}