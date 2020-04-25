$(function() {
    // Then hide the second div
    $(".groups").hide();

    // Then add a click handlers to the buttons
    $("#mates").click(function() {
      $(".mates").show();
      $(".groups").hide();
    });
    $("#groups").click(function() {
      $(".mates").hide();
      $(".groups").show();
    });
}) 