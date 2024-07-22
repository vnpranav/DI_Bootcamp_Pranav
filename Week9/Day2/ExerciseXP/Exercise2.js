function displayStudentInfo(objUser){
   const {first, last} = objUser
   console.log(`${first} ${last}`)
}

displayStudentInfo({first: 'Elie', last:'Schoppik'});