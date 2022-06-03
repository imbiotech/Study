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
const loginForm = document.querySelector(".login-form");
const loginInput = document.querySelector(".login-form input");

// arg를 안 주면 code가 실행되지 않음
function onLISubmit (event) {
    // Submit에 대해서 default event 발생을 방지하는 방법
    event.preventDefault();
    console.log(loginInput.value);
    // const name = loginInput.value;
    // console.log(name);
    // console.log(event);
};

loginForm.addEventListener("submit", onLISubmit);

