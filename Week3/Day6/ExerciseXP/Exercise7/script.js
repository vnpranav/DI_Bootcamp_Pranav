const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
var secret = [];
for (let name of names){
    secret.push(name.at(0));
}
console.log(secret.sort().join(""));