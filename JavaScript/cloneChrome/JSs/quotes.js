
"Variables" 
const quotes = [
    {
        quote:"1q",
        author:"1a"
    },
    {
        quote:"2q",
        author:"2a"
    },
    {
        quote:"3q",
        author:"3a"
    },
    {
        quote:"4q",
        author:"4a"
    },
    {
        quote:"5q",
        author:"5a"
    },
    {
        quote:"6q",
        author:"6a"
    },
    {
        quote:"7q",
        author:"7q"
    },
    {
        quote:"8q",
        author:"8a"
    },
    {
        quote:"9q",
        author:"9a"
    },
    {
        quote:"10q",
        author:"10a"
    }
]

const quote = document.querySelector("#quote span:first-child");
const author = document.querySelector("#quote span:last-child");

// Math 모듈을 사용
Math.random(); // 0 보다 크거나 같고 1 보다 작은 임의의 실수 출력
Math.round(); // 반올림
Math.ceil(); // 올림
Math.floor(); // 내림
let indexing_quotes = Math.floor(Math.random() * quotes.length);
let quoetOfToday = quotes[indexing_quotes];

quote.innerText = quoetOfToday.quote;
author.innerText = quoetOfToday.author