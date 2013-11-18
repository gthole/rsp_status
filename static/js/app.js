$(document).ready(function() {

  $.getJSON('/api/v1/temp/?limit=1&_order_by=-time',
    function(response) {
      var latest = response['data'][0].val;
      $("#temp").html(latest.toFixed(1) + '°');
  });

  $.getJSON('/api/v1/motion/?limit=1&_order_by=-time',
    function(response) {
      dateFormat = d3.time.format('%a %b %d, %Y');
      timeFormat = d3.time.format('%I:%M %p');
      motion = new Date(response['data'][0].time);
      $("#motion").html(dateFormat(motion) + '<br />' + timeFormat(motion));
  });
  
  var d = new Date();
  d.setDate(d.getDate() - 1);
  $.getJSON('/api/v1/flood/?limit=1&_order_by=-time&time__gt=' + d.toISOString(),
    function(response) {
      if (response['data'].length) {
        $("#flood").html('<i class="fa fa-warning fa-5x text-warning"></i>');
      } else {
        $("#flood").html('<i class="fa fa-check-square fa-5x text-success"></i>');
      }
  });

  // Only show graphs on large-width screens
  if (window.screen.width > 1000) {
    d = new Date();
    d.setDate(d.getDate() - 7);
    $.getJSON(
      '/api/v1/temp/?time__gt=' + d.toISOString(),
      function(response) {
        datePlot(response['data'], '#temp-graph');
      });
    $.getJSON(
      '/api/v1/motion/?time_gt=' + d.toISOString(),
      function(response) {
        densityPlot(response['data'], '#motion-graph');
      });
  }
});

/*
function renderTemplate(name, selector, context) {
  $.get("templates/" + name + ".html", function(view) {
    $.Mustache.add('template', view);
    $(selector).mustache('template', context);
  });
}
*/
