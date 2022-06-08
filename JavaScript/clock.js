"Variable"
const clock = document.querySelector("h2#clock");


"Functinos"
function sayHello() {
    console.log("Hello");
};


"Main Parts"
setInterval(sayHello,5000) // setInterval은 (function, msec) 를 arg로 받음
