const students = [{name: "Ray", course: "Computer Science", isPassed: true}, 
   {name: "Liam", course: "Computer Science", isPassed: false}, 
   {name: "Jenner", course: "Information Technology", isPassed: true}, 
   {name: "Marco", course: "Robotics", isPassed: true}, 
   {name: "Kimberly", course: "Artificial Intelligence", isPassed: false}, 
   {name: "Jamie", course: "Big Data", isPassed: false}];
let passed  = students.filter(student => student.isPassed).forEach(student => console.log(`Good job ${student.name} for passing in ${student.course}`))