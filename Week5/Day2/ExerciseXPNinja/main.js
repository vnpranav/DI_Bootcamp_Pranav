function calculateTip(){
   let billAmount = document.getElementById('billAmt').value 
   let serviceQual = document.getElementById('serviceQual').value 
   let numOfPeople = document.getElementById('numofPeople').value

   if (serviceQual == 0 || billAmount == ""){
      alert("Please enter valid values")
      return 
   }
   if (numOfPeople <1 || numOfPeople == ""){
      numOfPeople = 1
      document.getElementById('each').style.display = 'none'
   } else {
      document.getElementById('each').style.display = 'inline'
   }

   let total = (billAmount * serviceQual) / numOfPeople
   total = total.toFixed(2)
   
   const totalTipElement = document.getElementById('totalTip')
   totalTipElement.style.display = 'block'
   document.getElementById('tip') = total 
}

document.getElementById('totalTip').style.display = 'none'
document.getElementById('calculate').onclick = function(){
   calculateTip
}