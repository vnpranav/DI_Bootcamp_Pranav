let planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
let colors = ["grey","lightyellow","lightblue","red","orange","lightcoral","cornflowerblue","royalblue","purple"]
let moons = [0,0,1,2,95,146,27,14,0]
let section = document.body.querySelector("section");

for (let planet in planets)
{
    let div = document.createElement("div");
    div.innerText = planets[planet];
    div.classList.add("planet", planets[planet]);
    div.style.color = "black";
    div.style.backgroundColor = colors[planet];
    div.style.margin = "10px";

    let moon = document.createElement("div");
    moon.classList.add("moon")
    moon.innerText = moons[planet];
    moon.style.fontSize = "smaller";
    
    div.appendChild(moon);
    section.appendChild(div);
}