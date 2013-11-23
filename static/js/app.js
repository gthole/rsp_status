$(document).ready(function() {

  $.getJSON('/api/v1/temp/?_limit=1&_order_by=-time',
    function(response) {
      var latest = response['data'][0].val;
      $("#temp").html(latest.toFixed(1) + '°');
  });

  $.getJSON('/api/v1/motion/?_limit=1&_order_by=-time',
    function(response) {
      dateFormat = d3.time.format('%a %b %d, %Y');
      timeFormat = d3.time.format('%I:%M %p');
      motion = new Date(response['data'][0].time);
      $("#motion").html(dateFormat(motion) + '<br />' + timeFormat(motion));
  });
  
  var d = new Date();
  d.setDate(d.getDate() - 1);
  $.getJSON('/api/v1/flood/?_limit=1&_order_by=-time&time__gt=' + d.toISOString(),
    function(response) {
      if (response['data'].length) {
        $("#flood").html('<i class="fa fa-warning fa-5x text-warning"></i>');
      } else {
        $("#flood").html('<i class="fa fa-check-square fa-5x text-success"></i>');
      }
  });

  // Only show graphs on large-width screens
  if (window.screen.width > 1000) {

    // Temperature date plot
    d = new Date();
    d.setDate(d.getDate() - 7);
    $('#temp-graph').html("<h2>Temperature History</h2>");
    $.getJSON(
      '/api/v1/temp/?_limit=350&time__gt=' + d.toISOString(),
      function(response) {
        datePlot(response['data'], '#temp-graph');
      });

    // Motion density plot
    $('#temp-graph').html("<h2>Motion History</h2>");
    $.getJSON(
      '/api/v1/motion/?_limit=1100&time_gt=' + d.toISOString(),
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
