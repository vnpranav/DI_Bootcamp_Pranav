const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];
// reduce into a single string
const epicString = epic.reduce((acc, curr) => acc + ' ' + curr);
console.log(epicString)