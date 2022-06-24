"Variables"
const APIKEY = "1aa3ed89c34931deceeeea725cc1f917";

"Functions"
function onGeoOk(position) {
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;
    const URL = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${APIKEY}&units=metric`;
    // URL을 열고 기다림, response 데이터를 받아옴
    fetch(URL).then(response => {
        return response.json()
    }).then(data=>{
        const divWeather = document.querySelector("#weather");
        const city = divWeather.querySelector("span:first-child");
        const weather = divWeather.querySelector("span:last-child");
        city.innerText = data.name+",";
        weather.innerText = `${data.weather[0].main}, ${data.main.temp}°C`;
    });
}

function onGeoErr() {
    alert("Can't find you. No weather for you.");
}


"Main Parts"
// getCurrentPosition 함수는 위치 호출이 성공했을 때의 함수와 실패했을 때의 함수를 args 로 받음
navigator.geolocation.getCurrentPosition(onGeoOk, onGeoErr);