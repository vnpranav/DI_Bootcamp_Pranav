const users = [{ firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
   { firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
   { firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
   { firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
   { firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
   { firstName: 'Wes', lastName: 'Reid', role: 'Instructor'},
   { firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor'}];

let welcome_users = users.map(person => {
   return {user : person.firstName,
      hello : `Hello ${person.firstName}`
    }
})
console.log(welcome_users)

let fullStackResidents = users.filter(user => user.role == 'Full Stack Resident')
console.log(fullStackResidents)
let fullStackResidentsLastName = users.filter(user => user.role == 'Full Stack Resident').map(user => user.lastName)
console.log(fullStackResidentsLastName)
