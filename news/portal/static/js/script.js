$(document).ready(function () {
  //script that performs part of the search bar
  //Jquery
  var searchBtn = $('#search-btn');   // instantiates the search bar button
  var searchForm = $('#search-form'); // instance the search bar form

  $(searchBtn).on('click', function () {
    // function that checks if the button was clicked
    searchForm.submit(); // submit the form
  });

});