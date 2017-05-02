(function(){
  $(window).scroll(function () {
      var top = $(document).scrollTop();
      $('.corporate-jumbo').css({
        'background-position': '0px -'+(top/3).toFixed(2)+'px'
      });
      if(top > 50)
        $('.navbar').removeClass('navbar-transparent');
      else
        $('.navbar').addClass('navbar-transparent');
  }).trigger('scroll');
})();

$(".btn-group :input").change(function() {
    var checkbox = $(this);
   var label = checkbox.parent('label');
   if (checkbox.is(':checked'))  {
      label.addClass('active');
   }
   else {
      label.removeClass('active');
   }
});

$('input[name=generate_report]').click(function() {
  $('div.progress').show();
  $( this ).hide();
  startLoadingBar();
});

$( window ).load(function() {
  $('div.progress').hide()
});


function startLoadingBar() {
  var elem = $('div.progress-bar-success')[0];
  var width = 20;
  elem.style.width = width + '%';
  var id = setInterval(frame, 10000);
  function frame() {
    if (width == 100) {
      clearInterval(id);
    } else {
      width += 10;
      elem.style.width = width + '%';
    }
  }
}
