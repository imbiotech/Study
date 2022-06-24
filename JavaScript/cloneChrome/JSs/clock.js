"Variable"
const clock = document.querySelector("h2#clock");
let date = new Date();


"Functinos"
// function sayHello() {console.log("Hello");};
function getClock(){
    // 새로운 시간을 계속 받아옴
    date = new Date();
    
    // .padStart(length, "string") 길이가 될 때까지 string을 추가해줌
    let hrs = String(date.getHours()).padStart(2,"0");
    let mins = String(date.getMinutes()).padStart(2,"0");
    let secs = String(date.getSeconds()).padStart(2,"0");
    clock.innerText = `${hrs}:${mins}:${secs}`;
}


"Main Parts"
// setInterval과 setTimeout은 arg로 (function, msec)를 받음
// setInterval(sayHello,5000) // 지정된 매 시간마다 함수 반복
// setTimeout(sayHello,5000) // 지정된 시간 후에 함수 1회 호출
getClock()
setInterval(getClock,1000)