var mymap = L.map('mapid', {
  center: [39.052,-118.243],
  zoom: 5
});

let token='pk.eyJ1Ijoic2hvdWp1bmd1IiwiYSI6ImNqZWdsNzIyOTF3OHQycW8yZGt2cjZkOTAifQ.tvV-Oa9NnJx42g-O0Ia8Fw';
let link='https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.light',
    accessToken: token
}).addTo(mymap);

//start from here
function rad(dt){
  return dt*30000;
};

function col(dt){
  return dt>5?'red':
         dt>3?'orange':
         dt>1?'yellow':
         'green'
  };

function add_circle(data){
  let d=data.features;
  for (let i=0; i<d.length; i++) {
    let mag=d[i].properties.mag;
    let lon=d[i].geometry.coordinates[0];
    let lat=d[i].geometry.coordinates[1];
    let title=d[i].properties.title;
    let circle=L.circle([lat,lon],{
      radius:rad(mag),
      color:col(mag),
      fillColor:col(mag),
      stroke: false,
      fillOpacity: 0.5
    }
    ).addTo(mymap);
    circle.bindPopup(title);
  };
};

d3.json(link, function(error, data){
  if (error) return console.warn(error);
  add_circle(data);

  let legend = L.control({position: 'bottomright'});
  legend.onAdd = function (map) {
  let div = L.DomUtil.create('div', 'info legend'),
        grades = [0, 1, 3, 5],
        labels = [];
  for (var i = 0; i < grades.length; i++) {
      div.innerHTML +=
          '<i style="background:' + col(grades[i] + 1) + '"></i> ' +
          grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
    }
    return div;
};
legend.addTo(mymap);
});
