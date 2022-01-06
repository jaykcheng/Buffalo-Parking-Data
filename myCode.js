// path -- string specifying URL to which data request is sent 
// callback -- function called by JavaScript when response is received
function ajaxGetRequest(path, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("GET", path);
    request.send();
}

function getData(){
  ajaxGetRequest('scatter',displayScatter);
  ajaxGetRequest('pie',displayPie);
  ajaxGetRequest('line',displayLine);
}

//Scatter Plot
function displayScatter(response){
  var scat = JSON.parse(response)
  var trace1 = {
    x: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    y: scat,
    mode: 'markers',
    type: 'scatter'
};
var data = [trace1]
var layout = {
  title: 'Tows by Day of the Month',
  xaxis: {title: 'Day of the Month',},
  yaxis: {title: '# Tows',}
};
Plotly.newPlot('scatterplot', data, layout);
}

//Pie Chart
function displayPie(response){
  var pie = JSON.parse(response)
  var data = [{
    values: pie,
    labels: ['District A', 'District B', 'District C', 'District D', 'District E'],
    type: 'pie'
}];
  var layout = {
    title: 'Tows by District',
    height: 400,
    width: 500
};
Plotly.newPlot('piechart', data, layout);
}

//Line Graph

function displayLine(response){
  var line = JSON.parse(response)
  var trace1 = {
    x: ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    y: line[0],
    mode: 'lines',
    type: 'scatter',
    name: 'ILLEGAL VEHICLE'
};
  var trace2 = {
    x: ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    y: line[1],
    mode: 'lines',
    type: 'scatter',
    name: 'ACCIDENT'
};
  var trace3 = {
    x: ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    y: line[2],
    mode: 'lines',
    type: 'scatter',
    name: 'ABANDONED VEHICLE'
};
  var trace4 = {
    x: ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    y: line[3],
    mode: 'lines',
    type: 'scatter',
    name: 'STOLEN VEHICLE'
};
  var trace5 = {
    x: ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    y: line[4],
    mode: 'lines',
    type: 'scatter',
    name: 'ILLEGALLY PARKED'
};
  var trace6 = {
    x: ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    y: line[5],
    mode: 'lines',
    type: 'scatter',
    name: 'IMPOUNDED'
};
  var trace7 = {
    x: ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    y: line[6],
    mode: 'lines',
    type: 'scatter',
    name: 'GONE ON ARRIVAL'
};
  var data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7];
  var layout = {
    title: '# Tows by Month and Description',
    width: 750,
    height: 400,
    xaxis: {
      title: 'Month',
    },
    yaxis: {
      title: '# Tows',
  }
}
Plotly.newPlot('linegraph', data, layout);
}