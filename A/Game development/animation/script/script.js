const canvas = document.getElementById('canvas1');
const context = canvas.getContext('2d');
const CANVAS_HEIGHT = canvas.height = 600;
const CANVAS_WIDTH = canvas.width = 600;

const playerImage = new Image();
playerImage.src = "./playerImage/shadow_dog.png";
const spriteWidth = 575;
const spriteHeight = 523;

let frameX = 0;
let frameY = 0;
let fps = 0;
const skip = 5;

function animate() {
  context.clearRect(0,0, CANVAS_WIDTH, CANVAS_HEIGHT)
  //context.fillRect(50,50,100,100)
  //context.drawImage(image,sx,sy,sw,sh,dx,dy,dw,dh)
  context.drawImage(playerImage, frameX * spriteWidth, frameY * spriteHeight, spriteWidth, spriteHeight ,0, 0, spriteWidth, spriteHeight);
  if(fps % skip === 0) {
  	if(frameX < 6) frameX++;
  	else frameX = 0;
  }
  fps++
  requestAnimationFrame(animate);
}

animate();