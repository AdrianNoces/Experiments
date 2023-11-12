const colors = ['red','green','blue','red','blue','blue','white']

function findIndex(array,word) {
  const object = {}
  
  for (i = 0; i < array.length; i++) {
  
    if (typeof array[i] === 'string') {
      object[array[i]] = (object[array[i]] || 0) + 1
    }
    
    if (array[i] === word) {
      if (object[array[i]] > 1) {
        return
      }
      console.log(`${word} found at index[${i}]`)     
    }
  }
}

function unique(array) {
  const object = {}
  const results = []
  
  for (i = 0; i < array.length; i++) {
    if (typeof array[i] === 'string') {
      object[array[i]] = (object[array[i]] || 0) +1
    }
    
    if (object[array[i]] < 2) {
      results.push(array[i])
    }
  }
  console.log(results)
}

findIndex(colors,'blue')
unique(colors)