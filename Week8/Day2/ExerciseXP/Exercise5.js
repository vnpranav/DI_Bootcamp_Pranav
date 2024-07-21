function makeJuice(size){
   function addIngredients(ingredient1, ingredient2, ingredient3){
      const sentence = `the clients wants a ${size} ${ingredient1} juice with ${ingredient2} and ${ingredient3}`
      alert(sentence)
   }
   addIngredients("apple", 'orange', 'kiwi')
}
makeJuice('XL')

function makeJuice2(size){
   const ingredients = [];
   function addIngredients(ingredient1, ingredient2, ingredient3){
      ingredients.push(ingredient1, ingredient2, ingredient3)
    }
   function displayJuice(){
      alert(`the clients wants a ${size} ${ingredients.join(",")}`)
   }
   addIngredients("apple", 'orange', 'kiwi')
   addIngredients('mango','passionfruit','letchi')
   displayJuice()
}
makeJuice2('XL')