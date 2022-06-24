// Variables
const clockTitle = document.querySelector(".js-clock");
let date = new Date();
const yrs = date.getFullYear();
const xmas = new Date(yrs, 11, 25);

// Functions
function getDateLeft() {
  date = new Date();
  let interval = (xmas.getTime() - date.getTime()) / 1000;

  const days = String(Math.floor(interval / 24 / 60 / 60));
  interval -= days * 24 * 60 * 60;

  const hrs = String(Math.floor(interval / 60 / 60)).padStart(2, "0");
  interval -= hrs * 60 * 60;

  const mins = String(Math.floor(interval / 60)).padStart(2, "0");
  interval -= mins * 60;

  const secs = String(Math.floor(interval)).padStart(2, "0");

  clockTitle.innerText = `${days}d ${hrs}h ${mins}m ${secs}s`;
}

// Main parts
getDateLeft();
setInterval(getDateLeft, 1000);
