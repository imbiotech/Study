// JavaScript 에서 html data를 가져올 수 있음
// document.title = "Blah";
// document.body;
// document.location;
// const title = document.getElementById("title"); // html에 id="title"인 element를 가져옴
// console.dir(title); title의 요소를 가져옴
// title.innerText = "Got you!";
// console.log(title.id);
// console.log(title.className);

// const Byes = document.getElementsByClassName("Bye"); // 동일한 class가 있을 경우 순서대로 가져와서 array로 작성함
// console.log(Byes);

// const h1s = document.getElementsByTagName("h1");
// console.log(h1s);

// const title = document.querySelector(".hello h1"); // class hello 내부에 있는 첫 번째 h1을 가져옴
// const title1 = document.querySelectorAll(".hello h1"); // class hello 내부에 있는 h1을 모두 가져옴
// const title2 = document.querySelectorAll("div h1"); // div 내부에 있는 h1을 모두 가져옴
// console.log(title);
// console.log(title1);
// console.log(title2);
// title.innerText = "hello";

const h1 = document.querySelector(".hello h1")
// h1.style.color = "Red"

function handleTitleClick () {
    h1.style.color = "Blue";
    h1.innerText = "Title is clicked.";
};

function handleMouseEnter () {
    h1.innerText = "Mouse is here.";
};

function handleMouseLeave () {
    h1.style.color = "Black";
    h1.innerText = "Mouse is gone.";
};

function handleWindowResize () {
    document.body.style.backgroundColor = "tomato";
};

function handleWindowCopy () {
    alert("Copier!");
};

function handleWindowOffline () {
    alert("SOS! No internet.");
};

function handleWindowOnline () {
    alart("Online.");
};

// h1.addEventListener("click", handleTitleClick);
h1.onclick  = handleTitleClick;
// h1.addEventListener("mouseenter", handleMouseEnter);
h1.onmouseenter = handleMouseEnter;
// h1.addEventListener("mouseleave", handleMouseLeave);
h1.onmouseleave = handleMouseLeave;

window.addEventListener("resize", handleWindowResize);
window.addEventListener("copy", handleWindowCopy);
window.addEventListener("offline", handleWindowOffline);
window.addEventListener("online", handleWindowOnline)
