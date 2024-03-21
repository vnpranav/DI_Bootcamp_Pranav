
// Using Javascript, in the <div>, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.
let div = document.getElementById("navBar");
div.setAttribute("id", "socialNetworkNavigation");

// We are going to add a new <li> to the <ul>.
//     First, create a new <li> tag (use the createElement method).
let newListElement = document.createElement("li");
//     Create a new text node with “Logout” as its specified text.
let text = document.createTextNode("Logout");
//     Append the text node to the newly created list node (<li>).
newListElement.appendChild(text);
//     Finally, append this updated list node to the unordered list (<ul>), using the appendChild method.
document.body.querySelector("ul").appendChild(newListElement);
// Use the firstElementChild and the lastElementChild properties to retrieve the first and last <li> elements from their parent element (<ul>). Display the text of each link. (Hint: use the textContent property).
let first = document.body.querySelector("ul").firstElementChild;
let last = document.body.querySelector("ul").lastElementChild;

alert(`${first.textContent} & ${last.textContent}`);