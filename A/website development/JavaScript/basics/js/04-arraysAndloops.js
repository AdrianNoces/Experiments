const words = ['apple','grape','apple','apple','grape','grape','apple','grape','grape']

function countWords(array) {
  const object = {};
  for (i = 0; i < array.length; i++) {
    if (typeof array[i] === 'string') {
      object[array[i]] = (object[array[i]] || 0) + 1
    }
  }
  console.log(object)
}

countWords(words)
