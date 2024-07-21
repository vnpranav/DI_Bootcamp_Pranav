let client = "John";

const groceries = {
    fruits : ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice : "20$",
    other : {
        paid : true,
        meansOfPayment : ["cash", "creditCard"]
    }
}
const displayGroceries = () => {
   groceries.fruits.forEach(fruit => console.log(fruit))
}

const cloneGroceries = () => {
   let user = client; // user is now a copy of client

   // Change client variable
   client = "Betty";
   console.log("client:", client); // Output: Betty
   console.log("user:", user); // Output: John

   let shopping = groceries;
   
   shopping.totalPrice = "35$";
   console.log("Modified totalPrice in shopping:", shopping.totalPrice); // Output: 35$

   // Change paid in other object within shopping
   shopping.other.paid = false;
   console.log("Modified paid in shopping:", shopping.other.paid); // Output: false

   console.log("groceries after modification:", groceries);
};

cloneGroceries();