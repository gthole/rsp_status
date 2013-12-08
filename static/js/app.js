$(document).ready(function() {
  // Populate the station select box and render with the first station.
  $.getJSON('/api/v1/stations/',
    function(response) {
      var stations = response['data'];
      var stationOptions = '';
      for (var i in stations) {
        stationOptions += '\n<option value="' + stations[i] + '">' + stations[i] + '</option>';
      }
      $('#select-station').html(stationOptions);
      $('#select-station-row').attr('hidden', false);
      render(stations[0]);
  });

  $('#select-station').change(function() {
    render($( "#select-station option:selected" ).text());
  });
});

function render(station) {
  $('#title').html(station + ' Status');

  $.getJSON('/api/v1/temp/?_limit=1&_order_by=-time&station=' + station,
    function(response) {
      var latest = response['data'][0].val;
      $("#temp").html(latest.toFixed(1) + '°');
  });

  $.getJSON('/api/v1/motion/?_limit=1&_order_by=-time&station=' + station,
    function(response) {
      var dateFormat = d3.time.format('%a %b %d, %Y');
      var timeFormat = d3.time.format('%I:%M %p');
      var motion = new Date(response['data'][0].time);
      $("#motion").html(dateFormat(motion) + '<br />' + timeFormat(motion));
  });
  
  var d = new Date();
  d.setDate(d.getDate() - 1);
  $.getJSON('/api/v1/flood/?_limit=1&_order_by=-time&time__gt=' + d.toISOString() + '&station=' + station,
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
      '/api/v1/temp/?_limit=350&_order_by=-time&time__gt=' + d.toISOString() + '&station=' + station,
      function(response) {
        datePlot(response['data'], '#temp-graph');
      });

    // Motion density plot
    $('#motion-graph').html("<h2>Motion History</h2>");
    $.getJSON(
      '/api/v1/motion/?_limit=1100&_order_by=-time&time_gt=' + d.toISOString() + '&station=' + station,
      function(response) {
        densityPlot(response['data'], '#motion-graph');
      });
  }
}
