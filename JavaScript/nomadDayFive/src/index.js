/* 
1. 창 크기에 따라 노랑 <-> 보라 <-> 하늘 로 배경색 변경
2. window.resizeTo(width, height)
*/

// "Variables";
// 청록, 하늘, 보라, 노랑, 빨강
const colors = ["#1abc9c", "#3498db", "#9b59b6", "#f39c12", "#e74c3c"];
const h2 = document.querySelector("h2");
const body = document.querySelector("body");

// "functions";
function windowResize(event) {
  let width = window.innerWidth;
  if (width < 450) {
    body.style.backgroundColor = colors[1];
  } else if (width <= 900) {
    body.style.backgroundColor = colors[2];
  } else {
    body.style.backgroundColor = colors[3];
  }
}

// "main parts";
h2.style.color = "#FFFFFF";
window.addEventListener("resize", windowResize);
