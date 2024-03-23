function insertRow() {
    let nextRow = document.getElementById("sampleTable");
    let rowCount = nextRow.childElementCount + 2;

    let newRow = document.createElement("tr");
    for (let i = 0; i < 2; i++) {
        let td = document.createElement("td");
        td.textContent = `Row${rowCount} Cell${i+1}`;
        newRow.appendChild(td);
    }

    document.getElementById("sampleTable").appendChild(newRow);
}