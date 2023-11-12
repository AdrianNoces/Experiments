const object = ['egg','chiken','egg','fried powder','egg','apple']

function removeEgg(foods) {
  let result = []
  const object = {}
  for (i = 0; i < foods.length; i++) {
  
    if (foods[i] === 'egg') {
      object[foods[i]] = (object[foods[i]] || 0) + 1
      if (object[foods[i]] < 2) {
        result.push(foods[i])   
      }
      continue
    } else {
      result.push(foods[i])
    }   
  }
  console.log(result)  
}

removeEgg(object)