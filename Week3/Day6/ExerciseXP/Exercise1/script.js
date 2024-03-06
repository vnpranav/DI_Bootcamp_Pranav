const people = ["Greg", "Mary", "Devon", "James"];
// Part 1
people.shift();

people[people.indexOf("James")] = "Jason";

people.push("Pranav");

console.log(people);
console.log(`Index of Mary: ${people.indexOf("Mary")}`);

var peopleCopy = people.slice(1,4);

console.log(`Index of Foo: ${people.indexOf("Foo")}`);
// foo does not exist

var last = people.at(-1);
// console.log(last);
console.log("****************************");

// Part 2
for (let person of people) {
    console.log(person);
}
console.log("----------------------------");
for (let person of people){
    console.log(person);
    if (person == "Devon") {
        break;
    }
}