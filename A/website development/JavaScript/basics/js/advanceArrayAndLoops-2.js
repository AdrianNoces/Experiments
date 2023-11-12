let positive = 0;
let negative = 0

const array = [1,6,-1,-8,0,5,8,-6,-1].forEach((value, index) => {
  if (value > 0) {
    positive++
  } else {
    negative++
  }
})

console.log(`Positive ${positive}, Negative ${negative}`)

let object = {};

const egg = ['egg','apple','egg','apple','egg','apple','egg']. filter ((value, index) => {
  if (typeof value === 'string') {
      object[value] = (object[value] || 0) + 1
    if (value != 'egg') {
      return value;
    } else if (object[value] > 2) {
        return value;
    }
  }
    
  
})

console.log(egg)
console.log(object)
