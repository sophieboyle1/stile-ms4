    var mymap = L.map('map').setView([53.3390102, -6.2641539], 13);
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiNXBlbmNlc3BlbmNlIiwiYSI6ImNrbWk4c3R1MDBld3QydXF2czR5NmNqNTIifQ.8G4oo2NMwbYjWvajipthaA'
}).addTo(mymap);
    var marker = L.marker([53.3390102,-6.2641539]).addTo(mymap);
    marker.bindPopup("<b>We are here!</b><br>Looking forward to meeting you").openPopup();