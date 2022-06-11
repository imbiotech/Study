// loginForm에 .login-form을 우선 할당한 후 내부에서 input과 button을 검색
// const loginForm = document.querySelector(".login-form");
// const loginInput = loginForm.querySelector("input");
// const loginButton = loginForm.querySelector("button");

// document에서 .login-form 내부의 input과 button을 검색
// const loginInput = document.querySelector(".login-form input");
// const loginButton = document.querySelector(".login-form button");

// function handleLIBtnClick () {
//     const name = loginInput.value;
//     if (name === "") {
//         alert("Plz write ur name.");
//     }
//     else if (name.length > 15 ) {
//         alert("Ur name is too long.");
//     };
// };

// loginButton.addEventListener("click",handleLIBtnClick);
// html의 validation 및 제한, 제출 기능을 사용하면 JS에서 지정할 필요가 없음


"Common Names" // Variable이 Common Name을 이용하는 경우가 많으니까 위로 올리는 게 좋을 듯
const HIDDEN_CLASSNAME = "hidden";
const USERNAME_KEY = "username";


"Variables" 
const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");
const link = document.querySelector("a");
const greeting = document.querySelector("#greeting");
const savedUsername = localStorage.getItem(USERNAME_KEY);


"Functinos" // 코드 내 중복 부분을 편하게 관리하기 위해 function으로 전환
function paintGreetings(username) { 
    greeting.classList.remove(HIDDEN_CLASSNAME);
    // `를 활용하면 python의 f"" 처럼 사용할 수 있음"
    greeting.innerText = `Hello ${username}`;
};

function onLISubmit (event) { // arg를 안 주면 code가 실행되지 않음
    // console.log(event); // event에 대한 정보 확인 방법
    event.preventDefault(); // Submit에 대한 default event 발생 방지
    const username = loginInput.value; // submit 된 username info를 가져옴
    loginForm.classList.add(HIDDEN_CLASSNAME);
    localStorage.setItem(USERNAME_KEY, username); // LocalStorage에 name을 저장함
    paintGreetings(username)
};


"Main Parts"
if (savedUsername === null) {
    // null 이면 form 출력
    loginForm.classList.remove(HIDDEN_CLASSNAME);
    loginForm.addEventListener("submit", onLISubmit);
}
else {
    // 입력된 데이터가 있으면 h1 - greeting 출력
    paintGreetings(savedUsername)
};


"ETC."
// link 삽입 후 link 클릭에 대한 사이트 이동 멈춤 방법
function handleLinkClick (event) {
    // alert("clicked!"); // alert는 순간적으로 코드를 멈춰주지만, 경고창이 없어지면 다시 실행됨
    event.preventDefault();
};
// link.addEventListener("click",handleLinkClick)