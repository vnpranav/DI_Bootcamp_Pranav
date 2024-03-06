const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }
  var keys = Object.keys(details);
  var values = Object.values(details);
  var sentence = "";
  
  for (let i = 0; i < keys.length; i++){
      sentence += keys[i] + " " + values[i] + " ";
  }
  console.log(sentence);