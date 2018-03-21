var mydata;
function load() {
    var request = new XMLHttpRequest();
    request.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            mydata = JSON.parse(this.responseText);
           
        }
    };

    request.open("GET", "../static/data.json", true);
    request.send(null);
    
    var chartData = [];
    var xData = [];
    labelData = "No data selected"
    makeChart(chartData, labelData, xData);
}

function clicked(id) {
   
    var num = document.getElementById("count").value;
    var chartData = [];
    var xData = []
    var  n = mydata.length	
        if (id == 0) {
            var table="<tr><th>Minute</th><th>Temperature (C)</th><th>Temperature (F)</th></tr>";
            for(i = n-num; i < n; i++) {
                table += "<tr><td>" +
                (i+1) +
                "</td><td>" +
                mydata[i].tempC +
                "</td><td>" +
                mydata[i].tempF +
                "</td></tr>";
                
                chartData.push(mydata[i].tempC)
                xData.push(i+1)
                
                }
           labelData="Temperature (C)"
           makeChart(chartData, labelData, xData);
        }
            
        if (id == 1) {
            var table="<tr><th>Minute</th><th>Light</th></tr>";
            for(i = n-num; i < n; i++) {
                table += "<tr><td>" +
                (i+1) +
                "</td><td>" +
                mydata[i].light +
                "</td>"
                
                chartData.push(mydata[i].light)
                xData.push(i+1)
                
                }
           labelData="Light Level"
           makeChart(chartData, labelData, xData);
        }
        if (id == 2) {
            var table="<tr><th>Minute</th><th>Sound</th></tr>";
            for(i = n-num; i < n; i++) {
                table += "<tr><td>" +
                (i+1) +
                "</td><td>" +
                mydata[i].envelope +
                "</td>"
                
                chartData.push(mydata[i].envelope)
                xData.push(i+1)
                
                }
           labelData="Sound Envelope"
           makeChart(chartData, labelData, xData);
        }
        if (id == 3) {
            var table="<tr><th>Minute</th><th>Humidity</th></tr>";
            for(i = n-num; i < n; i++) {
                table += "<tr><td>" +
                (i+1) +
                "</td><td>" +
                mydata[i].humidity +
                "</td>"
                
            chartData.push(mydata[i].humidity)
            xData.push(i+1)
                
                }
           labelData="Humidity"
           makeChart(chartData, labelData, xData);
        }
    document.getElementById("mytable").innerHTML = table;
}

function makeChart(chartData,labelData,xData) {
     var ctx = document.getElementById("myChart").getContext("2d");
     var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: xData,
            datasets: [{
            label: labelData,
            fill: false,
            data: chartData,
            borderColor: 'red'
                 }]
        },
        options: {
            events: [],
            scales: {
                xAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Time (min)'
                        }
                }],
                yAxes: [{
                        ticks: {
                            suggestedMin: 0
                        },
                		display: true,
						scaleLabel: {
							display: true,
							labelString: labelData
						}
                    
                
                }]
            }
        }
     });
}

