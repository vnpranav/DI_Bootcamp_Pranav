// Using Javascript:

//     Add a “light blue” background color and some padding to the <div>.
document.body.querySelector("div").style.backgroundColor = "lightblue";

//     Do not display the <li> that contains the text node “John”. (the first <li> of the <ul>)
let node = document.body.querySelector('ul').children[0];
node.style.display = "none"

//     Add a border to the <li> that contains the text node “Pete”. (the second <li> of the <ul>)
let node2 = document.body.querySelector("ul").children[1];
node2.setAttribute("style", "border: 5px dashed black");

//     Change the font size of the whole body.
document.body.style.fontSize = "larger";

// Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).
if(document.body.querySelector("div").style.getPropertyValue("background-color") == "lightblue")
{
    alert(`${node.innerHTML} & ${node2.innerHTML}`);
}
