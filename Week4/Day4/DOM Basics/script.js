var count = 0;

function Change() {
    let text = document.getElementById("title");
    count = count + 1;
    text.innerText = `DOM Basics (See i just changed this) ${count} time(s)`;

    const footertxt = document.createElement("h2");
    footertxt.innerText = "YooHoo";
    
    if (count = 1){
        document.getElementById("footer").appendChild(footertxt);
    }
}