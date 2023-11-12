/*
let num = [1,2,3]
console.log(num)

for (let i = 0; i < num.length; i++) {
  num[i] += 1;
}

console.log(num)


let num = [1,2,3]
let num2 = [-2,0,1,2,99]

function addOne(array) {
  for (i = 0; i < array.length; i++) {
    array[i] += 1;
  }
  console.log(array)
}

addOne(num)
addOne(num2)


let num = [1,2,3]

function addNum(array,num) {
  for (i = 0; i < array.length; i++) {
    array[i] += num;
  }
  console.log(array)
}

addNum(num,6)
*/

const num1 = [1,1,1];
const num2 = [1,2,3];

function addTwoArrays(array1,array2) {
  for (i = 0; i < array1.length; i++) {
    array1[i] += array2[i];
  }
  console.log(array1)
}

addTwoArrays(num1,num2)
