 
// Define function that builds metadata info panel
function buildMetadata(sample) {
  var url = `/metadata/${sample}`; 
  console.log("sample", sample); 
  d3.json(url).then(function(data) {
    var metadataPanel = d3.select("#sample-metadata"); 
    metadataPanel.html(""); 
    var info = Object.entries(data); 
    info.forEach(function([key, value]) {
      metadataPanel.append("div").text(`${key}: ${value}`);
    })
  })
}

// Define function to build Bubble and Pie Chart
function buildCharts(sample) {
  var url2 = `/samples/${sample}`;
  // Use `d3.json` to fetch the sample data for the plots
  d3.json(url2).then(function(data) {
    // Build a Bubble Chart using the sample data
    var bubbleIds = data.otu_ids;
    var bubbleLabels = data.otu_labels;
    var bubbleValues = data.sample_values;
    var bubbleData = {mode: 'markers', x: bubbleIds, y: bubbleValues, text: bubbleLabels, marker: {color: bubbleIds, size: bubbleValues}};
    var bData = [bubbleData];
    var layout = {showlegend: false}
    Plotly.newPlot('bubble', bData, layout);
    // Build Pie Chart - need slice() for first 10 sample_values, otu_ids, and labels
    var pieTopIds = data.otu_ids.slice(0, 10);
    var pieTopLabels = data.otu_labels.slice(0, 10);
    var pieTopValues  = data.sample_values.slice(0, 10);
    var pieData = [{"labels": pieTopIds, "values": pieTopValues, "hovertext": pieTopLabels, "type": "pie"}];
    layout2 = {title: "First 10 Bacterial Samples"};
    Plotly.newPlot('pie', pieData, layout2);

  })    
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");
  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });
    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

// Define function to update charts when new sample is selected
function optionChanged(newSample) { 
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
