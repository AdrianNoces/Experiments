const stringArray = [ 'hello','world','nice','search','good', 'search','hi']

function checkIndex(array) {
  const foundOrNot = ['not','found']
  const object = {}
  let first = [];
  
  for (i = 0; i < array.length; i++) {
    if (array[i] === 'search') {
      console.log(`${foundOrNot[1]} at index [${i}]`)
      first.push(i)
    } else {
      console.log(foundOrNot[0])
    }
    
    if (typeof array[i] === 'string') {
      object[array[i]] = (object[array[i]] || 0) + 1
    }
    
    if (object[array[i]] > 1) {
      console.log(`found ${array[i]} first at index[${first[0]}]`)
      return
    }
  }
  console.log(object)
  console.log(first)
}

checkIndex(stringArray)
    
    
    
