function isAnagram(word1 , word2){
   word1 = word1.toLowerCase().replaceAll(" ", "")
   word2 = word2.toLowerCase().replaceAll(" ", "")

   if (word1.length !== word2.length){
      return false
   }
   if (word1.split("").sort().join("") == word2.split("").sort().join("")){
      return true
   }
   return false
}
console.log(isAnagram("Astronomer", "Moon starer"))