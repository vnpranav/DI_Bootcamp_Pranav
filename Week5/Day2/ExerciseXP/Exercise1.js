let h1 = document.getElementsByTagName('h1')[0]
console.log(h1)

let article = document.getElementsByTagName('article')[0]
article.lastElementChild.remove()

let h2 = document.querySelector('h2')
h2.addEventListener(
   'click', function(){
      h2.style.backgroundColor = 'red';
   }
)

let h3 = document.querySelector('h3')
h3.onclick = function(){
   h3.style.display = 'none'
}

let btn = document.createElement('button')
btn.textContent = 'Click me to make all elements bold'
btn.onclick = function(){
   // make all paragraphs bold
   let paragraphs = document.getElementsByTagName('p')
   for(let i = 0; i < paragraphs.length; i++){
      paragraphs[i].style.fontWeight = 'bold'
   }
}

document.body.appendChild(btn)

h1.onmouseover = function(){
   let size = Math.random() * 101
   h1.style.fontSize = `${size}px`
}

let paragraph2 = document.querySelectorAll('p')[1]
paragraph2.onmouseover = function(){
   paragraph2.style.opacity = 0
   // make it fade in
   paragraph2.style.transform = 'fade'
   paragraph2.style.transition = 'fade 1s'
}