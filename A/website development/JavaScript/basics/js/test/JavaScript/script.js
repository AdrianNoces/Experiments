const button = document.getElementById('js')

function storage() {
  if (button.textContent === 'Subscribe') {
    button.textContent = 'Subscribed'
  } else {
    button.textContent = 'Subscribe'
  }
  
  localStorage.setItem('a', button.textContent)
}

if (localStorage.getItem('a') === 'Subscribed') {
    button.textContent = 'Subscribed'
}
