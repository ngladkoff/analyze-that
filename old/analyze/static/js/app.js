$(document).foundation()

$('[data-app-dashboard-toggle-shrink]').on('click', function(e) {
    e.preventDefault();
    $(this).parents('.app-dashboard').toggleClass('shrink-medium').toggleClass('shrink-large');
  });

var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  }
})
