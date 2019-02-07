// // BONUS: Build the Gauge Chart
// // to plot Washing Frequency obtained from the route /wfreq/<sample>
// // modify code to account for values ranging from 0 - 9.
// // Update the chart whenever a new sample is selected

 // BONUS: Build the Gauge Chart: buildGauge(data.WFREQ) 
//  function buildGauge(data.WFREQ) {  

//       // convert washing level 0-9 to a number between 0-180 - so need to multiply by 20
//       var level = data.WFREQ * 20
      
//       // Trig to calc meter point
//       var degrees = 180 - level, radius = .5;
//       var radians = degrees * Math.PI / 180;
//       var x = radius * Math.cos(radians);
//       var y = radius * Math.sin(radians);

//       // Path: may have to change to create a better triangle
//       var mainPath = 'M -.0 -0.025 L .0 0.025 L ', pathX = String(x), space = ' ', pathY = String(y), pathEnd = ' Z';
//       var path = mainPath.concat(pathX,space,pathY,pathEnd);

//       // alter values, text, marker colors, and labels of data to match our dataset
//       var data = [{type: "scatter", x: [0], y: [0], marker: { size: 12, color: "850000" }, showlegend: false, name: "Freq", text: level, hoverinfo: "text+name"}, {values: [50 / 9, 50 / 9, 50 / 9, 50 / 9, 50 / 9, 50 / 9, 50 / 9, 50 / 9, 50 / 9, 50], rotation: 90,
//             text: ["8-9", "7-8", "6-7", "5-6", "4-5", "3-4", "2-3", "1-2", "0-1", ""], textinfo: "text",
//             textposition: "inside", marker: {colors: ['rgba(165,0,38,.5)','rgba(215,48,39,.5)','rgba(244,109,67,.5)','rgba(253,174,97,.5)','rgba(254,224,144,.5)','rgba(224,243,248,.5)','rgba(171,217,233,.5)','rgba(116,173,209,.5)','rgba(69,117,180,0)']},
//             labels: ["8-9", "7-8", "6-7", "5-6", "4-5", "3-4", "2-3", "1-2", "0-1", ""],
//             hoverinfo: "label", hole: 0.5, type: "pie", showlegend: false}];

//       // change title and adjust size
//       var layout3 = {shapes:[{type: 'path', path: path, fillcolor: '850000', line: {color: '850000'}}],
//         title: 'Belly Button Washing Frequency 
//         Scrubs per Week', 
//       height: 500, width: 500, xaxis: {zeroline:false, showticklabels:false,showgrid: false, range: [-1, 1]}, yaxis: {zeroline:false, showticklabels:false,showgrid: false, range: [-1, 1]}
//       };

//       Plotly.newPlot('gauge', data, layout3);
//     })
//   }
