/*
const num = [1,-2,-4,5,-6,4,5,-6,0,1]
let countPositiveNum = 0;

function countPositive(nums) {
  for (i = 0; i < nums.length; i++) {
    if (nums[i] > 0) {
      countPositiveNum++;
    }
  }
  console.log(countPositiveNum)
}

countPositive(num)
*/

const num = [9,6,7,1,11,10,0,-6]
const num1 = [6,-2,-3,-9,1,2,3,4,100]
const num2 = []

function minMax(array) {
  let smallest = array[0]
  let largest = array[0]

  for (i = 0; i < array.length; i++) {
    if (array[i] < smallest) {
      smallest = array[i];
    }
    
    if (array[i] > largest) {
        largest = array[i]
    }
  }
  console.log(`min: ${smallest} max: ${largest}`)
}

minMax(num)
minMax(num1)
minMax(num2)
