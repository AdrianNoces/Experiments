const list = /*JSON.parse(localStorage.getItem('list')) ||*/ [{
  name: 'name',
  dueDate: 'dueDate'
}];

renderList()

function add() {
  const namesToAdd = document.getElementById('toDoName');
  const date = document.getElementById('date');
  
  list.push({
    name: namesToAdd.value,
    dueDate: date.value
  });
  
  namesToAdd.value = '';
  renderList()
}

function renderList() { 
  let displayName = '';
  
  list.forEach(function(todoObject,index) {
    const { name, dueDate} = todoObject;
    const store = `
      <div class="container">
        <div class="childContainer">
          <div class="name">${name}</div>
          <div class="date">${dueDate}</div>
        </div>
        <button class="delButton" onclick="
          list.splice(${index},1)
          renderList()
        ">
          Delete 
        </button>
      </div>
      `;
      displayName += store
  });
  
  /*
  for (let i = 0; i < list.length; i++) {
    const todoObject = list[i];
    const { name, dueDate} = todoObject;
    const store = `
      <div class="container">
        <div class="childContainer">
          <div class="name">${name}</div>
          <div class="date">${dueDate}</div>
        </div>
        <button class="delButton" onclick="
          list.splice(${i},1)
          renderList()
        ">
          Delete 
        </button>
      </div>
      `;
      displayName += store
  };
  */
  document.getElementById('list')
    .innerHTML = displayName
    
  localStorage.setItem('list',JSON.stringify(list))
}

function keydown() {
  if (event.key === 'Enter') {
    add()
  }
}
