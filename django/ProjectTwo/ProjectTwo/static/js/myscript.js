var header = document.querySelector('h1')

function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

function setRandomColor() {
  colorInput = getRandomColor()
  header.style.color = colorInput;
}

setInterval("setRandomColor()",500)