$(document).ready(function() {


  $.getJSON('http://10.0.1.21:5000/temp/',
    function(response) {
      var latest = response[response.length - 1].val;
      $("#temp").html(latest.toFixed(1) + '°');
  });

  $.getJSON('http://10.0.1.21:5000/motion/',
    function(response) {
      dateFormat = d3.time.format('%a %b %d, %Y');
      timeFormat = d3.time.format('%I:%M %p');
      motion = new Date(response[response.length - 1].time);
      $("#motion").html(dateFormat(motion) + '<br />' + timeFormat(motion));
  });

  $.getJSON('http://10.0.1.21:5000/flood/',
    function(response) {
      if (response.length) {
        $("#flood").html('<i class="fa fa-warning fa-5x text-warning"></i>');
      } else {
        $("#flood").html('<i class="fa fa-check-square fa-5x text-success"></i>');
      }
  });

  if (window.screen.width > 1000) {
    var d = new Date();
    d.setDate(d.getDate() - 7);
    $.getJSON(
      /* '/temp/?since=' + d.toISOString() */
      'http://10.0.1.21:5000/temp/',
      function(response) {
        datePlot(response, '#temp-graph');
      });
    $.getJSON(
      /* '/motion/?since=' + d.toISOString() */
      'http://10.0.1.21:5000/motion/',
      function(response) {
        densityPlot(response, '#motion-graph');
      });
  }
});

function renderTemplate(name, selector, context) {
  $.get("templates/" + name + ".html", function(view) {
    $.Mustache.add('template', view);
    $(selector).mustache('template', context);
  });
}
