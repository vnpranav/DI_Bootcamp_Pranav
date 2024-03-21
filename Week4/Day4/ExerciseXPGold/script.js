let table = document.body.querySelector("table");

let rows = table.rows.length;

for (let row = 0; row < rows; row++) {
    let diagonal = table.querySelectorAll("tr")[row].children[row];
    diagonal.setAttribute("style", "color:red");
}

