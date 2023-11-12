let score = JSON.parse(localStorage.getItem('k')) || {
  wins: 0,
  losses: 0,
  ties: 0,
}

/*
if (!score) {
  score = {
    wins: 0,
    losses: 0,
      ties: 0,
    }
  }
  */
  
updateScoreElem()

let isAutoPlaying = false
let interval;

document.getElementById('autoplay')
  .addEventListener('click', () => {
      autoplay()
  });
  
document.getElementById('stopButton')
  .addEventListener('click', () => {
    stop()
  })
  
function stop() {
  clearInterval(interval)
}
  
function yes() {
  interval = setInterval(() => {
    const playerMove = pickComputerMove()
    Gameplay(playerMove)
  }, 1000)
  document.getElementById('confirmation')
    .innerHTML = ''
}

function no() {
  document.getElementById('confirmation')
    .innerHTML = ''
}

function autoplay() {
  document.getElementById('confirmation')
    .innerHTML = `    
      <div id="confirmContainer">
        <p>Are you sure?</p>
        <button id="noButton" onclick="no()">no</button>
        <button id="yesButton" onclick="yes()">yes</button>
      </div>
    `;
}

document.getElementById('rockButton')
  .addEventListener('click', () => {
    Gameplay('rock')
  })
  
document.getElementById('paperButton')
  .addEventListener('click', () => {
    Gameplay('paper')
  })
  
  
document.getElementById('scissorsButton')
  .addEventListener('click', () => {
    Gameplay('Scissors')
  })
  
function Gameplay(playerMove) {
  const computerMove = pickComputerMove();
  
  let results = '';
  
  if (playerMove === 'Scissors') {
    if (computerMove === 'rock') {
      results = 'You lose!'
    } else if (computerMove === 'paper') {
      results = 'You win!'
    } else if (computerMove === 'Scissors') {
      results = 'Tie!'
    }
    
  } else if (playerMove === 'paper') {
    if (computerMove === 'rock') {
      results = 'You win!'
    } else if (computerMove === 'paper') {
      results = 'Tie!'
    } else if (computerMove === 'Scissors') {
      results = 'You lose!'
    }
    
  } else if (playerMove === 'rock') {
    if (computerMove === 'rock') {
      results = 'Tie!'
    } else if (computerMove === 'paper') {
      results = 'You lose!'
    } else if (computerMove === 'Scissors') {
      results = 'You win!'
    }
  }
  
  if (results === 'You win!') {
    score.wins++;
  } else if (results === 'You lose!') {
    score.losses++;
  } else if(results === 'Tie!') {
    score.ties++;
  }
  
  document.querySelector('.js-result')
   .innerHTML = results;
  
  document.querySelector('.js-moves')
   .innerHTML = `You <img src="icon/${playerMove}-emoji.png" alt=""></img> <img src="icon/${computerMove}-emoji.png"></img> Computer`;
  updateScoreElem()
  
  localStorage.setItem('k',JSON.stringify(score))

  return;
  
  console.log(results);
  alert(`You picked ${playerMove}, Computer picked ${computerMove}. ${results}
wins: ${score.wins}, losses: ${score.losses}, ties: ${score.ties}`)
  
}

document.getElementById('reset')
  .addEventListener('click', () => {
    reset()
  })

function reset() {
 score.wins = 0;
 score.losses = 0;
 score.ties = 0;
 updateScoreElem()
 localStorage.removeItem('s')
 document.querySelector('.js-result')
   .innerHTML = '';
 document.querySelector('.js-moves')
   .innerHTML = '';
   
 localStorage.setItem('k',JSON.stringify(score))
}

function updateScoreElem() {
 document.querySelector('.js-score')
   .innerHTML = `wins: ${score.wins}, losses: ${score.losses}, ties: ${score.ties}`;
}
  
/* Math.random pick random number between 0 - 1 */
function pickComputerMove() {
  const randomNumber = Math.random();
  let computerMove = '';
  
  if (randomNumber >= 0 && randomNumber <= 1/3) {
      computerMove = 'rock';
  } else if (randomNumber >= 1/3 && randomNumber <= 2/3) {
      computerMove = 'paper';
  } else if (randomNumber >= 2/3 && randomNumber <= 1) {
      computerMove = 'Scissors'
  }
  
  return computerMove;
}


setInterval(function() {
  random = Math.random()
  
})

