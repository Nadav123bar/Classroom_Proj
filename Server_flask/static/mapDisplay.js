function displayLocation(xCoordinate, yCoordinate) {
    var map = L.map('map');

    map.setView([xCoordinate, yCoordinate], 12);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    L.marker([xCoordinate, yCoordinate]).addTo(map)
        .bindPopup('Your Current Location')
        .openPopup();
}

function helper()
{
    var currentUrl = window.location.href;
    var i = 36;
    var username ='';
    while(currentUrl[i] != '&')
    {
        username = username + currentUrl[i]
        i++;
    }
    return username
}
   

function getLocation() {
    // var currentUrl = window.location.search;
    // var urlParams = new URLSearchParams(currentUrl);
    var userName = helper();
    var manualLatitude = 0;
    var manualLongitude = 0;

    var url = "/get_location";
    var data = {
        user_name: userName,
    };

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams(data),
    })
    .then(response => response.json())
    .then(result => {
        // Handle the result as needed
        console.log(result);
        manualLatitude = result.lat
        manualLongitude = result.lng
        displayLocation(manualLatitude, manualLongitude);
    })
    .catch(error => {
        console.error('Error:', error);
    });
   
}

getLocation();