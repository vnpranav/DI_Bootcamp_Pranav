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
for (let i = 0; i <=1 ; i++) {
    document.querySelectorAll(".list")[i].children[0].innerText = "Pranav";
}

// Bonus - Using Javascript:

//     Add a class called student_list to both of the <ul>'s.
list1.classList.add("student");
list2.classList.add("student");

//     Add the classes university and attendance to the first <ul>.
list1.classList.add("university", "attendance");

