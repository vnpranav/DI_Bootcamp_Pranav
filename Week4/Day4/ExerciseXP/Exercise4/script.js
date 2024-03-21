// In the body of the HTML page, create an empty div:
// <div class="listBooks"></div>
let div = document.createElement("div");
div.className = "listBooks";
// In the js file, create an array called allBooks. This is an array of objects. Each object is a book that has 4 keys (ie. 4 properties) :
//     title,
//     author,
//     image : a url,
//     alreadyRead : which is a boolean (true or false).
let book1 = {
    title : "Harry Potter & the Philosopher's Stone",
    author : "JK Rowling",
    image : "https://images.pexels.com/photos/4132936/pexels-photo-4132936.png?auto=compress&cs=tinysrgb&w=600",
    alreadyRead : false
};

let book2 = {
    title : "The Adventures of Wonder Boy",
    author : "John Doe",
    image : "https://images.pexels.com/photos/922100/pexels-photo-922100.png?auto=compress&cs=tinysrgb&w=600",
    alreadyRead : true
};

// Initiate the array with 2 books of your choice (ie. Add manually 2 books objects in the array)
let Books = [book1, book2];

// Requirements : All the instructions below need to be coded in the js file:
//     Using the DOM, render the books inside an HTML table (the HTML table must be added to the <div> created in part 1).
let table = document.createElement("table")
let tableHead = document.createElement("thead");

let h1 = document.createElement("th");
h1.innerText = "Title";
let h2 = document.createElement("th");
h2.innerText = "Author";
let h3 = document.createElement("th");
h3.innerText = "Image";

tableHead.appendChild(h1);
tableHead.appendChild(h2);
tableHead.appendChild(h3);

table.appendChild(tableHead);


//     For each book :
//         You have to display the book’s title and the book’s author.


for (let book of Books) {
    let title = document.createElement("td");
    let pic = document.createElement("img");
    let author = document.createElement("td");
    let picture = document.createElement("td");
    let tableRow = document.createElement("tr");
//         Example: HarryPotter written by JKRolling.
    title.innerText = book.title;
    author.innerText = book.author;

    pic.src = book.image;
    pic.setAttribute("width", "100px");
    picture.appendChild(pic);

    if (book.alreadyRead == true) {
        title.style.color = "red";
    }
    tableRow.appendChild(title);
    tableRow.appendChild(author);
    tableRow.appendChild(picture)
    table.appendChild(tableRow)
}

div.appendChild(table)
//         The width of the image has to be set to 100px.
//         If the book is already read. Set the color of the book’s details to red.
document.body.appendChild(div);