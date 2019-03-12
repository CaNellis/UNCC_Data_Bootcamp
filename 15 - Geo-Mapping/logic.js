// Store API query urls
var earthquakeUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson";
// "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson"; 
var plateUrl = "https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json";

// function to change size of circle to be proportional to magnitude by a factor of 50,000
// reference getSize from heatmap Activity 17:2:2
function circleSize(magnitude) {return magnitude * 10000;};

// https://leafletjs.com/examples/choropleth/ 
// Create color range for circle diameter based on magnitude
 function getColor(d){
    return d > 5 ? "#f06b6b":
    d  > 4 ? "#f0a76b":
    d > 3 ? "#f3ba4d":
    d > 2 ? "#f3db4d":
    d > 1 ? "#e1f34d":
             "#b7f34d";
  }
// Note: Reference Activity 17:1:10
// Perform a GET request to the query URL
d3.json(earthquakeUrl, function(data) {
  // Once get response, send data.features object to create Features function
  createFeatures(data.features);
});

// define the create Features function
function createFeatures(earthquakeData) {
  // Create a GeoJSON layer containing the features array on the earthquakeData object
  var earthquakes = L.geoJSON(earthquakeData, { 
     // Define a function we want to run once for each feature in the features array
     onEachFeature(feature, layer) {
      // Give each feature a popup describing the location, magnitude, and time of the earthquake
      layer.bindPopup("<h3>Location: " + feature.properties.place + "</h3><hr>" + "<h3>Magnitude: " + feature.properties.mag + "</h3><hr>" + "<h3>Time: " + new Date(feature.properties.time) + "</h3>");
     }, 
     // add location layer with circle size and color related to magnitude  
     // reference activity 17:1:9 for general circle setup then use functions
     pointToLayer: function (feature, latlng) {
      return new L.circle(latlng, 
      {radius: circleSize(feature.properties.mag),
      fillcolor: getColor(feature.properties.mag),
      fillOpacity: 0.9,
      color: getColor(feature.properties.mag)
      })
     }
  });
  // Send our earthquakes layer to the createMap function
  createMap(earthquakes);
}

// define createmap function
function createMap(earthquakes) {
  // Define satelitemap, darkmap, and lightmap layers
  var satellitemap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.satellite",
    accessToken: "pk.eyJ1Ijoia3VsaW5pIiwiYSI6ImNpeWN6bjJ0NjAwcGYzMnJzOWdoNXNqbnEifQ.jEzGgLAwQnZCv9rA6UTfxQ"
  });
  var darkmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.dark",
    accessToken: "pk.eyJ1Ijoia3VsaW5pIiwiYSI6ImNpeWN6bjJ0NjAwcGYzMnJzOWdoNXNqbnEifQ.jEzGgLAwQnZCv9rA6UTfxQ"
  });
  var lightmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.light",
    accessToken: "pk.eyJ1Ijoia3VsaW5pIiwiYSI6ImNpeWN6bjJ0NjAwcGYzMnJzOWdoNXNqbnEifQ.jEzGgLAwQnZCv9rA6UTfxQ"
  });
  // Define a baseMaps object to hold our base layers
  var baseMaps = {"Satellite Map": satellitemap, "Dark Map": darkmap, "Light Map": lightmap};

  // level 2: add in plates
  // create tectonic plate layer
  var plateLayer = new L.LayerGroup();
  // Add plates data as line to plate layer
  d3.json(plateUrl, function(plateData) {
    L.geoJson(plateData, {
      color: "orange",
      weight: 2
    })
    .addTo(plateLayer);
  });

  // Create overlay object to hold our overlay layer
  var overlayMaps = {"Earthquakes": earthquakes, "Tectonic Plates": plateLayer};
  // Create our map, giving it the satellitemap, earthquake, and plate layers to display on load
  var myMap = L.map("map", {center: [35.09, -95.71], zoom: 3, layers: [satellitemap, earthquakes, plateLayer]});
  // Create a layer control, Pass in baseMaps and overlayMaps, Add the layer control to the map
  L.control.layers(baseMaps, overlayMaps, {collapsed: false}).addTo(myMap);
 
  // Add legend
  var legend = L.control({position: 'bottomright'});
    legend.onAdd = function(myMap) {
      var div = L.DomUtil.create('div', 'info legend'),
         grades = [0, 1, 2, 3, 4, 5],
         labels = [];
      // loop through density intervals and generate a label with a colored square for each interval
      for (var i = 0; i < grades.length; i++) {
          div.innerHTML +=
              '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' + grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
      }
      return div;
  };
  legend.addTo(myMap);
}