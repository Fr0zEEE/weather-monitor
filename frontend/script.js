let cityInput = document.getElementById("getWeather");
let button = document.getElementById("getWeatherBtn");
let weatherResult = document.getElementById("weatherResult");


button.addEventListener("click", function(){
    let cityName = cityInput.value;
    fetch(`http://127.0.0.1:8000/weather?city=${cityName}`)
        .then(response => response.json())
        .then(data => {
            console.log(data);
                weatherResult.innerHTML = `
                    <h2>Weather in ${data.city}</h2>
                    <p>Temperature: ${data.temperature}°C</p>
                    <p>Description: ${data.description}</p>
                    <p>Humidity: ${data.humidity}%</p>
                    <p>Wind speed: ${data.windspeed}m/s</p>
                    <img src="${data.icon_url}" alt="weather icon">
                `;
            })
            .catch(error => {
                console.error("Error fetch:", error);
                weatherResult.innerHTML = "<p>Error by getting data</p>";
            });
});