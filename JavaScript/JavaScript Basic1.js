// ###################################### JavaScript 이론 ########################################

// console에 출력하는 방식
console.log(54545454);
console.log("hihihi");
console.log('hello');


console.log(5 + 2);
console.log(5 * 2);
console.log(5 / 2);
// 대신에 const로 변수 지정, const는 immutable
const a = 10;
const b = 3;
console.log("a + b =", a + b);
console.log("a & b =", a * b);
console.log("a / b =", a / b);


// string도 지정 가능
const myName = "MS.J";
console.log("hello " + myName);
// myName = "CC"
// console.log(myName), 출력 시 에러 


// let 변수 지정, let은 mutable
let c = 10;
console.log("let c = 10");
console.log("c =", c);
c = 9;
console.log("c = 9");
console.log("c =", c);


// const로 대부분의 변수를 지정하고, 일부 mutable 변수 관리에만 let 사용하는 것이 좋음
// const와 let 사용 전에는 var를 사용 했으며, var은 mutable 선언임
var d = 5;
console.log("var d = 5");
console.log("d =", d);
d = 10;
console.log("d = 10");
console.log("d =", d);


// boolean 
const amIFat = true;
console.log("const amIFat = true");
console.log("amIFat =",amIFat);


// null * python None
const nothing = null;
console.log("const nothing = null");
console.log("nothing =",nothing);


// undefined
let something;
console.log("let something");
console.log("something =",something);


// array * python list

// array 없이는 하나하나 변수를 지정해줘야 하고 데이터에 대한 접근이 어려움
const mon = "Mon";
const tue = "Tue";
const wed = "Wed";
// blahh.............

// array를 사용하면 한 번에 변수 지정 및 접근 가능
const daysOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
console.log(daysOfWeek);

// array에서 주소로 값 호출
console.log("daysOfWeek[3] =",daysOfWeek[3]);

// array에 값 추가
daysOfWeek.push("Sun");
console.log("daysOfWeek.push('Sun')");
console.log(daysOfWeek);


// object * python dict

// object 없이는 하나하나 변수를 지정해줘야 하고 데이터 통합 관리가 어려움
const playerName = "MS";
const playerPoints = 111;
const playerHandsome = false;
const playerFat = "little bit";

// array를 사용할 경우에는 어느정도는 관리가 가능하지만
// 다수의 데이터를 관리하기 위해서는 여전히 어려움
// const player = ["MS", 111, false, "little bit"]

// object를 사용할 경우
const player = {
    Name: "MS",
    Points: 111,
    Handsome: false,
    Fat: "little bit"
};
console.log(player);
console.log(player.Name);

// constant는 수정이 안 되는 것이 맞지만 object를 하나하나 수정하는 것은 가능
player.Fat = "yes";
console.log("player.Fat = 'yes'");
console.log(player);

// object는 추가 하는 것 가능
player.lastName = "J";
console.log("player.lastName = 'J'");
console.log(player);

// 기존 변수에 업데이트
player.Points = player.Points + 10;
console.log("player.Points = player.Points + 10");
console.log(player);


// function, 변수를 받지 못하면 undefined 출력
function sayHello(Name, age){
    console.log("Hello! My name is", Name, "and I'm", age, "years old.")
};
sayHello("MS", 10);
sayHello("MJ", 11);


// object에 function 삽입
const player2 = {
    name: "MS",
    sayHello: function (name) {
        console.log("Hello!", name)
    },
    points: 1000
};
player2.sayHello(player2.name);


// object 및 function 사용해서 계산기 만들기
const calculator = {
    add: function (a, b) {
        console.log(a + b);
    },
    subt: function (a, b) {
        console.log(a - b);
    },
    prod: function (a, b) {
        console.log(a * b);
    },
    divs: function (a, b) {
        console.log(a / b);
    },
    powe: function (a, b) {
        console.log(a**b);
    }
};
calculator.add(3, 5);
calculator.subt(3, 5);
calculator.prod(3, 5);
calculator.divs(3, 5);
calculator.powe(3, 5);


// return = function에서 결과를 반환
const age = 96;
function calcKRAge(ageOfForeigner) {
    return ageOfForeigner + 2;
};
const KRage = calcKRAge(age);
console.log(KRage);


// obj-func에서 console.log를 쓰지 않고 결과 반환
const calculator2 = {
    add: function (a, b) {
        return (a + b); // function은 return 행에서 종료됨. 이후는 실행하지 않음
    },
    subt: function (a, b) {
        return (a - b);
    },
    prod: function (a, b) {
        return (a * b);
    },
    divs: function (a, b) {
        return (a / b);
    },
    powe: function (a, b) {
        return (a**b);
    }
};
// return 하지 않고 console 로그로 반환할 경우에는 변수가 선언되지 않음
const result = calculator2.subt(211,234);
console.log(result);


// if else 
// prompt; User가 입력하도록하는 명령창, JS를 일시 정지하고, CSS 적용이 안 됨. 그래서 지금은 잘 안 씀.
// 입력된 값은 모두 string으로 저장됨
const ageForAlcohol = prompt("How old R U?");
console.log(ageForAlcohol);
console.log(typeof ageForAlcohol);
parseInt(ageForAlcohol); // string으로 받아진 수를 int형으로 전환함, 수가 아니면 NaN 출력
console.log(isNaN(ageForAlcohol)); // NaN인지를 boolean으로 출력
// parseInt(prompt("aa")); parseInt 내에 prompt를 넣어서 실행할 수 있음

if (isNaN(ageForAlcohol) || ageForAlcohol <= 0) {
    console.log("Please write a real positive number.");
}
else if (ageForAlcohol < 18) {
    console.log("You are too young.");
}
else if (18 <= ageForAlcohol && ageForAlcohol <= 50) {
    console.log("You can drink.");
}
else if (50 < ageForAlcohol && ageForAlcohol <= 80) {
    console.log("You should exercise.");
}
else if (ageForAlcohol === 100) {
    console.log("Wow! You are wise.")
}
else {
    console.log("You can do whatever you want.");
};

// &&; And, ||; or, ===; is same, !== not same


console.log("End Line")