function w3_open() {
  document.getElementById("main").style.marginLeft = "25%";
  document.getElementById("mySidebar").style.width = "25%";
  document.getElementById("mySidebar").style.display = "block";
  document.getElementById("openNav").style.display = 'none';
}

function w3_close() {
  document.getElementById("main").style.marginLeft = "0%";
  document.getElementById("mySidebar").style.display = "none";
  document.getElementById("openNav").style.display = "inline-block";
} 

window.onload = function () {

  var dps = []; // dataPoints
  var chart = new CanvasJS.Chart("chartContainer", {
    title :{
      text: "Dynamic Data"
    },
    axisY: {
      includeZero: false
    },      
    data: [{
      type: "line",
      dataPoints: dps
    }]
  });
  
  var xVal = 0;
  var yVal = 100; 
  var updateInterval = 1000;
  var dataLength = 20; // number of dataPoints visible at any point
  
  var updateChart = function (count) {
  
    count = count || 1;
  
    for (var j = 0; j < count; j++) {
      yVal = yVal +  Math.round(5 + Math.random() *(-5-5));
      dps.push({
        x: xVal,
        y: yVal
      });
      xVal++;
    }
  
    if (dps.length > dataLength) {
      dps.shift();
    }
  
    chart.render();
  };
  
  updateChart(dataLength);
  setInterval(function(){updateChart()}, updateInterval);
  
  }