const num1 = Number(prompt("enter first number: "));
const num2 = Number(prompt("enter second number: "));
const operator = prompt("select operator(+,-,*,/) : ");

switch(operator) {
    case "+":
        alert(num1 + num2);
        break;
    case "-":
        alert(num1 - num2);
        break;
    case "*":
        alert(num1 * num2);
        break;
    case "/":
        alert(num1/num2);
        break;
}