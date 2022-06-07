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
const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");
const link = document.querySelector("a");
const greeting = document.querySelector("#greeting")

const HIDDEN_CLASSNAME = "hidden"


// arg를 안 주면 code가 실행되지 않음
function onLISubmit (event) {
    // Submit에 대해서 default event 발생을 방지하는 방법
    event.preventDefault();
    
    // console.log(loginInput.value);
    // const name = loginInput.value;
    // console.log(name);
    // console.log(event);

    // submit 된 username info를 가져옴
    const username = loginInput.value;
    loginForm.classList.add(HIDDEN_CLASSNAME);

    greeting.classList.remove(HIDDEN_CLASSNAME);
    greeting.innerText = `Hello ${username}`; // `를 활용하면 python의 f"" 처럼 사용할 수 있음"

};

// link 클릭에 대한 함수 제한 방법
function handleLinkClick (event) {
    // alert로 인해서 순간적으로 정지됨.
    // alert("clicked!");
    event.preventDefault();
};


loginForm.addEventListener("submit", onLISubmit);
// link.addEventListener("click",handleLinkClick)