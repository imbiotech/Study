// <⚠️ DONT DELETE THIS ⚠️>
// import "src/styles.css";
const colors = ["#1abc9c", "#3498db", "#9b59b6", "#f39c12", "#e74c3c"];
// <⚠️ /DONT DELETE THIS ⚠️>

/*
✅ The text of the title should change when the mouse is on top of it.
✅ The text of the title should change when the mouse is leaves it.
✅ When the window is resized the title should change.
✅ On right click the title should also change.
✅ The colors of the title should come from a color from the colors array.
✅ DO NOT CHANGE .css, or .html files.
✅ ALL function handlers should be INSIDE of "superEventHandler"

마우스가 title위로 올라가면 텍스트가 변경되어야 합니다. colors[0] Mouse is here!
마우스가 title을 벗어나면 텍스트가 변경되어야 합니다. colors[1] Mouse is gone!
브라우저 창의 사이즈가 변하면 title이 바뀌어야 합니다. colors[2] You just resized!
마우스를 우 클릭하면 title이 바뀌어야 합니다. colors[4] That was a right click!
title의 색상은 colors 배열에 있는 색을 사용해야 합니다.
.css 와 .html 파일은 수정하지 마세요.
모든 함수 핸들러는 superEventHandler내부에 작성해야 합니다.
모든 조건이 충족되지 못하면 ❌를 받습니다.

*/

// ("Variables");
const h2 = document.querySelector("h2");

// ("functions");
function handleMouseEnter() {
  h2.style.color = colors[0];
  h2.innerText = "Mouse is here!";
}

function handleMouseLeave() {
  h2.style.color = colors[1];
  h2.innerText = "Mouse is leave!";
}

function handleResizing() {
  h2.style.color = colors[2];
  h2.innerText = "You just resized!";
}

function handleClick(event) {
  if (event.button === 0) {
    h2.style.color = colors[3];
    h2.innerText = "That was a left click!";
  } else if (event.button === 2) {
    h2.style.color = colors[4];
    h2.innerText = "That was a right click!";
  }
}

// ("handler");
const superEventHandler = {
  mouseenter: h2.addEventListener("mouseenter", handleMouseEnter),
  mouseLeave: h2.addEventListener("mouseleave", handleMouseLeave),
  resizing: window.addEventListener("resize", handleResizing),
  click: window.addEventListener("mouseup", handleClick)
};

superEventHandler;