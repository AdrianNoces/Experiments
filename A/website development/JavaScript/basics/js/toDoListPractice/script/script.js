const list = [];

function add() {
  const namesToAdd = document.getElementById('toDoName');
  
  list.push(namesToAdd.value);
  namesToAdd.value = '';
  renderList()
}

function renderList() {
  const displayName = document.getElementById('list');
  let store = '';
  
  for (let i = 0; i < list.length; i++) {
    store = `<p>${list[i]}</p>`;
  };
  displayName.innerHTML += store;
}

function keydown() {
  if (event.key === 'Enter') {
    add()
  }
}
