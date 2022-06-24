// "Vairables"
const rangeInput = document.querySelector("#range input");
const number = document.querySelector("#choose");
const numberInput = document.querySelector("#choose input");
const game = document.querySelector("h3#game");
const result = document.querySelector("h3#result");

// "Functinos"
function onNumberSubmit(event) {
  event.preventDefault();
  const max = parseInt(rangeInput.value);
  const choose = parseInt(numberInput.value);
  if (max < 0 || choose < 0) {
    alert("Type number at least 0.");
    return;
  } else if (choose > max) {
    alert(`Guess number in range between 0 and ${max}`);
    return;
  }
  const rand = randbetween(max);
  game.innerText = `You choose: ${choose}, the machine choose: ${rand}.`;
  if (choose === rand) {
    result.innerText = "You won!";
  } else {
    result.innerText = "You lost!";
  }
}

function randbetween(max) {
  return Math.floor(Math.random() * max);
}

// Main parts
number.addEventListener("submit", onNumberSubmit);
