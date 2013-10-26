function datePlot(data, selector) {
    var margin = {top: 20, right: 20, bottom: 30, left: 50},
        width = 960 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;

    var parseDate = Date.parse;

    var x = d3.time.scale()
        .range([0, width]);

    var y = d3.scale.linear()
        .range([height, 0]);

    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom");

    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left")
        .tickFormat(function(d) { return d + '°'; });

    var area = d3.svg.area()
        .x(function(d) { return x(d.time); })
        .y0(height)
        .y1(function(d) { return y(d.val); });

    var svg = d3.select(selector).append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
      .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    data.forEach(function(d) {
        d.time = parseDate(d.time);
        d.val = +d.val;
    });

    x.domain(d3.extent(data, function(d) { return d.time; }));
    y.domain([0, d3.max(data, function(d) { return d.val; })]);

    svg.append("path")
      .datum(data)
      .attr("class", "area")
      .attr("d", area);

    svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

    svg.append("g")
      .attr("class", "y axis")
      .call(yAxis);
}