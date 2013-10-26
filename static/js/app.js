$(document).ready(function() {


  $.getJSON('/fixtures/lasttemp.json',
    function(response) {
      $("#temp").html(response.val + '°');
  });

  $.getJSON('/fixtures/lastmotion.json',
    function(response) {
      dateFormat = d3.time.format('%a %b %d, %Y');
      timeFormat = d3.time.format('%I:%M %p');
      motion = new Date(response.time);
      $("#motion").html(dateFormat(motion) + '<br />' + timeFormat(motion));
  });

  $.getJSON('/fixtures/flood.json',
    function(response) {
      if (response.length) {
        $("#flood").html("Ack!");
      } else {
        $("#flood").html('<i class="fa fa-check-square fa-5x text-success"></i>');
      }
  });

  if (window.screen.width > 1000) {
    var d = new Date();
    d.setDate(d.getDate() - 7);
    $.getJSON(
      /* '/temp/?since=' + d.toISOString() */
      '/fixtures/temp.json',
      function(response) {
        datePlot(response, '#temp-graph');
      });
    $.getJSON(
      /* '/motion/?since=' + d.toISOString() */
      '/fixtures/motion.json',
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
