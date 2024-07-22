// console.log([2] === [2])
// console.log({} === {})

const object1 = { number: 5 }; 
const object2 = object1; 
const object3 = object2; 
const object4 = { number: 5};

object1.number = 4;
console.log(object2.number)
console.log(object3.number)
console.log(object4.number)
// object 2 and 3 point to same object

class Animal{
   constructor(name, type, color){
      this.name = name;
      this.type = type;
      this.color = color;
   }
};

class Mammal extends Animal{
   sound(sound){
      return `${sound}\n I'm a ${this.type}, named ${this.name} and I'm ${this.color}\n`;
   }
};

let FarmerCow = new Mammal('Lily', 'cow', 'white')
console.log(FarmerCow.sound('Moo'))