"Keys"
TODOS_KEY = "toDos"

"Variables"
const toDoForm = document.querySelector("#todo_form");
const toDoInput = toDoForm.querySelector("input")
const toDoList = document.querySelector("#todo_list");
let toDos = [];
const savedtoDos = localStorage.getItem(TODOS_KEY);


"Functions"
function saveToDos() {
    // JSON.stringify는 내부에 입력된 모든 데이터를 그 자체로 string으로 바꿔줌
    localStorage.setItem(TODOS_KEY,JSON.stringify(toDos));
}


function buttonClicker(event) {
    // event가 발생한 li의 데이터 획득 
    const li = event.target.parentElement;
    
    // html 상에서 해당 li 삭제
    li.remove();

    // toDos array에서 해당 데이터를 삭제한 array를 만들고 toDos에 덮어씀
    toDos = toDos.filter(element => {
        console.log(element.id === parseInt(li.id))
        element.id === parseInt(li.id);
        console.log(toDos);
    })
    saveToDos();
}

function paintToDo(toDos) {
    // element를 생성
    const li = document.createElement("li");
    const span = document.createElement("span");
    const button = document.createElement("button");
    
    // text와 button 사이에 간격, toDos가 Object이므로 .text로 전환
    span.innerText = toDos.text+" ";
    
    // button에 emoji를 넣고 클릭에 대한 이벤트 추가
    button.innerText = "❌";
    button.addEventListener("click",buttonClicker);

    // li를 특정하기 위해서 toDos 생성 시 만들어진 id를 동일하게 부여함
    li.id = toDos.id

    // li 하단에 span, button을 추가, toDoList에 li 추가
    li.appendChild(span);
    li.appendChild(button);
    toDoList.appendChild(li);
}

function handleToDoSubmit(event) {
    // submit의 default값인 refresh를 방지함
    event.preventDefault();

    // submit된 값을 newToDo에 추가하고 입력란 초기화
    const newToDo = toDoInput.value;
    toDoInput.value = "";

    // 모든 newToDo를 구분하기 위한 random id 생성하여 부여하고 toDos array에 추가
    const newToDoObj = {
        text:newToDo,
        id: Date.now(),
    }
    toDos.push(newToDoObj);

    // saveToDos 함수를 호출하여 toDos array를 localStorage에 저장
    saveToDos();
    
    // paintToDo 함수를 호출하여 화면에 나타냄
    paintToDo(newToDoObj);
}


"Main Parts"
if (savedtoDos !== null) {
    // localStorage에 저장된 이상한 형식의 data를 다시 array로 바꿔줌
    const parsedtoDos = JSON.parse(savedtoDos);
    toDos = parsedtoDos;
    
    // forEach를 사용하여 array 내부 item들에 대해서 특정 함수를 사용할 수 있음
    // function을 직접 작성해서 사용해도 되고 arrow function으로 작성해도 됨
    parsedtoDos.forEach(element => {
        paintToDo(element)
    });
}

toDoForm.addEventListener("submit", handleToDoSubmit);