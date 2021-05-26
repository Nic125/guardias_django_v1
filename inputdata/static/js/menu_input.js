$('#department').click(function(){
  $(".service").slideUp(200)
  $(".personal").slideUp(200)
  $(".guard").slideUp(200)
  $(".department").slideDown(200)
  $(".notworking").slideUp(200)
  $(".points").slideUp(200)
  $(".licences").slideUp(200)
});


$('#service').click(function(){
  $(".department").slideUp(200)
  $(".personal").slideUp(200)
  $(".guard").slideUp(200)
  $(".service").slideDown(200)
  $(".notworking").slideUp(200)
  $(".points").slideUp(200)
  $(".licences").slideUp(200)
});

$('#guard').click(function(){
  $(".department").slideUp(200)
  $(".service").slideUp(200)
  $(".personal").slideUp(200)
  $(".guard").slideDown(200)
  $(".notworking").slideUp(200)
  $(".points").slideUp(200)
  $(".licences").slideUp(200)
});

$('#personal').click(function(){
  $(".department").slideUp(200)
  $(".service").slideUp(200)
  $(".guard").slideUp(200)
  $(".personal").slideDown(200)
  $(".notworking").slideUp(200)
  $(".points").slideUp(200)
  $(".licences").slideUp(200)
});

$('#notworking').click(function(){
  $(".department").slideUp(200)
  $(".service").slideUp(200)
  $(".guard").slideUp(200)
  $(".personal").slideUp(200)
  $(".notworking").slideDown(200)
  $(".points").slideUp(200)
  $(".licences").slideUp(200)

});

$('#licences').click(function(){
  $(".department").slideUp(200)
  $(".service").slideUp(200)
  $(".guard").slideUp(200)
  $(".personal").slideUp(200)
  $(".notworking").slideUp(200)
  $(".licences").slideDown(200)
  $(".points").slideUp(200)
});

$('#points').click(function(){
  $(".department").slideUp(200)
  $(".service").slideUp(200)
  $(".guard").slideUp(200)
  $(".personal").slideUp(200)
  $(".notworking").slideUp(200)
  $(".points").slideDown(200)
  $(".licences").slideUp(200)
});
