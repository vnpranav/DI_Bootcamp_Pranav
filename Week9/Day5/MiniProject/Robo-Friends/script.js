const robots = [
    {
      id: 1,
      name: 'Leanne Graham',
      username: 'Bret',
      email: 'Sincere@april.biz',
      image: 'https://robohash.org/1?200x200'
    },
    {
      id: 2,
      name: 'Ervin Howell',
      username: 'Antonette',
      email: 'Shanna@melissa.tv',
      image: 'https://robohash.org/2?200x200'
    },
    {
      id: 3,
      name: 'Clementine Bauch',
      username: 'Samantha',
      email: 'Nathan@yesenia.net',
      image: 'https://robohash.org/3?200x200'
    },
    {
      id: 4,
      name: 'Patricia Lebsack',
      username: 'Karianne',
      email: 'Julianne.OConner@kory.org',
      image: 'https://robohash.org/4?200x200'
    },
    {
      id: 5,
      name: 'Chelsey Dietrich',
      username: 'Kamren',
      email: 'Lucio_Hettinger@annie.ca',
      image: 'https://robohash.org/5?200x200'
    },
    {
      id: 6,
      name: 'Mrs. Dennis Schulist',
      username: 'Leopoldo_Corkery',
      email: 'Karley_Dach@jasper.info',
      image: 'https://robohash.org/6?200x200'
    },
    {
      id: 7,
      name: 'Kurtis Weissnat',
      username: 'Elwyn.Skiles',
      email: 'Telly.Hoeger@billy.biz',
      image: 'https://robohash.org/7?200x200'
    },
    {
      id: 8,
      name: 'Nicholas Runolfsdottir V',
      username: 'Maxime_Nienow',
      email: 'Sherwood@rosamond.me',
      image: 'https://robohash.org/8?200x200'
    },
    {
      id: 9,
      name: 'Glenna Reichert',
      username: 'Delphine',
      email: 'Chaim_McDermott@dana.io',
      image:'https://robohash.org/9?200x200'
    },
    {
      id: 10,
      name: 'Clementina DuBuque',
      username: 'Moriah.Stanton',
      email: 'Rey.Padberg@karina.biz',
      image:'https://robohash.org/10?200x200'
    }
    ];

    function addRobots() {
        for (let robot of robots ) {
            let newCard = document.createElement("div");
            let imgContainer = document.createElement("div");
            let newImg = document.createElement("img")
            let lineBreak = document.createElement("br");
            let robotName = document.createElement("h3");
            let robotEmail = document.createElement("div");

            newCard.className = "card";
            imgContainer.className = "imageContainer";
            newImg.className = "robotImage";
            robotName.className = "robotName";
            robotEmail.className = "robotEmail";

            newImg.src = robot.image;
            robotName.innerText = robot.name;
            robotEmail.innerText = robot.email;

            imgContainer.appendChild(newImg)

            newCard.appendChild(imgContainer);
            newCard.appendChild(lineBreak);
            newCard.appendChild(robotName);
            newCard.appendChild(robotEmail);

            let cardSection = document.getElementById("cardSection");
            cardSection.appendChild(newCard)
        }
    }

addRobots()

function filterRobots(){
  let inputTag = document.getElementById("searchBar");
  let searchValue = inputTag.value;

  let cardSection = document.getElementById("cardSection");
  cardSection.innerHTML = "";

  for (let robot of robots ) {

    if (robot.name.toLowerCase().includes(searchValue)){
      let newCard = document.createElement("div");
      let imgContainer = document.createElement("div");
      let newImg = document.createElement("img")
      let lineBreak = document.createElement("br");
      let robotName = document.createElement("h3");
      let robotEmail = document.createElement("div");
  
      newCard.className = "card";
      imgContainer.className = "imageContainer";
      newImg.className = "robotImage";
      robotName.className = "robotName";
      robotEmail.className = "robotEmail";
  
      newImg.src = robot.image;
      robotName.innerText = robot.name;
      robotEmail.innerText = robot.email;
  
      imgContainer.appendChild(newImg)
  
      newCard.appendChild(imgContainer);
      newCard.appendChild(lineBreak);
      newCard.appendChild(robotName);
      newCard.appendChild(robotEmail);
  
      
      cardSection.appendChild(newCard)
    }
  }  

  if (searchValue == ""){
    addRobots()
  }
}