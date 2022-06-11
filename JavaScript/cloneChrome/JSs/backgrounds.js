"Variable"

const images = [
    "0.jpg",
    "1.jpg",
    "2.jpg"
];
let indexing_images = Math.floor(Math.random() * images.length);
let imageOfToday = images[indexing_images];
// JavaScript에서 Element를 생성하는 함수
const backgrounds = document.createElement("img");


"Main Parts"
// backgrounds 의 src에 image 파일의 링크를 걸어줌
backgrounds.src = `img/${imageOfToday}`;
// body에 child를 추가해서 실제로 html에 나타나도록 함
document.body.appendChild(backgrounds)