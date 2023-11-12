const add = function() {
  console.log('hello')
}

setInterval(function() {
  console.log('hello')
}, 2000)

const array = [1,-3,5,-6].filter((value, index) => {
  if (value < 0) {
    return value = false;
  } else if (value > 0){
    console.log(value)
  }
  
  /*
  return value >= 0;
  */
})

console.log([1,7,7,7,-1].map((value, index) => {
  if (value === 7) {
    return value;
  }
}))