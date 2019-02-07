// Unit 14 | Assignment - JavaScript and DOM Manipulation

// Level 1: Automatic Table and Date Search - - - - 
// append sightings to table body - - reference activity 14:3:3
var tbody = d3.select("tbody");
data.forEach((sighting) => {
    var row = tbody.append("tr");
    Object.entries(sighting).forEach(([key, value]) => {
      var cell = tbody.append("td");
      cell.text(value);
    });
  });
// event listener for button to filter dates
var submit = d3.select("#filter-btn");submit.on("click", function() {
    d3.event.preventDefault();    
    var inputValue = d3.select("#datetime").property("value");
    var filteredData = data.filter(data => data.datetime === inputValue)
    // delete tbody's cells
    d3.selectAll("td").html("");
    // then populate tbody's cells with filtered data
    var tbody = d3.select("tbody");
    filteredData.forEach((sighting) => {
        var row = tbody.append("tr");
        Object.entries(sighting).forEach(([key, value]) => {
            var cell = row.append("td");
            cell.text(value);
        });
    });
});
