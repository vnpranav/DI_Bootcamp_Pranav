// -----1------
const fruits = ["apple", "orange"];
const vegetables = ["carrot", "potato"];

const result = ['bread', ...vegetables, 'chicken', ...fruits];
// [bread carrot potato chicekn apple orange]
console.log(result);

// ------2------
const country = "USA";
console.log([...country]);
// u s a

// ------Bonus------
let newArray = [...[,,]];
console.log(newArray);
// undefined undefined