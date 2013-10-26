function densityPlot(data, selector) {
  var margin = { top: 50, right: 0, bottom: 100, left: 50 },
      width = 960 - margin.left - margin.right,
      height = 430 - margin.top - margin.bottom,
      gridSize = Math.floor(width / 24),
      legendElementWidth = gridSize*2,
      today = new Date(),
      dayOffset = 7 - (today.getDay()),
      hourLimit = today.getHours(),
      buckets = 9,
      colors = ["#ffffd9","#edf8b1","#c7e9b4","#7fcdbb","#41b6c4","#1d91c0",
                "#225ea8","#253494","#081d58"],
      days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"],
      times = ["1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a",
               "11a", "12a", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p",
               "9p", "10p", "11p", "12p"];

  days = days.slice(7 - dayOffset, 7).concat(days.slice(0, 7 - dayOffset));

  // Aggregate sensor data 
  var aggData = d3.nest()
                  .key(function(d) {
                    var date = new Date(d.time);
                    return [date.getDay() + dayOffset, date.getHours()];
                  })
                  .rollup(function(d) {
                    return d3.sum(d, function(e) { return +e.val; });
                  })
                  .entries(data)
                  .map(function(d) {
                    return {
                      day: parseInt(d.key.split(',')[0], 10),
                      hour: parseInt(d.key.split(',')[1], 10),
                      value: d.values
                    };
                  });

  function scaleFill(d) {
    if (d.day == 7 && d.hour >= hourLimit) {
      return '#F8F8F8';
    } else {
      return colorScale(d.value);
    }
  }

  var colorScale = d3.scale.quantile()
      .domain([0, buckets - 1, 60])
      .range(colors);

  var svg = d3.select(selector).append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  var dayLabels = svg.selectAll(".dayLabel")
      .data(days)
      .enter().append("text")
        .text(function (d) { return d; })
        .attr("x", 0)
        .attr("y", function (d, i) { return i * gridSize; })
        .style("text-anchor", "end")
        .attr("transform", "translate(-6," + gridSize / 1.5 + ")")
        .attr("class", function (d, i) { return ((i >= 0 && i <= 4) ? "dayLabel mono axis axis-workweek" : "dayLabel mono axis"); });

  var timeLabels = svg.selectAll(".timeLabel")
      .data(times)
      .enter().append("text")
        .text(function(d) { return d; })
        .attr("x", function(d, i) { return i * gridSize; })
        .attr("y", 0)
        .style("text-anchor", "middle")
        .attr("transform", "translate(" + gridSize / 2 + ", -6)")
        .attr("class", function(d, i) { return ((i >= 7 && i <= 16) ? "timeLabel mono axis axis-worktime" : "timeLabel mono axis"); });

  var heatMap = svg.selectAll(".hour")
      .data(aggData)
      .enter().append("rect")
      .attr("x", function(d) { return (d.hour - 1) * gridSize; })
      .attr("y", function(d) { return (d.day - 1) * gridSize; })
      .attr("rx", 4)
      .attr("ry", 4)
      .attr("class", "hour bordered")
      .attr("width", gridSize)
      .attr("height", gridSize)
      .style("fill", '#F8F8F8');

  heatMap.transition().duration(1000)
      .style("fill", scaleFill);

  heatMap.append("title").text(function(d) { return d.value; });
      
  var legend = svg.selectAll(".legend")
      .data([0].concat(colorScale.quantiles()), function(d) { return d; })
      .enter().append("g")
      .attr("class", "legend");

  legend.append("rect")
    .attr("x", function(d, i) { return legendElementWidth * i; })
    .attr("y", height)
    .attr("width", legendElementWidth)
    .attr("height", gridSize / 2)
    .style("fill", function(d, i) { return colors[i]; });

  legend.append("text")
    .attr("class", "mono")
    .text(function(d) { return "≥ " + Math.round(d); })
    .attr("x", function(d, i) { return legendElementWidth * i; })
    .attr("y", height + gridSize);
}