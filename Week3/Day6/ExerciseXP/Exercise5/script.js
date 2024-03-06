const family = {
    members : 4,
    surname : "Nenooth",
    religion : "Hindu",
    address : "Rose Belle",
    mauritian : true
};

console.log("Keys for object");
for (let key of Object.keys(family)) {
    console.log(key);
}
console.log("--------------------");
console.log("Values for object");
for (let value in Object.values(family)) {
    console.log(Object.values(family)[value]);
}