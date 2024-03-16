// Using Javascript:

//     Retrieve the div and console.log it
var container = document.getElementById("container");
console.log(container.innerText);

//     Change the name “Pete” to “Richard”.
var list1 = document.getElementsByClassName("list")[0];
list1.children[1].innerText = "Richard";

//     Delete the <li> that contains the text node “Sarah”. (It’s the second <li> of the second <ul>)
var list2 = document.getElementsByClassName("list")[1];
list2.removeChild(list2.children[1]);

//     Change each first name of the two <ul>'s to your name. (Hint : use a loop)


// Bonus - Using Javascript:

//     Add a class called student_list to both of the <ul>'s.

//     Add the classes university and attendance to the first <ul>.


